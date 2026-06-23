# 📄 AI-Powered Resume Analyzer using NLP & Machine Learning

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)
![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-FF8C00?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-Intelligent%20System-purple?style=for-the-badge)

---

# 📌 Project Overview

The **AI-Powered Resume Analyzer** is an intelligent NLP-based system designed to analyze resumes (PDF format) and compare them with job descriptions to generate a **skill match score and missing skill insights**.

The system uses **Natural Language Processing (NLP) techniques and Machine Learning concepts like TF-IDF and Cosine Similarity** to understand textual similarity between resumes and job descriptions.

This project demonstrates how AI can automate **recruitment screening and candidate-job matching**, reducing manual HR effort and improving hiring efficiency.

---

# 🚀 Problem Statement

In traditional hiring systems:

- HR manually screens hundreds of resumes
- Important candidates may get missed
- Time-consuming selection process
- No standard scoring system for matching resumes

👉 This project solves this by using AI to automatically:
- Extract skills from resumes
- Compare with job descriptions
- Generate match score
- Identify missing skills

---

# ⚙️ How the System Works

1. User uploads a **PDF resume**
2. Resume text is extracted using `PyPDF2`
3. Job description is entered manually
4. NLP processes both texts
5. Skills are extracted using keyword-based NLP matching
6. TF-IDF converts text into numerical vectors
7. Cosine similarity calculates match score
8. Output is displayed using Streamlit UI

---

# 🧠 Why These Techniques Are Used

## 📌 PDF Text Extraction (PyPDF2)
Used to extract raw text from resume PDFs.

👉 Why?
- Resumes are usually in PDF format
- Machine learning cannot directly read PDFs
- So we convert PDF → text

---

## 📌 NLP-based Skill Extraction
Used keyword matching like:
Python, SQL, ML, NLP, Pandas

👉 Why?
- Fast and lightweight approach
- Works well for structured skill detection
- Easy to scale later with advanced NLP

---

## 📌 TF-IDF Vectorization
Converts text into numerical format.

👉 Why?
- Machines don’t understand text
- TF-IDF measures importance of words
- Helps compare resume vs job description

---

## 📌 Cosine Similarity
Used to calculate similarity score.

👉 Why?
- Measures angle between two text vectors
- Gives similarity between 0 to 1
- Better than simple word matching

---

## 📌 Streamlit UI
Used for frontend interface.

👉 Why?
- No need for HTML/CSS
- Fast deployment
- Beginner-friendly for ML apps

---

# 📊 Output Features

- Resume Upload (PDF)
- Job Description Input
- Match Score (%)
- Skills Found
- Missing Skills

---

# 📁 Project Structure

resume_analyzer/
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── similarity.py
├── llm_helper.py
├── test.py
├── requirements.txt
├── .gitignore

---

# 🔥 Key Features

- End-to-end NLP pipeline
- PDF resume parsing
- Skill extraction system
- Resume-job matching engine
- AI-based scoring system
- Streamlit web application
- Modular code structure

---

# 🌍 Applications

- HR Resume Screening
- Recruitment Automation
- Job Matching Platforms
- Career Guidance Tools
- AI-powered ATS systems

---

# 📈 Key Insights

- TF-IDF helps understand textual importance
- Cosine similarity gives accurate match scoring
- Keyword-based NLP works well for structured resumes
- System can be upgraded to LLM-based analysis

---


# 🚀 Future Improvements

- LLM-based resume feedback
- Smart skill recommendation system
- ATS score prediction system
- Resume ranking system
- Cloud deployment
- Downloadable PDF report

---

# ▶️ How to Run

pip install -r requirements.txt
streamlit run app.py

---

# 🧑‍💻 Author

Built as a NLP + Machine Learning portfolio project demonstrating:
- NLP skills
- ML pipeline understanding
- Real-world problem solving
- AI application development

