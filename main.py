from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

app = FastAPI()

@app.post("/item/")
async def create_item(item: Item):
    #下記を表示することに成功
    return {'message': f"{item.name}は、税込価格{int(item.price*item.tax)}円です"}



