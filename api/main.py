import random

import fastapi

app = fastapi.FastAPI()

@app.get("/generate_name")
async def generate_name():
    names = ["Minnie", "Margaret", "Myrtle", "Noa", "Nadia"]
    random_name = random.choice(names)
    return {"name": random_name}