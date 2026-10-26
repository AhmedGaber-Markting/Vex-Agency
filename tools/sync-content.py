"""Refresh the local/offline content fallback after editing content.json."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent.parent
content=(root/'content.json').read_text(encoding='utf-8-sig')
json.loads(content)
script='window.__PORTFOLIO_CONTENT__ = '+content+';\n'
(root/'content-data.js').write_text(script,encoding='utf-8')
print('content-data.js is up to date.')
