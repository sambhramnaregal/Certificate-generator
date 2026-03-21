import argparse
import sys
from pathlib import Path
from datetime import datetime

from fpdf import FPDF
from PIL import Image

# Configuration for PDF generation
PLACEHOLDER_CONFIG = {
    "default": {
        "page_size": "A4",
        "name_pos": (105, 120),  # (x_center_mm, y_mm)
        "date_pos": (105, 140),
        "font": "Helvetica",
        "font_size": 24,
        "font_style": "",
        "text_color": (0, 0, 0),
    }
}

class PDFCertificate(FPDF):
    def __init__(self, template_path: Path | None = None):
        super().__init__(orientation="P", unit="mm", format=PLACEHOLDER_CONFIG["default"]["page_size"])
        self.unifontsubset = False
        self.add_page()
        if template_path and template_path.is_file():
            # Add background image scaled to page size
            img = Image.open(template_path)
            img_width, img_height = img.size
            # Convert pixels to mm (assuming 72 dpi)
            dpi = img.info.get("dpi", (72, 72))[0]
            width_mm = img_width * 25.4 / dpi
            height_mm = img_height * 25.4 / dpi
            self.image(str(template_path), x=0, y=0, w=width_mm, h=height_mm)

    def add_centered_text(self, text: str, x_center: float, y: float, cfg: dict):
        # Set the font first so that get_string_width works correctly
        self.set_font(cfg["font"], cfg["font_style"], cfg["font_size"])
        self.set_text_color(*cfg["text_color"])
        text_width = self.get_string_width(text)
        self.set_xy(x_center - (text_width / 2), y)
        self.cell(w=text_width, h=10, txt=text, border=0)

def generate_certificate_pdf(template_path: Path | None, name: str, date_str: str, output_dir: Path):
    cfg = PLACEHOLDER_CONFIG["default"]
    pdf = PDFCertificate(template_path)
    pdf.add_centered_text(name, cfg["name_pos"][0], cfg["name_pos"][1], cfg)
    pdf.add_centered_text(date_str, cfg["date_pos"][0], cfg["date_pos"][1], cfg)
    output_dir.mkdir(parents=True, exist_ok=True)
    safe_name = "_".join(name.split())
    output_path = output_dir / f"{safe_name}_Certificate.pdf"
    pdf.output(str(output_path))
    print(f"Certificate saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate a simple PDF internship certificate.")
    parser.add_argument("--name", "-n", help="Intern's full name")
    parser.add_argument("--date", "-d", help="Completion date (YYYY-MM-DD). Defaults to today.")
    parser.add_argument("--template", "-t", type=Path, help="Optional background image (e.g., .webp, .png) for the PDF.")
    parser.add_argument("--output", "-o", type=Path, default=Path("output"), help="Directory to store generated certificates.")
    args = parser.parse_args()
    name = args.name or input("Enter intern's name: ")
    date_str = args.date or datetime.today().strftime("%Y-%m-%d")
    generate_certificate_pdf(args.template, name, date_str, args.output)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(0)
