# resume-
# 📝 AI Resume Evaluator

An intelligent *resume evaluation tool* that extracts text from a resume, analyzes job relevance, and provides *structured feedback* on missing skills and job match percentage.

## 🔧 Features
- ✅ *Extracts text* from PDF or image-based resumes using pdfplumber and Google Vision API
- ✅ *Identifies job titles* from the resume automatically
- ✅ *Matches resume skills* with required job skills using fuzzy matching
- ✅ *Analyzes job fit* using g4f (GPT-based AI model)
- ✅ *Provides human-readable job evaluation reports*

---

## 📌 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ai-resume-evaluator.git
cd ai-resume-evaluator
2️⃣ Install Dependencies
Make sure you have Python 3.8+ installed. Then, run:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up Google Vision API (Optional for Image Resumes)
If you want to process image-based resumes, configure Google Cloud Vision API:

Create a Google Cloud account and enable Vision API.
Download your service-account.json file.
Set the environment variable:
bash
Copy
Edit
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account.json"
🛠 How to Use
1️⃣ Run the Script
bash
Copy
Edit
python resume_evaluator.py
2️⃣ Upload Your Resume
Place your resume file (PDF or image) in the project folder and update file_path in resume_evaluator.py:

python
Copy
Edit
file_path = "resume.pdf"  # Replace with your actual file
3️⃣ View Results
The script will:

Extract your job title, experience, and skills
Match your skills with job requirements
Provide a detailed job evaluation report with recommendations
📊 Sample Output
plaintext
Copy
Edit
🔍 Job Evaluation Report for Rohan Dev

📌 Job Title: DevOps Developer

📊 Match Percentage: 75.00%
✅ Matched Skills: Cloud Security, DevOps, Kubernetes, Python, Azure
❌ Missing Skills: Docker, CI/CD, Networking

🎯 Chances of Getting the Job: 85%

📢 Final Recommendation:
You have a strong skill match for the DevOps Developer role. However, you should focus on improving your expertise in Docker, CI/CD, and Networking to enhance your chances further.
🛠 Technologies Used
Python 🐍
pdfplumber (Extracts text from PDFs)
Google Vision API (Extracts text from images)
NLTK (Processes text and removes stopwords)
FuzzyWuzzy (Matches resume skills with job requirements)
g4f (GPT-4 API) (Analyzes job fit and suggests improvements)
💡 Future Improvements
🚀 Add GUI for better user experience
🔍 Improve job title detection using machine learning
📊 Enhance job fit analysis with industry benchmarks
📜 License
This project is open-source and licensed under the MIT License. Feel free to modify and improve it!

👨‍💻 Author
👤 Rohan Dev
🔗 LinkedIn

🚀 Ready to Analyze Your Resume? Run the Script Now!
bash
Copy
Edit
python resume_evaluator.py
markdown
Copy
Edit

---

### ✅ *What’s Included?*
- *Markdown formatting* for GitHub compatibility  
- *Well-structured sections* for installation, usage, and features  
- *Sample output* for clarity  
- *Future improvements & license*  

Let me know if you need any modifications! 🚀
