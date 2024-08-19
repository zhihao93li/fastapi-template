# test_app.py
import pytest
import httpx

# 假设你的 FastAPI 应用运行在 http://localhost:8000
BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_get_ingredient_info_list():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        # 正常情况下的测试
        response = await client.get("/getingredientinfo", params={"ingredient_names": ["ingredient1", "ingredient2"]})
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) == 2
        assert response.json()[0]["name"] == "ingredient1"
        assert response.json()[1]["name"] == "ingredient2"

        # 测试不存在的食材
        response = await client.get("/getingredientinfo", params={"ingredient_names": ["ingredient4"]})
        assert response.status_code == 200
        assert response.json() == []

        # 测试空列表
        response = await client.get("/getingredientinfo", params={"ingredient_names": []})
        assert response.status_code == 200
        assert response.json() == []

        # 测试包含非法类型的参数
        with pytest.raises(httpx.RequestError):
            await client.get("/getingredientinfo", params={"ingredient_names": ["ingredient1", 123]})