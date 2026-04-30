import requests
import json
import os
import re
import subprocess
from datetime import datetime

# === CONFIG ===
MODELO = "phi3:3.8b" 
URL = "http://localhost:11434/api/generate"

TIMEOUT_CONNECT = 10
TIMEOUT_READ = 120 

DIRETORIOS = ["Sandbox", "Projetos_Ativos"]
REGEX_CODIGO = re.compile(r'```python\n(.*?)\n```', re.DOTALL)

session = requests.Session()

def inicializar():
    for pasta in DIRETORIOS:
        os.makedirs(pasta, exist_ok=True)

# === SEGURANÇA INTELIGENTE ===
def codigo_seguro(codigo):
    bloqueados = ["os.remove", "shutil.rmtree", "__import__", "eval(", "exec(", "subprocess.call"]
    if any(b in codigo for b in bloqueados):
        return False
    if ("open(" in codigo or "with open" in codigo) and "Sandbox" not in codigo:
        return False
    return True

# === EXECUÇÃO COM FEEDBACK ===
def executar_codigo(codigo):
    nome = f"exec_{int(datetime.now().timestamp())}.py"
    caminho = os.path.join("Sandbox", nome)

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(codigo)

    try:
        r = subprocess.run(
            ["python", caminho],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=15
        )
        output = (r.stdout + r.stderr).strip()
        return (r.returncode == 0), output
    except subprocess.TimeoutExpired:
        return False, "Erro: Timeout na execução (Possível loop ou modo r+ travado)"

def stream_ollama(prompt, max_tokens=2048):
    payload = {
        "model": MODELO,
        "prompt": prompt,
        "stream": True,
        "options": {"temperature": 0.2, "num_ctx": 4096}
    }
    try:
        with session.post(URL, json=payload, stream=True, timeout=(TIMEOUT_CONNECT, TIMEOUT_READ)) as r:
            resposta_completa = ""
            for linha in r.iter_lines():
                if linha:
                    data = json.loads(linha.decode("utf-8"))
                    token = data.get("response", "")
                    print(token, end="", flush=True)
                    resposta_completa += token
                    if data.get("done"): break
            print()
            return resposta_completa
    except Exception as e:
        print(f"\n[ERRO Ω] Falha: {e}")
        return ""

# === MOTOR DE PROMPT AUTO-CORRETIVO (v30.7) ===
def montar_prompt(pergunta, erro=None, codigo_falho=None):
    if erro:
        return (
            f"ERRO CRÍTICO NO SEU CÓDIGO: {erro}\n"
            f"CÓDIGO QUE VOCÊ ESCREVEU:\n```python\n{codigo_falho}\n```\n"
            "CORRIJA AGORA:\n"
            "1. Você usou uma variável que não existe? Verifique os nomes!\n"
            "2. IMPORTANTE: Use apenas 'import os' e 'import json'.\n"
            "3. Use caminhos simples: 'Sandbox/estoque.json'.\n"
            "4. APENAS O CÓDIGO NO BLOCO."
        )
    
    return (
        "Aja como um Desenvolvedor Python Minimalista da LIMA CORP.\n"
        "REGRAS:\n"
        "1. SEMPRE verifique se a variável que você está salvando foi definida com o mesmo nome.\n"
        "2. Use o fluxo: dados = json.load(open('r')) -> modificar -> json.dump(dados, open('w')).\n"
        "3. Se o arquivo não existir, trate isso com um IF simples.\n"
        f"Tarefa: {pergunta}"
    )
    
    gatilhos = ["script", "codigo", "python", "def ", "import ", "programa", "inventory"]
    if any(g in pergunta.lower() for g in gatilhos):
        return (
            "Aja como um Desenvolvedor Python Sênior da LIMA CORP.\n"
            "TAREFA: " + pergunta + "\n"
            "RESTRICÕES:\n"
            "1. Responda APENAS com o bloco ```python ... ```.\n"
            "2. Se for manipular JSON, use o fluxo: ler('r') -> modificar -> salvar('w').\n"
            "3. Use caminhos: os.path.join('Sandbox', 'arquivo.json').\n"
            "4. Verifique se o arquivo existe antes de ler."
        )
    return f"Diretor de Tecnologia LIMA CORP. Responda de forma curta: {pergunta}"

if __name__ == "__main__":
    inicializar()
    print("="*40)
    print("PACHECO AI Ω - VERSÃO 30.7 SELF-HEALING")
    print("STATUS: OPERACIONAL | FOCO: AUTO-CORREÇÃO")
    print("="*40)

    while True:
        try:
            user_input = input("\n> ").strip()
            if user_input.lower() in ["sair", "exit", "quit"]: break
            if not user_input: continue

            prompt = montar_prompt(user_input)
            print("\n[PACHECO Ω PENSANDO...]\n")
            resposta = stream_ollama(prompt)

            # Loop de Tentativa Única de Auto-Cura
            blocos = REGEX_CODIGO.findall(resposta)
            if blocos:
                cod_final = "\n".join(blocos)
                if codigo_seguro(cod_final):
                    print("\n" + "-"*20 + "\n[EXECUTANDO PROTÓTIPO]")
                    sucesso, out = executar_codigo(cod_final)
                    print(out + "\n" + "-"*20)

                    if not sucesso:
                        print("\n[DETECTADO ERRO] Iniciando Auto-Cura...")
                        prompt_correcao = montar_prompt(user_input, erro=out, codigo_falho=cod_final)
                        resposta_corrigida = stream_ollama(prompt_correcao)
                        
                        blocos_corrigidos = REGEX_CODIGO.findall(resposta_corrigida)
                        if blocos_corrigidos:
                            cod_final = "\n".join(blocos_corrigidos)
                            sucesso, out = executar_codigo(cod_final)
                            print("\n" + "-"*20 + "\n[RESULTADO PÓS-CURA]")
                            print(out + "\n" + "-"*20)

                    if sucesso:
                        nome_base = re.sub(r'\W+', '_', user_input)[:20]
                        caminho = os.path.join("Projetos_Ativos", f"{nome_base}.py")
                        with open(caminho, "w", encoding="utf-8") as f: f.write(cod_final)
                        print(f"[SISTEMA] Projeto salvo: {caminho}")

        except KeyboardInterrupt: break
