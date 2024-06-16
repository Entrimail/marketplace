from fastapi import FastAPI
from products.products import router as product_router
from categories.categories import router as categories_router

app = FastAPI(title="Marketplace")
app.include_router(product_router)
app.include_router(categories_router)
