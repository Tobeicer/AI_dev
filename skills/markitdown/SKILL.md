---
name: markitdown
description: Convert file formats to Markdown using Microsoft's markitdown. Trigger when user wants to convert PDF, Word (docx), PowerPoint (pptx), Excel (xlsx/xls), images (jpg/png), audio (wav/mp3), HTML, EPUB, CSV, JSON, XML, ZIP archives, or YouTube URLs to Markdown. Also trigger when user says "convert to markdown", "extract text from this file", "transcribe this audio", "what's in this PDF/PPT/Excel", "turn this document into text", or needs to prepare documents for LLM/RAG processing. This skill must be invoked ANY TIME a user mentions a file containing data they want to read or analyze.
---

# MarkItDown - Document to Markdown Converter

Convert files to Markdown using Microsoft's open-source `markitdown` CLI/Python library. Output is optimized for LLM consumption — preserves headings, lists, tables, links while staying token-efficient.

## Decision Flow

```
User provides a file or URL to convert
  ↓
Is markitdown installed? → pip show markitdown
  ├─ No → pip install 'markitdown[all]'
  ↓
Is it a single file? → CLI: markitdown file.pdf -o file.md
Is it a stream/batch/Python context? → Python API
  ↓
Read the output .md, present summary to user (don't dump full content unless asked)
```

## Step 1: Check & Install

```bash
pip show markitdown
```

If not installed:
```bash
pip install 'markitdown[all]'
```

Requirements: Python 3.10+

## Step 2: Convert

### CLI (preferred for single files)

```bash
markitdown "<input_file>" -o "<output>.md"
```

Pipe mode:
```bash
markitdown "<input_file>"
```

### Python API (for streams, batch, programmatic use)

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("document.pdf")
print(result.text_content)
```

Stream mode (no temp file):
```python
with open("document.pdf", "rb") as f:
    result = md.convert_stream(f, file_extension=".pdf")
```

LLM-powered image descriptions (PPTX, images):
```python
from openai import OpenAI
md = MarkItDown(llm_client=OpenAI(), llm_model="gpt-4o")
result = md.convert("presentation.pptx")
```

### Batch convert directory

```python
import os
from markitdown import MarkItDown

md = MarkItDown()
for f in os.listdir("documents/"):
    if f.endswith(('.pdf', '.docx', '.pptx', '.xlsx')):
        result = md.convert(f"documents/{f}")
        out = os.path.splitext(f)[0] + ".md"
        with open(f"output/{out}", "w") as fh:
            fh.write(result.text_content)
```

## Step 3: Present

After conversion, read the generated `.md` and give the user a quick summary (line count, key sections found). Do NOT dump full content unless user explicitly asks.

## Supported Formats

| Format | Extensions | Deps | Notes |
|--------|-----------|------|-------|
| PDF | .pdf | `[pdf]` | Text, headings, tables, lists |
| Word | .docx | `[docx]` | Full document structure |
| PowerPoint | .pptx | `[pptx]` | Slides with notes |
| Excel | .xlsx, .xls | `[xlsx]` or `[xls]` | Tables as Markdown |
| Images | .jpg, .png, .gif | `[all]` | EXIF + OCR via LLM |
| Audio | .wav, .mp3 | `[audio-transcription]` | Metadata + transcription |
| YouTube | URL | `[youtube-transcription]` | Caption extraction |
| HTML | .html | built-in | Clean conversion |
| CSV | .csv | built-in | Markdown table |
| JSON | .json | built-in | Structured output |
| XML | .xml | built-in | Structured output |
| ZIP | .zip | built-in | Iterates contents |
| EPUB | .epub | built-in | Full text extraction |
| Outlook | .msg | `[outlook]` | Email conversion |

### Modular Install (instead of `[all]`)

```bash
pip install 'markitdown[pdf,docx,pptx]'  # specific formats only
```

### Plugins

MarkItDown supports 3rd-party plugins. Key one: `markitdown-ocr` for OCR on embedded images in PDF/DOCX/PPTX/XLSX.

```bash
pip install markitdown-ocr
```

Enable plugins: `markitdown --use-plugins file.pdf`

### Azure Document Intelligence

For higher-quality PDF extraction (complex tables, layout analysis):
```python
md = MarkItDown(docintel_endpoint="<endpoint>")
result = md.convert("complex.pdf")
```

## Anti-patterns

- ❌ Don't use for high-fidelity human-readable conversions (use pandoc)
- ❌ Don't forget to check optional deps are installed before converting
- ❌ Don't use `convert_stream` in text mode — always binary (`rb`)
- ❌ Don't ignore the `file_extension` parameter in `convert_stream`
- ❌ Don't try unsupported formats without a custom DocumentConverter

## Tips

- Output `.md` next to source by default, use `-o` for custom path
- Large PDFs may take time — tell user you're working on it
- ZIP archives: all contents are concatenated into one output
- For RAG prep: convert → split by headings → index chunks
