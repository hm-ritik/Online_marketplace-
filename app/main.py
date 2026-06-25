from fastapi import FastAPI 
from app.api.user_router import router



app=FastAPI()
app.include_router(router)
@app.get("/health")
async def health():
    return{
        "Message" : "System is Starting"
    }