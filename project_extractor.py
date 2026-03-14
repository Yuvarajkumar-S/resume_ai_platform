def extract_projects(text):

    projects = []

    lines = text.split("\n")

    for line in lines:

        l = line.lower()

        if "project" in l or "developed" in l or "built" in l:
            projects.append(line.strip())

    return projects