from fastapi import FastAPI
from app.routers import product, order, category, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(order.router)
app.include_router(category.router)

@app.get("/")
async def root():
    return {"message": "API funcionando, Basta testar o forntEnd agora!!"}