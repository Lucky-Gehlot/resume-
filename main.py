import io
import re
import pdfplumber
import nltk
import g4f
from google.cloud import vision
from fuzzywuzzy import fuzz
from nltk.corpus import stopwords

# Download NLTK stopwords
nltk.download('stopwords')

# Initialize Google Vision Client
vision_client = vision.ImageAnnotatorClient()

# Function to extract text from an image using Google Vision API
def extract_text_from_image(image_path):
    with io.open(image_path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = vision_client.text_detection(image=image)
    return response.text_annotations[0].description if response.text_annotations else ""

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return text.strip()

# Function to extract job title from resume text
def extract_job_title(text):
    # Searching for job title in the resume header
    match = re.search(r"(Cloud Security|DevOps Developer|Private Blockchain)", text, re.IGNORECASE)
    return match.group(0) if match else "Unknown Job Title"

# Function to extract skills from resume text
def extract_resume_skills(text):
    words = set(re.findall(r'\b\w+\b', text.lower()))
    stop_words = set(stopwords.words('english'))
    return [word for word in words if word not in stop_words]

# Function to get required job skills using g4f
def get_required_skills(job_title):
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in job requirements."},
            {"role": "user", "content": f"List the top technical and soft skills required for a {job_title} position."}
        ]
    )
    print("\n🔍 Raw g4f Skill Response:\n", response)  # Debugging: Print full response from g4f
    return response.split("\n") if isinstance(response, str) else []

# Function to match resume skills with required skills
def match_skills(resume_skills, required_skills):
    matched_skills = [skill for skill in required_skills if any(fuzz.ratio(skill.lower(), rs.lower()) > 80 for rs in resume_skills)]
    match_percentage = (len(matched_skills) / len(required_skills)) * 100 if required_skills else 0

    print("\n✅ Skills Debugging:")
    print("Matched Skills:", matched_skills)
    print("Unmatched Required Skills:", set(required_skills) - set(matched_skills))

    return match_percentage, matched_skills

# Function to evaluate job fit with g4f
def evaluate_resume_with_g4f(job_title, resume_text, matched_skills, match_percentage):
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant that evaluates resumes based on job fit."},
            {"role": "user", "content": f"Given this resume text:\n{resume_text[:1500]}...\n\n"
                                         f"Detected job title: {job_title}\n"
                                         f"Matched skills: {', '.join(matched_skills)}\n"
                                         f"Match percentage: {match_percentage:.2f}%\n\n"
                                         f"Evaluate the chances of getting the job and list the missing skills."}
        ]
    )

    print("\n🔍 Raw g4f Evaluation Response:\n", response)  # Debugging: Print full response from g4f

    if isinstance(response, str):
        lines = response.strip().split("\n")
        job_chances = "Not Available"
        missing_skills = []

        for line in lines:
            if "Chances:" in line:
                job_chances = line.split(":", 1)[-1].strip()
            elif "Missing Skills:" in line:
                missing_skills = line.split(":", 1)[-1].strip().split(",")

        return f"""
        🔍 *Job Match Evaluation*
        *Job Title:* {job_title}
        
        *Chances of Getting the Job:* {job_chances}
        
        *Missing Skills:* {", ".join(missing_skills) if missing_skills else "None"}
        """
    else:
        return "⚠ Error: Unable to process job evaluation."

# Main function to process resume
def process_resume(file_path):
    # Extract text from resume
    text = extract_text_from_pdf(file_path) if file_path.endswith(".pdf") else extract_text_from_image(file_path)

    print("\n📝 *Extracted Resume Text (First 500 Characters):*\n", text[:500])  # Debugging: Print text preview

    job_title = extract_job_title(text)
    if job_title == "Unknown Job Title":
        job_title = input("❌ Job Title not found in resume. Please enter manually: ").strip()

    print(f"\n🔎 *Detected Job Title:* {job_title}")

    required_skills = get_required_skills(job_title)
    print("\n📌 *Required Skills:*", required_skills)

    resume_skills = extract_resume_skills(text)
    print("\n🛠 *Extracted Resume Skills:*", resume_skills)

    match_percentage, matched_skills = match_skills(resume_skills, required_skills)
    print(f"\n📊 *Match Percentage:* {match_percentage:.2f}%")

    evaluation = evaluate_resume_with_g4f(job_title, text, matched_skills, match_percentage)
    print("\n📢 *Final Job Evaluation:*", evaluation)

# Run the function on the uploaded resume
file_path = "resume_rohan.pdf"
process_resume(file_path)
