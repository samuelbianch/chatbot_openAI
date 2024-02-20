from flask import Flask
from openai import OpenAI
import dotenv
from time import sleep
from helpers import *

App = Flask(__name__)
App.secret_key = 'alura'
    
dotenv.load_dotenv()
client = OpenAI()

dados_ecommerce = carrega('dados_ecommerce.txt')

def bot(prompt,historico):
    maxima_repeticao = 1
    repeticao = 0
    while True:
        try:
            model='gpt-3.5-turbo'
            prompt_do_sistema = f"""
            
            ## Historico:
            {historico}
            """
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": prompt_do_sistema
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                stream = True,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                model = model)
            return response
        except Exception as erro:
            repeticao += 1
            if repeticao >= maxima_repeticao:
                return "Erro no GPT3: %s" % erro
            print('Erro de comunicação com OpenAI:', erro)
            sleep(1)

from views import *

if __name__ == "__main__":
    App.run(debug = True)
