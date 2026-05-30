from fastapi import FastAPI
from app.models.schemas import InvestigationRequest, InvestigationResponse
from app.orchestrator import AgentOrchestrator

app = FastAPI(title="SRE Agent Platform", version="0.1.0")
orchestrator = AgentOrchestrator()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/investigate", response_model=InvestigationResponse)
def investigate(request: InvestigationRequest):
    return orchestrator.route(request.model_dump())
