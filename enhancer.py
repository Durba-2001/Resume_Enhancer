from resume_reader import read_resume, read_resume_pdf
from utils import get_llm_response

def enhance_resume_section(path, outpath, role="General"):
    outpath += "/enhanced_resume.txt"
    if path.endswith(".txt"):
        resume_text = read_resume(path)
    elif path.endswith(".pdf"):
        resume_text = read_resume_pdf(path)

    # Load prompt from file
    f = open("prompts/enhancer_prompt.txt", "r")
    prompt_template = f.read()
    f.close()

    enhance_prompt = prompt_template.format(role=role, resume_text=resume_text)
    enhanced_resume = get_llm_response(enhance_prompt)

    fp=open(outpath,"w")
    fp.write(enhanced_resume)
    fp.close()
    print("Enhanced resume saved to ",outpath)
    return
