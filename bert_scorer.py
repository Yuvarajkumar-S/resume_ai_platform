from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

ideal_resume = """
Strong engineer with technical skills,
impactful projects and measurable achievements.
"""

def score_resume_bert(text):

    emb = model.encode([text, ideal_resume])

    sim = cosine_similarity([emb[0]], [emb[1]])[0][0]

    score = round(sim * 10, 2)

    return min(score, 10)