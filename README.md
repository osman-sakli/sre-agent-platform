# SRE Agent Platform

Read-only AI assisted SRE investigation platform. A personal side project: a FastAPI service that gathers incident evidence and asks an LLM for an on-call style summary, without ever touching prod.

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
    "service":"checkout-api",
    "env":"prod",
    "business_unit":"demo",
    "severity":"sev2"
  }'
```

## Stack

Python 3.11+, FastAPI, Pydantic, OpenAI API (`app/llm.py`), Honeycomb API, Kubernetes client, boto3 (CloudWatch), Docker, Kubernetes manifests in `k8s/`.

## Layout

```
app/main.py           FastAPI app, /investigate endpoint
app/orchestrator.py   routes an incident to the right agent
app/agents/           incident triage, observability quality, SLO burn rate
app/tools/            Honeycomb, Kubernetes, CloudWatch, deployments, Slack
app/playbooks/        YAML playbooks (steps + allowed / blocked actions)
app/guardrails/       read-only policy
tests/
```

Some tools still return mock data (see ROADMAP.md).

## Safety

By default this platform is read-only. Prod remediation actions like restart, rollback, delete, or config changes are blocked unless human approval is added later.

## Secrets

No keys in the repo. Copy `.env.example` to `.env` (git-ignored).

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## License

[MIT](LICENSE)
