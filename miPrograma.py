import os
from dotenv import load_dotenv
import openai


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
# Tiene que usar nuestra clave
openai.api_key = api_key

# modelos = openai.Model.list()
# print(modelos)

modelo = "text-davinci-002"
prompt = "Elige un nombre para elefante"

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    # Numero de respuestas
    n=1,
    # Temperatura es creatividad
    temperature=0.1,
    # max_tokens es el largo de la respuesta
    max_tokens=50
)

# Loop for para leer varias respuestas
for idx, opcion in enumerate(respuesta.choices):
    texto_generado = opcion.text.strip()
    print(f'Respuesta: {idx + 1}: {texto_generado}\n')
# strip elimina espacios blancos antes y despues
# texto_generado = respuesta.choices[0].text.strip()
# print(texto_generado)
