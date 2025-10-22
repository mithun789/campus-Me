"""
Optimization Module for HF Spaces Free Tier (2vCPU + 16GB RAM)
Provides all optimizations needed for resource-constrained deployment
"""

from .optimization_config import (
    MEMORY_OPTIMIZATION,
    INFERENCE_OPTIMIZATION,
    DOCUMENT_GENERATION_OPTIMIZATION,
    VISUALIZATION_OPTIMIZATION,
    DATA_PROCESSING_OPTIMIZATION,
    DEPENDENCY_OPTIMIZATION,
    CACHING_STRATEGY,
    STARTUP_OPTIMIZATION,
    RUNTIME_OPTIMIZATION,
    HF_SPACES_OPTIMIZATIONS,
    RECOMMENDED_CONFIG,
    OPTIMIZED_MODEL_CHOICES,
    OPTIMIZATION_CHECKLIST
)

from .optimization_manager import (
    OptimizationManager,
    optimization_manager,
    get_model_loading_params,
    get_inference_settings,
    get_system_health,
    print_optimization_report
)

__all__ = [
    # Config exports
    'MEMORY_OPTIMIZATION',
    'INFERENCE_OPTIMIZATION',
    'DOCUMENT_GENERATION_OPTIMIZATION',
    'VISUALIZATION_OPTIMIZATION',
    'DATA_PROCESSING_OPTIMIZATION',
    'DEPENDENCY_OPTIMIZATION',
    'CACHING_STRATEGY',
    'STARTUP_OPTIMIZATION',
    'RUNTIME_OPTIMIZATION',
    'HF_SPACES_OPTIMIZATIONS',
    'RECOMMENDED_CONFIG',
    'OPTIMIZED_MODEL_CHOICES',
    'OPTIMIZATION_CHECKLIST',
    
    # Manager exports
    'OptimizationManager',
    'optimization_manager',
    'get_model_loading_params',
    'get_inference_settings',
    'get_system_health',
    'print_optimization_report'
]
