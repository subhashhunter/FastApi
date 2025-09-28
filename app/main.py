from fastapi import FastAPI
from app.routes import cases, metadata

# Create FastAPI app instance
app = FastAPI(title="Lexi Backend Assignment")

# Root route
@app.get("/")
async def root():
    return {"message": "FastAPI server is running!"}


app.include_router(metadata.router)
app.include_router(cases.router)

