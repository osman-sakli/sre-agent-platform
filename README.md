# SRE Agent Platform

Read-only AI assisted SRE investigation platform.

It routes incidents to specialized agents:

- Incident Triage Agent
- Observability Quality Agent
- SLO / Burn Rate Agent

The AI part is inside `app/llm.py`. The platform collects evidence from Honeycomb, Kubernetes, CloudWatch, and deployment history, then asks the LLM to produce an SRE-style investigation summary.

## Quick start

```bash
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

Test:

```bash
curl -X POST http://localhost:8080/investigate \
  -H 'Content-Type: application/json' \
  -d '{
    "type":"5xx_spike",
    "service":"payment-authorization",
    "env":"prod",
    "business_unit":"paze",
    "severity":"sev2"
  }'
```

## Safety

By default this platform is read-only. Prod remediation actions like restart, rollback, delete, or config changes are blocked unless human approval is added later.
