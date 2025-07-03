from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

jobs = []


class Job(BaseModel):
    name: str
    title: str

@app.post("/job/")
def create_job(job: Job):
    jobs.append(job)
    return {"Message": "Job created", "Job": job}


@app.get("/job/")
def get_job():
    return jobs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("post:app", host="127.0.0.1", port = 8000, reload=True)



