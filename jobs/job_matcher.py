from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_jobs(job_desc, jobs_df):

    vectorizer = TfidfVectorizer()

    documents = [job_desc] + jobs_df["title"].tolist()

    vectors = vectorizer.fit_transform(documents)

    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    jobs_df["match_score"] = similarities

    jobs_df = jobs_df.sort_values(by="match_score", ascending=False)

    return jobs_df.head(5) 