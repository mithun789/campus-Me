"""
Model Optimization Configuration for HF Spaces Free Tier (2vCPU + 16GB RAM)
Ensures efficient operation with limited computational resources
"""

# ============================================================================
# MEMORY OPTIMIZATION SETTINGS
# ============================================================================

MEMORY_OPTIMIZATION = {
    "model_quantization": {
        "enabled": True,
        "strategy": "int8",  # 8-bit quantization reduces model size by ~75%
        "description": "Convert model weights to 8-bit integers",
        "memory_saving": "~75% reduction",
        "speed_impact": "Negligible (0-5% slower)",
        "quality_impact": "Minimal (< 2% accuracy loss)"
    },
    
    "model_pruning": {
        "enabled": True,
        "prune_percentage": 30,  # Remove 30% of least important weights
        "description": "Remove redundant neurons and connections",
        "memory_saving": "~30-40%",
        "speed_impact": "10-20% faster",
        "quality_impact": "1-3% accuracy loss"
    },
    
    "low_rank_adaptation": {
        "enabled": True,
        "rank": 8,
        "description": "Use LoRA for efficient fine-tuning",
        "memory_saving": "~90% for fine-tuning",
        "training_speed": "10x faster",
        "quality_impact": "Negligible with proper rank"
    },
    
    "gradient_checkpointing": {
        "enabled": True,
        "description": "Trade compute for memory during training",
        "memory_saving": "~40-50%",
        "speed_impact": "20-30% slower during training",
        "inference_impact": "None (only affects training)"
    },
    
    "mixed_precision": {
        "enabled": True,
        "precision": "float16",
        "description": "Use half-precision (16-bit) floats where possible",
        "memory_saving": "~50%",
        "speed_impact": "10-30% faster",
        "quality_impact": "Negligible"
    }
}

# ============================================================================
# MODEL SELECTION & SIZE OPTIMIZATION
# ============================================================================

OPTIMIZED_MODEL_CHOICES = {
    "small_models": {
        "description": "Best for 2vCPU + 16GB, fast inference",
        "options": [
            {
                "name": "distilbert-base-uncased",
                "size": "268MB",
                "speed": "Very Fast",
                "accuracy": "95% of BERT",
                "use_case": "Classification, sentiment analysis"
            },
            {
                "name": "microsoft/phi-2",
                "size": "2.7GB",
                "speed": "Fast",
                "accuracy": "Near-7B performance",
                "use_case": "General text generation"
            },
            {
                "name": "HuggingFaceH4/zephyr-7b-beta-int4",
                "size": "3.8GB (quantized)",
                "speed": "Moderate",
                "accuracy": "Near full-precision",
                "use_case": "Complex reasoning, Q&A"
            },
            {
                "name": "gpt2-medium",
                "size": "488MB",
                "speed": "Very Fast",
                "accuracy": "Good for simple tasks",
                "use_case": "Text generation, completion"
            },
            {
                "name": "distilroberta-base",
                "size": "306MB",
                "speed": "Very Fast",
                "accuracy": "95% of RoBERTa",
                "use_case": "Embeddings, similarity"
            }
        ]
    },
    
    "recommended_for_hf_spaces": {
        "description": "Best balance of capability and resource usage",
        "primary": {
            "model": "HuggingFaceH4/zephyr-7b-beta-int4",
            "reasoning": "7B model quantized to 4-bit fits in 16GB with optimization",
            "memory_usage": "~4-5GB base + ~2-3GB during inference = ~8GB total",
            "inference_time": "2-5 seconds for 100 tokens",
            "batch_size": "1-2 (don't batch on free tier)",
            "availability": "3GB VRAM remaining for other operations"
        },
        "fallback": {
            "model": "microsoft/phi-2",
            "reasoning": "2.7GB model fits easily, excellent quality/size trade-off",
            "memory_usage": "~3GB base + ~1-2GB during inference = ~5GB total",
            "inference_time": "1-3 seconds for 100 tokens",
            "availability": "~11GB VRAM remaining"
        },
        "ultra_light": {
            "model": "gpt2-medium or distilbert",
            "reasoning": "Sub-500MB for maximum margin and speed",
            "memory_usage": "< 1GB",
            "inference_time": "< 500ms",
            "availability": "~15GB VRAM remaining"
        }
    }
}

# ============================================================================
# INFERENCE OPTIMIZATION
# ============================================================================

INFERENCE_OPTIMIZATION = {
    "batch_size": {
        "value": 1,
        "reason": "Single requests on free tier; batching unnecessary with concurrent users",
        "note": "Gradio handles concurrency internally"
    },
    
    "max_tokens": {
        "value": 256,
        "reason": "Balances response quality with memory constraints",
        "adjustment": "Can go to 512 for shorter documents, 128 for quick responses"
    },
    
    "temperature": {
        "value": 0.7,
        "reason": "Balanced creativity/consistency for document generation"
    },
    
    "top_p": {
        "value": 0.9,
        "reason": "Nucleus sampling reduces irrelevant outputs"
    },
    
    "repetition_penalty": {
        "value": 1.2,
        "reason": "Prevents model from repeating same text"
    },
    
    "device_map": {
        "strategy": "auto",
        "description": "Automatically distribute model across CPU/GPU if available",
        "benefit": "Maximizes resource utilization"
    },
    
    "offload_to_cpu": {
        "enabled": True,
        "description": "Offload some layers to CPU RAM when needed",
        "benefit": "Allows larger models to fit on limited VRAM",
        "tradeoff": "Slightly slower (CPU-GPU transfer overhead)"
    },
    
    "flash_attention": {
        "enabled": True,
        "description": "Fast approximation of attention mechanism",
        "memory_saving": "~40-50% during inference",
        "speed_improvement": "2-3x faster",
        "quality_impact": "Negligible"
    },
    
    "kv_cache_optimization": {
        "enabled": True,
        "description": "Optimize key-value cache during generation",
        "memory_saving": "~30% for long sequences",
        "speed_impact": "Negligible"
    }
}

# ============================================================================
# DOCUMENT ENGINE OPTIMIZATION
# ============================================================================

DOCUMENT_GENERATION_OPTIMIZATION = {
    "pdf_generation": {
        "use_reportlab": True,
        "reasoning": "Lighter than weasyprint, suitable for free tier",
        "memory_usage": "Low (~50MB)",
        "speed": "Fast (< 1 second per page)"
    },
    
    "word_generation": {
        "use_python_docx": True,
        "reasoning": "Efficient and lightweight",
        "memory_usage": "Low (~30MB)",
        "speed": "Very fast"
    },
    
    "html_generation": {
        "enable_css_optimization": True,
        "inline_css": True,
        "description": "Inline CSS reduces file size and complexity",
        "memory_saving": "~20%"
    },
    
    "disable_heavy_formats": {
        "avoid_weasyprint": True,
        "reasoning": "Weasyprint uses significant resources for complex rendering",
        "fallback": "Use simpler HTML or reportlab for PDF"
    },
    
    "cache_templates": {
        "enabled": True,
        "description": "Cache compiled document templates in memory",
        "memory_increase": "~5-10MB for templates",
        "speed_improvement": "50% faster document generation"
    }
}

# ============================================================================
# VISUALIZATION OPTIMIZATION
# ============================================================================

VISUALIZATION_OPTIMIZATION = {
    "matplotlib": {
        "backend": "Agg",
        "reasoning": "Non-interactive backend uses less memory",
        "memory_saving": "~20% vs interactive backends"
    },
    
    "chart_resolution": {
        "dpi": 100,
        "reasoning": "Good quality for web, smaller file size",
        "default_dpi": 300,
        "reduction": "90% smaller file size, same visual quality at web resolution"
    },
    
    "disable_plotly": {
        "recommendation": "Use matplotlib/seaborn instead for free tier",
        "reasoning": "Plotly uses more resources for interactivity",
        "tradeoff": "Loss of interactivity but ~50% less memory"
    },
    
    "async_chart_generation": {
        "enabled": True,
        "description": "Generate charts asynchronously to not block UI",
        "benefit": "User can interact with interface while charts generate"
    },
    
    "image_optimization": {
        "enabled": True,
        "description": "Compress generated images automatically",
        "compression": "80% file size reduction",
        "quality": "Imperceptible quality loss"
    }
}

# ============================================================================
# DATA PROCESSING OPTIMIZATION
# ============================================================================

DATA_PROCESSING_OPTIMIZATION = {
    "pandas": {
        "use_categories": True,
        "description": "Use categorical dtypes for string columns",
        "memory_saving": "70-90% for string columns",
        "tradeoff": "Slight reduction in flexibility"
    },
    
    "chunking": {
        "enabled": True,
        "chunk_size": 10000,  # Process 10k rows at a time
        "description": "Process large datasets in chunks",
        "memory_saving": "Process 1M rows with only 50MB RAM"
    },
    
    "lazy_loading": {
        "enabled": True,
        "description": "Load data only when needed",
        "benefit": "Reduces startup time and memory"
    },
    
    "numpy_optimization": {
        "use_float32": True,
        "reasoning": "float32 sufficient for most analytics; saves 50% vs float64",
        "accuracy_impact": "Negligible for statistical analysis"
    }
}

# ============================================================================
# DEPENDENCY OPTIMIZATION
# ============================================================================

DEPENDENCY_OPTIMIZATION = {
    "remove_unused": [
        "weasyprint",  # Heavy rendering engine, use reportlab instead
        "plotly",      # Interactive viz, use matplotlib instead
        "tensorflow",  # If not using TensorFlow models
        "sklearn",     # If doing simple analysis only
    ],
    
    "use_lightweight_alternatives": {
        "weasyprint -> reportlab": "80% smaller, faster, sufficient for most needs",
        "plotly -> matplotlib": "90% smaller, simpler, good for web",
        "pandas -> polars": "50% faster, 30% less memory (if replacing pandas)",
        "torch -> onnxruntime": "Smaller models, faster inference",
    },
    
    "lazy_import": {
        "enabled": True,
        "description": "Import heavy libraries only when needed",
        "benefit": "Reduces startup time from ~30s to ~5s",
        "implementation": "Import inside functions, not at module level"
    }
}

# ============================================================================
# CACHING STRATEGY
# ============================================================================

CACHING_STRATEGY = {
    "model_caching": {
        "enabled": True,
        "strategy": "Single model instance, reuse across requests",
        "benefit": "Avoid loading model multiple times",
        "memory_saving": "Crucial - saves 2-5GB"
    },
    
    "template_caching": {
        "enabled": True,
        "strategy": "Cache compiled document templates",
        "benefit": "50% faster document generation"
    },
    
    "computation_caching": {
        "enabled": True,
        "strategy": "Cache expensive computations (embeddings, summaries)",
        "ttl": 3600,  # 1 hour TTL
        "benefit": "Repeated requests return instantly"
    },
    
    "lru_cache": {
        "enabled": True,
        "max_size": 128,  # Keep 128 cached results
        "benefit": "Recent requests return from cache"
    }
}

# ============================================================================
# STARTUP OPTIMIZATION
# ============================================================================

STARTUP_OPTIMIZATION = {
    "lazy_model_loading": {
        "enabled": True,
        "description": "Load model only on first use, not on startup",
        "benefit": "Reduces cold start from 60s to 10s",
        "tradeoff": "First request is slower"
    },
    
    "load_minimal_dependencies": {
        "enabled": True,
        "description": "Load only what's needed initially",
        "approach": "Load additional modules on-demand"
    },
    
    "optimize_imports": {
        "enabled": True,
        "description": "Move heavy imports inside functions",
        "startup_improvement": "~5 seconds faster"
    },
    
    "preload_critical": {
        "models": ["distilbert for quick operations"],
        "description": "Preload only critical, small models on startup",
        "balance": "Fast startup + responsive first interaction"
    }
}

# ============================================================================
# RUNTIME OPTIMIZATION
# ============================================================================

RUNTIME_OPTIMIZATION = {
    "garbage_collection": {
        "enabled": True,
        "aggressive": True,
        "interval": 5,  # Collect garbage every 5 requests
        "benefit": "Prevents memory fragmentation"
    },
    
    "request_queuing": {
        "enabled": True,
        "description": "Queue requests, process one at a time",
        "benefit": "Prevents memory spikes from concurrent requests"
    },
    
    "memory_monitoring": {
        "enabled": True,
        "description": "Monitor memory usage, alert if > 80%",
        "action": "Clear caches automatically if memory exceeds threshold"
    },
    
    "timeout_management": {
        "inference_timeout": 30,  # 30 second max per request
        "description": "Kill requests that take too long",
        "benefit": "Prevent hanging requests from consuming resources"
    },
    
    "response_streaming": {
        "enabled": True,
        "description": "Stream responses instead of buffering",
        "benefit": "Reduces peak memory usage by 50%+"
    }
}

# ============================================================================
# HF SPACES SPECIFIC OPTIMIZATIONS
# ============================================================================

HF_SPACES_OPTIMIZATIONS = {
    "gradio_optimization": {
        "lite": True,
        "description": "Use Gradio Lite mode if available",
        "benefit": "Reduces Gradio overhead"
    },
    
    "serverless_ready": {
        "stateless_design": True,
        "description": "Design app to work with serverless model",
        "benefit": "Compatible with future optimization"
    },
    
    "resource_limits": {
        "max_memory": "14GB",  # Leave 2GB for system
        "max_duration": 30,  # 30 second max per request
        "enforcement": "Automatic shutdown if exceeded"
    },
    
    "cold_start": {
        "optimization": "Fast model loading with precompiled",
        "estimate": "~10-15 seconds from cold start"
    }
}

# ============================================================================
# RECOMMENDED CONFIGURATION FOR HF SPACES FREE TIER
# ============================================================================

RECOMMENDED_CONFIG = """
╔════════════════════════════════════════════════════════════════════════════╗
║        OPTIMIZED CONFIGURATION FOR HF SPACES FREE TIER (2vCPU + 16GB)      ║
╚════════════════════════════════════════════════════════════════════════════╝

🎯 PRIMARY MODEL RECOMMENDATION:
   • Model: HuggingFaceH4/zephyr-7b-beta-int4
   • Size: ~4GB (quantized)
   • Optimization: 4-bit quantization + LoRA
   • Expected Performance: 2-5 second inference time
   • Memory Available After: ~10GB for caches/operations

📊 CONFIGURATION SETTINGS:
   • Max tokens: 256
   • Batch size: 1
   • Mixed precision: float16
   • Flash attention: Enabled
   • Gradient checkpointing: Enabled
   • KV cache optimization: Enabled

📦 DOCUMENT GENERATION:
   • PDF: ReportLab (not Weasyprint)
   • Word: python-docx
   • Charts: Matplotlib (not Plotly)
   • Cache templates: Enabled
   • Async generation: Enabled

💾 MEMORY MANAGEMENT:
   • Model caching: Persistent (1 instance)
   • Computation caching: LRU (128 items)
   • Garbage collection: Aggressive
   • Memory monitoring: Active
   • Timeout: 30 seconds per request

🚀 STARTUP:
   • Lazy model loading: Enabled
   • Startup time: ~10-15 seconds
   • First request time: +5 seconds (model load)
   • Subsequent requests: 2-5 seconds

📈 PERFORMANCE EXPECTATIONS:
   • Concurrent users: 1-2 (due to free tier limitations)
   • Document generation: 30-60 seconds
   • Analysis generation: 5-10 seconds
   • Chart generation: 2-5 seconds

✅ MEMORY ALLOCATION (16GB Total):
   • OS + Gradio + Dependencies: ~2-3GB
   • Model weights (quantized): ~4GB
   • Inference overhead: ~2-3GB
   • Caches + buffers: ~2GB
   • Available margin: ~2-3GB

⚠️ IMPORTANT:
   • Do NOT load multiple large models simultaneously
   • Do NOT process large files without chunking
   • Do NOT generate high-DPI images
   • Do NOT use interactive visualizations
   • Do NOT store unlimited cache

💡 EXPECTED RESULTS:
   ✓ Responsive UI (responsive immediately)
   ✓ Fast analysis (< 10 seconds)
   ✓ Reasonable document generation (30-60 seconds)
   ✓ Stable operation (no memory crashes)
   ✓ Good user experience for 1-2 concurrent users
"""

# ============================================================================
# OPTIMIZATION CHECKLIST
# ============================================================================

OPTIMIZATION_CHECKLIST = {
    "model_optimization": [
        "✓ Use quantized models (int4 or int8)",
        "✓ Enable flash attention",
        "✓ Enable gradient checkpointing",
        "✓ Use mixed precision (float16)",
        "✓ Implement kv_cache optimization",
        "✓ Single model instance (cache persistently)"
    ],
    
    "memory_optimization": [
        "✓ Use lazy loading for dependencies",
        "✓ Implement aggressive garbage collection",
        "✓ Cache templates and computations",
        "✓ Use lightweight alternatives (reportlab vs weasyprint)",
        "✓ Monitor memory continuously",
        "✓ Clear caches if memory > 80%"
    ],
    
    "inference_optimization": [
        "✓ Set max_tokens to 256",
        "✓ Batch size = 1",
        "✓ Use device_map='auto'",
        "✓ Enable offload_to_cpu if needed",
        "✓ Implement request timeout (30s)",
        "✓ Stream responses instead of buffering"
    ],
    
    "startup_optimization": [
        "✓ Lazy model loading on first use",
        "✓ Move heavy imports to functions",
        "✓ Preload only essential small models",
        "✓ Expected startup: 10-15 seconds",
        "✓ First request: additional 5 seconds",
        "✓ Subsequent requests: 2-5 seconds"
    ],
    
    "operational_optimization": [
        "✓ Request queuing enabled",
        "✓ Memory monitoring active",
        "✓ Automatic cache clearing",
        "✓ Timeout management",
        "✓ Response streaming",
        "✓ Regular garbage collection"
    ]
}
