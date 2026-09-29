# OWASP Top 10 for Large Language Model Applications (2025)

**Citation:** OWASP Top 10 for LLM Applications, 2025 edition (v2025, published November 2024 by the OWASP Gen AI Security Project). Successor to the 2023-24 v1.x list. Companion: OWASP Top 10 for Agentic Applications (December 2025), covered in Phase 2 of `SKILL.md`.

**Enforcement:** **Voluntary best-practice framework** maintained by the Open Worldwide Application Security Project. Not a regulation. De-facto reference for any AppSec or AI security review on LLM-powered software. Cited in EU AI Act high-risk cybersecurity discussions and NIST AI 600-1 GenAI Profile.

---

## Scope: who it applies to

Any application that integrates a Large Language Model into its functionality: chatbots, copilots, RAG systems, AI agents, content generators, code assistants, classification systems. **Doesn't matter if the LLM is third-party (Claude, GPT, Gemini) or self-hosted (Llama, Mistral)**: application-layer risks are the same.

---

## The 2025 list (LLM01–LLM10)

### LLM01: Prompt Injection

**What:** User prompts (direct) or external content (indirect) alter the LLM's behaviour or output in unintended, often malicious ways. Includes instruction override, system prompt extraction, encoding bypass, role-play attacks, multi-turn crescendo, delimiter escape.

**Why it's #1:** Any system that feeds untrusted text to a model is exposed, and no known defence removes the risk completely. It bypasses content filters, leaks system prompts, hijacks agent behaviour.

**Defences:** Instruction hierarchy enforcement, input sanitisation, sandwich-defence prompting, canary tokens, length limits, external-content sanitisation layer.

**Hank testing:** See SKILL.md Phase 1 → LLM01 for the full payload catalogue.

### LLM02: Sensitive Information Disclosure

**What:** LLM reveals PII, training data, RAG source documents, internal IDs, infrastructure details, secrets via outputs. Includes training-data extraction, RAG retrieval leakage, error-message disclosure, prompt-engineered exfiltration.

**Why it matters:** GDPR + privacy-law trigger. Reputational damage. Competitive intelligence leakage.

**Defences:** Output PII filtering, RAG retrieval sensitivity filtering, generic error messages, output constraints + temperature controls.

### LLM03: Supply Chain Vulnerabilities

**What:** LLM supply chains have vulnerabilities: compromised pre-trained models, poisoned model weights, vulnerable inference libraries, malicious dependencies, pickle-format risks, typosquatted MCP packages.

**Why it matters:** Trust-on-first-use problem. A compromised model or package can sit unnoticed for a long time, because nothing re-checks it after install.

**Defences:** Model provenance tracking, signature verification, SafeTensors over pickle, dependency auditing (pip audit, npm audit), no unverified models in production.

### LLM04: Data and Model Poisoning

**What:** Training data, fine-tuning data, or embedding/RAG data is manipulated to introduce backdoors, biases, or weaknesses. Research has shown that a handful of poisoned documents in a RAG corpus can reliably steer answers to targeted questions.

**Why it matters:** Persistent compromise, manifests at inference long after the attack. Hard to detect.

**Defences:** Training data provenance + integrity controls, RAG corpus access controls + integrity checks, embedding pipeline anomaly detection, data deduplication.

### LLM05: Improper Output Handling

**What:** LLM output is consumed by downstream systems (HTML rendering, SQL queries, shell commands, file ops) without sanitisation. Classic injection vectors enabled at LLM scale: XSS via `<script>`, SQLi via `DROP TABLE`, RCE via shell metacharacters, SSRF via crafted URLs.

**Why it matters:** Turns a benign LLM bug into RCE/data exfiltration/privilege escalation.

**Defences:** Never execute LLM output as code without validation; HTML sanitisation (DOMPurify, bleach); parameterised SQL; no shell construction from LLM output; URL allowlisting.

### LLM06: Excessive Agency

**What:** LLMs granted too many tools, too much permission, or too much autonomy. Tool chains used in unintended ways. High-impact actions (delete, send, pay, modify perms) executed without human gating.

**Why it matters:** AI agents are increasingly autonomous, and overprivileged agents are the equivalent of overprivileged service accounts.

**Defences:** Least-privilege tool design, human-in-the-loop for high-impact actions, scoped resource access (not broad fs/net), rate limits, agent cannot self-modify permissions.

### LLM07: System Prompt Leakage

**What:** System prompts are extractable via direct prompts, encoding tricks, delimiter escape, indirect prompts, or refusal-pattern analysis. When system prompts contain secrets (API keys, internal URLs, business logic), extraction = breach.

**Why it matters:** Often contains business logic an attacker can use to craft better attacks. Sometimes contains secrets directly.

**Defences:** No secrets in system prompts (period), training/prompting to refuse extraction, canary-token monitoring, system-prompt structure that doesn't reveal exploitable business logic.

### LLM08: Vector and Embedding Weaknesses

**What:** RAG retrieval can be manipulated to fetch attacker-controlled documents. Embeddings can be inverted to reconstruct source text. Vector DBs without access controls leak cross-tenant data.

**Why it matters:** RAG is the most common production LLM pattern, and the most commonly under-secured layer.

**Defences:** Vector DB read/write access control, relevance threshold filtering, embedding model not publicly accessible, metadata filtering for multi-tenant isolation.

### LLM09: Misinformation

**What:** LLMs produce confident but incorrect outputs (hallucination). In high-stakes domains (medical, legal, financial), confidently wrong answers cause real harm. Citation fabrication compounds the problem.

**Why it matters:** Regulatory trigger (EU AI Act high-risk classification, FTC unfairness, professional liability). Reputational ruin. User trust collapse.

**Defences:** Grounding via RAG with source citation, knowledge-cutoff disclosure, output validation against KB, configured uncertainty expression, high-stakes disclaimers.

### LLM10: Unbounded Consumption

**What:** No limits on input size, output size, request rate, recursive agent loops, or cost. Enables Denial-of-Service AND Denial-of-Wallet (attacker burns your API budget).

**Why it matters:** Every token costs money, so an attacker who can drive usage can run up the bill (denial of wallet) as well as degrade service.

**Defences:** Input token limit, explicit `max_tokens` (never unbounded), per-user/session rate limits, cost monitoring + alerting, recursive-agent circuit breakers.

---

## What changed from 2023-24 to 2025

The 2025 list is a significant reshape, reflecting deployment maturity and new attack surfaces:

| 2023-24 | 2025 | Change |
|---|---|---|
| LLM01 Prompt Injection | LLM01 Prompt Injection | Same, broadened |
| LLM02 Insecure Output Handling | LLM05 Improper Output Handling | Renumbered |
| LLM03 Training Data Poisoning | LLM04 Data and Model Poisoning | Broadened to include fine-tuning + embedding |
| LLM04 Model Denial of Service | LLM10 Unbounded Consumption | Broadened to include cost attacks |
| LLM05 Supply Chain | LLM03 Supply Chain | Renumbered |
| LLM06 Sensitive Information Disclosure | LLM02 Sensitive Information Disclosure | Promoted |
| LLM07 Insecure Plugin Design | (folded into LLM06 Excessive Agency) | Consolidated |
| LLM08 Excessive Agency | LLM06 Excessive Agency | Renumbered |
| LLM09 Overreliance | LLM09 Misinformation | Reframed |
| LLM10 Model Theft | (dropped from Top 10) | n/a |
| n/a | LLM07 System Prompt Leakage | **NEW** |
| n/a | LLM08 Vector and Embedding Weaknesses | **NEW** |

**New entries (LLM07, LLM08) reflect production-RAG patterns** that didn't exist at 2023-24 scale. **Dropped entries (Model Theft)** moved to lower priority as cloud-hosted models reduced the threat surface for most apps.

---

## OWASP LLM Top 10 vs other frameworks

| | OWASP LLM | NIST AI 600-1 GenAI | EU AI Act |
|---|---|---|---|
| Focus | App-layer security risks | Org-level risk management for GenAI | Legal obligations by risk tier |
| Granularity | Specific vulnerability classes | Risk categories + actions | Regulatory requirements |
| Best use | Application security review | Org-wide GenAI governance | Legal compliance |
| Test methodology | Concrete payloads + defences | Mostly procedural | Conformity assessment |

**Hank uses all three together:** OWASP LLM Top 10 for what to test, NIST GenAI Profile for what to govern, EU AI Act for what's legally required. Findings in Hank's report tag each applicable framework.

---

## Tooling

Open-source tools for OWASP LLM testing (Hank's stack):

- **Garak**: LLM vulnerability scanner (NVIDIA), covers 100+ probes mapped to OWASP LLM Top 10
- **PyRIT**: Microsoft AI Red Team Toolkit
- **Promptfoo**: eval framework with red-team capabilities
- **LLMGuard**: output filtering + input scanning
- **Rebuff**: prompt injection detection
- **NeMo Guardrails**: NVIDIA programmable guardrails

Payload categories to start from are in Phase 1 of `SKILL.md`.

---

## Common OWASP LLM Top 10 gotchas (Hank's reviewer lens)

1. **"We use Claude/GPT so injection is handled by the provider."** No. Provider's filters catch obvious attacks. Application-layer injection (indirect via documents, RAG context, tool outputs) is your problem.
2. **Testing LLM01 once and calling it done.** Prompt injection is statistical: run each payload at least 3x. Models are non-deterministic.
3. **Treating output handling (LLM05) as the LLM's problem.** It's the application's problem. The LLM is a string generator; what you do with that string is on you.
4. **No `max_tokens` set.** Default unbounded outputs = denial-of-wallet target.
5. **Secrets in system prompts.** One of the most common findings in a first review. Move to env vars + reference the env var in the prompt at runtime (don't inject the secret value).
6. **RAG with public ingestion.** If users can upload documents to a vector DB that other users query, you have an LLM04 + LLM08 problem by design.
7. **Agents with broad tool access.** "Just give it read access to everything" → LLM06 finding with potential RCE through tool chaining.
8. **Hallucination treated as "we'll fix it later."** LLM09 is a design problem, not a deployment polish problem: grounding + uncertainty expression + disclaimers must be designed in.

---

## Sources

- [OWASP Gen AI Security Project: LLM Top 10 landing](https://genai.owasp.org/llm-top-10/): canonical
- [OWASP Top 10 for LLM Applications 2025 PDF (full standard)](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf): primary source
- Per-item deep dives at `https://genai.owasp.org/llmrisk/llm0X-...` (linked from landing)
- Garak: https://github.com/leondz/garak
- PyRIT: https://github.com/Azure/PyRIT
- Promptfoo: https://www.promptfoo.dev/

**Last reviewed:** 2026-06-01 by Hank. Aligned to OWASP LLM v2025 edition. Watch for v2026, typically published November.
