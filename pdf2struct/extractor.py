from typing import Dict, Any
import pdfplumber

from .models import PDFStruct, PDFPage
from .kv import extract_kv_fields
from .ocr import try_ocr_pdfplumber_page


def extract_pdf(path: str, use_ocr: bool = False) -> Dict[str, Any]:
    pages = []
    all_text = ""

    with pdfplumber.open(path) as pdf:
        meta = dict(pdf.metadata or {})

        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""

            if use_ocr and len(text.strip()) < 30:
                ocr_text = try_ocr_pdfplumber_page(page)
                if ocr_text:
                    text = ocr_text

            tables = []
            try:
                extracted_tables = page.extract_tables()
                if extracted_tables:
                    tables = extracted_tables
            except Exception:
                tables = []

            all_text += "\n" + text

            pages.append(
                PDFPage(
                    page_number=i + 1,
                    text=text,
                    tables=tables,
                    width=page.width,
                    height=page.height,
                )
            )

    detected_fields = extract_kv_fields(all_text)

    doc = PDFStruct(
        file=path,
        metadata=meta,
        pages=pages,
        detected_fields=detected_fields,
    )
    return doc.model_dump()
