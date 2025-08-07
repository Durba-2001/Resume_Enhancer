from resume_reader import read_resume, read_resume_pdf
from utils import get_llm_response

def enhance_resume_section(path, outpath, role="General"):
    outpath += "/enhanced_resume.txt"
    if path.endswith(".txt"):
        resume_text = read_resume(path)
    elif path.endswith(".pdf"):
        resume_text = read_resume_pdf(path)
    #role checker
    f1 = open("prompts/check_role.txt","r")
    prompt=f1.read()
    f1.close()

    check_response=prompt.format(role=role,resume_text=resume_text)
    role_check=get_llm_response(check_response)
    
    if "No" in role_check:
        print (f"The resume does not align with the {role} role")
        Cp = input("Do you still wanna enhance your resume?(Y/N):: ")
        if Cp.upper() == "N":
            return 1

    # Load prompt from file
    f = open("prompts/enhancer_prompt.txt", "r")
    prompt_template = f.read()
    f.close()

    enhance_prompt = prompt_template.format(role=role, resume_text=resume_text)
    enhanced_resume = get_llm_response(enhance_prompt)
    try:
       fp=open(outpath,"w")
       fp.write(enhanced_resume)
       fp.close()
       print("Enhanced resume saved to ",outpath)
    except Exception as e:
        print(f"Error creating file: {e}")
    return 0
