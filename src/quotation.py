from catalogue import get_product


TAX_RATE = 18

def calculate_discount(subtotal):
    if subtotal >= 100000:
        return subtotal * 0.10

    if subtotal >= 50000:
        return subtotal * 0.05
    
    return 0 


def create_quotation(items):
    quotation_items = []
    subtotal = 0 
    
    for item in items:
        
        product = get_product(item["product_id"])
        quantity = item["quantity"]
        
        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero"
            )
            
        unit_price = product["price"]
        total = unit_price * quantity
        
        quotation_items.append({
            "product_id": item["product_id"],
            "name": product["name"],
            "quantity": quantity,
            "unit_price": unit_price,
            "total": total            
        })
        
        subtotal += total
        
    discount = calculate_discount(subtotal)
    
    taxable_amount = subtotal - discount
    
    tax = taxable_amount * TAX_RATE / 100
    
    grand_total = taxable_amount + tax 
    
    return{
        "items": quotation_items,
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "grand_total": grand_total
    }