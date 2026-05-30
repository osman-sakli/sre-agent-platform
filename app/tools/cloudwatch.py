class CloudWatchTool:
    def get_service_metrics(self, service: str, env: str) -> dict:
        return {
            "service": service,
            "env": env,
            "cpu": "mock",
            "memory": "mock",
            "alb_5xx": "mock",
            "note": "Wire boto3 CloudWatch get_metric_data here."
        }
