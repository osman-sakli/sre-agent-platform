from openai import OpenAI
from app.settings import settings


class LLMClient:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None

    def summarize_investigation(self, request: dict, evidence: dict) -> str:
        if not self.client:
            return "AI summary disabled because OPENAI_API_KEY is not configured. Evidence was collected in read-only mode."

        prompt = f"""
You are a senior SRE incident triage assistant for a fintech production platform.
Be practical, evidence-based, and honest about uncertainty.
Do not recommend risky prod changes without human approval.

Incident request:
{request}

Evidence:
{evidence}

Return short sections:
- Impact
- Most likely cause
- Evidence
- Safe next actions
- What not to do yet
"""
        response = self.client.responses.create(
            model=settings.openai_model,
            input=prompt,
        )
        return response.output_text
