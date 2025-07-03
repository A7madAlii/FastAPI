from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import os

app= FastAPI()

@app.get("/var", response_class=PlainTextResponse)
def get_var():
    var = os.environ.get('name', 'var non existent')
    return var


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("envvar:app", host ="127.0.0.1", port = 8000, reload = True)