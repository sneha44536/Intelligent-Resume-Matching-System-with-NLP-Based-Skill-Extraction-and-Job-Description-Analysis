def extract_skills(text):

    skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "nlp",
        "tensorflow",
        "pandas",
        "numpy",
        "power bi",
        "tableau"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return found_skills