import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


# funcion para traducir texto
def traducir_texto(texto, idioma):
    prompt = f"Traduce el texto '{texto} al {idioma}'"
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        n=1,
        temperature=0.5,
        max_tokens=150
    )
    return response.choice[0].text.strip()


# probar la funcion

mi_texto = input('Escribe el texto que quieres traducir: ')
mi_idioma = input('A que idioma lo quieres traducir: ')
traduccion = traducir_texto(mi_texto, mi_idioma)
print(traduccion)
