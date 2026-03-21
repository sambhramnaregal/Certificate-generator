# Internship Certificate Generator

## Overview
This small Python utility generates a personalized internship completion certificate by inserting an intern's **name** and **date** into a provided image template (WebP by default). It also works with PNG and JPEG templates and can optionally export to PDF.

## Project Structure
```
internship_certificate/
│   generate_certificate.py   # Main script
│   requirements.txt          # Python dependencies
│   README.md                 # This file
│
├───templates/
│       internship_template.webp   # Your supplied template (replace as needed)
│
└───output/                     # Generated certificates will be saved here
```

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python generate_certificate.py --name "John Doe" --date "2026-03-21" --template templates/internship_template.webp
```
- `--name` : Intern's full name (required or will be prompted).
- `--date` : Completion date in `YYYY-MM-DD` format (defaults to today).
- `--template` : Path to the certificate image template.
- `--output` : Directory where the generated certificate will be stored (default `output`).

The script will produce `output/John_Doe_Certificate.webp` (or the same extension as the template).

## Extending to Other Formats
The script detects the file extension (`.webp`, `.png`, `.jpg`) and uses Pillow to draw text. To support additional formats, add a new entry to the `PLACEHOLDER_CONFIG` dictionary in `generate_certificate.py` with appropriate coordinates, font settings, and image size.

## Testing
A basic test suite is provided under `tests/`. Run it with:
```bash
pytest
```

## License
MIT – feel free to adapt and improve.
