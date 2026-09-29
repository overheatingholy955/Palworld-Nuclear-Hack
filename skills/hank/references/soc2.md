# SOC 2: AICPA System and Organisation Controls 2

**Citation:** AICPA Trust Services Criteria (2017, revised 2022). Defined by the American Institute of Certified Public Accountants (AICPA) and CIMA. Performed under AICPA's SSAE 18 attestation standard.

**Enforcement:** SOC 2 is **not a regulation**: it's an attestation. A licensed CPA firm performs the examination and issues a report. Buyers (enterprise customers, procurement teams) use the report as a trust signal. "Failure" = a qualified opinion or a finding, which kills deals; there is no fine.

---

## Scope: who it applies to

Any **service organisation** that holds, processes, or transmits customer data. In practice: B2B SaaS, cloud services, MSPs, data processors, payment processors, ML/AI APIs, anyone whose customers' auditors will ask "what's your SOC 2 report?"

SOC 2 is a US-rooted standard but is **the de facto trust signal globally for B2B SaaS**, and enterprise procurement teams ask for it everywhere.

---

## Type I vs Type II

| | Type I | Type II |
|---|---|---|
| What it shows | Controls are *designed* appropriately at a point in time | Controls *operated effectively* over a period (typically 3–12 months) |
| Effort | ~3 months readiness | Type I + 3–12 months of evidence accumulation |
| Buyer weight | Acceptable starter; enterprise will want Type II within 12 months | Gold standard |
| Renewal | Snapshot: re-do for any material change | Annual |

---

## The five Trust Services Criteria (TSC)

Security is **mandatory** for every SOC 2 examination. The other four are **optional**: pick based on what you sell.

### 1. Security (the "Common Criteria": mandatory)

The baseline. ~33 controls (CC1–CC9) covering:
- **CC1 Control environment**: governance, accountability, ethics
- **CC2 Communication + information**: internal + external comms
- **CC3 Risk assessment**: identifying + analysing risks
- **CC4 Monitoring activities**: ongoing + separate evaluations
- **CC5 Control activities**: selection + development of controls
- **CC6 Logical + physical access controls**: authentication, authorisation, physical security
- **CC7 System operations**: monitoring, incident response, change management
- **CC8 Change management**: system changes, code deployments
- **CC9 Risk mitigation**: risk response, vendor management

### 2. Availability

System is available for operation + use as committed. Add this if customers depend on uptime SLAs.
- Backup, disaster recovery, business continuity
- Capacity monitoring, performance management
- Incident response with availability impact

### 3. Processing Integrity

System processing is complete, valid, accurate, timely, authorised. Add this if you process financial transactions, e-commerce, billing.
- Input validation, error handling, output review
- Data quality monitoring, reconciliation

### 4. Confidentiality

Information designated as confidential is protected. Add this if customers entrust you with their business secrets (most B2B SaaS).
- Data classification, encryption in transit + at rest, secure disposal
- Confidentiality agreements with employees + vendors

### 5. Privacy

Personal information is collected, used, retained, disclosed, disposed of per the AICPA's privacy notice principles. Add this if you handle consumer PII at scale.
- Notice + consent, choice + control, access, disclosure, retention
- Aligns conceptually with GDPR but is its own framework (not a substitute)

---

## The audit lifecycle

1. **Readiness assessment** (4–8 weeks): gap analysis vs the chosen TSC. Often run by a compliance partner (Vanta, Drata, Secureframe, Tugboat Logic) before the auditor lands.
2. **Remediation** (variable): close gaps. Implement policies, configure tooling (MDM, access reviews, SIEM, vuln scanning), build evidence trails.
3. **Audit period** (Type II only): 3–12 months of continuous control operation, evidence accumulated.
4. **Audit fieldwork** (4–8 weeks): CPA firm reviews evidence, samples, interviews, tests.
5. **Report issuance**: clean (unqualified), qualified, adverse, or disclaimer of opinion. Report includes management's description of system, controls list, auditor's tests + results.
6. **Renewal**: annually for Type II; gap-free bridge letters cover the period between report dates.

**Bridge letter** = a short attestation from management covering the period between the SOC 2 report end-date and the procurement date. Standard ask from enterprise buyers.

---

## What goes in the report

Five sections:
1. **Independent service auditor's report**: auditor's opinion
2. **Management's assertion**: management states the system description is fair + controls met criteria
3. **System description**: narrative covering services, infrastructure, software, people, procedures, data
4. **Trust Services Criteria + related controls**: table of criteria, controls, tests performed, results
5. **Other information** (optional): anything not covered by the auditor's opinion

---

## SOC 2 + AI controls (emerging best practice 2026)

The AICPA hasn't issued an "AI TSC" but auditors increasingly expect AI-specific controls layered into the existing TSCs:

- **CC6 (access)**: Model + prompt template access controls, who can deploy fine-tunes
- **CC7 (operations)**: Monitoring for anomalous model behaviour, prompt injection detection
- **CC8 (change management)**: Prompt template changes treated as code changes (version-controlled, reviewed, tested)
- **CC9 (vendor mgmt)**: Risk assessment for every LLM/AI sub-processor (Anthropic, OpenAI, etc.), including their training-on-inputs policy
- **Processing integrity**: Output validation, schema enforcement on LLM outputs, guardrails
- **Confidentiality**: No-training-on-inputs guarantee from LLM providers; secrets never in prompts
- **Privacy**: PII handling in prompts + RAG context; output PII filtering

---

## SOC 2 vs ISO 27001: when buyers want which

| | SOC 2 | ISO 27001 |
|---|---|---|
| Geography | US-rooted, global trust signal | Global, especially EU/APAC |
| Format | Attestation report (signed by CPA) | Certificate (issued by accredited body) |
| Scope | Customer-facing controls | Whole ISMS |
| Renewal | Annual (Type II) | 3-year cert + annual surveillance |
| Cost | Auditor fees plus tooling; get quotes | Certification body fees plus tooling; get quotes |
| Best for | US enterprise SaaS sales | Multinational, EU government, healthcare |

**Many companies do both**: SOC 2 for US sales motion, ISO 27001 for EU/regulated sectors. Significant control overlap → audit consolidation reduces marginal cost.

---

## Common SOC 2 gotchas (Hank's reviewer lens)

1. **"We use AWS so we're SOC 2 compliant."** Wrong. AWS's SOC 2 covers AWS's controls. Your application + ops are out of scope for AWS's report.
2. **Missing change management for prompt templates.** Auditors increasingly catch this: prompt changes are code changes.
3. **Access reviews done annually instead of quarterly.** Annual is the floor, quarterly is the bar most enterprise customers expect.
4. **No evidence of training completion.** Security awareness training is a soft control; the evidence is who completed it + when.
5. **Vendor risk assessments not updated.** A sub-processor changing terms (e.g., training on inputs) without your re-assessment is a finding.
6. **Bridge letter expired.** Procurement asks "is your bridge letter current?", and if the gap exceeds the bridge period, deal stalls.
7. **Type I report sold as Type II.** Type I confirms design; Type II confirms operation. Misrepresenting kills trust.

---

## Sources

- [AICPA: SOC suite of services (canonical)](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
- [Secureframe: Trust Services Criteria](https://secureframe.com/hub/soc-2/trust-services-criteria): plain-English summary of the five TSCs
- [TSP Section 100: Trust Services Criteria (AICPA)](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-trust-services): primary source
- AICPA SOC 2 Description Criteria DC 200

**Last reviewed:** 2026-06-01 by Hank.
