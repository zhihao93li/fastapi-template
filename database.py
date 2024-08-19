# database.py
from pymongo import MongoClient
from typing import List, Dict, Generator

class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    async def get_ingredient(self, name: str):
        ingredient = self.db.ingredients.find_one({"name": name})
        return ingredient

    async def get_ingredients(self, ingredient_names: List[str]) -> List[dict]:
        # 使用合适的查询方法一次性获取所有食材的信息
        # 这里假设数据库支持这样的批量查询操作
        # 需要根据实际情况编写具体的查询和处理逻辑
        ingredients = []  # 假设这是从数据库批量获取的食材信息
        for ingredient_name in ingredient_names:
            if ingredient_name in ingredients:
                yield ingredient_name