# 🤖 Pacheco AI Ω — v31_7
### The Self-Healing, Autonomous Development Agent | LIMA CORP
*by Arthur Lima*

Pacheco AI is a self-healing, LLM-driven agent designed to bridge the gap
between AI-generated logic and real-world local execution. Operating under
the LIMA CORP methodology, it uses a modular, Object-Oriented architecture
to write, test, and autonomously repair Python scripts in real-time — inside
a secure, AST-monitored sandbox environment.

In v3.2, Pacheco gained a **natural conversation layer**: it now understands
when you want to chat, when you want code, and responds proportionally —
brief for simple questions, detailed for complex ones. No more one-trick pony.

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

Core external dependencies:
- `requests` — HTTP communication with the Ollama API
- `pandas`, `numpy` — Data manipulation and CSV/XLSX processing
- `openpyxl`, `reportlab` — Excel and PDF generation
- `matplotlib`, `pillow` — Charts and image processing
- `flask`, `fastapi` — Web server and API building
- `rich`, `colorama` — Beautiful terminal output
- And many more — see `requirements.txt` and `modulos.json`

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
python main.py
```

---

## 💬 Usage — Modes & Commands

Pacheco v3.2 operates in three modes. Switch anytime mid-conversation:

| Command | Mode | Description |
|---|---|---|
| `/chat` | 💬 Conversation | Natural chat, ideas, strategy, analysis |
| `/cod` | ⌨️ Programmer | Generates, runs, and auto-repairs Python code |
| `/auto` | 🤖 Automatic | Pacheco infers intent from your message |

Default mode on startup: **💬 Conversation** (safest — avoids accidental code execution).

### Quick Commands (work in any mode)

| Command | Action |
|---|---|
| `/hora` | Current time from your PC |
| `/data` | Today's date |
| `/versao` | System version info |
| `/memoria` | Session history |
| `/config` | Current configuration |
| `/ajuda` | Help screen |
| `/sair` | Exit |

### Input Tips
- **Single line:** just press Enter
- **Multi-line / pasted text:** press Enter twice to submit, or end with `---`

---

## 📂 System Architecture

Pacheco follows a **Zero-Leakage Security Protocol** with four managed directories:

| Directory | Purpose |
|---|---|
| `/Sandbox` | Temporary execution ground. Scripts are AST-analyzed and run here, then deleted automatically. |
| `/Memoria` | Persistence vault. Stores `memoria_longa.json` with successful solutions across sessions. |
| `/Logs` | Audit trail. Every session generates a timestamped log with status levels (SUCCESS, ERROR, FATAL, CHAT). |
| `/Projetos_Ativos` | Production vault. Reserved for validated, production-ready code. |

### Core Classes

| Class | Responsibility |
|---|---|
| `Classificador` | Intent detection — infers if input is code, conversation, or instant command |
| `ModuloChat` | Natural conversation engine — context-aware, proportional responses, anti-hallucination |
| `AnalisadorSeguranca` | AST-based static analysis — blocks dangerous calls before execution |
| `Executor` | Runs generated code in the sandbox with timeout and UTF-8 enforcement |
| `Memoria` | Dual-tier memory: RAM (short-term) + JSON (long-term) with Jaccard similarity search |
| `PromptBuilder` | Constructs and injects system rules, context, and directory paths into every prompt |
| `ClienteOllama` | Manages streaming HTTP communication with the local LLM (variable temperature per mode) |
| `Logger` | Session-scoped audit logging |
| `PachecoAI` | Orchestrator — coordinates all components, manages modes, and runs the self-healing retry loop |

---

## 🔒 Security Model

### AST Analysis (Pre-Execution)
Every generated script is parsed and analyzed **before** running. Blocked calls:

```python
os.system, os.popen, os.remove, os.rmdir, os.unlink
shutil.rmtree, shutil.move, shutil.copy
subprocess.run, subprocess.call, subprocess.Popen
eval, exec, compile, __import__
```

### Extensible Module Allowlist
Permitted modules live in two places:

1. **Hardcoded defaults** in `main.py` — stdlib + major third-party libs
2. **`modulos.json`** — drop new module names here to extend the allowlist without touching the source code

```json
["pandas", "numpy", "flask", "qrcode"]
```

---

## 🔄 How the Self-Healing Loop Works

```
User Input
│
▼
Classificador → detects intent (chat / code / instant command)
│
├── INSTANT COMMAND → responds immediately (no LLM call)
├── CHAT MODE → ModuloChat → proportional natural response
│
└── CODE MODE:
    │
    ▼
    PromptBuilder → builds context-aware prompt with rules + memory
    │
    ▼
    ClienteOllama → streams response from local LLM (temp: 0.1)
    │
    ▼
    AnalisadorSeguranca → AST scan (blocks dangerous code)
    │
    ▼
    Executor → runs in Sandbox (30s timeout, UTF-8, auto-cleanup)
    │
    ├── SUCCESS → saves to Memoria, logs result
    │
    └── FAILURE → re-prompts with error context (up to 3 attempts)
```

---

## 🧠 Memory System

Pacheco maintains two memory layers:

- **Short-term (RAM):** last 5 interactions per session — used for immediate context
- **Long-term (JSON):** up to 200 successful solutions persisted across sessions

When you make a new code request, Pacheco performs a **Jaccard similarity search** over long-term memory to find relevant past solutions and inject them as reference into the prompt.

Chat conversations have their own rolling context window (last 4 exchanges) kept separate from code memory.

---

## 📋 Updates

See the [`/updates`](./updates) folder for the full version changelog.

---

## 📌 Project Status

🚧 **Actively in development.** Each version expands Pacheco's autonomy,
memory, and reasoning capabilities toward the long-term goal of a
fully self-sufficient AI assistant.

**Roadmap:**
- [ ] Voice input/output integration
- [ ] Web interface (Flask)
- [ ] Multi-agent task delegation
- [ ] Automatic skill learning from successful sessions
- [ ] Upgrade to larger model (llama3 70b / mistral large) when hardware allows
