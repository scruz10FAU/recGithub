import requests
import base64
import re
from collections import defaultdict
import math
import argparse

GENRE_KEYWORDS = {
    "AI / Data / ML": [
        # core ml/ai / LLM / vision
        "machine-learning", "deep-learning", "artificial-intelligence", "ai",
        "llm", "llms", "large-language-model", "large-language-models",
        "language-model", "generative-ai", "transformer", "gpt", "gpt-2",
        "nanogpt", "qwen", "qwen3", "qwen3-vl", "vision-language-model",
        "multimodal", "multimodal-llm", "vlm", "pretrained-models",
        "foundation-models", "reasoning", "brain-inspired-ai",
        "embedding", "embeddings", "embedding-models", "semantic-search",
        "vector-search", "vector-database", "reranking",
        "rag", "retrieval-augmented-generation", "multi-modal-rag",
        "text-to-sql", "text2sql", "text-to-chart",
        "forecasting", "timeseries", "time-series", "time-series-forecasting",
        "sota", "state-of-the-art",
        # training / backprop / autograd / from-scratch repos (micrograd, nanoGPT)
        "training", "finetuning", "fine-tuning", "from scratch",
        "backprop", "backpropagation", "autograd", "gradient descent",
        "neural network", "neural-net", "pytorch", "torch", "pytorch-like api",
        "tiny autograd engine", "micrograd",
        # agents / autonomy / trading agents
        "agent", "agents", "multi-agent", "multi-agents", "ai-agents",
        "agentic", "agentic-ai", "agentic coding", "coding agent",
        "agentic coding tool", "agentic coding assistant",
        "agent-computer-interface", "computer-use-agent", "gui-agents",
        "autonomous ai agents", "autonomous trading agent",
        "algorithmic trading", "trading agent", "trading-agents",
        "backtest", "backtesting", "quant", "quantitative trading",
        "financial trading", "stock trading",
        "in-context-reinforcement-learning", "reinforcement-learning",
        "planning", "memory", "long-term-memory", "memory-management",
        "state-management",
        # OCR / doc understanding / PDF-to-text (olmocr)
        "ocr", "pp-ocr", "chineseocr", "document-parsing",
        "document-translation", "pdf-extractor-rag", "pdf2markdown",
        "pdf-to-text", "pdf linearization", "pdf parsing",
        "paddleocr-vl", "ai4science", "healthcare-imaging",
        "medical-image-computing", "medical-image-processing", "monai",
        # high-perf AI kernels / compilers (tilelang, FlashAttention)
        "flashattention", "flash-attention", "linearattention",
        "high-performance kernels", "gpu kernel", "cuda kernel",
        "kernel fusion", "tvm", "compiler", "dsl for kernels",
        "tilelang", "tile-lang", "tile language",
        "accelerator kernels", "gpu acceleration", "npu",
        # eval / prompt engineering
        "evaluation", "model-eval", "prompt-engineering", "prompt engineering",
        "human-in-the-loop", "humanlayer", "proactive-ai",
        "context-engineering", "mcp", "mllm", "multimodel",
        "claude", "claude-code", "anthropic", "openai", "ollama",
        "localai", "llamacpp", "gemini", "deepseek", "qwen",
        # watermarking for images often uses CV/ML
        "image-processing", "watermark", "blind-watermark",
        "invisible-watermark", "digital-watermark", "steganography"
    ],

    "Systems / Embedded / Robotics": [
        # embedded / hardware / robotics (SO-ARM100)
        "firmware", "embedded", "embedded-ml", "microcontroller", "mcu",
        "stm32", "register map", "risc-v", "riscv", "arm32", "aarch64",
        "raspberry-pi", "jetson", "edge-machine-learning",
        "realtime", "rtos", "pid", "pid controller", "sensor fusion",
        "uav", "drone", "mavlink",
        "robot", "robotics", "robot arm", "humanoid", "humanoid robot",
        "manipulator", "servo", "actuator", "kinematics",
        "so-arm100", "so-100", "so-101", "the-robot-studio",
        "ros", "ros2", "moveit", "gazebo", "urdf",
        # OS / low-level runtime / system tooling
        "wayland-compositor", "wayland", "tiling-window-manager",
        "window-manager", "browser-engine", "webengine", "webbrowser",
        "browser-automation", "computer-automation", "computer-use",
        # desktop / cross-platform native apps
        "desktop", "desktop-app", "desktop-application", "desktop-apps",
        "cross-platform", "multiplatform", "application", "app", "apps",
        "software", "windows", "windows-10", "windows-11",
        "mac", "macos", "macosx", "mac-osx", "macos-app", "macos-apps",
        "linux", "ios", "android", "object-pascal", "lazarus", "mfc",
        "cpp", "cplusplus", "c-plus-plus", "cpp11", "csharp", "dotnet",
        "onnx", "vits",
        # power tools / shell integration
        "powertoys", "microsoft-powertoys", "fancyzones",
        "keyboard-manager", "command-palette", "color-picker",
        "windows-terminal", "terminal", "console", "cmd", "wsl"
    ],

    "Web / Mobile / Application Development": [
        # modern web/fullstack app frameworks and server toolkits (nitro)
        "webapp", "web", "single-page-app", "spa", "responsive", "frontend",
        "nextjs", "next.js", "react", "react-native",
        "typescript", "javascript", "tailwindcss", "vite", "webpack",
        "svelte", "svelte-kit", "sveltekit", "vue", "vuejs", "vueuse",
        "web-components", "design-systems", "styleguide",
        "components", "ui", "ui component", "stories", "storybook",
        "router", "routing", "route", "state-management", "ssr",
        "fullstack", "framework", "frameworks", "server toolkit",
        "server-toolkit", "zero-config server", "deploy anywhere",
        "edge runtime", "edge deployment", "server routes", "api routes",
        "nitro", "nitrojs",
        "vercel",
        # app / product style repos
        "assistant", "note-taking", "notes-app", "wiki", "notes",
        "markdown", "whiteboard", "tableview", "workspace",
        "notion", "notion-alternative", "miro",
        # app runtimes / clients
        "electron", "tauri", "tauri-v2", "pwa",
        "websocket", "socket-io", "sse", "graphql", "grpc",
        "api-client", "api-rest", "rest-api", "rest", "http",
        "http-client", "https", "rpc", "server-functions",
        "searchparams", "url",
        # distribution / hosting
        "selfhosted", "self-hosted", "self-hosting"
    ],

    "DevOps / Infrastructure / Cloud": [
        # containers / orchestration / infra
        "docker", "dockerfile", "docker-compose", "container", "containers",
        "kubernetes", "k8s", "eks", "ecs", "ecr", "cncf",
        "helm", "helm chart", "chart", "charts",
        "distributed-systems", "multi-tenant", "multi-cloud",
        "multi-cloud-kubernetes",
        "cloud", "cloudnative", "cloudstorage", "cloud-drive",
        "s3", "amazon-s3", "objectstorage", "object-storage", "s3-storage",
        "storage", "tiered-file-system", "distributed-file-system",
        "distributed-storage", "replication", "fuse", "erasure-coding",
        "blob-storage", "hdfs", "hadoop-hdfs", "seaweedfs",
        "virtualization", "rdp",
        "infrastructure", "infrastructure as code", "iac",
        "terraform", "ansible",
        # observability / ops
        "uptime", "uptime-monitoring", "monitor", "monitoring", "metrics",
        "telemetry", "observability", "opentelemetry", "open-telemetry",
        "cloudwatch", "cloudtrail",
        # CI/CD toolchains and workflows
        "github-actions", "pipeline", "ci/cd", "cicd", "workflow",
        "automation", "deployment", "cluster", "scalability",
        "codepipeline", "codebuild", "codedeploy", "codecommit",
        # AWS DevOps topics (aws-devops-zero-to-hero)
        "aws", "amazon web services", "devops", "devops engineer",
        "iam", "vpc", "ec2", "s3", "rds", "lambda", "eks",
        "route 53", "route53", "auto scaling", "autoscaling",
        "cloudformation",
        # cost / migration / best practices training
        "cloud migration", "migration", "cost optimization",
        "best practices",
        # Biz/data infra services that deploy in cloud
        "postgres", "postgresql", "duckdb", "bigquery", "bedrock",
        "vertex", "business-intelligence", "charts", "sql", "sqlai",
        "text-to-sql", "text2sql"
    ],

    "Security / Networking": [
        # security / exploits / scanning
        "security", "security-tools", "pentest", "pentesting", "pentester",
        "information-gathering", "osint", "sosint", "reconnaissance",
        "social-analyzer", "social-media", "username", "person-profile",
        "bugbounty", "vulnerability-detection", "vulnerability",
        "exploit", "exploit-development", "exploits",
        "nuclei", "nuclei-templates", "nuclei-checks",
        "fingerprint", "fingerprinting",
        # auth / crypto / blockchain / payments (coinbase/x402)
        "auth", "authentication", "oauth", "jwt", "mfa", "rbac",
        "ssh", "tls", "ssl", "https",
        "encryption", "cryptography", "blockchain", "cryptocurrency",
        "bitcoin", "p2p", "fhe",
        "stablecoin", "on-chain payment", "onchain payment",
        "payment protocol", "payments protocol", "crypto payments",
        "micropayments", "402 payment required", "http 402",
        "paywall", "paid api access", "x402",
        # networking / dns / federation
        "dns", "domain", "subdomain", "cloudflare",
        "federation", "decentralized", "sharing", "collaboration",
        "free-domain", "free-for-developers", "free-for-dev",
        # watermarking for leak tracing / copyright protection
        "data leakage", "data-leakage", "leak traceability",
        "copyright protection", "digital-watermark"
    ],

    "Data Platforms / Backend Services / Integrations": [
        # backend services / APIs / integration layers
        "backend", "backend-roadmap", "fullstack", "microservice",
        "middleware", "integration", "integrations", "adapter",
        "api", "api route", "api routes", "http", "http-client",
        "graphql", "grpc", "webhook", "message-broker",
        "broker", "kafka", "mqtt",
        "ingestion", "ingest", "etl", "pipeline", "workflow",
        "server toolkit", "server-toolkit", "nitro",
        "deploy anywhere", "edge runtime", "edge deployment",
        # data storage / DBs
        "database", "relational-database", "relational", "mini-database",
        "dataoriented", "knowledge-base",
        "state-management", "memory-management",
        # business platforms / payments API (x402)
        "payment protocol", "payments protocol", "paid api access",
        "x402", "http 402", "402 payment required",
        # app platforms
        "application", "applications", "app-builder", "ai-app-builder",
        "ecommerce", "ecommerce-platform", "ecommerce-framework",
        "collaboration", "file-sharing", "owncloud", "nextcloud",
        "decentralized", "federation", "enterprise",
        # openness / distro
        "cloud", "oss", "foss", "open-source", "opensource",
        "free-software", "self-hosted", "selfhosted", "self-hosting"
    ],

    "CLI / Utilities / Developer Tools": [
        # terminal tools / runtime managers / env/task runners (mise, claude-code)
        "cli", "command-line", "terminal", "console", "cmd", "shell", "bash",
        "zsh", "wsl", "windows-terminal",
        "mise", "runtime manager", "version manager", "tool version manager",
        "polyglot tool manager", "task runner", "task-runner",
        "env vars", "env var manager", "environment manager", "direnv replacement",
        "asdf", "pyenv", "rbenv", "nvm", "nvmrc",
        "install", "lts", "version-manager", "package", "pip install",
        # dev workflow helpers
        "developer-tools", "dev tool", "devtools", "debugger",
        "static analysis", "analysis", "analyzer", "codegen",
        "profile", "git workflows", "git workflow", "git",
        "pull request", "pull-requests", "pr automation", "pr review",
        "code review", "code assistant", "coding assistant",
        "agentic coding tool", "agentic coding assistant",
        "@claude", "claude-code",
        # power-user desktop utils
        "powertoys", "fancyzones", "keyboard-manager",
        "color-picker", "command-palette",
        # API/dev testing helpers
        "postman-alternative", "insomnia-alternative", "bruno-alternative",
        "api-client", "api-testing", "testing-tools",
        # docs / workshops for tools
        "workshop"
    ],

    "Libraries / SDKs / Framework Components": [
        # reusable frameworks, SDKs, server kits, payment protocols as libs
        "sdk", "client library", "wrapper", "library", "libraries",
        "module", "package import", "npm install",
        "public api:", "reusable component",
        "typescript", "javascript", "react", "react-native", "nextjs",
        "vue", "vuejs", "svelte", "sveltekit",
        "web-components", "components", "ui", "ui component",
        "design-systems", "styleguide", "storybook",
        "router", "routing", "route", "rpc", "server-functions",
        "tauri", "electron", "bolt", "v0", "lovable", "vercel",
        "ai-app-builder",
        "pp-ocr", "onnx", "monai", "cpp11", "header-only",
        # server / edge frameworks
        "nitro", "server toolkit", "server-toolkit",
        # payment protocol as SDK (x402)
        "x402", "payments protocol", "payment protocol"
    ],

    "Research / Experiments / Demos": [
        # research repos, cookbooks, prompt-eng tutorials, evaluation cookbooks
        "experiment", "experimental", "prototype", "proof of concept",
        "reference implementation", "baseline", "benchmark", "evaluation",
        "evaluation results", "research", "paper", "arxiv", "ablation",
        "prompt-engineering", "prompt engineering", "prompt-eng",
        "interactive tutorial", "interactive-tutorial",
        "cookbook", "cookbooks", "recipe", "recipes",
        "notebook", "notebooks", "jupyter", "colab-notebook",
        "quickstart", "quickstarts",
        "claude-cookbooks", "claude cookbooks", "claude-code",
        "mcp", "agentic", "agentic-ai", "proactive-ai",
        "human-in-the-loop", "humanlayer",
        # curated lists / roadmaps
        "awesome", "awesome-list", "awesome-lists", "awesome-mac",
        "resource", "resources", "list", "lists",
        "roadmap", "roadmaps", "developer-roadmap",
        "frontend-roadmap", "backend-roadmap", "react-roadmap",
        "java-roadmap", "python-roadmap", "go-roadmap",
        "angular-roadmap", "nodejs-roadmap", "vue-roadmap",
        "blockchain-roadmap", "devops-roadmap", "qa-roadmap",
        "software-architect-roadmap",
        "computer-science", "computer-systems", "python3"
    ],

    "Education / Tutorials / Docs": [
        # structured learning paths, zero-to-hero content, notebooks for learning
        "education", "training", "classroom", "class", "lesson", "lessons",
        "learn", "learning", "self-learning", "teaching",
        "course", "courseware", "textbook", "curriculum",
        "tutorial", "tutorials", "interactive tutorial", "interactive-tutorial",
        "walkthrough", "step-by-step", "guide", "quickstart",
        "quickstarts", "getting started", "how to run",
        "lab exercise", "for learning", "for beginners",
        "beginner", "beginners", "microsoft-for-beginners",
        "practice", "interview", "interview questions",
        "interview-questions", "job preparation", "job prep",
        "preparation", "real time examples", "real-time examples",
        "real-time knowledge", "best practices",
        # aws-devops-zero-to-hero style phrasing
        "zero to hero", "zero-to-hero", "aws zero to hero",
        "30 days", "30-day", "30days", "30 days of",
        "day 1", "day 2", "day-1", "day-2",
        "for devops engineers", "for devops",
        "playlist", "youtube playlist", "youtube", "tutorial series",
        "aws tutorial", "aws learning",
        # notebooks / hands-on docs
        "notebook", "notebooks", "jupyter", "colab-notebook",
        "slides", "presentation", "presentations", "cookbook", "cookbooks",
        "recipes", "recipe", "claude-cookbooks",
        # teaching ML basics (micrograd, nanoGPT explainer repos)
        "from scratch", "autograd engine", "tiny autograd engine",
        "neural network from scratch", "backprop explained"
    ],
}




def score_repo_from_topics(topics_str):
    # normalize topics into a list of tokens
    if isinstance(topics_str, list):
        topics_list = topics_str
    elif isinstance(topics_str, str):
        # split on commas or whitespace
        topics_list = re.split(r"[,\s]+", topics_str.strip())
    else:
        topics_list = []

    topics_list = [t.lower() for t in topics_list if t]

    # join all topics into a single searchable blob for substring/phrase matches
    topic_blob = " ".join(topics_list)

    raw_scores = defaultdict(int)

    for genre, keywords in GENRE_KEYWORDS.items():
        for kw in keywords:
            kw_l = kw.lower()

            # If keyword is multiple words ("neural network"),
            # do substring search on the blob.
            # If it's a single token ("ros2"), also check exact topic match.
            if " " in kw_l:
                if kw_l in topic_blob:
                    raw_scores[genre] += 1
            else:
                # exact match in topics OR substring in blob
                if kw_l in topics_list or kw_l in topic_blob:
                    raw_scores[genre] += 1

    # normalize scores 0..1 per repo so the highest genre = 1.0
    if raw_scores:
        max_score = max(raw_scores.values())
        if max_score == 0:
            norm_scores = {g: 0.0 for g in GENRE_KEYWORDS.keys()}
        else:
            norm_scores = {
                g: (raw_scores.get(g, 0) / max_score)
                for g in GENRE_KEYWORDS.keys()
            }
    else:
        norm_scores = {g: 0.0 for g in GENRE_KEYWORDS.keys()}

    return norm_scores

def get_repo_readme(owner, repo):
    #fetch github repo
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    #get readme if it exists
    r = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"})
    if r.status_code != 200:
        return ""
    data = r.json()
    if "content" in data and data.get("encoding") == "base64":
        return base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
    return ""

def get_repo_file_tree(owner, repo):
    # recursive=1 gives the whole tree (paths only, not contents) for default branch
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/HEAD?recursive=1"
    r = requests.get(url)
    if r.status_code != 200:
        return []
    data = r.json()
    tree = data.get("tree", [])
    return [item["path"] for item in tree if item["type"] == "blob"]

def score_genres(text_blob, file_paths):
    genre_scores = defaultdict(int)

    # Lowercase once
    blob = (text_blob + "\n" + "\n".join(file_paths)).lower()

    for genre, keywords in GENRE_KEYWORDS.items():
        for kw in keywords:
            # simple keyword frequency
            hits = len(re.findall(r"\b" + re.escape(kw.lower()) + r"\b", blob))
            genre_scores[genre] += hits

    return dict(genre_scores)


def normalize_scores(raw_scores):
    # avoid divide-by-zero
    if not raw_scores:
        return {}
    max_score = max(raw_scores.values()) or 1
    return {genre: score / max_score for genre, score in raw_scores.items()}

def classify_repo(owner_repo):
    owner, repo = owner_repo.split("/", 1)

    readme_text = get_repo_readme(owner, repo)
    file_paths = get_repo_file_tree(owner, repo)

    raw_scores = score_genres(readme_text, file_paths)
    norm_scores = normalize_scores(raw_scores)

    # Pick top genre
    top_genre = max(norm_scores, key=norm_scores.get) if norm_scores else None

    return {
        "repo": owner_repo,
        "top_genre": top_genre,
        "scores": norm_scores,
        "debug": {
            "readme_len_chars": len(readme_text),
            "num_files_seen": len(file_paths),
        },
    }

def main():
    result = classify_repo("pallets/flask")
    print(result["top_genre"])
    print(result["scores"])


if __name__ == "__main__":
    main()


