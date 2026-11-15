
## Imports 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.random_forest_router import random_forest_router

app = FastAPI()

## Add Routers 
app.include_router(random_forest_router, tags=['RandomForestModel'])

## open the CORS Middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

## End Points

@app.get("/")
async def check_server():
    return "The Server Is Up And Running ✅"