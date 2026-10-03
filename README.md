# MSME_Quotation_Engine-

-> A simple Python project taht generates quotations based on products, quantity, discount rules, and tax.


# What this project does

-> The application takes a product from the catalogue and calculates the quotation based on the quantity ordered.

=> The basic flow is:
    Product -> Quantity -> Subtotal -> Discount -> Tax -> Final Total

FOR EXAMPLE:- 
              If a customer orders multiple products, the system checker whether the products exit, calculates the price, applies the required discount, adds tax, and returns the final quotation.

# Discount Rules

• 5% discount when the subtotal is ₹50,000 or more
• 10% discount when the subtotal is ₹1,00,000 or more 
• No discount below ₹50,000

Tax is calculated at 18%.

# This project designed using professional Python project structure 

• Data validation
• Business logic
• Exception handling
• Logging
• Pydantic models
• API integreation using FastAPI
• Testing support

# Features

• Product catalogue management
• Product validation
• Quantity validation
• Tax calculation
• Discount calculation
• Final quotation calculation
• Input validation
• Error handling
• API ready architecture

# Technologies Used

• Python
• Json
• FastAPI
• Postman
• Github

# Run the Project

1. Run main Quotation program:
  • python src/main.py 

  * Run the API:
-> The project also include a FastAPI.

-> Start the servercfrom the project root folder.
    python -m uvicorn api:app --reload

-> After starting the server, open:
    http://127.0.0.1:8000 

-> FastAPI also provides an interactive documentation page:
    http://127.0.0.1:8000/docs

* The API can be tested using Postman.

