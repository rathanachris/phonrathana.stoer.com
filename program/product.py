from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

# Initialize FastAPI App with System Documentation Metadata
app = FastAPI(
    title="E-Shop Management API",
    description="A robust backend REST API for managing retail shop products and orders.",
    version="1.0.0"
)

# --- DATA MODELS (SCHEMAS) ---

class Product(BaseModel):
    id: int = Field(..., description="Unique Identifier for the product")
    name: str = Field(..., max_length=50, description="The commercial name of the item")
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    stock: int = Field(..., ge=0, description="Available stock quantity cannot be negative")

class OrderItem(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0, description="Quantity ordered must be at least 1")

class OrderPlacement(BaseModel):
    customer_name: str
    items: List[OrderItem]

# --- IN-MEMORY DATABASE MOCKS ---
PRODUCTS_DB = [
    {"id": 1, "name": "Mechanical Keyboard", "price": 89.99, "stock": 15},
    {"id": 2, "name": "Wireless Ergonomic Mouse", "price": 49.99, "stock": 30}
]
ORDERS_DB = []

# --- ENDPOINTS / ROUTES ---

@app.get("/products", response_model=List[Product], tags=["Products"])
def get_all_products():
    """Retrieve all available items in the shop inventory."""
    return PRODUCTS_DB

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
def get_product(product_id: int):
    """Retrieve details of a single product using its unique ID."""
    for prod in PRODUCTS_DB:
        if prod["id"] == product_id:
            return prod
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED, tags=["Products"])
def create_product(product: Product):
    """Insert a new product into the shop catalog."""
    for prod in PRODUCTS_DB:
        if prod["id"] == product.id:
            raise HTTPException(status_code=400, detail="Product ID already exists")
    
    new_product_dict = product.model_dump()
    PRODUCTS_DB.append(new_product_dict)
    return new_product_dict

@app.post("/orders", status_code=status.HTTP_201_CREATED, tags=["Orders"])
def place_order(order: OrderPlacement):
    """Process a customer transaction, calculate totals, and update stock counts."""
    total_bill = 0.0
    processed_items = []
    
    # Validate stock and calculate metrics safely
    for item in order.items:
        product_found = None
        for prod in PRODUCTS_DB:
            if prod["id"] == item.product_id:
                product_found = prod
                break
                
        if not product_found:
            raise HTTPException(
                status_code=404, 
                detail=f"Product with ID {item.product_id} does not exist"
            )
            
        if product_found["stock"] < item.quantity:
            raise HTTPException(
                status_code=400, 
                detail=f"Insufficient stock for {product_found['name']}. Available: {product_found['stock']}"
            )
        
        # Calculate pricing tiers
        item_total = product_found["price"] * item.quantity
        total_bill += item_total
        
        processed_items.append({
            "product_found": product_found,
            "quantity": item.quantity,
            "item_total": item_total
        })

    # Commit deductions to database state
    for transaction in processed_items:
        transaction["product_found"]["stock"] -= transaction["quantity"]

    order_receipt = {
        "order_id": len(ORDERS_DB) + 1,
        "customer": order.customer_name,
        "total_amount": round(total_bill, 2),
        "status": "Completed"
    }
    ORDERS_DB.append(order_receipt)
    return {"message": "Order processed successfully!", "receipt": order_receipt}
{
  "product_id": 1,
  "quantity": 2
}
{
  "id": 3,
  "name": "Keychron Q1 Mechanical Keyboard",
  "price": 169.99,
  "inventory": 25
}
{
  "id": 3,
  "name": "Keychron Q1 Mechanical Keyboard",
  "price": 169.99,
  "inventory": 25
}
    