import requests
from app.config import SYMPLICITY_JOB_SEARCH_URL, HEADERS, PARAMS

def fetch_sorted_jobs():
    """
    Fetch jobs from Symplicity API, filter paid jobs, and sort by pay range.
    """
    try:
        response = requests.get(SYMPLICITY_JOB_SEARCH_URL, headers=HEADERS, params=PARAMS)

        # Check if response is empty
        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

        try:
            job_data = response.json()
        except ValueError:
            raise Exception(f"Invalid JSON response: {response.text}")

        jobs = []

        for job in job_data.get("models", []):
            job_id = job.get("job_id")
            company_name = job.get("name")
            role_name = job.get("job_title")
            compensation_from = job.get("compensation_from")
            compensation_to = job.get("compensation_to")

            # Skip unpaid jobs
            if compensation_from is None and compensation_to is None:
                continue

            # Convert pay range to float for sorting
            try:
                min_pay = float(compensation_from) if compensation_from else 0
                max_pay = float(compensation_to) if compensation_to else min_pay
                avg_pay = (min_pay + max_pay) / 2  # Sorting based on average pay
            except ValueError:
                avg_pay = 0

            jobs.append({
                "job_id": job_id,
                "company_name": company_name,
                "role_name": role_name,
                "pay_range": f"${compensation_from or 'N/A'} - ${compensation_to or 'N/A'}",
                "avg_pay": avg_pay  # Used only for sorting
            })

        # Sort jobs by average pay (highest first)
        sorted_jobs = sorted(jobs, key=lambda x: x["avg_pay"], reverse=True)

        # Remove avg_pay key before returning results
        for job in sorted_jobs:
            del job["avg_pay"]

        return sorted_jobs

    except requests.RequestException as e:
        raise Exception(f"Error fetching jobs: {str(e)}")
