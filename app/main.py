from fastapi import FastAPI
from app.routes.query import router as query_router

app = FastAPI()

# Include the query route
app.include_router(query_router)
