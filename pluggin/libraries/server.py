import json
from pathlib import Path

import requests


class Server:
    def __init__(self, address: str = "http://0.0.0.0:", port: str = "8080"):
        self.base_url = address + port

    def ask_llm(self, question: str) -> dict:
        url = f"{self.base_url}/generate"
        headers = {"Content-Type": "application/json"}
        payload = {"content": f"{question} *** responda de forma sucinta!!! ***"}

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            print("Resposta:", response.json())
        else:
            print(f"Erro {response.status_code}: {response.text}")

        return response.json()["responses"]

    def change_llm(self, llm_option):
        url = f"{self.base_url}/change"
        headers = {"Content-Type": "application/json"}
        payload = {
                "ConfigName": "llm_model",
                "Value": f"{llm_option}"
        }

        response = requests.patch(url, headers=headers, json=payload)

        if response.status_code == 200:
            print("Resposta:", response.json())
        else:
            print(f"Erro {response.status_code}: {response.text}")

    def get_info(self):
        url = f"{self.base_url}/info"
        response = requests.get(url)

        if response.status_code == 200:
            print("Resposta:", response.json())
        else:
            print(f"Erro {response.status_code}: {response.text}")
