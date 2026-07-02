from fastapi import FastAPI, HTTPException

app = FastAPI(title="Command Center API")

# Toy DB
system_logs = {
    1: {"service": "SSH", "status": "active"},
    2: {"service": "Firewall", "status": "active"},
}

@app.get("/")
async def root():
    return {"message": "System operational."}


@app.get("/logs/{log_id}")
async def get_log(log_id: int):
    if log_id not in system_logs:
        raise HTTPException(status_code=404, detail="Log entry not found")
    return system_logs[log_id]

@app.get("/services/")
async def filter_services(status: str = "active", limit: int = 10):
    results = [log for log in system_logs.values() if log["status"] == status]
    return results[:limit]

