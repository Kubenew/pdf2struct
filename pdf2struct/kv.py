import re
from typing import Dict, Any


DEFAULT_PATTERNS = {
    "invoice_number": r"(Invoice\s*(No\.|Number)?\s*[:#]?\s*)([A-Z0-9\-\/]+)",
    "date": r"(Date\s*[:#]?\s*)(\d{1,2}[\/\.\-]\d{1,2}[\/\.\-]\d{2,4})",
    "total": r"(Total\s*(Amount)?\s*[:#]?\s*)([0-9\.,]+\s?[A-Z]{0,3})",
    "vat": r"(VAT\s*[:#]?\s*)([0-9\.,]+\s?[A-Z]{0,3})",
    "iban": r"(IBAN\s*[:#]?\s*)([A-Z0-9 ]{10,})",
}


def extract_kv_fields(text: str) -> Dict[str, Any]:
    """
    Extract invoice-like key-value fields from text using regex heuristics.
    """
    results = {}

    for key, pattern in DEFAULT_PATTERNS.items():
        m = re.search(pattern, text, re.IGNORECASE)
        if not m:
            continue

        value = m.group(len(m.groups()))
        results[key] = value.strip()

    return results
