# Usage

```python
from pdf2struct import extract, extract_tables

# Extract text and metadata
data = extract("document.pdf")
print(data["text"])
print(data["metadata"])

# Extract tables
tables = extract_tables("document.pdf")
for table in tables:
    print(table)
```