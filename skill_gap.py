from skill_extractor import extract_skills

def detect_skill_gap(resume_text, jd_text):

    # Extract skills from resume
    resume_skills = set(extract_skills(resume_text))

    # Extract skills from job description
    jd_skills = set(extract_skills(jd_text))

    # Matching skills
    matched = list(resume_skills.intersection(jd_skills))

    # Missing skills
    missing = list(jd_skills - resume_skills)

    return matched, missing