from fastapi import FastAPI 
from app.api.user_router import router as rt1
from app.api.locality_router import router as rt2
from app.api.store_router import router as rt3


app=FastAPI()
app.include_router(rt1)
app.include_router(rt2)
app.include_router(rt3)
@app.get("health/")
async def health():
    return{
        "Message" : "System is Starting"
    }