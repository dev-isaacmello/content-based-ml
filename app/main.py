from fastapi import FastAPI
from pydantic import BaseModel
from .model import ImplicitRecommender

app = FastAPI()

recommender = ImplicitRecommender()

VIDEOS = {
    "python_basico": [1, 0, 0, 0],
    "python_avancado": [0, 0, 1, 0],
    "ia_intro": [0, 1, 0, 1],
    "ia_avancado": [0, 0, 0, 2],
}

class WatchInput(BaseModel):
    video: str
    seconds: int

@app.post("/watch")
def watch(data: WatchInput):
    recommender.watch(
        VIDEOS[data.video],
        data.seconds
    )

    return {"message": f"Assistiu {data.video} por {data.seconds} segundos."}

@app.get("/recommend")
def recommend():
    ranked = []

    for name, vector in VIDEOS.items():
        ranked.append({
            "video": name,
            "score": round(recommender.score(vector), 2)
        })

    return sorted(ranked, key=lambda x: x["score"], reverse=True)