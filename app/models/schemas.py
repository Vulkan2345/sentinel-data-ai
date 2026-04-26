from pydantic import BaseModel
from typing import List, Optional

class Finding(BaseModel):
    type: str
    match_value: str
    line_number: Optional[int] = None
    severity: str

class AnalysisReport(BaseModel):
    filename: str
    size_bytes: int
    mime_type: str
    findings: List[Finding]
    status: str
