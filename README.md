# AI-Powered Resume Enhancer

A Python-based tool that uses large language models (LLMs) to enhance and improve resumes by analyzing clarity, grammar, impact, and role relevance.
##  Objective

To develop an application that:
- Reads resumes from `.txt` or `.pdf` files
- Analyzes and enhances content using an LLM API
- Generates a polished version of the resume with improved:
  - Clarity
  - Structure
  - Professional language
  - Role alignment

---

##  Functional Scope

### Core Features
- **Resume Ingestion**: Supports `.txt` and `.pdf` formats
- **Resume Analysis**: Uses an LLM API to evaluate:
  - Grammar and conciseness
  - Clarity and impact
  - Action verbs and outcomes
- **Section-wise Enhancement**:
  - Professional Summary / Objective
  - Work Experience
  - Skills
  - Education
- **Output Generation**: Writes enhanced resume to a new file
- **Version Comparison**: Highlights differences between original and enhanced resumes
- **Role-Based Optimization**: Customizes content for a user-defined job role

##  Project Structure
<pre>
resume_enhancer/
│
├── main.py # Entry point for the enhancement process
├── enhancer.py # Handles prompt-based enhancement logic
├── resume_reader.py # Reads resumes from TXT or PDF format
├── comparator.py # Compares original and enhanced resumes
├── utils.py # Utility functions (e.g., LLM API calls)
│
├── prompts/
│ └── enhancer_prompt.txt # Prompt template for the LLM
│
├── resumes/
│ ├── input_resume.txt # Sample resume to enhance
│ └── enhanced_resume.txt # Output after enhancement
│
├── .env # API key and config (not committed)
├── requirements.txt # Python dependencies
</pre>

## Running the Project (VS Code Recommended)
### 1. Install dependencies
pip install -r requirements.txt
## NOTE: Replace "YOUR_API_KEY" in utils.py
### 2. Run the program
python main.py

## Technologies Used
 - Python 3
 - File Handling 
 - pymupdf4llm
 - Gemini API 
 - LLM(Large Language Model)
 - Environment variables (dotenv)

