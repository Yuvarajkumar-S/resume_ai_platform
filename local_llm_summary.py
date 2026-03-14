def generate_summary(text):
    """
    Simple local summary generator for resumes
    """

    lines = text.split("\n")

    important = []

    keywords = [
        "experience",
        "project",
        "developed",
        "engineer",
        "data",
        "machine learning"
    ]

    for line in lines:
        l = line.lower()

        for k in keywords:
            if k in l:
                important.append(line.strip())
                break

        if len(important) >= 3:
            break

    if not important:
        return "Professional with experience in technical development and problem solving."

    return " ".join(important)
