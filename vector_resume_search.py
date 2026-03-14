from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = None
documents = []

def build_resume_index(resumes):

    global index, documents

    documents = resumes

    vectors = model.encode(resumes)

    vectors = np.array(vectors).astype("float32")

    index = faiss.IndexFlatL2(vectors.shape[1])

    index.add(vectors)

def search_resumes(query, top_k=3):

    q = model.encode([query]).astype("float32")

    D, I = index.search(q, top_k)

    results = []

    for idx in I[0]:
        results.append(documents[idx])

    return results