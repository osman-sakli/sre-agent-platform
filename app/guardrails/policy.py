class GuardrailPolicy:
    PROD_BLOCKED_ACTIONS = {
        "restart_pod",
        "rollback_deploy",
        "delete_resource",
        "scale_down",
        "change_security_group",
        "change_database_config",
        "disable_alert",
    }

    def is_allowed(self, action: str, env: str) -> bool:
        if env.lower() == "prod" and action in self.PROD_BLOCKED_ACTIONS:
            return False
        return True

    def blocked_actions(self, env: str) -> list[str]:
        if env.lower() != "prod":
            return []
        return sorted(self.PROD_BLOCKED_ACTIONS)
