class SlackTool:
    def format_incident_summary(self, response: dict) -> str:
        return (
            f"*{response['service']} / {response['env']}*\n"
            f"Impact: {response['impact']}\n"
            f"Likely cause: {response['probable_root_cause']}\n"
            f"Next: {', '.join(response['safe_next_actions'])}"
        )
