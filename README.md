# 🤖 Pacheco AI Ω — v31.3 (v2.0)
### The Self-Healing, Autonomous Agent by LIMA CORP

Pacheco AI is a self-healing, LLM-driven development agent designed to bridge the gap between AI-generated logic and local execution. Operating under the **LIMA CORP** methodology, it utilizes a modular, Object-Oriented architecture to write, test, and repair Python scripts in real-time within a secure, AST-monitored sandbox environment.

## 🛠 Prerequisites & Installation
To deploy the Pacheco Ω system and achieve peak performance, follow these technical requirements:

### 1. Python Environment
*   **Version:** Python 3.10+ (Recommended)
*   **Why?** We leverage advanced type hinting, modern subprocess handling, and the latest `requests` session management for low-latency communication with the LLM.

### 2. Dependencies
Install the required libraries using the provided `requirements.txt`. Note that Pacheco Ω leverages several Python Standard Libraries for advanced operations:

*   **requests:** For robust HTTP communication with the Ollama API.
*   **ast (Standard Library):** Used for **Static Code Analysis**, scanning for malicious calls before execution.
*   **pathlib (Standard Library):** For modern, cross-platform file system path management.
*   **json (Standard Library):** For persistent state management and **Long-Term Memory** storage.

### 3. Local LLM Setup (The "Brain")
Pacheco Ω is currently optimized for **Phi-3 (3.8b)**, providing high-speed reasoning and minimal hallucination in Python syntax.

*   **Download Ollama:** [ollama.com](https://ollama.com)
*   **Pull the Model:**
    ```bash
    ollama pull phi3:3.8b
    ```
*   **Run the Server:** Ensure the Ollama service is running locally on `http://localhost:11434`.

## 📂 System Architecture & Workspace
The system follows a **Zero-Leakage Security Protocol** and an automated organizational structure. It manages four primary directories:

1.  **/Sandbox**
    *   **Purpose:** The testing ground where generated scripts are analyzed via **AST** and executed with unique timestamps (e.g., `exec_1714495200.py`).
    *   **Validation:** If the script fails, the **Self-Healing Loop** is triggered with the specific error context.

2.  **/Memoria**
    *   **Purpose:** The persistence vault. It stores `memoria_longa.json`, allowing the agent to retain successful solutions across different sessions.

3.  **/Logs**
    *   **Purpose:** Technical auditability. Every session generates a detailed log file to track the internal reasoning and execution flow.

4.  **/Projetos_Ativos**
    *   **Purpose:** The production-ready vault. Only code that passes all security and execution tests is promoted here.

## ⚡ Quick Start
1. Clone the repository.
2. Launch the core engine:
```bash
python pacheco_v31_3.py
