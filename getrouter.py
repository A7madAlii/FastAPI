from fastapi import APIRouter

app = APIRouter()

@app.get("/router")
def getMessage():
    return {"Hello"}


