def recommend_jobs(skills):

    job_db = {

        "Data Scientist": ["python", "machine learning", "pandas"],

        "ML Engineer": ["python", "tensorflow", "pytorch"],

        "Backend Developer": ["python", "flask", "docker"],

        "DevOps Engineer": ["docker", "kubernetes", "aws"],

        "Frontend Developer": ["react", "javascript", "css"]
    }

    matches = []

    for job, req in job_db.items():

        overlap = len(set(req).intersection(skills))

        if overlap >= 2:
            matches.append(job)

    return matches