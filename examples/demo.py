from pdf2struct import extract_pdf

data = extract_pdf("sample.pdf", use_ocr=True)

print("Pages:", len(data["pages"]))
print("Detected fields:", data["detected_fields"])
