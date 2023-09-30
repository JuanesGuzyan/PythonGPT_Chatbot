import openai
import os
import spacy
import numpy as np
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []
modelo_spacy = spacy.load('es_core_news_md')
palabras_prohibidas = ['madrid', 'palabra2']


def similitud_coseno(vec1, vec2):
    superposicion = np.dot(vec1, vec2)
    magnitud1 = np.linalg.norm(vec1)
    magnitud2 = np.linalg.norm(vec2)
    sim_cos = superposicion / (magnitud1 * magnitud2)
    return sim_cos


def es_relevante(respuesta, entrada, umbral=0.5):
    entrada_vectorizada = modelo_spacy(entrada).vector
    respuesta_vectorizada = modelo_spacy(respuesta).vector
    similitud = similitud_coseno(entrada_vectorizada, respuesta_vectorizada)
    return similitud >= umbral


def filtar_lista_negra(texto, lista_negra):
    token = modelo_spacy(texto)
    resultado = []
    # loop que se encargue de ver la t
    for t in token:
        if t.text.lower() not in lista_negra:
            resultado.append(t.text)
        else:
            resultado.append('[xxxx]')

    return "".join(resultado)


# Preguntar y acceder, esto es una funcion
def preguntar_chat_gtp(prompt, modelo='text-davinci-002'):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=1.5
    )
    # interceptar respuesta
    respuesta_sin_controlar = respuesta.choices[0].text.strip()
    respuesta_controlada = filtar_lista_negra(respuesta_sin_controlar, lista_negra=palabras_prohibidas)
    return respuesta_controlada


# implementar funcionamiento basico con While, le damos y guardamos el contexto para chatgpt para que comprenda mejor
# una conversacion completa
print('Bienvenido a nuestro Chatbot básico. Escribe "salir" cuando quieras terminar')

while True:
    conversacion_historica = ''
    ingreso_usuario = input('\nTú:')
    if ingreso_usuario.lower() == 'salir':
        break

    for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        conversacion_historica += f'El usuario pregunta: {pregunta}\n'
        conversacion_historica += f'ChatGPT responde: {respuesta}\n'

    prompt = f'El usuario pregunta: {ingreso_usuario}\n'
    conversacion_historica += prompt
    respuesta_gpt = preguntar_chat_gtp(conversacion_historica)

    relevante = es_relevante(respuesta_gpt, ingreso_usuario)
    if relevante:
        print(f'{respuesta_gpt}')
        preguntas_anteriores.append(ingreso_usuario)
        respuestas_anteriores.append(respuesta_gpt)
    else:
        print('La respuesta no es relevante')
