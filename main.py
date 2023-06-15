from fastapi import FastAPI

app = FastAPI()

#@はデコレーターという機能。 APIの根幹を作成
@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}

@app.get("/countries/japan")
async def japan():
    return {"country_name": "This is Japan!"}