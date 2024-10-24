import json
import os
from pathlib import Path

import openai


class GPTApi:
    def __init__(self, config_file: str = f"{Path.cwd()}/config.json"):
        self.config_file = config_file
        self.openai = openai

    def login(self):
        self.api_key = self._load_api_key()
        if not self.api_key:
            self._configure_api_key()
        self.openai.api_key = self.api_key

    def _load_api_key(self):
        """Função para carregar a chave da API a partir do arquivo de configuração."""
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                config = json.load(f)
                return config.get("api_key", "")
        return ""

    def _configure_api_key(self):
        """Função para configurar a chave da API."""
        api_key = input("Por favor, insira sua chave de API da OpenAI: ")
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, "w") as f:
            json.dump({"api_key": api_key}, f)
        self.api_key = api_key

    def ask_llm(self, question: str):
        """Função para consultar a API do ChatGPT."""
        response = self.openai.Completion.create(
            engine="text-davinci-003", prompt=question, max_tokens=150
        )
        return response.choices[0].text.strip()
