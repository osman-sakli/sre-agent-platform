# Roadmap

## Real data instead of mocks
- [ ] Kubernetes tool: real pods / events / restarts by namespace + label selector
- [ ] CloudWatch tool: real CPU, memory, ALB 5xx metrics
- [ ] Honeycomb tool: real error rate, top endpoints, dependency spans via Query API
- [ ] Deployments tool: read recent deploys from GitHub Actions / Argo CD

## Agents
- [ ] SLO burn rate: multi-window, multi-burn-rate alerts (fast + slow windows)
- [ ] Observability quality: score services on missing fields, high-cardinality, sampling
- [ ] More playbooks: latency spike, pod crashloop, dependency outage

## Platform
- [ ] LLM provider switch (OpenAI / Anthropic) behind one interface
- [ ] Human-approval flow for remediation (still blocked by default)
- [ ] Slack delivery of investigation summaries
- [ ] Local demo stack: docker-compose with a sample app + OpenTelemetry → Honeycomb

## Quality
- [ ] Unit tests for each agent and tool with fixtures (only a health test today)
- [ ] GitHub Actions CI: lint, type check, tests
- [ ] Docs: architecture diagram and example investigation output
