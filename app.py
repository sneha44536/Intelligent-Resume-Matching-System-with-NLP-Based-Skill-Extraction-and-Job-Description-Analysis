import streamlit as st

from resume_parser import extract_text
from skill_extractor import extract_skills
from similarity import calculate_similarity

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description Here"
)

if st.button("Analyze Resume"):

    if uploaded_file is not None and job_description:

        resume_text = extract_text(uploaded_file)

        resume_skills = extract_skills(resume_text)

        jd_skills = extract_skills(job_description)

        score = calculate_similarity(
            resume_text,
            job_description
        )

        missing_skills = list(
            set(jd_skills) - set(resume_skills)
        )

        st.subheader("Match Score")
        st.write(f"{score}%")

        st.subheader("Skills Found")
        st.write(resume_skills)

        st.subheader("Missing Skills")
        st.write(missing_skills)

    else:
        st.warning("Please upload a resume and enter a job description.")