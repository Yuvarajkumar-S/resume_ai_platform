def generate_cover_letter(name, skills, jd):

    skills_text = ", ".join(skills[:6])

    letter = f"""
Dear Hiring Manager,

My name is {name} and I am excited to apply for this role.

I have experience in {skills_text} and have worked on projects
that demonstrate strong technical and problem-solving abilities.

I believe my background aligns well with your job requirements.

I would welcome the opportunity to contribute to your team.

Sincerely
{name}
"""

    return letter