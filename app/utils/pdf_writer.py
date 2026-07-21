from pathlib import Path
from datetime import datetime
# uv add reprotlab
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(
    TTFont("Arial", "assets/fonts/arial.ttf")
)

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)

def save_pdf(report: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    pdf_path = REPORT_DIR / f"report_{timestamp}.pdf"
    
    doc = SimpleDocTemplate(str(pdf_path))
    
    styles = getSampleStyleSheet()
    
    style = styles["BodyText"]
    style.fontName = "Arial"
    
    story = []
    
    for line in report.split("\n"):
        line = (
            line.replace("-", " ")
            .replace("--", "--")
            .replace("---", "---")
            .replace("✅", "✅")
            .replace("❌", "❌")
        )
        story.append(Paragraph(line, style))
        
    doc.build(story)
    
    return str(pdf_path)    