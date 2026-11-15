
## Imports 
from fastapi import FastAPI

app = FastAPI()

## End Points

@app.get("/")
async def check_server():
    return "The Server Is Up And Running ✅"