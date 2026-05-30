from app.llm import LLMClient
from app.tools.honeycomb import HoneycombTool


class ObservabilityQualityAgent:
    name = "observability_quality_agent"

    def __init__(self):
        self.honeycomb = HoneycombTool()
        self.llm = LLMClient()

    def run(self, request: dict) -> dict:
        service = request["service"]
        env = request["env"]
        evidence = {"cardinality": self.honeycomb.get_cardinality_summary(service, env)}
        ai_summary = self.llm.summarize_investigation(request, evidence)
        return {
            "service": service,
            "env": env,
            "issue_type": request["type"],
            "agent": self.name,
            "impact": "Telemetry quality may reduce incident investigation speed or increase cost.",
            "probable_root_cause": "Possible missing attributes, high-cardinality fields, or sampling mismatch.",
            "evidence": evidence,
            "safe_next_actions": ["Review OTel resource attributes", "Check dataset naming", "Check noisy high-cardinality fields"],
            "blocked_actions": [],
            "ai_summary": ai_summary,
        }
