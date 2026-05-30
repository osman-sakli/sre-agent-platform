class DeploymentTool:
    def get_recent_deployments(self, service: str, env: str) -> dict:
        return {
            "service": service,
            "env": env,
            "recent_deploy_found": False,
            "deployments": [],
            "note": "Wire GitHub/GitLab/Harness deploy metadata here."
        }
