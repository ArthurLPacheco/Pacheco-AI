import requests
import json
import logging

# Configuração de Logging - Padrão de indústria para monitoramento
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PachecoEngine:
    def __init__(self, model_name="phi3", base_url="http://localhost:11434/api/generate"):
        self.model_name = model_name
        self.base_url = base_url
        self.context = [] # Buffer para evolução da memória da IA

    def generate_response(self, prompt):
        """Orquestra a chamada para o modelo local com persistência de contexto."""
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "context": self.context # Envia o histórico para a IA "aprender" com a conversa
        }

        try:
            response = requests.post(self.base_url, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            # Atualiza o contexto para a próxima iteração (Base do auto-aprimoramento)
            self.context = data.get("context", [])
            return data.get("response")
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Falha na comunicação com o Core: {e}")
            return None

if __name__ == "__main__":
    # Instancia a Engine da LIMA CORP
    engine = PachecoEngine()
    print("PACHECO AI CORE - System Ready")
    
    while True:
        query = input(">> ")
        if query.lower() in ['exit', 'quit']: break
        
        output = engine.generate_response(query)
        if output:
            print(f"\n[PACHECO]: {output}\n")
