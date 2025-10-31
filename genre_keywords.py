GENRE_KEYWORDS = {
    "AI / Data / ML": [
        # (original terms)
        "machine-learning", "deep-learning", "artificial-intelligence", "ai", "llm",
        "llms", "large-language-model", "large-language-models", "language-model",
        "generative-ai", "transformer", "embedding", "embeddings", "embedding-models",
        "rag", "retrieval-augmented-generation", "multi-modal-rag", "text-to-sql",
        "text2sql", "text-to-chart", "textbook", "courseware", "edge-machine-learning",
        "machine-learning-systems", "tinyml", "cloud-ml", "embedded-ml", "mobile-ml",
        "computer-vision", "vision", "object-detection", "instance-segmentation",
        "sota", "detr", "rf-detr", "ocr", "pp-ocr", "chineseocr", "document-parsing",
        "document-translation", "pdf-extractor-rag", "pdf2markdown", "pp-structure",
        "paddleocr-vl", "ai4science", "healthcare-imaging", "medical-image-computing",
        "medical-image-processing", "monai", "forecasting", "timeseries",
        "time-series", "time-series-forecasting", "pretrained-models",
        "foundation-models", "reasoning", "brain-inspired-ai",
        # (original agent / memory terms)
        "agent", "agents", "ai-agents", "agentic", "agentic-ai", "agentic-ai",
        "agent-computer-interface", "computer-use-agent", "computer-use", "gui-agents",
        "agentic-ai", "in-context-reinforcement-learning", "reinforcement-learning",
        "planning", "memory", "long-term-memory", "memory-management",
        "state-management", "mcp", "rag", "vector-search", "semantic-search",
        "reranking", "knowledge-base", "question-answering", "chatbot", "chatbots",
        "chatgpt", "gpt", "openai", "anthropic", "claude", "claude-code", "anthropic-claude",
        "gemini", "qwen", "deepseek", "ollama", "localai", "llamacpp",
        "proactive-ai", "context-engineering", "vision-language-model",
        "text-to-speech", "speech-to-text", "asr", "tts", "voice-cloning", "xtts",
        # (original mlops-ish)
        "mlops", "evaluation", "model-eval", "human-in-the-loop", "humanlayer",
        "prompt-engineering", "mllm", "multimodel",
        # (new additions)
        "gpt-2", "nanogpt",
        "qwen3", "qwen3-vl",
        "multimodal", "multimodal-llm", "vlm",
        "state-of-the-art",
        "training", "finetuning", "fine-tuning",
        "from scratch", "neural network", "neural-net",
        "backprop", "backpropagation", "gradient descent",
        "autograd", "tiny autograd engine", "micrograd",
        "pytorch", "torch", "pytorch-like api",
        # multi-agent / trading agents
        "multi-agent", "multi-agents", "agentic coding", "coding agent",
        "agentic coding tool", "agentic coding assistant",
        "autonomous ai agents", "autonomous trading agent",
        "trading agent", "trading-agents",
        "algorithmic trading", "financial trading", "quant", "quantitative trading",
        "stock trading", "backtest", "backtesting",
        # OCR / PDF cleanup variants
        "pdf-to-text", "pdf parsing", "pdf linearization",
        # high-perf AI kernels / compiler DSLs
        "flashattention", "flash-attention", "linearattention",
        "high-performance kernels", "gpu kernel", "cuda kernel",
        "kernel fusion", "tvm", "compiler", "dsl for kernels",
        "tilelang", "tile-lang", "tile language",
        "accelerator kernels", "gpu acceleration", "npu",
        # eval / prompt eng extras
        "prompt engineering", "agentic coding tool",
        # watermarking / stego
        "image-processing", "watermark", "blind-watermark",
        "invisible-watermark", "digital-watermark", "steganography"
    ],

    "Systems / Embedded / Robotics": [
        # (original embedded / hardware / low-level systems)
        "firmware", "embedded", "embedded-ml", "microcontroller", "mcu", "stm32",
        "register map", "risc-v", "arm32", "aarch64", "riscv", "raspberry-pi",
        "jetson", "edge-machine-learning", "realtime", "rtos", "pid", "pid controller",
        "sensor fusion", "uav", "drone", "mavlink",
        # (original OS / system tooling)
        "wayland-compositor", "wayland", "tiling-window-manager", "window-manager",
        "webengine", "webplatform", "webbrowser", "servo", "browser-engine",
        "browser", "browser-engine", "browser-automation", "computer-automation",
        "computer-use", "desktop", "desktop-app", "desktop-application",
        "desktop-apps", "cross-platform", "multiplatform", "application",
        "app", "apps", "software", "windows", "windows-10", "windows-11",
        "mac", "macos", "macosx", "mac-osx", "macos-app", "macos-apps",
        "linux", "ios", "android", "raspberry-pi", "lazarus", "object-pascal",
        "cpp", "cplusplus", "c-plus-plus", "cpp11", "csharp", "dotnet", "mfc",
        "onnx", "vits", "aarch64", "arm32",
        # (original power tools)
        "powertoys", "microsoft-powertoys", "fancyzones", "keyboard-manager",
        "command-palette", "color-picker", "windows-terminal", "terminal",
        "console", "cmd", "wsl",
        # (new robotics-specific terms)
        "robot", "robotics", "robot arm", "humanoid", "humanoid robot",
        "manipulator", "servo", "actuator", "kinematics",
        "so-arm100", "so-100", "so-101", "the-robot-studio",
        "ros", "ros2", "moveit", "gazebo", "urdf"
    ],

    "Web / Mobile / Application Development": [
        # (original web / frontend / app terms)
        "webapp", "web", "single-page-app", "spa", "responsive", "frontend",
        "react", "react-native", "nextjs", "next.js", "typescript", "javascript",
        "tailwindcss", "svelte", "svelte-kit", "sveltekit", "vue", "vuejs",
        "vueuse", "vite", "webpack", "storybook", "design-systems", "components",
        "ui", "ui component", "styleguide", "web-components", "stories",
        "router", "routing", "route", "state-management", "ssr",
        "fullstack", "framework", "frameworks", "typescript", "typescript",
        "vercel",
        # (original app/platform terms)
        "mobile-game", "tower-defense", "rts", "sandbox-game", "mindustry",
        "game", "game-development", "desktop-app", "desktop-apps",
        "note-taking", "notes-app", "assistant", "wiki", "notes", "markdown",
        "whiteboard", "tableview", "workspace", "notion", "notion-alternative",
        "miro",
        # (original runtimes / shells)
        "electron", "tauri", "tauri-v2", "pwa", "websocket", "socket-io",
        "http", "https", "http-client", "sse", "rpc", "grpc", "graphql",
        "api-client", "api-rest", "rest-api", "rest", "api", "server-functions",
        "searchparams", "url",
        # (original hosting)
        "selfhosted", "self-hosted", "self-hosting",
        # (new server / edge terms for nitro)
        "server toolkit", "server-toolkit", "zero-config server",
        "deploy anywhere", "edge runtime", "edge deployment",
        "server routes", "api routes", "nitro", "nitrojs"
    ],

    "DevOps / Infrastructure / Cloud": [
        # (original containers / orchestration / infra)
        "docker", "dockerfile", "docker-compose", "container", "containers",
        "kubernetes", "k8s", "cncf", "helm", "helm chart", "chart", "charts",
        "distributed-systems", "multi-tenant", "multi-cloud", "multi-cloud-kubernetes",
        "cloud", "cloudnative", "cloudstorage", "cloud-drive", "s3", "amazon-s3",
        "objectstorage", "object-storage", "s3-storage", "storage", "tiered-file-system",
        "distributed-file-system", "distributed-storage", "replication", "fuse",
        "erasure-coding", "blob-storage", "hdfs", "hadoop-hdfs", "seaweedfs",
        "posix", "posix-compliant",
        "virtualization", "rdp",
        "uptime", "uptime-monitoring", "monitor", "monitoring", "metrics",
        "telemetry", "observability", "opentelemetry", "open-telemetry",
        "github-actions", "pipeline", "ci/cd", "workflow", "automation",
        "mlops", "deployment", "cluster", "scalability", "infrastructure",
        "infrastructure as code",
        # (original secrets / PKI)
        "vault", "secret-management", "secrets-management", "secret-manager",
        "secret-scanning", "secret-management", "secrets", "environment-variables",
        "private-ca", "certificate-management", "certificate", "acme", "pki",
        # (original biz / data infra)
        "postgres", "postgresql", "duckdb", "bigquery", "bedrock", "vertex",
        "business-intelligence", "charts", "sql", "sqlai", "text-to-sql",
        "text2sql", "aws", "amazon web services", "devops", "cloudformation", "codepipeline", 
        "codebuild", "codedeploy", "vpc", "ec2", "iam", "s3", "eks", "cloudwatch", "cloudtrail", 
        "auto scaling", "rds", "route 53",
        # (new additions)
        "eks", "ecs", "ecr",
        "lambda",
        "autoscaling",
        "iac", "terraform", "ansible",
        "cicd", "cicd",  # keep both spellings
        "devops engineer", "devops engineers",
        "route53",
        "cloud migration", "migration", "cost optimization", "best practices"
    ],

    "Security / Networking": [
        # (original security / osint / vuln terms)
        "security", "security-tools", "pentest", "pentesting", "pentester",
        "pentest", "information-gathering", "osint", "sosint", "social-analyzer",
        "social-media", "username", "person-profile", "reconnaissance",
        "bugbounty", "vulnerability-detection", "vulnerability", "exploit",
        "exploit-development", "exploits", "nuclei", "nuclei-templates",
        "nuclei-checks", "fingerprint", "fingerprinting",
        "auth", "authentication", "oauth", "jwt", "mfa", "rbac",
        "ssh", "tls", "ssl", "https", "http", "http-client",
        "privacy", "encryption", "cryptography", "blockchain", "cryptocurrency",
        "bitcoin", "p2p", "fhe", "decentralized", "federation", "sharing",
        "collaboration",
        # (original networking / dns)
        "dns", "domain", "subdomain", "cloudflare", "github-pages", "free-domain",
        "free-for-developers", "free-for-dev",
        # (new payment / protocol terms from x402)
        "stablecoin", "on-chain payment", "onchain payment",
        "payment protocol", "payments protocol", "crypto payments",
        "micropayments", "402 payment required", "http 402",
        "paywall", "paid api access", "x402",
        # (new watermark / IP protection terms)
        "data leakage", "data-leakage", "leak traceability",
        "copyright protection", "digital-watermark"
    ],

    "Data Platforms / Backend Services / Integrations": [
        # (original backend / api / integration terms)
        "database", "relational-database", "relational", "mini-database",
        "dataoriented", "dba-roadmap", "smart-contracts",
        "integration", "integrations", "adapter", "api", "api route",
        "grpc", "graphql", "http", "http-client", "webhook",
        "message-broker", "broker", "kafka", "mqtt",
        "ingestion", "etl", "ingest", "pipeline", "workflow",
        "backend", "backend-roadmap", "fullstack", "microservice",
        "middleware", "distributed-storage", "storage", "object-storage",
        "knowledge-base", "vector-database", "vector-search",
        "reranking", "semantic-search",
        "state-management", "memory-management",
        "application", "applications", "app-builder", "ai-app-builder",
        "ecommerce", "ecommerce-platform", "ecommerce-framework",
        "collaboration", "file-sharing", "owncloud", "nextcloud",
        "decentralized", "federation", "sharing", "enterprise",
        "cloud", "oss", "foss", "open-source", "opensource",
        "free-software", "self-hosted", "selfhosted", "self-hosting",
        # (new server / edge / nitro terms)
        "server toolkit", "server-toolkit", "nitro",
        "deploy anywhere", "edge runtime", "edge deployment",
        # (new payment API protocol terms from x402)
        "payment protocol", "payments protocol",
        "paid api access", "x402", "http 402", "402 payment required"
    ],

    "CLI / Utilities / Developer Tools": [
        # (original CLI / shell / dev helper terms)
        "cli", "command-line", "terminal", "console", "cmd", "shell", "bash",
        "zsh", "posix", "posix-compliant", "windows-terminal", "wsl",
        "nodejs-cli", "jj", "jujutsu", "mercurial", "git", "vcs",
        "syntax-highlighting", "tool", "tools", "developer-tools",
        "dev", "dev tool", "debugger", "static analysis", "analysis", "analyzer",
        "codegen", "profile", "monitor", "monitoring",
        "uptime-monitoring", "uptime", "powertoys", "fancyzones",
        "keyboard-manager", "color-picker", "command-palette",
        # (original setup/install/version mgmt)
        "nodejs", "node-js", "node", "install", "nvm", "nvmrc", "lts",
        "version-manager", "package", "pip install",
        # (original editors / workspace)
        "editor", "wiki", "notes", "notes-app", "note-taking", "workspace",
        "whiteboard", "tableview", "markdown", "table", "crdt",
        "notion-alternative", "bruno-alternative", "insomnia-alternative",
        "postman-alternative", "api-client", "api-testing", "testing-tools",
        "testing", "workshop",
        # (new devtools / mise / claude-code terms)
        "mise", "runtime manager", "version manager", "tool version manager",
        "polyglot tool manager", "task runner", "task-runner",
        "env vars", "env var manager", "environment manager",
        "direnv replacement", "asdf", "pyenv", "rbenv",
        "devtools", "git workflows", "git workflow", "pull request",
        "pull-requests", "pr automation", "pr review", "code review",
        "code assistant", "coding assistant",
        "agentic coding tool", "agentic coding assistant", "@claude", "claude-code"
    ],

    "Libraries / SDKs / Framework Components": [
        # (original reusable / SDK / UI component terms)
        "sdk", "client library", "wrapper", "library", "libraries",
        "module", "module provides", "public api:", "reusable component",
        "package import", "npm install", "react", "react-native", "nextjs",
        "typescript", "javascript", "angular", "svelte", "sveltekit",
        "vue", "vuejs", "web-components", "components", "ui", "ui component",
        "design-systems", "styleguide", "storybook",
        "state-management", "router", "routing", "route", "rpc",
        "server-functions",
        "tauri", "electron", "bolt", "v0", "lovable", "vercel",
        "ai-app-builder",
        "pp-ocr", "monai", "onnx", "cpp11", "header-only",
        # (new server toolkit / payment protocol as SDK)
        "nitro", "server toolkit", "server-toolkit",
        "x402", "payments protocol", "payment protocol"
    ],

    "Research / Experiments / Demos": [
        # (original research / experiment / roadmap terms)
        "experiment", "experimental", "prototype", "proof of concept",
        "reference implementation", "baseline", "benchmark", "evaluation",
        "evaluation results", "research", "paper", "arxiv", "ablation",
        "brain-inspired-ai", "in-context-reinforcement-learning",
        "human-in-the-loop", "humanlayer",
        "mcp", "agentic", "agentic-ai", "proactive-ai",
        # (original curated lists / roadmaps)
        "awesome", "awesome-list", "awesome-lists", "awesome-mac",
        "awesome-mac", "resource", "resources", "list", "lists",
        "roadmap", "developer-roadmap", "frontend-roadmap", "backend-roadmap",
        "react-roadmap", "java-roadmap", "python-roadmap", "go-roadmap",
        "angular-roadmap", "nodejs-roadmap", "vue-roadmap", "blockchain-roadmap",
        "devops-roadmap", "qa-roadmap", "software-architect-roadmap",
        "computer-science", "computer-systems", "python3",
        # (new prompt eng / cookbooks / tutorials-as-labs)
        "prompt-engineering", "prompt engineering", "prompt-eng",
        "interactive tutorial", "interactive-tutorial",
        "cookbook", "cookbooks", "claude-cookbooks", "claude cookbooks",
        "recipe", "recipes",
        "notebook", "notebooks", "jupyter", "colab-notebook",
        "quickstart", "quickstarts", "claude-code"
    ],

    "Education / Tutorials / Docs": [
        # (original education / tutorial / docs terms)
        "education", "training", "classroom", "learn", "learning",
        "self-learning", "teaching", "course", "textbook", "courseware",
        "curriculum", "tutorial", "tutorials", "walkthrough",
        "step-by-step", "guide", "quickstart", "getting started",
        "how to run", "lab exercise", "lesson", "for learning",
        "microsoft-for-beginners", "beginner", "beginners",
        "practice", "algorithm", "algorithms-implemented", "sorting-algorithms",
        "sorts", "searches", "interview", "algorithm-competitions",
        "community-driven", "resource", "resources", "books",
        "roadmap", "roadmaps",
        # (original notebooks / docs terms)
        "notebook", "colab-notebook", "kaggle", "audiobook", "audiobooks",
        "tts", "epub", "english", "chinese", "multilingual", "gradio",
        "pdf-parser", "pdf2markdown", "pdf-extractor-rag",
        "presentation", "slides", "zero to hero", "zero-to-hero", "30 days", 
        "30-day", "30days", "30 days of", "day 1", "day 2", "day-1", "day-2", 
        "interview questions", "interview-questions", "real time examples", 
        "real-time examples", "real-time knowledge", "for devops engineers", 
        "for devops", "for beginners", "playlist", "youtube playlist", "youtube",
        "aws tutorial", "tutorial series", "best practices", "job preparation", 
        "job prep", "preparation", "course", "class", "classroom",
        # (new additions for zero-to-hero, Claude cookbooks, micrograd/nanoGPT teaching)
        "interactive tutorial", "interactive-tutorial",
        "quickstarts", "aws zero to hero", "aws learning",
        "presentations", "presentations",
        "from scratch", "autograd engine", "tiny autograd engine",
        "neural network from scratch", "backprop explained",
        "cookbook", "cookbooks", "recipes", "recipe", "claude-cookbooks",
        "claude cookbooks"
    ],
}
GENRE_KEYWORDS["Education / Tutorials / Docs"] += [
    "interview-questions", "real-time-project", "devops",
    "amazon-web-services", "aws",
    "30-days", "30-days-of", "zero-to-hero"
]

GENRE_KEYWORDS["DevOps / Infrastructure / Cloud"] += [
    "interview-questions", "real-time-project",
    "devops-engineer", "devops-engineers",
    "infrastructure-as-code"
]

GENRE_KEYWORDS["CLI / Utilities / Developer Tools"] += [
    "task-runner", "version-manager", "env-vars", "env",
    "polyglot", "polyglot-tool-manager",
    "monorepo", "monorepo-tasks"
]

GENRE_KEYWORDS["AI / Data / ML"] += [
    "gpt2", "gpt-2", "nanogpt", "micrograd",
    "autograd", "autodiff", "reverse-mode-autodiff",
    "neural-networks", "neural-networks-from-scratch",
    "financial-trading", "quant-trading", "quantitative-trading",
    "trading", "trading-framework", "backtesting",
    "multimodal", "multimodal-llm", "multimodal-large-language-model",
    "vision-language-models",
    "pdf", "document-ai", "document-processing",
    "document-understanding", "dataset-prep",
    "dataset-preparation", "dataset-generation",
    "gpu", "gpu-kernel", "gpu-kernels", "cuda",
    "high-performance", "high-performance-kernels",
    "tvm", "compiler-dsl", "dsl", "kernel-fusion",
    "flashattention", "flash-attention", "linearattention",
    "multi-agent-llm", "multi-agent-llms",
    "multi-agent-llm-trading-framework",
    "autonomous-ai-agents", "ai-agents-for-trading"
]

GENRE_KEYWORDS["Data Platforms / Backend Services / Integrations"] += [
    "server", "serverless", "server-toolkit",
    "production-ready-server",
    "deploy-anywhere", "zero-config",
    "zero-config-server", "edge-runtime",
    "edge-deployment", "edge",
    "api-routes", "server-routes",
    "payments-protocol", "onchain", "on-chain",
    "onchain-payment", "crypto-payments",
    "http-402", "402-payment-required", "web3"
]

GENRE_KEYWORDS["Systems / Embedded / Robotics"] += [
    "robot-arm", "open-hardware", "open-robotics",
    "3d-printable", "3d-printed",
    "3d-printed-robot", "3d-printable-robot-arm",
    "servo-motors", "servo-motor"
]

GENRE_KEYWORDS["Research / Experiments / Demos"] += [
    "prompt-engineering-tutorial",
    "prompting", "prompting-guide",
    "cookbook-examples", "code-recipes",
    "developer-recipes"
]

GENRE_KEYWORDS["Security / Networking"] += [
    "web3", "onchain", "on-chain",
    "http-402", "402-payment-required"
]