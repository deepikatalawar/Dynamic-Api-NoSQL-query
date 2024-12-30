from fastapi import FastAPI
from app.routes.query import router

app = FastAPI(
    title="Dynamic NoSQL Query API",
    description="An API to query MongoDB dynamically with filtering, sorting, and aggregation.",
    version="1.0.0"
)

app.include_router(router, prefix="/api", tags=["Dynamic Query API"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Dynamic NoSQL Query API!"}
