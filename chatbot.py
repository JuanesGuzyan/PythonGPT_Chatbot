import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []


# Preguntar y acceder, esto es una funcion
def preguntar_chat_gtp(prompt, modelo='text-davinci-002'):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=1.5
    )
    return respuesta.choices[0].text.strip()


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
    print(f'{respuesta_gpt}')

    preguntas_anteriores.append(ingreso_usuario)
    respuestas_anteriores.append(respuesta_gpt)
