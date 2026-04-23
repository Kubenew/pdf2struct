# pdf2struct

Extract structured JSON from PDF documents.

## Features

- Text extraction
- Metadata extraction  
- Table extraction
- OCR fallback (optional)
- Invoice-like key-value extraction

## Quick Start

```bash
pip install pdf2struct
```

```python
from pdf2struct import extract

data = extract("document.pdf")
print(data)
```