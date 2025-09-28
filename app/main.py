import os
from fastapi import FastAPI
from app.routes import cases, metadata
import uvicorn

app = FastAPI(title="Lexi Backend Assignment")

@app.get("/")
async def root():
    return {"message": "FastAPI server is running!"}

app.include_router(metadata.router)
app.include_router(cases.router)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)