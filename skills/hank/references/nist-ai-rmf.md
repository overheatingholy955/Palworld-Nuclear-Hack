# NIST AI Risk Management Framework (AI RMF 1.0)

**Citation:** NIST AI 100-1, Artificial Intelligence Risk Management Framework (AI RMF 1.0), released 26 January 2023. Companion: NIST AI 600-1, Generative AI Profile, released 26 July 2024. Latest addition: AI RMF Profile on Trustworthy AI in Critical Infrastructure (concept note April 2026).

**Enforcement:** **Voluntary**, sector-agnostic. Developed by the US National Institute of Standards and Technology (NIST). No fines, no certificate. Used by US federal agencies, regulated industries, and globally as the most-cited AI risk methodology.

---

## Scope: who it applies to

Any organisation designing, developing, deploying, or using AI systems. Particularly relevant for:
- US federal agencies + contractors (de-facto requirement)
- Regulated industries (finance, healthcare) using AI
- Any organisation wanting a sector-agnostic, mature AI risk methodology
- Organisations using it inside an ISO 42001 management system (NIST publishes a 42001 crosswalk)

---

## Trustworthy AI characteristics

The framework defines seven characteristics of trustworthy AI. Every AI system should be assessable against them:

1. **Valid + reliable**: performs as intended, robust to expected conditions
2. **Safe**: doesn't endanger life, health, property, environment
3. **Secure + resilient**: withstands attack, recovers from disruption (overlaps OWASP LLM Top 10, MITRE ATLAS)
4. **Accountable + transparent**: actions are explainable + assignable
5. **Explainable + interpretable**: outputs can be understood + reasoned about
6. **Privacy-enhanced**: preserves data confidentiality + integrity
7. **Fair (with managed harmful bias)**: bias measured + mitigated

**The seven characteristics are the questions Hank asks** when running an AI security review on a new feature. Each finding tags which characteristic(s) it threatens.

---

## The four core functions

### GOVERN: applies across all stages

Sets the organisational context for AI risk management. Outcomes:

- AI risk policies + processes in place
- Accountability structures defined
- Workforce diversity + cross-functional input
- AI risk awareness + training
- Documented org-wide approach to AI risk

**Hank's checklist:**
- [ ] AI risk policy exists + signed by leadership
- [ ] Roles + responsibilities for AI defined (who decides? who builds? who monitors? who responds to incidents?)
- [ ] AI risk register maintained
- [ ] Third-party AI supplier oversight documented
- [ ] Workforce competence in AI documented

### MAP: establishes context

Identifies the AI system's purpose, deployment context, stakeholders, potential impacts. Outcomes:

- Context established
- Categorisation of the AI system
- Capabilities, intended use, costs, benefits documented
- Risks + benefits mapped (across the seven trustworthy characteristics)
- Impacts to individuals + groups + organisations + ecosystems identified

**Hank's checklist:**
- [ ] AI system purpose + boundaries documented
- [ ] Stakeholders identified (developers, deployers, end users, affected non-users)
- [ ] Intended + reasonably foreseeable misuse documented
- [ ] Impact assessment performed
- [ ] Data sources + lineage mapped

### MEASURE: assesses risks

Analyses, assesses, benchmarks, monitors AI risks + related impacts. Outcomes:

- Appropriate methods + metrics identified + applied
- AI systems evaluated for trustworthy characteristics
- Mechanisms for tracking AI risks identified + implemented
- Feedback about efficacy collected + assessed

**Hank's checklist:**
- [ ] Performance metrics defined for each trustworthy characteristic
- [ ] Adversarial testing performed (overlaps Mode 1 Phase 1 OWASP)
- [ ] Bias evaluation done with appropriate methodology
- [ ] Monitoring telemetry in place (input distributions, output distributions, drift)
- [ ] Red-team / eval suite covers known attack patterns

### MANAGE: responds to risks

Prioritises + acts on mapped + measured risks. Outcomes:

- AI risks prioritised + responded to
- Strategies to maximise benefits + minimise impacts implemented
- AI risks + benefits tracked across lifecycle
- Treated risks documented; responses to identified incidents documented

**Hank's checklist:**
- [ ] Risk treatment plan exists (mitigate / transfer / avoid / accept)
- [ ] Incident response process tested for AI-specific incidents
- [ ] Post-market monitoring in place (overlaps ISO 42001 Annex A.6)
- [ ] Model retirement + replacement process defined
- [ ] Continuous improvement loop (lessons learned feed back into Govern)

---

## Generative AI Profile (NIST AI 600-1, July 2024)

The Generative AI Profile applies the AI RMF specifically to GenAI risks. Adds 12 risks unique to or amplified by GenAI:

1. **CBRN information or capabilities**: chemical, biological, radiological, nuclear uplift
2. **Confabulation**: hallucination, fabricated facts
3. **Dangerous, violent, hateful content**
4. **Data privacy**: training data leakage, prompt PII
5. **Environmental impacts**: compute + energy
6. **Harmful bias + homogenisation**
7. **Human-AI configuration**: over-reliance, automation bias
8. **Information integrity**: misinformation, deepfakes
9. **Information security**: overlaps OWASP LLM Top 10
10. **Intellectual property**: training data IP, output IP
11. **Obscene, degrading, abusive content**
12. **Value chain + component integration**: supply chain risk

For each, the profile provides suggested actions per function (Govern / Map / Measure / Manage).

---

## Crosswalks (NIST publishes these, and they save a lot of audit work)

NIST AI RMF has formal crosswalks to:

- **ISO/IEC 42001**: clause-by-clause mapping
- **ISO/IEC 23894:2023**: AI risk management
- **EU AI Act**: function-to-article mapping
- **OECD AI Principles**
- **EO 14110** (US AI Executive Order, since rescinded but reference material)
- **NIST Cybersecurity Framework 2.0** (general-cyber → AI-cyber bridge)
- **NIST Privacy Framework**

Using these crosswalks, an org can map a single set of evidence to multiple frameworks, which cuts audit overhead when pursuing ISO 42001 + EU AI Act conformity + SOC 2 + NIST AI RMF alignment together.

---

## NIST AI RMF Playbook

NIST publishes a [Playbook](https://airc.nist.gov/airmf-resources/playbook/): granular action suggestions for each AI RMF outcome. Treats every outcome as a "do these things" checklist. Use it as Hank's reference cookbook for operationalising AI RMF.

Also worth knowing: **AI Resource Center (AIRC)** at airc.nist.gov, playbook, crosswalks, use cases, glossary, all in one place.

---

## NIST AI RMF vs other frameworks

| | NIST AI RMF | ISO 42001 | EU AI Act |
|---|---|---|---|
| Type | Risk framework | Management system | Regulation |
| Mandatory? | No | No (cert is voluntary) | Yes (in EU) |
| Approach | Risk-by-risk, function-by-function | Management-system clauses | Tiered obligations |
| Best use | Methodology inside an ISMS/AIMS or for orgs without one | Audited management system | Legal compliance |
| Geography | US-rooted, global use | Global | EU |

**Common stack:** NIST AI RMF as risk methodology → ISO 42001 as management system → EU AI Act conformity for high-risk deployments. NIST's crosswalks make the stack tractable.

---

## Common NIST AI RMF gotchas (Hank's reviewer lens)

1. **Treating AI RMF as a checklist.** It's a framework: outcomes, not controls. Tailor to the org. A pure checklist application produces audit theatre, not real risk reduction.
2. **GOVERN function skipped because "we're small."** Even a single-founder shop needs a documented AI policy and accountability; otherwise there is no foundation for Map/Measure/Manage.
3. **MAP function under-specified.** Vague stakeholder identification + impact analysis = downstream Measure can't be anchored. The most common audit gap.
4. **MEASURE without baseline.** Evals + metrics need a baseline + a target. "We measured accuracy" without a target = no risk signal.
5. **MANAGE bypassed for "we'll deal with incidents when they happen."** Incident response must be documented + tested before deployment, not after the first incident.
6. **GenAI Profile risks acknowledged but not mitigated.** The profile is action-oriented: list of risks + suggested actions. Pick mitigations + implement, don't just acknowledge.
7. **Old EO 14110 still cited as authoritative.** The Biden EO was rescinded in 2025. Cite NIST AI RMF + relevant state laws + EU AI Act, not EO 14110.

---

## Sources

- [NIST AI Risk Management Framework (canonical landing page)](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI 100-1: AI RMF 1.0 (full PDF)](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf): primary source
- [NIST AI 600-1: Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf): GenAI-specific risks + actions
- [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/): operational action suggestions
- [NIST AI Resource Center (AIRC)](https://airc.nist.gov/): crosswalks, use cases, glossary
- [Concept note: AI RMF Profile on Trustworthy AI in Critical Infrastructure (April 2026)](https://www.nist.gov/programs-projects/concept-note-ai-rmf-profile-trustworthy-ai-critical-infrastructure)

**Last reviewed:** 2026-06-01 by Hank. AI RMF v2 rumoured for 2026, watch NIST releases.
