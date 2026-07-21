from pathlib import Path
from datetime import datetime

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)

def save_report(report: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    report_path = REPORT_DIR / f"report_{timestamp}.txt"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
        
    return str(report_path)    