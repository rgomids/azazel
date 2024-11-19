import requests
import json
from pathlib import Path


class OllamaApi:
    def __init__(self, config_file: str = f"{Path.cwd()}/config.json"):
        # config_file responsable for credentials on llm
        self.config_file = config_file
        
    def login(self):
        # Not implemented yet
        pass

    def ask_llm(self, question):

        url = "http://localhost:8080/generate"
        headers = {
            "Content-Type": "application/json" 
        }
        
        payload = {
            "content": f"{question}"
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            print("Resposta:", response.json())
        else:
            print(f"Erro {response.status_code}: {response.text}")

        return response
