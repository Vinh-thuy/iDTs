import os
from dotenv import load_dotenv
from openai import OpenAI

# Charger les variables d'environnement
load_dotenv()

# Initialiser le client OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

try:
    # Test avec GPT-4 Omni
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un assistant technique qui répond de manière concise."},
            {"role": "user", "content": "Peux-tu me donner un exemple simple de test de connexion API ?"}
        ]
    )
    
    # Afficher la réponse
    print("Réponse de l'API :")
    print(response.choices[0].message.content)
    
except Exception as e:
    print(f"Erreur lors de l'appel à l'API OpenAI : {e}")
