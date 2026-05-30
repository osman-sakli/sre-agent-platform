from app.llm import LLMClient
from app.tools.honeycomb import HoneycombTool
from app.tools.kubernetes import KubernetesTool
from app.tools.cloudwatch import CloudWatchTool
from app.tools.deployments import DeploymentTool
from app.guardrails.policy import GuardrailPolicy


class IncidentTriageAgent:
    name = "incident_triage_agent"

    def __init__(self):
        self.honeycomb = HoneycombTool()
        self.kubernetes = KubernetesTool()
        self.cloudwatch = CloudWatchTool()
        self.deployments = DeploymentTool()
        self.policy = GuardrailPolicy()
        self.llm = LLMClient()

    def run(self, request: dict) -> dict:
        service = request["service"]
        env = request["env"]
        window = request.get("window_minutes", 30)

        evidence = {
            "honeycomb": self.honeycomb.get_error_summary(service, env, window),
            "kubernetes": self.kubernetes.get_pod_health(service, env),
            "cloudwatch": self.cloudwatch.get_service_metrics(service, env),
            "deployments": self.deployments.get_recent_deployments(service, env),
        }

        ai_summary = self.llm.summarize_investigation(request, evidence)

        return {
            "service": service,
            "env": env,
            "issue_type": request["type"],
            "agent": self.name,
            "impact": "Potential customer-facing impact. Validate affected endpoints, error rate, and duration.",
            "probable_root_cause": "Unknown until Honeycomb/deploy/dependency evidence is wired. Start with recent deploy and dependency spans.",
            "evidence": evidence,
            "safe_next_actions": [
                "Check top failing endpoint and status code in Honeycomb",
                "Compare before/after latest deployment",
                "Check pod restarts and readiness",
                "Check DB, Redis, and Kafka dependency spans",
                "Post human-readable summary to incident channel",
            ],
            "blocked_actions": self.policy.blocked_actions(env),
            "ai_summary": ai_summary,
        }
