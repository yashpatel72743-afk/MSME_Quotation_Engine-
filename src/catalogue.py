import json

def load_catalogue():
    with open("data/products.json", "r") as file:
        return json.load(file)
    
    
def get_product(product_id):
    catalogue = load_catalogue()
    
    if product_id not in catalogue:
        raise ValueError(f"Product {product_id} not found")
    
    return catalogue[product_id]