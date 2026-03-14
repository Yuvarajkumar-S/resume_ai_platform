import json

def load_skills():

    with open("skills.json") as f:
        return json.load(f)

def extract_skills(text):

    skills_db = load_skills()

    text = text.lower()

    found = []

    for skill in skills_db:

        if skill.lower() in text:
            found.append(skill)

    return list(set(found))