from fastapi import FastAPI, HTTPException, Query
import logging
from pydantic import BaseModel
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()



# Set allowed origins
origins = [
    "http://localhost:5173",
    "http://localhost",
    "https://stage1.up.railway.app",
    '*'
]

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






@app.post("/stage1/")
def stage1():
    async def get_info( slack_name: str = Query(..., description="Slack name"), track: str = Query(..., description="Track"),):
        
        # Get the date of today
        current_day = datetime.utcnow().strftime('%A')

        # Calc UTC  +/-2 hours
        utc_time = datetime.utcnow() + timedelta(hours=0)
        utc_time_str = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

        # Github code urls
        github_file_url = f"https://github.com/vortex-hue/hng-stage1/blob/main/main.py"
        github_repo_url = f"https://github.com/vortex-hue/hng-stage1"

        # Create the response JSON
        response = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time_str,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200
        }

        return response