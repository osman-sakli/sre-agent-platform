from app.agents.incident_triage_agent import IncidentTriageAgent
from app.agents.observability_quality_agent import ObservabilityQualityAgent
from app.agents.slo_burn_rate_agent import SLOBurnRateAgent


class AgentOrchestrator:
    def __init__(self):
        self.incident_agent = IncidentTriageAgent()
        self.observability_agent = ObservabilityQualityAgent()
        self.slo_agent = SLOBurnRateAgent()

    def route(self, request: dict) -> dict:
        issue_type = request.get("type")

        if issue_type in {"5xx_spike", "latency_spike", "pod_crashloop", "redis_issue", "db_issue", "kafka_lag"}:
            return self.incident_agent.run(request)

        if issue_type in {"missing_traces", "high_cardinality", "bad_attributes", "sampling_issue"}:
            return self.observability_agent.run(request)

        if issue_type in {"slo_breach", "burn_rate", "error_budget"}:
            return self.slo_agent.run(request)

        request["type"] = "unknown"
        return self.incident_agent.run(request)
