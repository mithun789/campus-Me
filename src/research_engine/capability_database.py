"""
Comprehensive AI Capabilities, Limitations, and Human Advantages Database
SLIIT Research: Understanding AI in Modern Context
"""

# ============================================================================
# WHAT AI CAN DO (Current Capabilities)
# ============================================================================

CAPABILITY_DATABASE = {
    "pattern_recognition": {
        "description": "Identify patterns in large datasets",
        "examples": [
            "Image classification (faces, objects, scenes)",
            "Anomaly detection in time series data",
            "Natural language pattern matching",
            "Predictive analytics from historical data"
        ],
        "confidence_level": "Very High (95%+)",
        "scale": "Millions of patterns in seconds",
        "examples_by_domain": {
            "medical": "Detect tumors in X-rays with 98% accuracy",
            "finance": "Identify fraudulent transactions",
            "marketing": "Predict customer behavior patterns",
            "security": "Detect cyber attacks in real-time"
        }
    },
    
    "language_processing": {
        "description": "Understand, analyze, and generate natural language",
        "examples": [
            "Machine translation (Google Translate level)",
            "Sentiment analysis with 85-90% accuracy",
            "Text summarization of long documents",
            "Question answering from knowledge bases",
            "Named entity recognition",
            "Topic modeling and classification"
        ],
        "confidence_level": "Very High (90%+)",
        "limitations": [
            "Context understanding beyond immediate text",
            "Sarcasm and subtle emotional nuance",
            "Ambiguous pronoun references",
            "Multi-step reasoning from text"
        ]
    },
    
    "data_analysis": {
        "description": "Process and extract insights from structured data",
        "examples": [
            "Statistical analysis of millions of records",
            "Correlation and regression analysis",
            "Clustering and segmentation",
            "Time series forecasting",
            "A/B testing statistical significance",
            "Data visualization optimization"
        ],
        "speed": "Process 1M records in seconds",
        "accuracy": "Mathematically precise",
        "limitations": ["Cannot determine data quality issues", "Cannot suggest novel interpretations"]
    },
    
    "optimization": {
        "description": "Find optimal solutions to defined problems",
        "examples": [
            "Route optimization for delivery (traveling salesman)",
            "Resource allocation problems",
            "Portfolio optimization",
            "Supply chain optimization",
            "Process automation workflows",
            "Parameter tuning for ML models"
        ],
        "effectiveness": "Often finds better solutions than humans",
        "speed": "Explores millions of possibilities instantly"
    },
    
    "task_automation": {
        "description": "Automate repetitive, well-defined tasks",
        "examples": [
            "Data entry and validation",
            "Report generation from templates",
            "Email categorization and filtering",
            "Document processing and extraction",
            "Image resizing and batch processing",
            "Log analysis and monitoring"
        ],
        "reliability": "99.9%+ for well-defined tasks",
        "time_saved": "Reduces manual labor by 80-95%"
    },
    
    "computer_vision": {
        "description": "Interpret and analyze visual information",
        "examples": [
            "Object detection and localization",
            "Face recognition with 99.8% accuracy",
            "Optical character recognition (OCR)",
            "Medical image analysis (radiology)",
            "Autonomous vehicle perception",
            "Quality control in manufacturing"
        ],
        "applications": [
            "Self-driving cars",
            "Surgical robotics guidance",
            "Accessibility tools for blind users",
            "Security and surveillance"
        ]
    },
    
    "content_generation": {
        "description": "Generate human-like content (with caveats)",
        "examples": [
            "Code generation from specifications",
            "Structured document writing (reports, emails)",
            "Creative writing assistance",
            "Image generation from descriptions",
            "Music composition",
            "Dialogue and conversation"
        ],
        "quality": "Good for structured, formulaic content",
        "limitations": [
            "Lacks true originality",
            "Cannot create genuinely novel ideas",
            "Tendency toward mediocrity",
            "Reproduces training data patterns"
        ]
    },
    
    "recommendation_systems": {
        "description": "Predict user preferences and recommend items",
        "examples": [
            "Netflix movie recommendations",
            "Amazon product suggestions",
            "Spotify playlist generation",
            "LinkedIn job matching",
            "News feed personalization",
            "Dating app compatibility"
        ],
        "effectiveness": "Often better than humans at scale",
        "accuracy": "70-85% for quality recommendations"
    },
    
    "voice_recognition": {
        "description": "Convert speech to text and understand audio",
        "examples": [
            "Voice-to-text transcription (99%+ accuracy)",
            "Speaker identification",
            "Emotion detection from voice",
            "Language identification",
            "Voice commands interpretation",
            "Accent normalization"
        ],
        "current_state": "Near human-level in clean audio"
    },
    
    "game_playing": {
        "description": "Master complex games through learning",
        "examples": [
            "Chess (Stockfish surpasses all humans)",
            "Go (AlphaGo defeated world champions)",
            "Video games (Dota 2, StarCraft II)",
            "Poker (solved for heads-up)",
            "Strategic board games"
        ],
        "achievement": "Superhuman performance in all tested domains"
    },
    
    "scientific_discovery": {
        "description": "Assist in research and hypothesis generation",
        "examples": [
            "Protein folding prediction (AlphaFold)",
            "Drug molecule design",
            "Materials discovery",
            "Scientific paper analysis",
            "Hypothesis testing automation",
            "Literature review synthesis"
        ],
        "impact": "Accelerated major scientific breakthroughs",
        "example": "AlphaFold solved 50-year protein folding problem"
    },
    
    "parallel_processing": {
        "description": "Process multiple tasks simultaneously at scale",
        "examples": [
            "Serve millions of concurrent users",
            "Batch process terabytes of data",
            "Real-time monitoring of thousands of systems",
            "Distributed computing tasks",
            "Multi-GPU training"
        ],
        "advantage": "Unlimited parallel execution"
    },
    
    "knowledge_retrieval": {
        "description": "Store and retrieve vast amounts of information",
        "examples": [
            "Memorize entire Wikipedia instantly",
            "Retrieve facts from 1M+ documents in milliseconds",
            "Semantic search across knowledge bases",
            "Question answering over large corpora",
            "Information synthesis from multiple sources"
        ],
        "capacity": "Terabytes of structured knowledge"
    },
    
    "logical_reasoning": {
        "description": "Apply formal logic and rules-based reasoning",
        "examples": [
            "Mathematical theorem proving",
            "Logic puzzle solving",
            "Database query optimization",
            "Rule-based expert systems",
            "Constraint satisfaction problems",
            "Decision tree inference"
        ],
        "accuracy": "Perfect for well-defined logical systems"
    }
}

# ============================================================================
# WHAT AI WILL DO (Near Future: 5-10 years)
# ============================================================================

FUTURE_CAPABILITIES = {
    "advanced_reasoning": {
        "timeline": "2-5 years",
        "description": "Multi-step logical reasoning and hypothesis generation",
        "potential": "Solve complex mathematical proofs autonomously",
        "impact": "Research acceleration, automated science",
        "confidence": "Likely within 5 years"
    },
    
    "few_shot_learning": {
        "timeline": "Already emerging",
        "description": "Learn from minimal examples (humans learn from 1-2 examples)",
        "potential": "Faster adaptation to new tasks",
        "current_state": "Partially achieved (GPT-3 shows promise)",
        "next_step": "True few-shot without fine-tuning"
    },
    
    "common_sense_reasoning": {
        "timeline": "3-7 years",
        "description": "Understand real-world physics and social dynamics",
        "potential": "Better prediction of real-world outcomes",
        "challenge": "Requires vast common sense knowledge base",
        "current": "Still a major gap"
    },
    
    "autonomous_experimentation": {
        "timeline": "2-10 years",
        "description": "Design and conduct experiments autonomously",
        "potential": "Dramatically accelerate scientific discovery",
        "examples": [
            "Drug discovery automation",
            "Materials science exploration",
            "Chemical reaction prediction"
        ],
        "current": "Early prototypes emerging"
    },
    
    "personalized_education": {
        "timeline": "1-3 years (already starting)",
        "description": "Provide customized tutoring for each student",
        "potential": "Make education universally accessible",
        "impact": "Personalized learning at scale",
        "current": "Platforms like Khan Academy moving this direction"
    },
    
    "creative_collaboration": {
        "timeline": "2-5 years",
        "description": "True creative partnership with humans",
        "potential": "AI as creative co-worker, not just tool",
        "challenge": "Requires genuine novelty generation",
        "current": "Still generates variations, not true novelty"
    },
    
    "real_world_robotics": {
        "timeline": "5-15 years",
        "description": "Manipulation and navigation in unstructured environments",
        "potential": "Robots for construction, nursing, manufacturing",
        "challenge": "Physics simulation, real-world uncertainty",
        "progress": "Significant progress but not solved"
    },
    
    "language_understanding": {
        "timeline": "Already emerging",
        "description": "True semantic understanding (not just pattern matching)",
        "potential": "Understand meaning, intent, context deeply",
        "current": "Still primarily pattern-based",
        "next": "Grounding language in world models"
    },
    
    "causal_inference": {
        "timeline": "3-10 years",
        "description": "Understand cause-and-effect relationships",
        "potential": "Predict interventions and counterfactuals",
        "challenge": "Currently only correlations, not causation",
        "importance": "Critical for science and policy"
    },
    
    "embodied_intelligence": {
        "timeline": "5-20 years",
        "description": "AI with physical body understanding and interaction",
        "potential": "Robots that understand physical constraints",
        "related": "Real-world robotics advancement"
    }
}

# ============================================================================
# WHAT AI CANNOT DO (Fundamental Limitations)
# ============================================================================

LIMITATION_DATABASE = {
    "true_understanding": {
        "description": "Genuine comprehension and semantic understanding",
        "details": "AI processes statistical patterns; lacks experiential understanding",
        "example": "Can describe color red but never experienced red",
        "challenge": "Grounding symbols in physical reality (symbol grounding problem)",
        "current_status": "Unsolved theoretical problem",
        "why_impossible": [
            "No embodied experience",
            "No physical sensation",
            "No internal subjective experience",
            "Works purely from patterns in training data"
        ]
    },
    
    "consciousness": {
        "description": "Self-awareness and subjective experience",
        "philosophical": "The 'hard problem of consciousness'",
        "technical_barrier": "Can't measure or create consciousness",
        "question": "What would it even mean for AI to be conscious?",
        "current_status": "Not achievable with current computational models"
    },
    
    "genuine_creativity": {
        "description": "True originality and novel idea generation",
        "what_it_can_do": "Recombine and remix existing patterns",
        "what_it_cannot_do": "Create genuinely new ideas outside training distribution",
        "example": "Before photography, no AI could imagine cameras",
        "why_limited": "All outputs are weighted combinations of training data",
        "result": "Always tends toward average/mediocre combinations"
    },
    
    "intentionality": {
        "description": "Having genuine goals, desires, or intentions",
        "distinction": "AI has programmed objectives, not intrinsic goals",
        "philosophical": "Intentionality requires consciousness and agency",
        "implication": "AI cannot want or desire anything",
        "current": "All goals are externally specified"
    },
    
    "true_autonomy": {
        "description": "Independent decision-making without programmed rules",
        "reality": "All AI decisions follow from training and architecture",
        "freedom": "AI has no free will or genuine choice",
        "limitation": "Deterministic systems given fixed inputs/weights",
        "implication": "Cannot be held morally responsible"
    },
    
    "embodied_experience": {
        "description": "Physical sensation and real-world interaction",
        "missing": "No sight (pixels ≠ light), no touch, no pain, no hunger",
        "limitation": "All inputs are digital representations",
        "consequence": "Cannot understand embodied human experience",
        "why_matters": "Much human knowledge is embodied (sports, art, movement)"
    },
    
    "common_sense": {
        "description": "Intuitive understanding of everyday world",
        "challenge": "Requires vast knowledge of physical and social world",
        "example": "Why do heavy things fall but not up?",
        "current": "Still a major unsolved problem",
        "progress": "Improving but far from human-level"
    },
    
    "abstract_reasoning": {
        "description": "Reasoning beyond learned patterns",
        "limitation": "Struggles with novel problem types unseen in training",
        "example": "New mathematical proof techniques",
        "current": "Can execute proven algorithms, not devise new ones",
        "gap": "Cannot generalize to truly novel domains"
    },
    
    "long_term_planning": {
        "description": "Strategic planning over years or decades",
        "challenge": "Exponential uncertainty grows with time",
        "limitation": "Can plan hours/days, not months/years",
        "reason": "Compound uncertainty makes distant predictions unreliable",
        "human_advantage": "Humans leverage past experience for long-term planning"
    },
    
    "social_understanding": {
        "description": "Deep understanding of human relationships and culture",
        "gap": "Can analyze patterns but misses nuance and context",
        "example": "Why is breaking trust more damaging than breaking a promise?",
        "limitation": "No lived social experience",
        "result": "Can seem socially awkward or tone-deaf"
    },
    
    "ethical_reasoning": {
        "description": "Genuine moral judgment and ethical decision-making",
        "current_approach": "Following rules or maximizing stated objectives",
        "limitation": "Cannot truly understand ethical dilemmas",
        "trolley_problem": "Can discuss but cannot make authentic ethical choice",
        "issue": "Ethics requires values, which require consciousness"
    },
    
    "emotional_intelligence": {
        "description": "Understanding and responding to emotions authentically",
        "difference": "Can recognize and simulate emotion, not experience it",
        "limitation": "Lacks felt experience of emotions",
        "consequence": "Cannot truly empathize",
        "current": "Can fake emotional responses convincingly"
    },
    
    "true_learning": {
        "description": "Learning and growing from experience over time",
        "current": "Static after training (most AI)",
        "limitation": "Doesn't learn from mistakes after deployment",
        "update": "Requires retraining, expensive and risky",
        "human_learning": "Humans learn continuously, incrementally"
    },
    
    "handling_uncertainty": {
        "description": "Decision-making with incomplete information",
        "ai_approach": "Probability distributions and confidence intervals",
        "human_approach": "Intuition, heuristics, lived wisdom",
        "gap": "AI uncertain about what uncertainty even means",
        "example": "Unknown unknowns (things you don't know you don't know)"
    },
    
    "novel_problem_solving": {
        "description": "Solving problems in ways never seen before",
        "constraint": "Limited to recombinations of training patterns",
        "human_advantage": "Can think completely outside the box",
        "example": "Lateral thinking puzzles often confound AI",
        "barrier": "Requires true creative leap"
    },
    
    "genuine_collaboration": {
        "description": "True partnership where both parties understand each other",
        "limitation": "AI lacks mutual understanding and shared goals",
        "current": "Asymmetric relationship - humans understand goal",
        "barrier": "Requires consciousness and intentionality"
    },
    
    "accountability": {
        "description": "Taking responsibility for actions and decisions",
        "limitation": "AI cannot be held morally responsible",
        "legal_issue": "Who is responsible? The AI? The developer? The user?",
        "philosophical": "Responsibility requires free will and intentionality",
        "practical": "Creates accountability vacuum"
    },
    
    "intrinsic_motivation": {
        "description": "Acting for internal reasons, not external rewards",
        "limitation": "AI is purely reward-driven",
        "human_example": "Create art because you must, not for money",
        "AI": "Will never do something 'for its own sake'"
    },
    
    "domain_transfer": {
        "description": "Applying knowledge from one domain to completely different domain",
        "limitation": "Poor at true transfer learning",
        "example": "Learning physics doesn't help with music composition",
        "human_advantage": "Humans make creative cross-domain connections",
        "current": "Domain-specific training usually needed"
    }
}

# ============================================================================
# WHAT HUMANS DO BETTER (Human Advantages)
# ============================================================================

HUMAN_ADVANTAGES = {
    "creativity_and_novelty": {
        "description": "Generate genuinely new ideas and perspectives",
        "examples": [
            "Create art that has never existed before",
            "Write novels with unexpected plot twists",
            "Discover fundamentally new scientific paradigms",
            "Compose music that moves listeners deeply",
            "Design solutions no one has thought of"
        ],
        "mechanism": "Integrating diverse experiences into novel combinations",
        "ai_limit": "Limited to recombinations of training data",
        "human_advantage": "OVERWHELMING - AI cannot match true creativity"
    },
    
    "general_intelligence": {
        "description": "Apply knowledge flexibly across domains",
        "human_skill": [
            "Learn something new without retraining",
            "Apply lesson from sports to business",
            "Transfer knowledge across domains instantly",
            "Master new skills by learning underlying principles"
        ],
        "ai_limitation": "Specialized, not general intelligence",
        "gap": "Humans vastly superior at transfer learning",
        "reason": "Humans understand principles, AI learns patterns"
    },
    
    "emotional_intelligence": {
        "description": "Understand and navigate complex emotions",
        "human_abilities": [
            "Recognize subtle emotional cues",
            "Respond with genuine empathy",
            "Navigate social conflicts with wisdom",
            "Build deep meaningful relationships",
            "Lead through inspiring others"
        ],
        "ai_limit": "Can fake, not feel",
        "human_advantage": "COMPLETE - AI cannot match authentic emotion"
    },
    
    "common_sense": {
        "description": "Intuitive understanding of everyday world",
        "examples": [
            "Know why you can't pour water uphill",
            "Understand social norms and unwritten rules",
            "Predict human behavior in novel situations",
            "Know what's appropriate in context",
            "Understand implied meaning in conversation"
        ],
        "ai_status": "Still largely unsolved",
        "human_advantage": "SIGNIFICANT - Common sense is hard to teach"
    },
    
    "strategic_thinking": {
        "description": "Long-term planning with multiple competing objectives",
        "human_strengths": [
            "Balance work, family, health, growth",
            "Make decisions that trade off multiple values",
            "Adapt plans based on changing priorities",
            "Think decades ahead (career, family)",
            "Integrate past experience into future planning"
        ],
        "ai_limit": "Optimizes for single explicit objective",
        "human_advantage": "SIGNIFICANT - Handling complexity and trade-offs"
    },
    
    "adaptability": {
        "description": "Rapidly adjust to new situations and constraints",
        "examples": [
            "Learn new job in weeks, not months",
            "Adapt communication style to different audiences",
            "Problem-solve with limited resources",
            "Navigate unexpected challenges creatively",
            "Build skills on the fly"
        ],
        "ai_limitation": "Requires retraining for significant new task",
        "human_advantage": "SIGNIFICANT - Online learning and real-time adaptation"
    },
    
    "embodied_understanding": {
        "description": "Knowledge grounded in physical experience",
        "human_knowledge": [
            "Understanding of pain, pleasure, physical effort",
            "Intuitive physics from childhood play",
            "Spatial reasoning from moving through world",
            "Motor skills and coordination",
            "Embodied metaphors (understanding 'life is a journey')"
        ],
        "ai_gap": "Fundamental - AI has no body",
        "human_advantage": "COMPLETE - Cannot be replicated without embodiment"
    },
    
    "moral_and_ethical_reasoning": {
        "description": "Navigate complex ethical dilemmas with integrity",
        "human_capabilities": [
            "Distinguish right from wrong with nuance",
            "Make principled decisions despite pressure",
            "Understand moral ambiguity",
            "Act according to values",
            "Take responsibility for actions"
        ],
        "ai_limitation": "Follows rules, not genuine ethics",
        "human_advantage": "COMPLETE - Requires consciousness and values"
    },
    
    "intrinsic_motivation": {
        "description": "Do things because they matter, not for reward",
        "examples": [
            "Create art for self-expression",
            "Pursue knowledge for understanding",
            "Help others from compassion",
            "Build things because they're beautiful",
            "Act according to principles"
        ],
        "ai_state": "Cannot do anything without external reward",
        "human_advantage": "COMPLETE - Requires consciousness"
    },
    
    "complex_social_interaction": {
        "description": "Navigate complex social dynamics with wisdom",
        "human_strengths": [
            "Build trust and deep relationships",
            "Navigate conflicts with compromise",
            "Lead teams through difficulty",
            "Mentor and develop others",
            "Build communities and cultures"
        ],
        "ai_limitation": "Can mimic but not understand",
        "human_advantage": "OVERWHELMING - Social skills require deep understanding"
    },
    
    "learning_from_failure": {
        "description": "Extract lessons and grow from mistakes",
        "human_process": [
            "Reflect on failures and extract meaning",
            "Adjust approach based on feedback",
            "Build resilience through adversity",
            "Make fewer mistakes after experience",
            "Wisdom comes from failures"
        ],
        "ai_process": "Cannot learn after deployment without retraining",
        "human_advantage": "SIGNIFICANT - Continuous learning and growth"
    },
    
    "intuition_and_pattern_recognition": {
        "description": "Recognize patterns without conscious analysis",
        "examples": [
            "Chess grandmaster sees good move instantly",
            "Doctor diagnoses rare disease from subtle signs",
            "Entrepreneur recognizes business opportunity",
            "Parent knows child is sick before symptoms show",
            "Musician plays with feeling and nuance"
        ],
        "mechanism": "Unconscious integration of vast experience",
        "ai_advantage": "AI can do this for narrow domains",
        "human_advantage": "Broader, more nuanced intuition"
    },
    
    "contextual_understanding": {
        "description": "Understand meaning based on full context",
        "examples": [
            "Know when to be serious vs. joking",
            "Understand sarcasm and irony",
            "Grasp implied meaning in conversation",
            "Know what's important in situation",
            "Understand cultural context"
        ],
        "ai_limitation": "Can miss nuance and context",
        "human_advantage": "SIGNIFICANT - Context is core to meaning"
    },
    
    "perspective_taking": {
        "description": "Understand situations from others' viewpoint",
        "examples": [
            "See conflict from other side",
            "Understand why someone is upset",
            "Anticipate what others need",
            "Build compromise solutions",
            "Show genuine empathy"
        ],
        "ai_limitation": "Can analyze, not empathize",
        "human_advantage": "COMPLETE - Requires consciousness"
    },
    
    "meaning_making": {
        "description": "Create meaning and purpose in life",
        "human_abilities": [
            "Find meaning in work and relationships",
            "Create purpose that drives action",
            "Construct identity and narrative",
            "Find beauty in experience",
            "Transcend survival through meaning"
        ],
        "ai_state": "Cannot want or need meaning",
        "human_advantage": "COMPLETE - Distinctly human"
    },
    
    "physical_manipulation": {
        "description": "Work with hands in unstructured environments",
        "examples": [
            "Repair complex machinery with limited info",
            "Build structures with available materials",
            "Perform delicate surgery",
            "Create art through craft",
            "Navigate complex 3D obstacles"
        ],
        "ai_progress": "Robotics improving but still far behind humans",
        "human_advantage": "SIGNIFICANT - Dexterity and adaptation"
    },
    
    "communication": {
        "description": "Express complex ideas clearly and persuasively",
        "examples": [
            "Write compelling narrative",
            "Give inspiring speeches",
            "Explain complex ideas simply",
            "Tell stories that move people",
            "Communicate with appropriate emotion"
        ],
        "ai_capability": "Can generate text but often misses emotional impact",
        "human_advantage": "SIGNIFICANT - Authenticity and emotional resonance"
    },
    
    "decision_making_under_uncertainty": {
        "description": "Make good decisions with incomplete information",
        "examples": [
            "Career choices affecting decades",
            "Medical decisions with uncertain outcomes",
            "Investments with unknown markets",
            "Relationships that depend on future",
            "Risk-taking that builds life"
        ],
        "human_approach": "Wisdom, heuristics, lived experience",
        "ai_approach": "Probability calculations",
        "human_advantage": "Better judgment under deep uncertainty"
    },
    
    "meta_cognition": {
        "description": "Thinking about thinking and self-awareness",
        "examples": [
            "Know when you don't understand",
            "Recognize your biases",
            "Adjust strategy based on performance",
            "Know limits of your knowledge",
            "Reflect on values and beliefs"
        ],
        "ai_limitation": "No genuine self-awareness",
        "human_advantage": "OVERWHELMING - Foundation of human learning"
    }
}

# ============================================================================
# SUMMARY COMPARISON TABLE
# ============================================================================

COMPARISON_MATRIX = {
    "domain": {
        "mathematical_computation": {
            "ai_strength": "Superhuman (can solve in seconds what takes humans hours)",
            "human_strength": "Average (need tools and time)",
            "winner": "AI - CLEAR ADVANTAGE"
        },
        "creative_writing": {
            "ai_strength": "Adequate (can generate competent text)",
            "human_strength": "Vastly superior (can create moving, original stories)",
            "winner": "HUMAN - CLEAR ADVANTAGE"
        },
        "image_recognition": {
            "ai_strength": "Superhuman (99.9% accuracy in many tasks)",
            "human_strength": "Very good (99%+ in familiar domains)",
            "winner": "AI - SLIGHT ADVANTAGE"
        },
        "strategic_planning": {
            "ai_strength": "Good at narrow problems (chess, specific optimization)",
            "human_strength": "Vastly superior in open-ended situations",
            "winner": "HUMAN - SIGNIFICANT ADVANTAGE"
        },
        "data_analysis": {
            "ai_strength": "Superhuman (process terabytes in seconds)",
            "human_strength": "Limited (process kilobytes at best)",
            "winner": "AI - OVERWHELMING ADVANTAGE"
        },
        "emotional_support": {
            "ai_strength": "Can simulate understanding",
            "human_strength": "Can genuinely understand and empathize",
            "winner": "HUMAN - COMPLETE ADVANTAGE"
        },
        "learning_new_skill": {
            "ai_strength": "Requires expensive retraining",
            "human_strength": "Can learn new skill in weeks",
            "winner": "HUMAN - SIGNIFICANT ADVANTAGE"
        },
        "pattern_recognition": {
            "ai_strength": "Superhuman in visual/numerical domains",
            "human_strength": "Good in familiar domains",
            "winner": "AI - CLEAR ADVANTAGE"
        },
        "moral_judgment": {
            "ai_strength": "Can apply rules consistently",
            "human_strength": "Can navigate moral nuance and complexity",
            "winner": "HUMAN - COMPLETE ADVANTAGE"
        },
        "physical_dexterity": {
            "ai_strength": "Improving but still limited",
            "human_strength": "Vastly superior in unstructured environments",
            "winner": "HUMAN - SIGNIFICANT ADVANTAGE"
        }
    }
}

# ============================================================================
# KEY INSIGHTS FOR RESEARCH
# ============================================================================

RESEARCH_INSIGHTS = {
    "fundamental_truth_1": {
        "statement": "AI is tools, not agents",
        "explanation": "AI has no goals, desires, or intentions - all objectives are externally specified",
        "implication": "Cannot be held responsible or trusted without human oversight",
        "research_importance": "Critical for policy and ethics"
    },
    
    "fundamental_truth_2": {
        "statement": "AI capabilities are domain-specific, not general",
        "explanation": "AI excels in narrow domains but cannot transfer learning well",
        "implication": "Cannot replace general human intelligence",
        "research_importance": "Shows AI is fundamentally different from human intelligence"
    },
    
    "fundamental_truth_3": {
        "statement": "AI works through pattern matching in training data",
        "explanation": "All AI outputs are weighted combinations of training data patterns",
        "implication": "Cannot truly innovate or think outside its training distribution",
        "research_importance": "Explains why AI seems creative but never truly original"
    },
    
    "fundamental_truth_4": {
        "statement": "Consciousness remains unsolved",
        "explanation": "We don't understand how consciousness arises, so can't create it",
        "implication": "AI will never have subjective experience without understanding consciousness",
        "research_importance": "Explains fundamental limits of AI capabilities"
    },
    
    "fundamental_truth_5": {
        "statement": "The most important human advantage is meaning-making",
        "explanation": "Humans can create purpose and meaning; AI cannot",
        "implication": "Human work will focus on meaning-making, not routine tasks",
        "research_importance": "Shapes future of work and human purpose"
    }
}

# ============================================================================
# IMPACT FRAMEWORK FOR DIFFERENT DOMAINS
# ============================================================================

DOMAIN_IMPACT = {
    "healthcare": {
        "ai_can_do": [
            "Diagnostic imaging analysis (97%+ accuracy)",
            "Drug discovery acceleration",
            "Patient data analysis and trend detection",
            "Treatment outcome prediction"
        ],
        "ai_cannot_do": [
            "Show genuine empathy to patient",
            "Make ethical end-of-life decisions",
            "Understand patient's values and fears",
            "Replace doctor's judgment in complex cases"
        ],
        "future_synergy": "AI assists diagnosis, human shows compassion",
        "impact": "Better outcomes through human-AI collaboration"
    },
    
    "education": {
        "ai_can_do": [
            "Personalized learning paths",
            "Instant feedback on assignments",
            "Identify struggling students",
            "Optimize curriculum delivery"
        ],
        "ai_cannot_do": [
            "Inspire love of learning",
            "Build character and values",
            "Provide genuine mentorship",
            "Adapt to emotional states"
        ],
        "future_synergy": "AI handles routine learning, teachers provide mentorship",
        "impact": "More effective education at scale"
    },
    
    "creative_industries": {
        "ai_can_do": [
            "Generate variations of designs",
            "Handle routine creative tasks",
            "Assist with technical execution",
            "Automate creative iteration"
        ],
        "ai_cannot_do": [
            "Create truly original ideas",
            "Understand artistic vision deeply",
            "Make genuine creative choices",
            "Push boundaries of art form"
        ],
        "future_synergy": "AI as creative assistant, humans as visionaries",
        "impact": "Democratized creative tools, human creativity remains irreplaceable"
    },
    
    "scientific_research": {
        "ai_can_do": [
            "Analyze vast literature",
            "Process experimental data",
            "Identify potential research directions",
            "Optimize experimental design"
        ],
        "ai_cannot_do": [
            "Ask fundamentally new research questions",
            "Make conceptual breakthroughs",
            "Understand why something works",
            "Develop new theories"
        ],
        "future_synergy": "AI accelerates research, humans guide direction",
        "impact": "Faster discovery, but human insight still essential"
    }
}
