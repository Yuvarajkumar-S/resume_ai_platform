import textstat

def ats_score(text, skills):

    text = text.lower()

    score = 0

    if "education" in text:
        score += 15

    if "experience" in text:
        score += 20

    if "projects" in text:
        score += 15

    if "skills" in text:
        score += 10

    if len(skills) >= 8:
        score += 20

    readability = textstat.flesch_reading_ease(text)

    if readability > 40:
        score += 20

    return min(score, 100)