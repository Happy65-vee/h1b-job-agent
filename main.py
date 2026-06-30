import csv
from src.scraper.h1b_scraper import fetch_jobs
from src.parser.job_parser import parse_jobs


def save_jobs(jobs, filename="h1b_jobs.csv"):
    keys = ["title", "company", "location", "apply_url"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(jobs)

    print(f"\nSaved {len(jobs)} jobs to {filename}")


def main():
    jobs = fetch_jobs()

    # 🔍 STEP 1 DEBUG: check raw output
    print("\nSAMPLE RAW JOB:")
    print(jobs[0])   # shows first job structure

    cleaned = parse_jobs(jobs)

    print("\n📌 Jobs you can APPLY to:\n")

    for job in cleaned:
        print(job["title"])
        print(job["company"])
        print(job["location"])
        print(job["apply_url"])
        print("-" * 40)

    save_jobs(cleaned)

if __name__ == "__main__":
    main()