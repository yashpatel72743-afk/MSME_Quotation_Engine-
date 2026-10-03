from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.catalogue import load_catalogue, get_product, update_product, delete_product
from src.quotation import create_quotation

app = FastAPI(title="MSME Quotation Engine")

class Product(BaseModel):
    product_id: str
    name: str
    price: float
    
    
class Item(BaseModel):
    product_id: str
    quantity: int
    
class ProductUpdate(BaseModel):
    product_id: str
    name: str
    price: int
    
    
class ProductPatch(BaseModel):
    name: str | None = None
    price: float | None = None


class QuotationRequest(BaseModel):
    customer_name: str
    items: list[Item] = Field(min_length=1)


@app.get("/")
def home():
    return {"message": "MSME Quotation Engine API chalu chhe"}


@app.get("/products")
def list_products():
    return load_catalogue()


@app.get("/products/{product_id}")
def product(product_id: str):
    try:
        return get_product(product_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@app.post("/quotation")
def quotation(request: QuotationRequest):
    items = [item.model_dump() for item in request.items]

    try:
        result = create_quotation(items)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return {"customer": request.customer_name, **result}

@app.put("/products/{product_id}")
def update(product_id: str, product: ProductUpdate):
    try:
        
        return update_product(
            product_id,
            {
                "product_id": product.product_id,
                "name": product.name,
                "price": product.price
            }
        )
        
        # updated_product = update_product(
        #     product_id,
        #     {
        #         "name": product.name,
        #         "price": product.price
        #     }
        # )

        # return {
        #     "message": "Product updated successfully",
        #     "product_id": product_id,
        #     "product": updated_product
        # }

    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@app.delete("/products/{product_id}")
def delete(product_id: str):
    try:
        deleted = delete_product(product_id)

        return {
            "message": "Product deleted successfully",
            "product": deleted
        }

    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    

@app.patch("/products/{product_id}")
def patch_product(product_id: str, product: ProductPatch):
    try:
        current = get_product(product_id)

        if product.name is not None:
            current["name"] = product.name

        if product.price is not None:
            current["price"] = product.price

        return update_product(product_id, current)

    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))