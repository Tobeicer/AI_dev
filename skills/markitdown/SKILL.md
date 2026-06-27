---
name: "markitdown"
description: "Convert various file formats (PDF, Office documents, images, audio, web content, structured data) to Markdown optimized for LLM processing. Invoke when converting documents to markdown, extracting text from PDFs/Office files, or transcribing audio."
---

# MarkItDown

## Overview

MarkItDown is a Python utility (developed by Microsoft) that converts various file formats into Markdown format, optimized for use with large language models and text analysis pipelines. It preserves document structure (headings, lists, tables, hyperlinks) while producing clean, token-efficient Markdown output.

## When to Use This Skill

Use this skill when users request:
- Converting documents to Markdown format
- Extracting text from PDF, Word, PowerPoint, or Excel files
- Performing OCR on images to extract text
- Transcribing audio files to text
- Extracting YouTube video transcripts
- Processing HTML, EPUB, or web content to Markdown
- Converting structured data (CSV, JSON, XML) to readable Markdown
- Batch converting multiple files or ZIP archives
- Preparing documents for LLM analysis or RAG systems

## Core Capabilities

### 1. Document Conversion

Convert Office documents and PDFs to Markdown while preserving structure.

**Supported formats:**
- PDF files (with optional Azure Document Intelligence integration)
- Word documents (DOCX)
- PowerPoint presentations (PPTX)
- Excel spreadsheets (XLSX, XLS)

**Basic usage:**
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("document.pdf")
print(result.text_content)
```

**Command-line:**
```bash
markitdown document.pdf -o output.md
```

### 2. Media Processing

Extract text from images using OCR and transcribe audio files to text.

**Supported formats:**
- Images (JPEG, PNG, GIF, etc.) with EXIF metadata extraction
- Audio files with speech transcription (requires speech_recognition)

**Image with OCR:**
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("image.jpg")
print(result.text_content)  # Includes EXIF metadata and OCR text
```

**Audio transcription:**
```python
result = md.convert("audio.wav")
print(result.text_content)  # Transcribed speech
```

### 3. Web Content Extraction

Convert web-based content and e-books to Markdown.

**Supported formats:**
- HTML files and web pages
- YouTube video transcripts (via URL)
- EPUB books
- RSS feeds

**YouTube transcript:**
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("https://youtube.com/watch?v=VIDEO_ID")
print(result.text_content)
```

### 4. Structured Data Handling

Convert structured data formats to readable Markdown tables.

**Supported formats:**
- CSV files
- JSON files
- XML files

**CSV to Markdown table:**
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("data.csv")
print(result.text_content)  # Formatted as Markdown table
```

### 5. Advanced Integrations

Enhance conversion quality with AI-powered features.

**Azure Document Intelligence:**
For enhanced PDF processing with better table extraction and layout analysis:
```python
from markitdown import MarkItDown

md = MarkItDown(docintel_endpoint="<endpoint>", docintel_key="<key>")
result = md.convert("complex.pdf")
```

**LLM-Powered Image Descriptions:**
Generate detailed image descriptions using GPT-4o:
```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(llm_client=client, llm_model="gpt-4o")
result = md.convert("presentation.pptx")  # Images described with LLM
```

### 6. Batch Processing

Process multiple files or entire ZIP archives at once.

**ZIP file processing:**
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("archive.zip")
print(result.text_content)  # All files converted and concatenated
```

**Batch script:**
Use the provided batch processing script for directory conversion:
```bash
python scripts/batch_convert.py /path/to/documents /path/to/output
```

## Installation

**Full installation (all features):**
```bash
pip install 'markitdown[all]'
```

**Modular installation (specific features):**
```bash
pip install 'markitdown[pdf]'      # PDF support
pip install 'markitdown[docx]'     # Word support
pip install 'markitdown[pptx]'     # PowerPoint support
pip install 'markitdown[xlsx]'     # Excel support
pip install 'markitdown[audio]'    # Audio transcription
pip install 'markitdown[youtube]'  # YouTube transcripts
```

**Requirements:** Python 3.10+

## Quick Reference

| Format | Extension | Notes |
|---|---|---|
| PDF | .pdf | Text, headings, tables, lists |
| Word | .docx | Full document structure |
| PowerPoint | .pptx | Slides with notes |
| Excel | .xlsx, .xls | Tables and data |
| Images | .jpg, .png | EXIF metadata + OCR |
| Audio | .wav, .mp3 | Metadata + transcription |
| HTML | .html | Clean conversion |
| CSV | .csv | Table format |
| JSON | .json | Structured representation |
| XML | .xml | Structured format |
| ZIP | .zip | Iterates contents |
| EPUB | .epub | Full text extraction |
| YouTube | URL | Transcript extraction |

## Common Workflows

### Convert PDF to Markdown

```bash
# CLI
markitdown report.pdf -o report.md

# Python
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert("report.pdf")
with open("report.md", "w") as f:
    f.write(result.text_content)
```

### Convert Stream (no temp file)

```python
from markitdown import MarkItDown

md = MarkItDown()
with open("document.pdf", "rb") as f:
    result = md.convert_stream(f, file_extension=".pdf")
    print(result.text_content)
```

### Batch Convert Directory

```python
import os
from markitdown import MarkItDown

md = MarkItDown()
for filename in os.listdir("documents/"):
    if filename.endswith(('.pdf', '.docx', '.pptx', '.xlsx')):
        result = md.convert(f"documents/{filename}")
        out_name = os.path.splitext(filename)[0] + ".md"
        with open(f"output/{out_name}", "w") as f:
            f.write(result.text_content)
        print(f"Converted: {filename}")
```

## Anti-patterns

- ❌ Don't use for high-fidelity human-readable conversions (use pandoc for that)
- ❌ Don't forget to handle the case where optional dependencies are missing
- ❌ Don't use `convert_stream` with text-mode files (use binary mode)
- ❌ Don't write to temp files when streaming is supported
- ❌ Don't try to convert formats not in the supported list without custom DocumentConverter

## References

- GitHub: https://github.com/microsoft/markitdown
- PyPI: https://pypi.org/project/markitdown/
- Supports 20+ formats including DOCX, XLSX, PPTX, PDF, HTML, EPUB, CSV, JSON, images with OCR, and audio with transcription.
