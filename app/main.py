from fastapi import FastAPI 



app=FastAPI()

@app.get("/health")
async def health():
    return{
        "Message" : "System is Starting"
    }