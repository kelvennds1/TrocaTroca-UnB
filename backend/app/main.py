from fastapi import FastAPI
from app.database import engine, Base
from app.routes import user, category, item, swap, login



app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/api/users")
app.include_router(category.router, prefix="/api/categories")
app.include_router(item.router, prefix="/api/items")
app.include_router(swap.router, prefix="/api/swaps")
app.include_router(login.router, prefix="/api/auth")

@app.get("/")
def read_root():
    return {"message": "Welcome to the TrocaTroca API!"}
