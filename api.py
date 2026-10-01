from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.catalogue import load_catalogue
from src.quotation import create_quotation

app = FastAPI(title="MSME Quotation Engine")


class Item(BaseModel):
    product_id: str
    quantity: int


class QuotationRequest(BaseModel):
    customer_name: str
    items: list[Item] = Field(min_length=1)


@app.get("/")
def home():
    return {"message": "MSME Quotation Engine API chalu chhe"}


@app.get("/products")
def list_products():
    return load_catalogue()


@app.post("/quotation")
def quotation(request: QuotationRequest):
    items = [item.model_dump() for item in request.items]

    try:
        result = create_quotation(items)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return {"customer": request.customer_name, **result}