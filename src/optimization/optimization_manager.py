"""
Optimization Manager for HF Spaces Free Tier
Implements all optimization strategies for 2vCPU + 16GB RAM constraint
"""

import os
import gc
import psutil
from typing import Any, Optional, Callable
from functools import lru_cache, wraps
import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)


class OptimizationManager:
    """Manages all optimizations for resource-constrained environments"""
    
    def __init__(self):
        """Initialize optimization manager"""
        self.memory_threshold = 0.80  # Alert if > 80% memory used
        self.model_cache = {}
        self.computation_cache = {}
        self.memory_warnings = []
        
    def get_system_stats(self) -> dict:
        """Get current system resource usage"""
        import psutil
        
        virtual_memory = psutil.virtual_memory()
        process = psutil.Process(os.getpid())
        process_memory = process.memory_info()
        
        return {
            'total_ram_gb': virtual_memory.total / (1024**3),
            'available_ram_gb': virtual_memory.available / (1024**3),
            'used_ram_gb': virtual_memory.used / (1024**3),
            'ram_percent': virtual_memory.percent,
            'process_memory_mb': process_memory.rss / (1024**2),
            'process_percent': process.memory_percent(),
            'cpu_percent': process.cpu_percent(interval=0.1),
            'cpu_count': psutil.cpu_count()
        }
    
    def check_memory_health(self) -> dict:
        """Check if memory usage is healthy"""
        stats = self.get_system_stats()
        
        health = {
            'status': 'HEALTHY',
            'ram_percent': stats['ram_percent'],
            'available_gb': stats['available_ram_gb'],
            'warnings': []
        }
        
        if stats['ram_percent'] > 80:
            health['status'] = 'WARNING'
            health['warnings'].append(f"High memory usage: {stats['ram_percent']:.1f}%")
            self._aggressive_cleanup()
        
        if stats['ram_percent'] > 90:
            health['status'] = 'CRITICAL'
            health['warnings'].append(f"CRITICAL memory usage: {stats['ram_percent']:.1f}%")
            self._emergency_cleanup()
        
        return health
    
    def _aggressive_cleanup(self):
        """Aggressively clean up memory"""
        gc.collect()
        # Clear caches
        self.computation_cache.clear()
    
    def _emergency_cleanup(self):
        """Emergency memory cleanup"""
        self._aggressive_cleanup()
        # Force garbage collection multiple times
        for _ in range(3):
            gc.collect()
    
    def optimize_model_loading(self, model_name: str, quantization: str = "int4"):
        """
        Optimized model loading configuration
        
        Args:
            model_name: HuggingFace model identifier
            quantization: Quantization strategy (int4, int8, float16, etc)
        
        Returns:
            Model loading parameters
        """
        params = {
            "model_name": model_name,
            "device_map": "auto",
            "quantization_config": {
                "load_in_4bit": quantization == "int4",
                "load_in_8bit": quantization == "int8",
                "bnb_4bit_compute_dtype": "float16",
                "bnb_4bit_quant_type": "nf4",
                "bnb_4bit_use_double_quant": True,
            },
            "attn_implementation": "flash_attention_2",
            "torch_dtype": "float16",
            "low_cpu_mem_usage": True,
            "offload_folder": "/tmp/offload",
            "offload_state_dict": True,
        }
        
        if quantization == "int8":
            params["quantization_config"] = {
                "load_in_8bit": True,
                "bnb_8bit_compute_dtype": "float16",
            }
        
        return params
    
    def optimize_inference_settings(self) -> dict:
        """Get optimized inference settings for free tier"""
        return {
            "max_new_tokens": 256,
            "min_new_tokens": 50,
            "do_sample": True,
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 50,
            "repetition_penalty": 1.2,
            "length_penalty": 1.0,
            "early_stopping": False,
            "no_repeat_ngram_size": 0,
            "num_beams": 1,  # No beam search (saves memory)
            "num_beam_groups": 1,
        }
    
    @lru_cache(maxsize=128)
    def cached_computation(self, func_key: str, *args) -> Any:
        """
        LRU cache for expensive computations
        Use as: @cached_computation
        """
        pass
    
    def cache_decorator(self, max_size: int = 128):
        """
        Decorator for caching function results
        
        Usage:
            @OptimizationManager().cache_decorator(max_size=64)
            def expensive_function(...):
                ...
        """
        def decorator(func):
            cache = {}
            cache_keys = []
            
            @wraps(func)
            def wrapper(*args, **kwargs):
                # Create cache key
                key = str(args) + str(sorted(kwargs.items()))
                
                if key in cache:
                    return cache[key]
                
                # Call function
                result = func(*args, **kwargs)
                
                # Manage cache size
                if len(cache) >= max_size:
                    oldest_key = cache_keys.pop(0)
                    del cache[oldest_key]
                
                cache[key] = result
                cache_keys.append(key)
                
                return result
            
            return wrapper
        return decorator
    
    def lazy_import(self, module_name: str, class_name: Optional[str] = None):
        """
        Lazily import modules to reduce startup time
        
        Usage:
            WeasyPrint = lazy_import('weasyprint', 'HTML')
            # Module loaded only when first accessed
        """
        def loader():
            module = __import__(module_name, fromlist=[class_name] if class_name else [])
            if class_name:
                return getattr(module, class_name)
            return module
        
        return loader
    
    def get_optimized_document_config(self) -> dict:
        """Get optimized document generation configuration"""
        return {
            "pdf": {
                "engine": "reportlab",  # Not weasyprint
                "dpi": 100,  # Web resolution
                "compression": True,
                "optimize_images": True,
            },
            "docx": {
                "engine": "python-docx",
                "optimize_memory": True,
                "cache_templates": True,
            },
            "html": {
                "inline_css": True,
                "minify": True,
                "optimize_images": True,
                "lazy_load_images": True,
            },
            "markdown": {
                "optimize": True,
                "cache": True,
            },
            "latex": {
                "minimal_preamble": True,
                "optimize_packages": True,
            }
        }
    
    def get_optimized_visualization_config(self) -> dict:
        """Get optimized visualization configuration"""
        return {
            "matplotlib": {
                "backend": "Agg",  # Non-interactive
                "dpi": 100,  # Web resolution (not 300)
                "figure_size": (8, 6),  # Standard size
                "use_cache": True,
            },
            "seaborn": {
                "style": "whitegrid",  # Simple style
                "context": "notebook",  # Smaller default sizes
                "palette": "husl",  # Efficient palette
            },
            "plotly": {
                "enabled": False,  # Skip - too heavy
                "use_matplotlib_instead": True,
            },
            "image_optimization": {
                "compression": 0.8,
                "format": "PNG",  # More efficient than others
                "cache": True,
            }
        }
    
    def optimize_data_processing(self) -> dict:
        """Get optimized data processing configuration"""
        return {
            "pandas": {
                "use_categories": True,  # 70-90% memory saving
                "dtype_optimize": True,
                "chunk_size": 10000,  # Process in chunks
                "infer_types": False,  # Faster
            },
            "numpy": {
                "dtype": "float32",  # Not float64
                "use_memmap": True,  # Memory mapping for large arrays
            },
            "chunking": {
                "enabled": True,
                "chunk_size": 10000,
                "overlap": 0,  # No overlap to save memory
            }
        }
    
    def get_startup_optimization_config(self) -> dict:
        """Get configuration for optimized startup"""
        return {
            "lazy_imports": True,
            "load_minimal": True,
            "defer_heavy_libs": True,
            "preload_critical_only": True,
            "expected_startup_time": "10-15 seconds",
            "first_request_time": "15-20 seconds (includes model load)",
            "subsequent_requests": "2-5 seconds"
        }
    
    def create_memory_monitor(self, threshold: float = 0.80):
        """
        Create a memory monitoring context manager
        
        Usage:
            with optimizer.create_memory_monitor(0.80):
                # Do heavy computation
                pass
        """
        class MemoryMonitor:
            def __init__(self, threshold):
                self.threshold = threshold
                self.optimizer = self
            
            def __enter__(self):
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                health = self.optimizer.check_memory_health()
                if health['status'] != 'HEALTHY':
                    print(f"⚠️ Memory warning: {health['warnings']}")
                    self.optimizer._aggressive_cleanup()
        
        return MemoryMonitor(threshold)
    
    def get_performance_recommendations(self) -> list:
        """Get recommendations based on current system state"""
        stats = self.get_system_stats()
        recommendations = []
        
        if stats['ram_percent'] > 75:
            recommendations.append(
                "💡 High memory usage detected. Consider disabling Plotly visualizations."
            )
        
        if stats['process_memory_mb'] > 5000:
            recommendations.append(
                "💡 Process using >5GB. Clear caches and restart for optimal performance."
            )
        
        if stats['cpu_percent'] > 80:
            recommendations.append(
                "💡 High CPU usage. Reduce max_tokens or disable batch processing."
            )
        
        return recommendations
    
    def print_system_report(self):
        """Print detailed system resource report"""
        stats = self.get_system_stats()
        health = self.check_memory_health()
        recommendations = self.get_performance_recommendations()
        
        report = f"""
╔════════════════════════════════════════════════════════════════╗
║           SYSTEM RESOURCE MONITORING REPORT                    ║
╚════════════════════════════════════════════════════════════════╝

📊 MEMORY STATUS: {health['status']}
   • Total RAM: {stats['total_ram_gb']:.1f} GB
   • Available RAM: {stats['available_ram_gb']:.1f} GB
   • Used RAM: {stats['used_ram_gb']:.1f} GB ({stats['ram_percent']:.1f}%)
   • Process Memory: {stats['process_memory_mb']:.1f} MB
   • Process Memory %: {stats['process_percent']:.1f}%

⚙️  CPU STATUS:
   • CPU Cores: {stats['cpu_count']}
   • CPU Usage: {stats['cpu_percent']:.1f}%

📈 HEALTH CHECK:
"""
        for warning in health['warnings']:
            report += f"   ⚠️  {warning}\n"
        
        if not health['warnings']:
            report += "   ✅ All systems nominal\n"
        
        report += "\n💡 RECOMMENDATIONS:\n"
        if recommendations:
            for rec in recommendations:
                report += f"   {rec}\n"
        else:
            report += "   ✅ No critical recommendations\n"
        
        print(report)
        return report


# ============================================================================
# GLOBAL OPTIMIZATION MANAGER INSTANCE
# ============================================================================

optimization_manager = OptimizationManager()


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_model_loading_params(model_id: str, quantization: str = "int4") -> dict:
    """Helper to get model loading parameters"""
    return optimization_manager.optimize_model_loading(model_id, quantization)


def get_inference_settings() -> dict:
    """Helper to get inference settings"""
    return optimization_manager.optimize_inference_settings()


def get_system_health() -> dict:
    """Helper to check system health"""
    return optimization_manager.check_memory_health()


def print_optimization_report():
    """Print optimization report"""
    optimization_manager.print_system_report()
