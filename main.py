from fastapi import FastAPI, List
from database import Database
from typing import List

app = FastAPI()
db = Database("mongodb://mongo:4q583jt2myJCXkNdlW0c7pMOu1w9UD6E@sha1.clusters.zeabur.com:31941/", "ingredient")

@app.get("/getingredientinfo")
async def get_ingredient_info_list(ingredient_names: List[str]):
    if not ingredient_names:
        return []
    if not all(isinstance(name, str) for name in ingredient_names):
        raise ValueError("All elements in ingredient_names must be strings.")

    ingredient_info = []
    try:
        ingredients = await db.get_ingredients(ingredient_names)
        return ingredients
    except Exception as e:
        print(f"Error fetching ingredients: {e}")
        return []ingredients = await db.get_ingredients(ingredient_names)
return ingredients