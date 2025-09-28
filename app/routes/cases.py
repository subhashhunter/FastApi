from fastapi import APIRouter
from app.services.jagriti_client import (
    search_by_case_number,
    search_by_complainant,
    search_by_respondent,
    search_by_complainant_advocate,
    search_by_respondent_advocate,
    search_by_industry_type,
    search_by_judge,
    get_state_id_by_name,
    get_commission_id_by_name,
)

router = APIRouter()

# Helper to get IDs
async def resolve_ids(state_name: str, commission_name: str):
    state_id = await get_state_id_by_name(state_name)
    if not state_id:
        return None, None
    commission_id = await get_commission_id_by_name(state_id, commission_name)
    return state_id, commission_id

@router.get("/cases/by-case-number")
async def cases_by_number(state: str, commission: str, value: str):
    state_id, commission_id = await resolve_ids(state, commission)
    if not state_id or not commission_id:
        return {"error": "State or Commission not found"}
    return await search_by_case_number(state_id, commission_id, value)

@router.get("/cases/by-complainant")
async def cases_by_complainant(state: str, commission: str, value: str):
    state_id, commission_id = await resolve_ids(state, commission)
    if not state_id or not commission_id:
        return {"error": "State or Commission not found"}
    return await search_by_complainant(state_id, commission_id, value)

@router.get("/cases/by-respondent")
async def cases_by_respondent(state: str, commission: str, value: str):
    state_id, commission_id = await resolve_ids(state, commission)
    if not state_id or not commission_id:
        return {"error": "State or Commission not found"}
    return await search_by_respondent(state_id, commission_id, value)

@router.get("/cases/by-complainant-advocate")
async def cases_by_complainant_advocate(state: str, commission: str, value: str):
    state_id, commission_id = await resolve_ids(state, commission)
    if not state_id or not commission_id:
        return {"error": "State or Commission not found"}
    return await search_by_complainant_advocate(state_id, commission_id, value)

@router.get("/cases/by-respondent-advocate")
async def cases_by_respondent_advocate(state: str, commission: str, value: str):
    state_id, commission_id = await resolve_ids(state, commission)
    if not state_id or not commission_id:
        return {"error": "State or Commission not found"}
    return await search_by_respondent_advocate(state_id, commission_id, value)

@router.get("/cases/by-industry-type")
async def cases_by_industry_type(state: str, commission: str, value: str):
    state_id, commission_id = await resolve_ids(state, commission)
    if not state_id or not commission_id:
        return {"error": "State or Commission not found"}
    return await search_by_industry_type(state_id, commission_id, value)

@router.get("/cases/by-judge")
async def cases_by_judge(state: str, commission: str, value: str):
    state_id, commission_id = await resolve_ids(state, commission)
    if not state_id or not commission_id:
        return {"error": "State or Commission not found"}
    return await search_by_judge(state_id, commission_id, value)
