import sys
from pathlib import Path
import pytest
from generate_certificate import generate_certificate_pdf

def test_generate_certificate_pdf(tmp_path: Path):
    name = "Alice as Name"
    date_str = "2026-03-21"
    output_dir = tmp_path / "output"
    generate_certificate_pdf(None, name, date_str, output_dir)
    expected = output_dir / f"{name}_Certificate.pdf"
    assert expected.exists(), "PDF certificate was not created"
