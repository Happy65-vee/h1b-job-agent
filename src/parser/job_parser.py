H1B_KEYWORDS = [
    "power bi",
    "powerbi",
    "ssrs",
    "sql",
    "business intelligence",
    "bi developer",
    "data analyst",
    "business analyst",
    "report developer",
    "reporting",
    "analytics",
    "data engineer",
    "etl",
    "warehouse"
]
def parse_jobs(raw_jobs):
    print("Parsing jobs...")

    cleaned = []

    for job in raw_jobs:
        title = (job.get("title") or "").lower()
        location = (job.get("location") or "").lower()

        # 🔥 REPLACE YOUR OLD LOCATION FILTER WITH THIS
        us_keywords = [
            "united states",
            "usa",
            "remote - us",
            "remote us",
            "new york",
            "california",
            "texas",
            "washington",
            "san francisco",
            "seattle",
            "austin",
            "ny",
            "ca",
            "tx",
        ]

        is_us = any(k in location for k in us_keywords)

        # keyword filter
        is_relevant = any(k in title for k in H1B_KEYWORDS)

        if is_us and is_relevant:
            cleaned.append(job)

    return cleaned