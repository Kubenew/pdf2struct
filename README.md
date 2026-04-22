# pdf2struct

`pdf2struct` extracts structured JSON from PDF documents.

Supports:
- text extraction
- metadata extraction
- table extraction
- OCR fallback (optional)
- invoice-like key-value extraction

## Install

```bash
pip install pdf2struct
```

OCR support:

```bash
pip install pdf2struct[ocr]
```

## CLI

Extract PDF:

```bash
pdf2struct input.pdf --out output.json
```

Extract with OCR:

```bash
pdf2struct input.pdf --ocr --out output.json
```

## Output JSON structure

- metadata
- pages (text + tables)
- detected_fields (invoice key-value pairs)

## License
MIT
