# 🤖 Pacheco AI — v1.0.0 ALPHA

### Autonomous Development & Self-Healing Agent | LIMA CORP
**Developed by Arthur Lima**

Pacheco AI is a localized, LLM-powered self-healing development agent engineered to bridge the gap between AI-generated logic and real-world local execution. Operating under the **LIMA CORP** software architecture methodology, it utilizes a modular, object-oriented framework to write, test, and dynamically repair Python scripts in real time—all within a secure sandbox monitored by Abstract Syntax Tree (AST) analysis.

With the **v1.0.0 Alpha** release, Pacheco has evolved into a hybrid ecosystem, featuring a beautiful split-screen desktop interface (Chat on the left, Clean Code execution on the right) powered by **PyQt6 and QtWebEngine**, completely decoupling the core engine from unstable web-based AI platforms.

**Long-Term Objective:** To evolve Pacheco into a fully autonomous assistant capable of independent chain-of-thought reasoning, self-directed skill acquisition, and complex multi-step task execution—a personal, offline Jarvis built from the ground up.

---

## 🛠️ System Architecture & Tech Stack

### 1. Requirements & Core Dependencies
* **Python Version:** `Python 3.10+` (leveraging modern type-hinting and robust pattern matching).
* **PyQt6 & PyQt6-WebEngine:** Powers the high-performance desktop interface, rendering a modern UI/UX with cross-thread communication.
* **SQLite3:** Relational database backend replacing old volatile JSON file storage for robust session state management and short/long-term memory persistence.
* **Requests:** Fast streaming HTTP communication with the local Ollama API server.
* **Security & Execution:** `ast` (Static analysis runtime firewall) and `subprocess` (Isolated sandbox wrapper).

### 2. Local LLM Setup (The Offline Brain)
Pacheco Alpha operates **100% offline**, ensuring zero API costs, absolute data privacy, and zero reliance on third-party platform bans.
* **Chat & Strategy Engine:** `llama3.2:3b` (Optimized for quick, contextual, and fluid conversations).
* **Coding & Repair Engine:** `qwen2.5-coder:7b` (State-of-the-art local model trained for precise Python syntax generation, producing clean code with minimal syntax errors).

---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/pacheco-ai.git](https://github.com/YOUR_USERNAME/pacheco-ai.git)
cd pacheco-ai

# 2. Setup folders and install dependencies
pip install -r requirements.txt

# 3. Ensure Ollama is running locally
ollama serve
ollama pull qwen2.5-coder:7b
ollama pull llama3.2:3b

# 4. Launch the Desktop Hybrid GUI
python gui.py
📂 File Structure & Architecture Blueprint
Pacheco Alpha enforces an Absolute Path Anchoring Protocol (PASTA_RAIZ). No matter where you launch the terminal from, the system mathematically anchors itself to its hardware directory (e.g., your dedicated drive), preventing ghost files or database dislocations.

Plaintext
Projeto Pacheco/
│
├── gui.py                  # PyQt6 Desktop UI Window & WebEngine Bridge
├── PachecoAlpha.py         # Core Orchestrator & Multi-Model Routing Logic
├── .gitignore              # Safeguards local DBs and Sandbox runtimes
│
├── Alpha/                  # Stable Alpha Release releases
│   └── .gitkeep
│
├── Memoria/                # ACID-Compliant Persistence Vault
│   └── pacheco.db          # Unified SQLite3 Database (Sessoes, Mensagens, Memoria)
│
├── Sandbox/                # Runtime Quarantine Zone (Auto-cleaned temporary scripts)
├── Logs/                   # Session-scoped cryptographic auditing logs
└── Habilidades/            # Validated production-ready script storage
🔒 Security Model & Sandbox Firewall
Abstract Syntax Tree (AST) Pre-Execution Scan
Before any code enters the local shell execution phase, Pacheco parses the script into an AST token stream to block malicious or system-breaking calls.

Blocked Operations: os.system, os.popen, subprocess.Popen, eval, exec, __import__.

Extensible Module Whitelist: Only predefined engineering/data science packages (e.g., pandas, numpy, matplotlib, fastapi, requests) are permitted to run.

🔄 The Self-Healing DeepThink Loop
Plaintext
User Request (UI Input)
│
▼
Classifier (Intent Detection)
│
├── CHAT MODE   ──► ModuloChat (llama3.2) ──► Proportional Natural Response
│
└── CODE MODE (qwen2.5-coder):
    │
    ▼
    [DeepThink Step] PromptBuilder injects Jaccard-similarity long memory + error context
    │
    ▼
    ClienteOllama streams response silently in background (Temp: 0.1)
    │
    ▼
    AnalisadorSeguranca runs AST runtime check (Blocks dangerous operations)
    │
    ▼
    Executor spawns isolated Sandbox subprocess (30s timeout, UTF-8 enforcement)
    │
    ├── SUCCESS ──► Persists solution to pacheco.db ──► Updates UI Right Panel (Clean Code)
    │
    └── FAILURE ──► Feeds compiler error trace back into the loop (Up to 3 Self-Correction Retries)
🧠 Relational Memory Schema
Unlike previous architectures that suffered from file fragmentation, the Alpha Core unifies memory under an ACID-compliant SQLite layer:

Short-Term Context: Rolling chronological session history using advanced SQL subqueries, preventing the AI from reading logs backward.

Long-Term Knowledge: Stores validated successful executions. When a new coding prompt is received, a Jaccard token-intersection algorithm scans past triumphs to feed working boilerplate code back into the prompt context.

📌 Project Status & Roadmap
🚧 Active Development (Alpha Stage). * [x] PyQt6 WebEngine Split-Screen Hybrid UI

[x] Absolute Path Anchoring (PASTA_RAIZ Architecture)

[x] Silent Self-Correction Engine (DeepThink simulation)

[x] SQLite3 Unified Session Memory

[ ] Multi-Agent task delegation pipelines

[ ] Automated offline skill-learning repository

[ ] Hardware-accelerated local voice processing (STT/TTS)
