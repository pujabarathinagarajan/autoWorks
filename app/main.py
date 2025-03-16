from fastapi import FastAPI, HTTPException
from app.job_service import fetch_sorted_jobs

app = FastAPI()

@app.get("/fetch-jobs")
def fetch_jobs():
    """
    Fetch jobs from Symplicity API and return sorted results.
    """
    try:
        sorted_jobs = fetch_sorted_jobs()
        return {"total_jobs": len(sorted_jobs), "jobs": sorted_jobs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
