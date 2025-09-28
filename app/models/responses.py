from pydantic import BaseModel
from typing import List

class CaseResponse(BaseModel):
    case_number: str
    case_stage: str
    filing_date: str
    complainant: str
    complainant_advocate: str
    respondent: str
    respondent_advocate: str
    document_link: str
