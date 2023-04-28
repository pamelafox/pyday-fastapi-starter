import random

import fastapi

app = fastapi.FastAPI()

@app.get("/generate_name")
async def generate_name(max_len: int = None, starts_with: str = None):
    names = ["Minnie", "Margaret", "Myrtle", "Noa", "Nadia"]
    if max_len:
        names = [name for name in names if len(name) <= max_len]
    if starts_with:
        names = [name for name in names if name.startswith(starts_with)]
    random_name = random.choice(names)
    return {"name": random_name}