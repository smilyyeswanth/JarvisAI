from docx import Document
from pypdf import PdfReader

def read_resume(file_path):

    try:

        if file_path.lower().endswith(".docx"):

            doc = Document(file_path)

            return "\n".join(
                p.text
                for p in doc.paragraphs
            )

        elif file_path.lower().endswith(".pdf"):

            reader = PdfReader(file_path)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            return text

        else:

            print("Unsupported file type")
            return ""

    except Exception as e:

        print(f"Error reading resume: {e}")
        return ""