import random

import fastapi

app = fastapi.FastAPI()

@app.get("/generate_name")
async def generate_name(starts_with: str = None):
    names = ["Minnie", "Margaret", "Myrtle", "Noa", "Nadia"]
    if starts_with:
        names = [n for n in names if n.lower().startswith(starts_with)]
    if len(names) == 0:
        raise fastapi.HTTPException(status_code=404, detail="No name found")
    random_name = random.choice(names)
    return {"name": random_name}