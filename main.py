from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph.builder import build_graph

app = FastAPI(title="Code Review Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReviewRequest(BaseModel):
    repo_url: str
    focus: str = "all"
@app.post('/')
def code_review_agent():
    return {"message":"code review agent is working...."}


@app.post('/review')
async def review_repo(request:ReviewRequest):
    initial_state = {
        "repo_url":request.repo_url,
        "focus":request.focus   
    }
    result = build_graph().invoke(initial_state)

    return {
        "repo_url": request.repo_url,
        "detected_language": result.get("detected_language", ""),
        "critical_found": result.get("critical_found", False),
        "total_files": len(result.get("files", {})),
        "final_report": result.get("final_report", "")
    }

@app.get("/health")
def health():
    return {"status": "ok"}