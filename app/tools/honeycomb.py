import requests
from app.settings import settings


class HoneycombTool:
    def _headers(self):
        return {"X-Honeycomb-Team": settings.honeycomb_api_key or "", "Content-Type": "application/json"}

    def get_error_summary(self, service: str, env: str, window_minutes: int = 30) -> dict:
        if not settings.honeycomb_api_key:
            return {"status": "mock", "message": "Honeycomb key missing", "service": service, "env": env}

        # Placeholder for real Honeycomb query API usage.
        # Keep it isolated here so the agent logic stays clean.
        return {
            "status": "todo",
            "message": "Wire Honeycomb query API here for error rate, top endpoints, status codes, dependency spans.",
            "service": service,
            "env": env,
            "window_minutes": window_minutes,
        }

    def get_cardinality_summary(self, service: str, env: str) -> dict:
        return {"status": "mock", "high_cardinality_fields": ["user.id", "request.id"], "service": service, "env": env}
