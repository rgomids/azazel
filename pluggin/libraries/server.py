import requests
from consts import AZAZEL_STONE
from utils.handle_server import handle_response


class Server:
    def __init__(self, address: str = "http://0.0.0.0:", port: str = "8080"):
        self.base_url = address + port
        # Seta no srv a opcao do plugin
        self.change_llm(AZAZEL_STONE.LLM_OPTIONS[0])

    @handle_response
    def ask_llm(self, question: str) -> dict:
        url = f"{self.base_url}/generate"
        headers = {"Content-Type": "application/json"}
        payload = {"content": f"{question}{AZAZEL_STONE.EGO}"}

        response = requests.post(url, headers=headers, json=payload)

        return response

    @handle_response
    def change_llm(self, llm_option):
        url = f"{self.base_url}/change"
        headers = {"Content-Type": "application/json"}
        payload = {"ConfigName": "llm_model", "Value": f"{llm_option}"}

        response = requests.patch(url, headers=headers, json=payload)

        return response

    @handle_response
    def get_info(self):
        url = f"{self.base_url}/info"
        response = requests.get(url)

        return response
