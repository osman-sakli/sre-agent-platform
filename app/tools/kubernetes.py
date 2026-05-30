class KubernetesTool:
    def get_pod_health(self, service: str, env: str) -> dict:
        return {
            "service": service,
            "env": env,
            "pods_not_ready": 0,
            "restarts_last_30m": 0,
            "crashlooping": False,
            "note": "Mock data. Wire Kubernetes client by namespace/label selector."
        }
