GENRE_KEYWORDS = {
    "AI / Data / ML": [
        # Core ML/AI
        "machine-learning", "deep-learning", "artificial-intelligence", "ai",
        "neural-network", "neural-net", "training", "finetuning", "fine-tuning",
        "backprop", "backpropagation", "gradient-descent", "autograd", "micrograd",
        "pytorch", "torch", "tensorflow",
        
        # LLMs & Language Models
        "llm", "llms", "large-language-model", "language-model",
        "generative-ai", "transformer", "gpt", "gpt-2", "nanogpt",
        "qwen", "qwen3", "deepseek", "claude", "gemini",
        
        # Embeddings & RAG
        "embedding", "embeddings", "embedding-models",
        "rag", "retrieval-augmented-generation", "vector-search", "semantic-search",
        "reranking", "knowledge-base",
        
        # Computer Vision
        "computer-vision", "vision", "object-detection", "instance-segmentation",
        "ocr", "document-parsing", "document-ai", "pdf-extractor-rag",
        
        # Multimodal
        "multimodal", "multimodal-llm", "vlm", "vision-language-model",
        "text-to-speech", "speech-to-text", "asr", "tts",
        
        # Agents
        "agent", "agents", "ai-agents", "agentic", "multi-agent",
        "autonomous-ai-agents", "reinforcement-learning",
        
        # Trading/Finance ML
        "trading-agent", "algorithmic-trading", "quantitative-trading",
        "backtesting", "financial-trading",
        
        # Specialized
        "forecasting", "timeseries", "time-series",
        "medical-image-computing", "healthcare-imaging",
        "foundation-models", "pretrained-models", "sota",
        
        # Performance
        "flashattention", "flash-attention", "gpu-kernel", "cuda-kernel",
        "kernel-fusion", "tvm", "high-performance-kernels",
        
        # Edge ML
        "edge-machine-learning", "tinyml", "embedded-ml",
        
        # Evaluation
        "mlops", "evaluation", "model-eval", "prompt-engineering"
    ],

    "Systems / Embedded / Robotics": [
        # Embedded/Hardware
        "firmware", "embedded", "microcontroller", "mcu", "stm32",
        "risc-v", "riscv", "raspberry-pi", "jetson",
        "rtos", "realtime",
        
        # Robotics
        "robot", "robotics", "robot-arm", "humanoid", "manipulator",
        "servo", "actuator", "kinematics", "so-arm100",
        "ros", "ros2", "moveit", "gazebo", "urdf",
        "drone", "uav", "mavlink",
        
        # Systems/OS
        "wayland", "wayland-compositor", "window-manager", "tiling-window-manager",
        "browser-engine", "servo", "webengine",
        
        # Low-level
        "cpp", "cplusplus", "c-plus-plus", "aarch64", "arm32"
    ],

    "Web / Mobile / Application Development": [
        # Frontend Frameworks
        "react", "react-native", "nextjs", "next.js", "vue", "vuejs",
        "svelte", "sveltekit", "angular",
        
        # Web Tech
        "typescript", "javascript", "tailwindcss", "vite", "webpack",
        "spa", "single-page-app", "ssr", "frontend", "fullstack",
        
        # UI Components
        "design-systems", "ui-component", "web-components", "storybook",
        
        # Mobile/Desktop
        "electron", "tauri", "pwa", "mobile-game",
        
        # Application Types
        "note-taking", "whiteboard", "notion-alternative",
        "game-development", "tower-defense",
        
        # Networking
        "websocket", "graphql", "rest-api", "api-client"
    ],

    "DevOps / Infrastructure / Cloud": [
        # Containers & Orchestration
        "docker", "dockerfile", "kubernetes", "k8s", "helm",
        "container", "containers",
        
        # Cloud Platforms
        "aws", "amazon-web-services", "eks", "ecs", "lambda",
        "cloudformation", "s3", "ec2", "rds", "route53",
        
        # IaC & Automation
        "terraform", "ansible", "infrastructure-as-code",
        "ci-cd", "cicd", "github-actions", "pipeline",
        
        # Storage
        "object-storage", "s3-storage", "distributed-storage",
        "seaweedfs", "fuse",
        
        # Monitoring
        "monitoring", "observability", "opentelemetry", "metrics",
        "uptime-monitoring",
        
        # Secrets & PKI
        "vault", "secret-management", "certificate-management", "pki",
        
        # Databases (operational)
        "postgres", "postgresql", "duckdb",
        
        # General
        "cloudnative", "scalability", "cluster", "deployment"
    ],

    "Security / Networking": [
        # Security
        "security", "pentest", "pentesting", "vulnerability",
        "exploit", "nuclei", "bugbounty",
        
        # Auth & Crypto
        "authentication", "oauth", "jwt", "mfa", "rbac",
        "encryption", "cryptography", "tls", "ssl",
        
        # OSINT
        "osint", "reconnaissance", "fingerprinting",
        "social-analyzer", "information-gathering",
        
        # Network
        "dns", "subdomain", "cloudflare",
        
        # Blockchain/Web3
        "blockchain", "cryptocurrency", "bitcoin", "web3",
        "stablecoin", "onchain-payment", "smart-contracts",
        
        # Privacy & Protection
        "privacy", "watermark", "digital-watermark", "steganography",
        
        # Payment Protocol
        "http-402", "402-payment-required", "x402", "payment-protocol"
    ],

    "Data Platforms / Backend Services / Integrations": [
        # Backend
        "backend", "microservice", "middleware", "fullstack",
        
        # Databases
        "database", "relational-database", "vector-database",
        
        # APIs & Integration
        "api-route", "grpc", "graphql", "webhook",
        "integration", "adapter",
        
        # Messaging & Pipelines
        "message-broker", "kafka", "mqtt",
        "etl", "pipeline", "ingestion",
        
        # Storage
        "object-storage", "distributed-storage",
        
        # Platforms
        "ecommerce", "ecommerce-platform",
        "collaboration", "file-sharing", "nextcloud",
        
        # Deployment
        "self-hosted", "selfhosted", "edge-runtime",
        "nitro", "server-toolkit", "deploy-anywhere"
    ],

    "CLI / Utilities / Developer Tools": [
        # CLI/Shell
        "cli", "command-line", "terminal", "shell", "bash", "zsh",
        
        # Version Control
        "git", "jujutsu", "vcs",
        
        # Version Managers
        "mise", "nvm", "version-manager", "runtime-manager",
        "asdf", "pyenv", "rbenv",
        
        # Dev Tools
        "developer-tools", "debugger", "static-analysis",
        "syntax-highlighting", "code-review",
        
        # Task Running
        "task-runner", "workflow-automation",
        
        # API Testing
        "api-client", "api-testing", "postman-alternative",
        "insomnia-alternative",
        
        # Workspace
        "editor", "wiki", "notes-app", "markdown",
        
        # Utilities
        "powertoys", "color-picker", "command-palette",
        
        # AI Coding
        "coding-assistant", "agentic-coding-tool", "claude-code"
    ],

    "Libraries / SDKs / Framework Components": [
        # SDK/Library
        "sdk", "client-library", "wrapper", "library",
        "package", "module", "npm-install",
        
        # Framework Components
        "react-component", "vue-component", "web-components",
        "ui-component", "design-systems",
        
        # State & Routing
        "state-management", "router", "routing",
        
        # Specific Libraries
        "monai", "onnx", "header-only"
    ],

    "Research / Experiments / Demos": [
        # Research
        "research", "paper", "arxiv", "experiment", "experimental",
        "prototype", "proof-of-concept", "baseline", "benchmark",
        "ablation", "evaluation",
        
        # Curated Lists
        "awesome", "awesome-list", "resource", "resources",
        
        # Roadmaps
        "roadmap", "developer-roadmap", "frontend-roadmap",
        "backend-roadmap", "devops-roadmap",
        
        # AI Research
        "brain-inspired-ai", "human-in-the-loop",
        "in-context-reinforcement-learning",
        
        # Interactive
        "notebook", "jupyter", "colab-notebook",
        "cookbook", "recipe", "interactive-tutorial"
    ],

    "Education / Tutorials / Docs": [
        # Learning
        "tutorial", "course", "textbook", "courseware",
        "learn", "learning", "teaching", "education",
        "beginner", "beginners",
        
        # Structured Learning
        "step-by-step", "walkthrough", "quickstart",
        "getting-started", "zero-to-hero",
        "30-days", "30-days-of",
        
        # Practice
        "practice", "exercise", "lab-exercise",
        "interview-questions", "algorithm-competitions",
        
        # Documentation
        "guide", "documentation", "how-to",
        "presentation", "slides",
        
        # Resources
        "resource", "resources", "books", "audiobooks",
        
        # Specific
        "aws-tutorial", "aws-zero-to-hero",
        "real-time-project", "job-preparation",
        "from-scratch", "cookbook", "recipes"
    ]
}

score_cols = [
    "AI / Data / ML",
    "Systems / Embedded / Robotics",
    "Web / Mobile / Application Development",
    "DevOps / Infrastructure / Cloud",
    "Security / Networking",
    "Data Platforms / Backend Services / Integrations",
    "CLI / Utilities / Developer Tools",
    "Libraries / SDKs / Framework Components",
    "Research / Experiments / Demos",
    "Education / Tutorials / Docs"
]