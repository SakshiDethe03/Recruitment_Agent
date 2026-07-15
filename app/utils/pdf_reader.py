from pypdf import PdfReader

file_path = ""

def extract_text_from_pdf(file_path: str) -> str:
    try:
        text = ""
        
        reader = PdfReader(file_path)
        
        # extract text
        for page in reader.pages:
            page_text = page.extract_text()
            
            if page_text:
                text += page_text + "\n"
                
        return text
            
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""
