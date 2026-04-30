import requests
import json

def pacheco_terminal():
    print("="*40)
    print("PACHECO AI - LIMA CORP SYSTEM v1.0")
    print("Status: Operational | Engine: Ollama")
    print("="*40)
    
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            break
            
        # Conecta com o seu Ollama local
        payload = {
            "model": "phi3", # Ou o modelo que você estiver usando
            "prompt": user_input,
            "stream": False
        }
        
        try:
            response = requests.post("http://localhost:11434/api/generate", json=payload)
            data = json.loads(response.text)
            print(f"\nPACHECO: {data['response']}\n")
        except Exception as e:
            print(f"Erro de conexão: {e}")

if __name__ == "__main__":
    pacheco_terminal()
