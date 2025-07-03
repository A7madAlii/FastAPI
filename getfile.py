from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


app = FastAPI()

@app.get("/file/", response_class=PlainTextResponse)
def read_file():
    with open("data.txt","r") as f:
        content = f.read()
    return content

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("getfile:app", host = "127.0.0.1", port = 8000, reload = True)