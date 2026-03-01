from fastapi import FastAPI, Request, Response
from datetime import datetime
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"{request.method} {request.url.path}")
    return await call_next(request)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/api/time")
async def get_time(request: Request, response: Response):
    if request.headers.get("X-Debug") == "fail":
        response.status_code = 500
        return {"error": "forced failure"}
    return {"time": datetime.utcnow().isoformat()}
