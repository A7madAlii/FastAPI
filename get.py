from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return ("Hello")

@app.get("/hello/{name}")
def read_name(name: str):
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("get:app", host="127.0.0.1", port= 8000)