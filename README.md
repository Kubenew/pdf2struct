# pdf2struct

[![PyPI Version](https://img.shields.io/pypi/v/pdf2struct)](https://pypi.org/project/pdf2struct/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pdf2struct)](https://pypi.org/project/pdf2struct/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/Kubenew/pdf2struct/actions/workflows/ci.yml/badge.svg)](https://github.com/Kubenew/pdf2struct/actions/workflows/ci.yml)
[![Downloads](https://pepy.tech/badge/pdf2struct)](https://pepy.tech/project/pdf2struct)

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
