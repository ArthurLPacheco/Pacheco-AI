# 🤖 Pacheco AI Ω — v31.4
### The Self-Healing, Autonomous Development Agent | LIMA CORP
*by Arthur Lima*

Pacheco AI is a self-healing, LLM-driven agent designed to bridge the gap 
between AI-generated logic and real-world local execution. Operating under 
the LIMA CORP methodology, it uses a modular, Object-Oriented architecture 
to write, test, and autonomously repair Python scripts in real-time — inside 
a secure, AST-monitored sandbox environment.

> **Long-term goal:** Evolve Pacheco into a fully autonomous assistant 
> capable of independent reasoning, self-improvement, and complex 
> multi-step task execution — a personal Jarvis, built from the ground up.

---

## 🛠 Prerequisites & Installation

### 1. Python Environment
- **Version:** Python 3.10+ (required for modern type hints and match statements)

### 2. Dependencies
```bash
pip install -r requirements.txt
```

Core external dependency:
- `requests` — HTTP communication with the Ollama API

Standard library modules used internally:
- `ast` — Static code analysis before execution
- `pathlib` — Cross-platform file system management  
- `json` — Persistent memory storage
- `subprocess` — Sandboxed script execution
- `sys` — Correct interpreter resolution via `sys.executable`

### 3. Local LLM Setup (The Brain)
Pacheco Ω runs entirely **offline** with no API costs, powered by Ollama.

- Download Ollama: [ollama.com](https://ollama.com/)
- Pull the model:
```bash
ollama pull qwen2.5-coder:7b
```
- Start the server:
```bash
ollama serve
```
> The server must be running on `http://localhost:11434` before launching Pacheco.

**Why `qwen2.5-coder:7b`?**  
Purpose-trained for code generation. Produces clean Python on the first 
attempt, with no Spanish variable names, no undefined function calls, and 
significantly fewer hallucinations compared to general-purpose models.

---

## 📂 System Architecture

Pacheco follows a **Zero-Leakage Security Protocol** with four managed directories:

| Directory | Purpose |
|---|---|
| `/Sandbox` | Temporary execution ground. Scripts are AST-analyzed and run here, then deleted automatically. |
| `/Memoria` | Persistence vault. Stores `memoria_longa.json` with successful solutions across sessions. |
| `/Logs` | Audit trail. Every session generates a timestamped log with status levels (SUCCESS, ERROR, FATAL). |
| `/Projetos_Ativos` | Production vault. Reserved for validated, production-ready code. |

### Core Classes

| Class | Responsibility |
|---|---|
| `AnalisadorSeguranca` | AST-based static analysis — blocks dangerous calls before execution |
| `Executor` | Runs generated code in the sandbox with timeout and UTF-8 enforcement |
| `Memoria` | Dual-tier memory: RAM (short-term) + JSON (long-term) with Jaccard similarity search |
| `PromptBuilder` | Constructs and injects system rules, context, and directory paths into every prompt |
| `ClienteOllama` | Manages streaming HTTP communication with the local LLM |
| `Logger` | Session-scoped audit logging |
| `PachecoAI` | Orchestrator — coordinates all components and manages the self-healing retry loop |

---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/pacheco-ai.git
cd pacheco-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start Ollama
ollama serve

# 4. Launch Pacheco
python pacheco_ai.py
```

---

## 🔄 How the Self-Healing Loop Works

User Input
│
▼
PromptBuilder → builds context-aware prompt with rules + memory
│
▼
ClienteOllama → streams response from local LLM
│
▼
AnalisadorSeguranca → AST scan (blocks dangerous code)
│
▼
Executor → runs in Sandbox (15s timeout, UTF-8, auto-cleanup)
│
├── SUCCESS → saves to Memoria, logs result
│
└── FAILURE → re-prompts with error context (up to 3 attempts)

---

## 📋 Updates

See the [`/updates`](./updates) folder for the full version changelog.

---

## 📌 Project Status

🚧 **Actively in development.** Each version expands Pacheco's autonomy, 
memory, and reasoning capabilities toward the long-term goal of a 
fully self-sufficient AI assistant.
