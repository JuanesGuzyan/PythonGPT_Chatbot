import os
from dotenv import load_dotenv
import openai
import spacy


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
# Tiene que usar nuestra clave
openai.api_key = api_key

# modelos = openai.Model.list()
# print(modelos)

modelo = "text-davinci-002"
prompt = "Cuenta una historia breve sobre un viaje a un país Europeo"

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

texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)
print("***")
# analizar tokens del texto generado
modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

ubicacion = None

for ent in analisis.ents:
    if ent.label_ == "LOC":
        ubicacion = ent
        break
# Generar un nuevo pedido tomando en cuenta la palabra extraida
if ubicacion:
    prompt2 = f'Dime más acerca de {ubicacion}'
    respuesta2 = openai.Completion.create(
        engine=modelo,
        prompt=prompt2,
        n=1,
        max_tokens=100
    )
    print(respuesta2.choices[0].text.strip())