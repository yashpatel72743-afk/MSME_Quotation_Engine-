import json

FILE_PATH = "data/products.json"


def load_catalogue():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_catalogue(catalogue):
    with open(FILE_PATH, "w") as file:
        json.dump(catalogue, file, indent=4)


def get_product(product_id):
    catalogue = load_catalogue()

    if product_id not in catalogue:
        raise ValueError(f"Product {product_id} not found")

    return catalogue[product_id]


def update_product(product_id, product_data):
    catalogue = load_catalogue()

    if product_id not in catalogue:
        raise ValueError(f"Product {product_id} not found")

    catalogue[product_id] = product_data

    save_catalogue(catalogue)

    return catalogue[product_id]


def delete_product(product_id):
    catalogue = load_catalogue()

    if product_id not in catalogue:
        raise ValueError(f"Product {product_id} not found")

    deleted_product = catalogue.pop(product_id)

    save_catalogue(catalogue)

    return deleted_product