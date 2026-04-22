from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class PDFPage(BaseModel):
    page_number: int
    text: str
    tables: List[List[List[str]]] = []
    width: Optional[float] = None
    height: Optional[float] = None


class PDFStruct(BaseModel):
    file: str
    metadata: Dict[str, Any] = {}
    pages: List[PDFPage]
    detected_fields: Dict[str, Any] = {}
