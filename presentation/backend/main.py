from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import openai
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Sert les images statiques
app.mount("/images", StaticFiles(directory="images"), name="images")

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
            except Exception as e:
                pass  # Ignore les fichiers illisibles
        docs_concat = "\n".join(docs_content)
        # Prompt système adapté
        system_prompt = (
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
        match = re.search(r"\[IMAGE:(.*?)\]", raw_answer)
        if match:
            image_name = match.group(1)
            image_url = f"/images/{image_name}"
            # Retirer la balise de la réponse affichée
            answer = re.sub(r"\[IMAGE:.*?\]", "", raw_answer).strip()
        return {"answer": answer, "image_url": image_url}
    except Exception as e:
        return JSONResponse(content={"answer": f"[Erreur OpenAI] {str(e)}"}, status_code=500)

@app.get("/images/{image_name}")
async def get_image(image_name: str):
    image_path = os.path.join("images", image_name)
    if os.path.exists(image_path):
        return JSONResponse(content={"url": f"/images/{image_name}"})
    return JSONResponse(content={"error": "Image non trouvée"}, status_code=404)
