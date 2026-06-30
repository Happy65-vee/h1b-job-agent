import requests

def fetch_jobs():
    print("Fetching real H1B-friendly jobs...")

    # Example company using Greenhouse
    url = "https://boards-api.greenhouse.io/v1/boards/airbnb/jobs"

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch jobs")
        return []

    data = response.json()

    jobs = []

    for job in data.get("jobs", [])[:10]:
        jobs.append({
            "title": job.get("title"),
            "company": "Airbnb",
            "location": job.get("location", {}).get("name"),
            "apply_url": job.get("absolute_url")
        })

    return jobs