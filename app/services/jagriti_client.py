import httpx
from httpx import HTTPStatusError, RequestError
from bs4 import BeautifulSoup
import json

BASE_URL = "https://e-jagriti.gov.in"

async def fetch_states():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(f"{BASE_URL}/getStates")
            resp.raise_for_status() 
            return resp.json()

    except HTTPStatusError:
        return []
    except json.JSONDecodeError:
        return []
    except RequestError:
        return []

async def fetch_commissions(state_id: str):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(f"{BASE_URL}/getCommissions/{state_id}")
            resp.raise_for_status()
            return resp.json()

    except HTTPStatusError:
        return []
    except json.JSONDecodeError:
        return []
    except RequestError:
        return []

async def search_cases(state_id: str, commission_id: str, search_type: str, search_value: str):
    payload = {
        "stateId": state_id,
        "commissionId": commission_id,
        search_type: search_value,
        "caseType": "DCDRC",
        "orderType": "DAILY",
    }
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(f"{BASE_URL}/searchCases", data=payload)
            resp.raise_for_status()

    except HTTPStatusError:
        return []
    except RequestError:
        return []

    soup = BeautifulSoup(resp.text, "html.parser")

    results = []
    rows = soup.select("table tbody tr") 
    
    for row in rows:
        cols = [c.get_text(strip=True) for c in row.find_all("td")]
        if not cols:
            continue
        
        if len(cols) >= 7:
            results.append({
                "case_number": cols[0],
                "case_stage": cols[1],
                "filing_date": cols[2],
                "complainant": cols[3],
                "complainant_advocate": cols[4],
                "respondent": cols[5],
                "respondent_advocate": cols[6],
                "document_link": f"{BASE_URL}/{row.find('a')['href']}" if row.find("a") else ""
            })
    return results

async def search_by_case_number(state_id, commission_id, value):
    return await search_cases(state_id, commission_id, "caseNumber", value)

async def search_by_complainant(state_id, commission_id, value):
    return await search_cases(state_id, commission_id, "complainant", value)

async def search_by_respondent(state_id, commission_id, value):
    return await search_cases(state_id, commission_id, "respondent", value)

async def search_by_complainant_advocate(state_id, commission_id, value):
    return await search_cases(state_id, commission_id, "complainantAdvocate", value)

async def search_by_respondent_advocate(state_id, commission_id, value):
    return await search_cases(state_id, commission_id, "respondentAdvocate", value)

async def search_by_industry_type(state_id, commission_id, value):
    return await search_cases(state_id, commission_id, "industryType", value)

async def search_by_judge(state_id, commission_id, value):
    return await search_cases(state_id, commission_id, "judge", value)

async def get_state_id_by_name(state_name: str):
    states = await fetch_states()
    for s in states:
        if s.get("name", "").lower() == state_name.lower():
            return s.get("id")
    return None

async def get_commission_id_by_name(state_id: str, commission_name: str):
    commissions = await fetch_commissions(state_id)
    for c in commissions:
        if c.get("name", "").lower() == commission_name.lower():
            return c.get("id")
    return None
