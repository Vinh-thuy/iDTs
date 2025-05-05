from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import pathlib
import openai
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# Sert les images statiques
BASE_DIR = pathlib.Path(__file__).parent
IMAGES_DIR = BASE_DIR.parent / "images"
print(f"[DEBUG] Images will be served from: {IMAGES_DIR}")
app.mount("/images", StaticFiles(directory=str(IMAGES_DIR)), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend IA prêt !"}

@app.post("/ask")
async def ask_bot(request: Request):
    data = await request.json()
    question = data.get("question", "")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        return JSONResponse(content={"answer": "[Erreur] Clé API OpenAI manquante."}, status_code=500)
    try:
        import glob
        # Lecture et concaténation des fichiers sources
        base_dir = "/Users/vinh/Documents/iDTs/Analyse_existant"
        docs_content = []
        for file_path in glob.glob(os.path.join(base_dir, "*.md")) + glob.glob(os.path.join(base_dir, "*.txt")):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    docs_content.append(f"\n---\nFichier : {os.path.basename(file_path)}\n" + f.read())
            except Exception:
                continue  # Ignore les fichiers illisibles
        docs_concat = "\n".join(docs_content)
        # Prompt système adapté
        system_prompt = (
            "IMPORTANT : Si l'utilisateur demande une introduction ou définition générale du Digital Twin, insère systématiquement la balise [IMAGE:digital_twin.png] dans ta réponse.\n"
            "IMPORTANT : Si l'utilisateur pose une question sur le LLM lors de la phase d'ingestion, insère la balise [IMAGE:llm_ingestion.jpeg] dans la réponse.\n"
            "IMPORTANT : Si l'utilisateur pose une question sur ce qu'est un réseau neuronal, un réseau symbolique, ou sur la comparaison ou l'explication des deux, insère la balise [IMAGE:symbolique_neuronale.jpeg] dans la réponse.\n"
            "IMPORTANT : Si la question de l'utilisateur porte sur le LLM agentique, insère la balise [IMAGE:agentic.jpeg] dans la réponse.\n"
            "IMPORTANT : Tu participes à une démonstration de 30 minutes devant un public non expert. Tes réponses doivent être très synthétiques, claires, pédagogiques et adaptées à ce contexte. Les longs textes ne sont pas appropriés : privilégie la concision, les explications simples et les formulations accessibles.\n"
            "IMPORTANT : Ta personnalité doit être fun, amicale, avec une bonne dose d’humour, comme un vrai pote qui brainstorme avec l’utilisateur. Tu simplifies au maximum, tu encourages, tu guides, tu fais sourire et tu rends la conversation vivante et motivante.\n"
            "Donne toujours des réponses TRÈS courtes, quitte à être un peu taquin ou à répondre par une blague. Si la question mérite plus de détails, propose à l’utilisateur de demander une explication ou d’aller plus loin.\n"
            "N’hésite pas à poser une question à l’utilisateur pour l’impliquer ou vérifier s’il souhaite plus de détails.\n"
            "IMPORTANT : Structure toujours tes réponses pour maximiser la lisibilité : \n"
            "- Utilise des paragraphes courts et espacés.\n"
            "- Mets les mots-clés et concepts importants en **gras** (markdown).\n"
            "- Utilise des listes à puces si pertinent.\n"
            "- Ajoute des retours à la ligne fréquents pour aérer le texte.\n"
            "- N’hésite pas à utiliser des emojis pour attirer l’attention si pertinent.\n"
            "IMPORTANT : Lorsque l'utilisateur demande une illustration ou une image, insère la balise [IMAGE:img1.png] à l'endroit voulu dans ta réponse (par exemple : 'Voici une illustration : [IMAGE:img1.png]'). Ne mets la balise que si l'image est pertinente.\n"
            "Tu es un assistant expert. Tu dois répondre en priorité en t'appuyant sur les documents suivants :\n"
            f"{docs_concat[:9000]}"  # Tronque si trop long
            "\nTu peux également utiliser tes connaissances générales pour compléter ou expliquer, mais tu dois toujours vérifier que tes réponses sont cohérentes avec le contenu des documents ci-dessus et ne jamais les contredire.\n"
            "Si tu apportes une information qui n'est pas explicitement présente dans les documents, précise-le ou formule avec prudence.\n"
            "En cas de contradiction, donne toujours la priorité à la logique et aux indications des documents indexés."
        )
        openai.api_key = openai_api_key
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            max_tokens=512,
            temperature=0.7
        )
        raw_answer = response.choices[0].message.content.strip()
        image_url = None
        answer = raw_answer
        import re
        # Image custom tag
        match = re.search(r"\[IMAGE:\s*(.*?)\s*\]", raw_answer)
        if match:
            image_name = match.group(1).strip()
            image_url = f"/images/{image_name}"
            # Retirer la balise de la réponse
            answer = re.sub(r"\[IMAGE:[^\]]*\]", "", raw_answer).strip()
        else:
            # Fallback: markdown image syntax
            md_match = re.search(r"!\[.*?\]\((.*?)\)", raw_answer)
            if md_match:
                raw_path = md_match.group(1).strip()
                # Normalize path
                if raw_path.startswith("/images/"):
                    image_url = raw_path
                else:
                    image_url = f"/images/{os.path.basename(raw_path)}"
                # Retirer le markdown image
                answer = re.sub(r"!\[.*?\]\(.*?\)", "", raw_answer).strip()
        # Debug: show image_url detected
        print(f"[DEBUG] Detected image_url: {image_url}", flush=True)
        return {"answer": answer, "image_url": image_url}
    except Exception as e:
        return JSONResponse(content={"answer": f"[Erreur OpenAI] {str(e)}"}, status_code=500)
