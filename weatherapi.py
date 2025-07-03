from fastapi import FastAPI
import httpx
import os

app = FastAPI()

WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY= os.environ.get("API", "API not set")

@app.get("/weather/{city}")
async def get_weather(city: str):
    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(WEATHER_API_URL,params=params)
        data=response.json()
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("weatherapi:app",host="127.0.0.1", port= 8000, reload = True)

