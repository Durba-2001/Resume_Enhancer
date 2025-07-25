from enhancer import enhance_resume_section
from resume_reader import read_resume
from comparator import compare_version  

if __name__ == "__main__":
    path = input("Enter the path of the resume file: ")
    role = input("Enter the role you want to apply for: ")
    output_dir = "resumes"

    enhance_resume_section(path, output_dir, role)

    original = read_resume(path)
    enhanced = read_resume(f"{output_dir}/enhanced_resume.txt")

    compare_version(original, enhanced)
