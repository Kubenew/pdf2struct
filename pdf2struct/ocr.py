from typing import Optional


def ocr_page_image(pil_image) -> str:
    """
    OCR a PIL image using pytesseract.
    Requires: pip install pdf2struct[ocr]
    """
    try:
        import pytesseract
    except ImportError:
        raise ImportError("OCR requires pytesseract. Install with: pip install pdf2struct[ocr]")

    return pytesseract.image_to_string(pil_image)


def try_ocr_pdfplumber_page(page) -> Optional[str]:
    """
    Converts pdfplumber page to image and OCR it.
    """
    try:
        pil = page.to_image(resolution=200).original
        return ocr_page_image(pil)
    except Exception:
        return None
