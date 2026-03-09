from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def rank(job, resumes):

    job_vec = model.encode([job])

    scores = []

    for r in resumes:

        vec = model.encode([r])

        score = cosine_similarity(job_vec, vec)[0][0]

        scores.append(score)

    return scores