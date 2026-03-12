import os
from dotenv import load_dotenv
import google.generativeai as genai

# cargar variables del .env
load_dotenv()

# obtener la api key
api_key = os.getenv("GENAI_API_KEY")

# configurar modelo
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

pregunta = input("Haz una pregunta: ")

respuesta = model.generate_content(pregunta)

print("\nRespuesta:")
print(respuesta.text)