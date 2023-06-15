from fastapi import FastAPI

app = FastAPI()

#@はデコレーターという機能。 APIの根幹を作成
@app.get("/")
async def index():
    return {"message": "Hello World"}