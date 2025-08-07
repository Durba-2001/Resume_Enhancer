import fitz

def read_resume(file_path="/content/drive/MyDrive/resume_enhancer/input_resume.txt"):
    try:
      f = open(file_path, "r")
      Resume = f.read()
      f.close()
      return Resume
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except Exception as e:
        return f"An error occurred while reading the file: {e}"
    


def read_resume_pdf(file_path="/content/drive/MyDrive/Durba_Paul_CV.pdf"):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text = text + page.get_text()
        doc.close()
        return text
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except Exception as e:
        return f"An error occurred while reading the PDF: {e}"
