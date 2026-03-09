import requests
import pandas as pd

def fetch_jobs():

    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(url)

    data = response.json()

    jobs = []

    for job in data["jobs"][:30]:

        jobs.append({
            "title": job["title"],
            "company": job["company_name"],
            "location": job["candidate_required_location"],
            "url": job["url"]
        })

    return pd.DataFrame(jobs) 