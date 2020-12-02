from app import is_alive_host
from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/healthz")
def read_item(hostname: str):
    return {"status": "up" if is_alive_host(hostname) else "down"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)