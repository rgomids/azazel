from consts import CONSTANTS as ct
from libraries.speach import Speach
from helpers.builder import build_class


class Azazel:
    def __init__(self):
        self.speach = Speach()
        self.llm = self._get_llm_class()
        self._prepare_images()
        
    def _get_llm_class(self): 
        for key, value in enumerate(ct.LLM_OPTIONS.values()):
            print(f"{key + 1}. {value}")
        option = (int(input("Escolha uma opção: ")))
        return build_class(ct.LLM_OPTIONS[option])
    
    def _prepare_images(self, use_graffics: bool = True):
        if use_graffics:
            root = tk.Tk()
            root.withdraw()
            load_gif()
            
    def run(self):
        while True:
            activate_voice_assistant()
            while True:
                question = input("Você: ")
                response = self.llm.ask_llm(question)
                print(f"Azazel: {response}")
                speak(response)
                
if __name__ == "__main__":
    a = Azazel()
    a.run()