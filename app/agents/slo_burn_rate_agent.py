from app.llm import LLMClient


class SLOBurnRateAgent:
    name = "slo_burn_rate_agent"

    def __init__(self):
        self.llm = LLMClient()

    def run(self, request: dict) -> dict:
        evidence = {
            "slo": "mock",
            "burn_rate": "mock",
            "note": "Wire Honeycomb SLO or query API here."
        }
        ai_summary = self.llm.summarize_investigation(request, evidence)
        return {
            "service": request["service"],
            "env": request["env"],
            "issue_type": request["type"],
            "agent": self.name,
            "impact": "Possible error budget burn. Need confirm affected SLO and burn window.",
            "probable_root_cause": "Unknown until SLO query is wired.",
            "evidence": evidence,
            "safe_next_actions": ["Check fast burn window", "Check slow burn window", "Correlate with deploy and 5xx rate"],
            "blocked_actions": [],
            "ai_summary": ai_summary,
        }
