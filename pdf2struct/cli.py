import argparse
import json
from .extractor import extract_pdf


def main():
    parser = argparse.ArgumentParser(prog="pdf2struct", description="Extract structured JSON from PDF")
    parser.add_argument("pdf_file")
    parser.add_argument("--out", required=True)
    parser.add_argument("--ocr", action="store_true", help="Enable OCR fallback (requires pdf2struct[ocr])")

    args = parser.parse_args()

    data = extract_pdf(args.pdf_file, use_ocr=args.ocr)

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
