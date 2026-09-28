from src.quotation import create_quotation

def main():
    
    customer_name = input("Customer name: ")
    
    items = []
    
    while True:
        
        product_id = input(
            "Product ID (or 'done'): "
        )
        
        if product_id.lower() == "done":
            break
        
        quantity = int(
            input("Quantity: ")
        )
        
        items.append({
            "product_id": product_id,
            "quantity": quantity
        })
        
    try:
             
            quotation = create_quotation(items)
            
            print("\n==== QUOTATION ====")
            print("Customer:", customer_name)
            
            for item in quotation["items"]:
                print(
                    f'{item["name"]} | '
                    f'{item["quantity"]} * '
                    f'₹{item["unit_price"]} = '
                    f'₹{item["total"]}'
                )
                
            print("------------------------")
            print("Subtotal:", quotation["subtotal"])
            print("Discount:", quotation["discount"])
            print("Tax:", quotation["tax"])
            print("Grand Total:", quotation["grand_total"])
            
    except ValueError as error:
            print("Error:", error)
            
if __name__ == "__main__":
    main()
                
            