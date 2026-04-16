from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from main import analyze_user, compare_users

app = FastAPI(title="GitHub Analyzer API 🚀")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    username: str

class CompareRequest(BaseModel):
    usernames: list[str]

@app.get("/")
def home():
    return {"message": "API running 🚀"}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    try:
        result = analyze_user(req.username)
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/compare")
def compare(req: CompareRequest):
    try:
        result = compare_users(req.usernames)
        return {"success": True, "comparison": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
