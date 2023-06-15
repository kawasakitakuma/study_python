from fastapi import FastAPI

app = FastAPI()

@app.get("/countries/{country_name}")
async def country(country_name: str ="japan", city_name: str = "Tokyo"):
    return {
        "country_name": country_name,
        "city_name": city_name
        }
