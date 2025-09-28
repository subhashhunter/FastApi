from fastapi import APIRouter
from app.services.jagriti_client import fetch_states, fetch_commissions

router = APIRouter()

@router.get("/states")
async def list_states():
    return await fetch_states()

@router.get("/commissions/{state_id}")
async def list_commissions(state_id: str):
    return await fetch_commissions(state_id)
