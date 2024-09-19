from fastapi import FastAPI
from products.products import router as product_router
from orders.orders import router as order_router

app = FastAPI(title="Storage")
app.include_router(product_router)
app.include_router(order_router)
