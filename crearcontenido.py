import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


# Funcion para crear contenido
def crear_contenido(tema, tokens, temperatura, modelo='text-davinci-002'):
    prompt = f'Por favor escribe un artículo corto sobre el tema: {tema}\n\n'
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()


# Funcion para resumir contenido
def resumir_text(texto, tokens, temperatura, modelo='text-davinci-002'):
    prompt = f'Por favor resume el siguiente texto en español: {texto}\n\n'
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()


# probar ambas funciones
# Escribir la dinamica del programa
original = input('Pega aqui el articulo que quieres resumir sin saltos de linea: ')
tokens = int(input('Cuantos tokens maximos tendra tu resumen: '))
temperatura = int(input('Del 1 al 10, que tan creativo quieres que sea tu resumen?: ')) / 10
resumen = resumir_text(original, tokens, temperatura)
print(resumen)

"""
tema = input('Elije un tema para tu articulo: ')
tokens = int(input('Cuantos tokens maximos tendra tu articulo: '))
temperatura = int(input('Del 1 al 10, que tan creativo quieres que sea tu articulo?: ')) / 10
articulo_creado = crear_contenido(tema, tokens, temperatura)
print(articulo_creado)

"""