"""
File Manager - Secure file upload, processing, and automatic cleanup for HF Spaces
Handles temporary files with automatic deletion after processing
"""

import os
import shutil
import tempfile
from typing import List, Optional, Tuple, Dict, Any
from pathlib import Path
from datetime import datetime, timedelta
import logging
import atexit
import threading

logger = logging.getLogger(__name__)


class FileManager:
    """
    Manage file uploads with automatic cleanup.
    - Accept file uploads (PDFs, Word, slides, images, etc.)
    - Track uploaded files
    - Auto-delete after processing
    - Clean up on app shutdown
    - Memory efficient for HF Spaces
    """

    def __init__(self, temp_base_dir: Optional[str] = None, max_age_minutes: int = 60):
        """
        Initialize file manager.

        Args:
            temp_base_dir: Base directory for temporary files (uses system temp if None)
            max_age_minutes: Maximum age of files before auto-cleanup (default 60 minutes)
        """
        self.temp_base_dir = temp_base_dir or os.path.join(tempfile.gettempdir(), "campus_me_uploads")
        self.max_age = timedelta(minutes=max_age_minutes)
        self.tracked_files: Dict[str, Dict[str, Any]] = {}
        self.lock = threading.Lock()

        # Create temp directory
        os.makedirs(self.temp_base_dir, exist_ok=True)

        # Register cleanup on exit
        atexit.register(self.cleanup_all)

        logger.info(f"File Manager initialized. Temp directory: {self.temp_base_dir}")

    def upload_file(self, source_path: str, original_filename: str = "") -> Tuple[bool, str]:
        """
        Upload and track a file for processing.

        Args:
            source_path: Path to source file
            original_filename: Original filename for reference

        Returns:
            Tuple of (success: bool, file_id: str or error_message: str)
        """
        try:
            source_path = Path(source_path)

            if not source_path.exists():
                return False, f"File not found: {source_path}"

            # Validate file size (limit to 50MB for safety)
            file_size = source_path.stat().st_size
            max_size = 50 * 1024 * 1024  # 50MB

            if file_size > max_size:
                return False, f"File too large: {file_size / (1024*1024):.1f}MB (max: 50MB)"

            # Generate unique file ID
            file_id = self._generate_file_id(source_path)

            # Copy to temp directory
            dest_path = self._get_dest_path(file_id, source_path.suffix)
            shutil.copy2(source_path, dest_path)

            # Track file
            with self.lock:
                self.tracked_files[file_id] = {
                    "source": str(source_path),
                    "destination": str(dest_path),
                    "original_name": original_filename or source_path.name,
                    "file_size": file_size,
                    "upload_time": datetime.now(),
                    "file_type": source_path.suffix,
                    "status": "uploaded",
                }

            logger.info(f"File uploaded: {file_id} ({file_size / (1024*1024):.1f}MB)")
            return True, file_id

        except Exception as e:
            logger.error(f"File upload error: {str(e)}")
            return False, f"Upload error: {str(e)}"

    def get_file_path(self, file_id: str) -> Optional[str]:
        """
        Get path to uploaded file.

        Args:
            file_id: File identifier

        Returns:
            Path to file or None if not found
        """
        with self.lock:
            if file_id in self.tracked_files:
                file_info = self.tracked_files[file_id]
                path = file_info.get("destination")
                if path and os.path.exists(path):
                    return path

        return None

    def mark_processed(self, file_id: str, delete_after: int = 0) -> bool:
        """
        Mark file as processed.

        Args:
            file_id: File identifier
            delete_after: Delete file after this many seconds (0 = delete immediately)

        Returns:
            Success status
        """
        try:
            with self.lock:
                if file_id in self.tracked_files:
                    self.tracked_files[file_id]["status"] = "processed"
                    self.tracked_files[file_id]["processed_time"] = datetime.now()

                    if delete_after <= 0:
                        # Delete immediately
                        return self.delete_file(file_id)
                    else:
                        # Schedule deletion
                        self.tracked_files[file_id]["delete_at"] = (
                            datetime.now() + timedelta(seconds=delete_after)
                        )
                        return True

            return False

        except Exception as e:
            logger.error(f"Error marking file as processed: {str(e)}")
            return False

    def delete_file(self, file_id: str) -> bool:
        """
        Delete a tracked file.

        Args:
            file_id: File identifier

        Returns:
            Success status
        """
        try:
            with self.lock:
                if file_id in self.tracked_files:
                    file_info = self.tracked_files[file_id]
                    dest_path = file_info.get("destination")

                    if dest_path and os.path.exists(dest_path):
                        os.remove(dest_path)
                        logger.info(f"File deleted: {file_id}")

                    # Remove from tracking
                    del self.tracked_files[file_id]
                    return True

            return False

        except Exception as e:
            logger.error(f"Error deleting file {file_id}: {str(e)}")
            return False

    def cleanup_expired_files(self) -> int:
        """
        Clean up files that have expired.

        Returns:
            Number of files cleaned up
        """
        cleaned_count = 0
        now = datetime.now()

        with self.lock:
            expired_files = []

            for file_id, file_info in list(self.tracked_files.items()):
                # Check if file has expired based on age
                upload_time = file_info.get("upload_time")
                if upload_time and (now - upload_time) > self.max_age:
                    expired_files.append(file_id)

                # Check if scheduled for deletion
                delete_at = file_info.get("delete_at")
                if delete_at and now >= delete_at:
                    expired_files.append(file_id)

            # Delete expired files
            for file_id in expired_files:
                if self._delete_file_internal(file_id):
                    cleaned_count += 1

        if cleaned_count > 0:
            logger.info(f"Cleaned up {cleaned_count} expired files")

        return cleaned_count

    def _delete_file_internal(self, file_id: str) -> bool:
        """Internal file deletion (without lock)."""
        try:
            if file_id in self.tracked_files:
                file_info = self.tracked_files[file_id]
                dest_path = file_info.get("destination")

                if dest_path and os.path.exists(dest_path):
                    os.remove(dest_path)

                del self.tracked_files[file_id]
                return True

            return False

        except Exception as e:
            logger.error(f"Error in internal delete: {str(e)}")
            return False

    def cleanup_all(self) -> int:
        """
        Clean up all tracked files (usually on app shutdown).

        Returns:
            Number of files cleaned up
        """
        cleaned_count = 0

        with self.lock:
            file_ids = list(self.tracked_files.keys())

            for file_id in file_ids:
                if self._delete_file_internal(file_id):
                    cleaned_count += 1

        logger.info(f"Total cleanup: {cleaned_count} files removed")
        return cleaned_count

    def get_file_info(self, file_id: str) -> Optional[Dict[str, Any]]:
        """
        Get information about a tracked file.

        Args:
            file_id: File identifier

        Returns:
            File information dictionary or None
        """
        with self.lock:
            if file_id in self.tracked_files:
                return self.tracked_files[file_id].copy()

        return None

    def get_all_files_info(self) -> List[Dict[str, Any]]:
        """
        Get information about all tracked files.

        Returns:
            List of file information dictionaries
        """
        with self.lock:
            return [info.copy() for info in self.tracked_files.values()]

    def get_storage_usage(self) -> Dict[str, Any]:
        """
        Get current storage usage statistics.

        Returns:
            Storage information
        """
        with self.lock:
            total_size = sum(
                info.get("file_size", 0) for info in self.tracked_files.values()
            )

            return {
                "total_files": len(self.tracked_files),
                "total_size_mb": total_size / (1024 * 1024),
                "total_size_bytes": total_size,
                "files_by_type": self._get_files_by_type(),
                "files_by_status": self._get_files_by_status(),
            }

    def _get_files_by_type(self) -> Dict[str, int]:
        """Get count of files by type."""
        by_type = {}
        for info in self.tracked_files.values():
            file_type = info.get("file_type", "unknown")
            by_type[file_type] = by_type.get(file_type, 0) + 1

        return by_type

    def _get_files_by_status(self) -> Dict[str, int]:
        """Get count of files by status."""
        by_status = {}
        for info in self.tracked_files.values():
            status = info.get("status", "unknown")
            by_status[status] = by_status.get(status, 0) + 1

        return by_status

    def _generate_file_id(self, source_path: Path) -> str:
        """Generate unique file ID."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name_hash = hash(str(source_path)) % 100000
        return f"file_{timestamp}_{name_hash:05d}"

    def _get_dest_path(self, file_id: str, file_ext: str) -> str:
        """Get destination path for file."""
        return os.path.join(self.temp_base_dir, f"{file_id}{file_ext}")

    def batch_upload(self, file_list: List[str]) -> Tuple[List[str], List[str]]:
        """
        Upload multiple files.

        Args:
            file_list: List of file paths

        Returns:
            Tuple of (successful_ids: List[str], failed_files: List[str])
        """
        successful_ids = []
        failed_files = []

        for file_path in file_list:
            success, result = self.upload_file(file_path)
            if success:
                successful_ids.append(result)
            else:
                failed_files.append(file_path)

        logger.info(f"Batch upload: {len(successful_ids)} success, {len(failed_files)} failed")
        return successful_ids, failed_files

    def batch_cleanup(self, file_ids: List[str]) -> int:
        """
        Delete multiple files.

        Args:
            file_ids: List of file IDs to delete

        Returns:
            Number of files deleted
        """
        deleted_count = 0

        for file_id in file_ids:
            if self.delete_file(file_id):
                deleted_count += 1

        return deleted_count

    def validate_file_type(self, file_path: str, allowed_extensions: List[str] = None) -> bool:
        """
        Validate if file type is allowed.

        Args:
            file_path: Path to file
            allowed_extensions: List of allowed extensions (default: all supported)

        Returns:
            True if file type is allowed
        """
        if allowed_extensions is None:
            allowed_extensions = [
                '.pdf', '.docx', '.doc', '.txt', '.md',
                '.pptx', '.ppt', '.jpg', '.jpeg', '.png', '.gif'
            ]

        file_ext = Path(file_path).suffix.lower()
        return file_ext in allowed_extensions


class FileCleanupScheduler:
    """
    Background scheduler for automatic file cleanup.
    """

    def __init__(self, file_manager: FileManager, cleanup_interval_seconds: int = 300):
        """
        Initialize cleanup scheduler.

        Args:
            file_manager: FileManager instance
            cleanup_interval_seconds: How often to run cleanup (default: 5 minutes)
        """
        self.file_manager = file_manager
        self.cleanup_interval = cleanup_interval_seconds
        self.running = False
        self.thread = None

    def start(self) -> None:
        """Start the background cleanup scheduler."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(daemon=True, target=self._cleanup_loop)
            self.thread.start()
            logger.info(f"File cleanup scheduler started (interval: {self.cleanup_interval}s)")

    def stop(self) -> None:
        """Stop the background cleanup scheduler."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=5)
        logger.info("File cleanup scheduler stopped")

    def _cleanup_loop(self) -> None:
        """Background cleanup loop."""
        import time

        while self.running:
            try:
                self.file_manager.cleanup_expired_files()
            except Exception as e:
                logger.error(f"Cleanup loop error: {str(e)}")

            time.sleep(self.cleanup_interval)
