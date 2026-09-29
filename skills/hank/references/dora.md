# DORA: Digital Operational Resilience Act

**Citation:** Regulation (EU) 2022/2554 on digital operational resilience for the financial sector. Signed 14 December 2022. **Applies from 17 January 2025** (Art. 64). Directly applicable, no national transposition needed for the Regulation itself.

**Who enforces:** National financial competent authorities (central banks, securities and insurance regulators) supervise financial entities (Art. 46). The three ESAs (EBA, EIOPA, ESMA) act as **Lead Overseer** for designated critical ICT third-party providers (Art. 31).

**Fines:** DORA sets **no EU-wide fine cap for financial entities**. Member states set administrative penalties and remedial measures (Art. 50), including public notices and measures against management body members (Art. 50(4)-(5)). For **critical ICT third-party providers**, the Lead Overseer can impose **periodic penalty payments of up to 1% of average daily worldwide turnover**, daily, for up to six months (Art. 35(6)-(8)).

**Relationship to NIS2:** for financial entities that are NIS2 essential/important entities, DORA is the sector-specific act (Art. 1(2)).

---

## Scope: who is in (Art. 2)

**Financial entities (Art. 2(1)(a)-(t)):**
credit institutions; payment institutions (incl. exempted); account information service providers; e-money institutions (incl. exempted); investment firms; crypto-asset service providers and issuers of asset-referenced tokens; central securities depositories; central counterparties; trading venues; trade repositories; AIFMs; UCITS management companies; data reporting service providers; insurance and reinsurance undertakings; insurance/reinsurance/ancillary intermediaries; IORPs (occupational pensions); credit rating agencies; administrators of critical benchmarks; crowdfunding service providers; securitisation repositories.

**Plus (Art. 2(1)(u)): ICT third-party service providers**, but only for the parts of DORA that address them (contract terms and the CTPP oversight framework).

**Carve-outs (Art. 2(3)):** small AIFMs under Art. 3(2) AIFMD; small insurers exempt from Solvency II (Art. 4 of Directive 2009/138/EC); IORPs with ≤15 members in total; MiFID-exempt persons; **insurance intermediaries that are micro, small or medium enterprises**; post office giro institutions.

**Simplified regime (Art. 16):** small and non-interconnected investment firms, exempted payment and e-money institutions, small IORPs and some others get a lighter ICT risk framework instead of Art. 5-15.

**Key definitions (Art. 3):**
- **ICT services** (3(21)): "digital and data services provided through ICT systems to one or more internal or external users on an ongoing basis", including hardware-as-a-service. Excludes analogue telephony. **SaaS, APIs, hosted AI models, managed services, data feeds all fit.**
- **ICT third-party service provider** (3(19)): "an undertaking providing ICT services". No size threshold.
- **Critical or important function** (3(22)): a function whose disruption would materially impair the entity's financial performance, the soundness or continuity of its services, or its regulatory compliance.
- **Major ICT-related incident** (3(10)): high adverse impact on systems supporting critical or important functions.

---

## The five pillars

### 1. ICT risk management (Art. 5-16)
- **Management body owns it** and is accountable (Art. 5(2)).
- Documented ICT risk management framework: identify, protect, detect, respond/recover, backup, learning, communication (Art. 6-14).
- ICT third-party risk is part of this framework (Art. 28(1)).
- Detail: RTS on ICT risk management framework and simplified framework (Commission Delegated Regulation (EU) 2024/1774; number taken from ESAs listing, text not fetched this session: UNVERIFIED).

### 2. ICT incident management and reporting (Art. 17-23)
- Record **all** ICT incidents and significant cyber threats (Art. 17(2)).
- Classify with the criteria in **Delegated Regulation (EU) 2024/1772**.
- **Report major ICT-related incidents** to the competent authority (Art. 19(1)); inform affected clients without undue delay if their financial interests are hit (Art. 19(3)).
- Voluntary notification of significant cyber threats (Art. 19(2)).
- **Deadlines, Delegated Regulation (EU) 2025/301, Art. 5** (applies since 12 Mar 2025):

| Report | Deadline |
|---|---|
| Initial notification | Within **4 hours of classifying** the incident as major, and **no later than 24 hours of becoming aware** of it. If classified as major only after 24h, within 4h of classification |
| Intermediate report | Within **72 hours of the initial notification**, even if nothing changed; updated when regular activities are recovered |
| Final report | Within **1 month** of the (latest) intermediate report |

  Weekend/bank-holiday rule: may file by noon next working day (Art. 5(4)), **except** credit institutions, CCPs, trading venue operators and NIS2 essential/important entities for initial and intermediate reports (Art. 5(5)).
- Templates: ITS, Commission Implementing Regulation (EU) 2025/302 (cited by the European Parliament EPRS briefing; OJ text not fetched: treat number as secondary-sourced).
- **Reporting can be outsourced to a third party, but the financial entity stays fully responsible** (Art. 19(5)).

### 3. Digital operational resilience testing (Art. 24-27)
- Risk-based testing programme: vulnerability scans, open source analysis, network security assessments, source code reviews where feasible, scenario tests, performance tests, end-to-end and penetration testing (Art. 25(1)).
- **Threat-led penetration testing (TLPT)** at least **every 3 years** for entities identified by their competent authority (Art. 26(1), (8)). Performed **on live production systems** supporting critical or important functions (Art. 26(2)).
- **ICT third-party providers in TLPT scope must participate** (Art. 26(3)). Where that would hurt the provider's other clients, **pooled testing** led by one financial entity is allowed (Art. 26(4)).
- External testers every third test if internal testers are used (Art. 26(8)). Tester requirements in Art. 27.
- Detail: RTS on TLPT, Commission Delegated Regulation (EU) 2025/1190, in force, applies since 8 Jul 2025 (per EBA).

### 4. ICT third-party risk (Art. 28-44)
Financial-entity side:
- Entity stays **fully responsible** for compliance when outsourcing (Art. 28(1)(a)).
- **ICT third-party risk strategy** and policy for services supporting critical or important functions (Art. 28(2)); detail in **Delegated Regulation (EU) 2024/1773** (applies since 15 Jul 2024 per EBA).
- **Register of information** on **all** ICT third-party contracts, flagging those supporting critical or important functions; reported to the authority at least yearly and on request (Art. 28(3)). Templates: **Implementing Regulation (EU) 2024/2956**.
- Pre-contract: assess criticality, risks, concentration risk, **due diligence on the provider**, conflicts of interest (Art. 28(4)); only use providers with "appropriate information security standards" (Art. 28(5)).
- Termination rights (Art. 28(7)) and tested **exit strategies** for critical/important services (Art. 28(8)).
- Concentration risk and subcontracting chains assessed pre-contract (Art. 29).
- **Mandatory contract terms: Art. 30** (see below).
- **Subcontracting RTS: Delegated Regulation (EU) 2025/532** (adopted 24 Mar 2025, OJ 2 Jul 2025, applies from 22 Jul 2025).

CTPP oversight side: Art. 31-44 (see below).

### 5. Information sharing (Art. 45)
Voluntary exchange of cyber threat intelligence (IoCs, TTPs, alerts) within trusted communities of financial entities, under confidentiality, GDPR and competition rules. Arrangements may define how ICT third-party providers are involved (Art. 45(2)). Entities notify their authority when they join or leave.

---

## Art. 30: what the contract must say

**All ICT services (Art. 30(2)):**
- (a) Full description of services; whether subcontracting of critical/important services is allowed and on what conditions
- (b) **Locations** (regions/countries) of service and data processing and storage, with **advance notice of changes**
- (c) Availability, authenticity, integrity, confidentiality of data, incl. personal data
- (d) Access, recovery and **return of data** in an easily accessible format on insolvency, resolution, discontinuation or termination
- (e) Service level descriptions
- (f) **Incident assistance** at no extra cost or at a cost fixed in advance
- (g) Full cooperation with the entity's competent and resolution authorities
- (h) Termination rights and minimum notice periods
- (i) Participation in the entity's ICT security awareness and resilience training

**Additionally, for services supporting critical or important functions (Art. 30(3)):**
- (a) Full SLAs with precise quantitative and qualitative targets
- (b) Notice and reporting duties, incl. any development that could materially affect service delivery
- (c) Implement and **test business contingency plans**; appropriate ICT security measures, tools and policies
- (d) **Participate and fully cooperate in the entity's TLPT**
- (e) **Unrestricted access, inspection and audit rights** for the entity, its appointee and the competent authority, incl. on-site; alternative assurance levels possible where other clients' rights are affected; cooperation with the Lead Overseer
- (f) **Exit strategy** with a mandatory adequate transition period

**Micro-enterprise financial entity exception:** audit rights may be delegated to an independent third party appointed by the provider (Art. 30(3), last subparagraph).

**Contract form:** one written document including SLAs, on paper or a downloadable, durable, accessible format (Art. 30(1)).

## Subcontracting RTS 2025/532: what it adds to the contract

For ICT services supporting critical or important functions that may be subcontracted, the contract must specify (Art. 4):
- which services can be subcontracted and on what conditions
- the provider stays responsible for subcontracted services and **monitors all of them**
- the provider's monitoring and reporting duties to the entity
- location risk assessment of subcontractors and their parents; data location
- flow-down: business contingency plans, ICT security standards, **same access, inspection and audit rights** for the entity and authorities
- continuity through the whole chain if a subcontractor fails
- **notification of material changes** to subcontracting

Material changes (Art. 5): the provider must inform the entity **well in time**; the contract sets a **reasonable notice period** to approve or object; the change can only go ahead after approval or no objection by the end of that period.

Termination (Art. 6): the entity may terminate if the provider implements a change despite objection, implements it before the notice period ends, or subcontracts something not explicitly permitted.

Pre-contract (Art. 3): the entity must check that the provider can identify all subcontractors supporting critical/important functions, has the resources to monitor them, and that subcontractors grant the same access and inspection rights.

---

## Critical ICT third-party providers (CTPPs)

**Designation criteria (Art. 31(2))**, all considered: systemic impact of a large-scale failure; systemic importance of dependent entities (G-SIIs/O-SIIs); reliance for critical or important functions; degree of substitutability. Further specified in **Delegated Regulation (EU) 2024/1502**. Group-level assessment (Art. 31(3)).

**Excluded from designation (Art. 31(8)):** financial entities serving other financial entities; intra-group providers; providers serving financial entities in **one member state only** whose clients are only active there; ECB-oversight frameworks.

**First designations: 18 November 2025.** The ESAs published 19 CTPPs:
Accenture plc; Amazon Web Services EMEA Sarl; Bloomberg L.P.; Capgemini SE; Colt Technology Services; Deutsche Telekom AG; Equinix (EMEA) B.V.; Fidelity National Information Services, Inc.; Google Cloud EMEA Limited; International Business Machines Corporation; InterXion HeadQuarters B.V.; Kyndryl Inc.; LSEG Data and Risk Limited; Microsoft Ireland Operations Limited; NTT DATA Inc.; Oracle Nederland B.V.; Orange SA; SAP SE; Tata Consultancy Services Limited.

The list is updated yearly (Art. 31(9)). As of 29 Sep 2026 the ESAs' oversight page still links the 18 Nov 2025 list; no 2026 update found this session. Notable absences some will expect: no AI model provider (e.g. Anthropic, OpenAI) is on the list.

**Other points:**
- A non-EU CTPP must set up an **EU subsidiary within 12 months** of designation for EU financial entities to keep using it (Art. 31(12)).
- **Opt-in:** a provider can ask to be designated (Art. 31(11)); fixed opt-in fee **€50,000** (Delegated Regulation (EU) 2024/1505, per ESAs page). ESAs reply within 6 months.
- Oversight tools: information requests, investigations, on-site inspections, recommendations, periodic penalty payments (Art. 35-39). Joint Examination Teams: Delegated Regulation (EU) 2025/420. Oversight conditions: Delegated Regulation (EU) 2025/295.
- EU-UK MoU on CTPP oversight published January 2026 (ESAs page).

---

## Level 2 acts relevant to suppliers (quick reference)

| Act | Topic | Status (source) |
|---|---|---|
| Delegated Reg. (EU) 2024/1773 | Policy on ICT services supporting critical/important functions (contract policy) | Applies since 15 Jul 2024 (EBA) |
| Implementing Reg. (EU) 2024/2956 | Register of information templates | Published in OJ (EBA) |
| Delegated Reg. (EU) 2024/1772 | Incident classification criteria and materiality thresholds | In force (cited in 2025/301) |
| Delegated Reg. (EU) 2025/301 | Incident report content and deadlines | Applies since 12 Mar 2025 (EUR-Lex) |
| Implementing Reg. (EU) 2025/302 | Incident report templates | Number via EPRS briefing; OJ not fetched |
| Delegated Reg. (EU) 2025/532 | Subcontracting of ICT services supporting critical/important functions | Applies since 22 Jul 2025 (EUR-Lex, EBA) |
| Delegated Reg. (EU) 2025/1190 | TLPT | Applies since 8 Jul 2025 (EBA) |
| Delegated Reg. (EU) 2024/1502 | CTPP designation criteria | In force (EBA) |
| Delegated Reg. (EU) 2024/1505 | Oversight fees incl. €50k opt-in fee | In force (EBA) |
| Delegated Reg. (EU) 2024/1774 | ICT risk management framework | UNVERIFIED number (ESAs listing title only) |

**Pending, not law:** the Digital Omnibus (COM(2025) 837) proposes a single-entry point for incident reports including DORA major incidents. EUR-Lex status on 2026-09-29: "Ongoing". The ECB asked for financial entities to be excluded (per EPRS briefing).

---

## Applying this in practice

For a small software or AI supplier selling to a bank, insurer, payment/e-money firm, investment firm, crypto firm or fintech.

**The core fact:** DORA mostly binds **the customer**, not you. You are hit through the contract. Unless you are designated a CTPP (very unlikely for a small supplier, and never if you only serve financial entities in one member state that only operate there), no regulator supervises you directly under DORA. But the customer cannot legally sign without the Art. 30 terms, and cannot keep you if you will not cooperate.

**1. Work out which bucket you are in**
- [ ] Is the customer a financial entity under Art. 2(1)? (Check the list; small insurance intermediaries are out.)
- [ ] Is what you sell an "ICT service" (ongoing digital or data service)? A hosted AI assistant, API, SaaS, data pipeline or managed service is. A one-off build handed over with no ongoing service is arguably not (Hank's reading; ask the customer how they classify it).
- [ ] **Ask the customer whether they classify your service as supporting a critical or important function.** This decides whether Art. 30(3), the subcontracting RTS, TLPT participation and exit plans apply. An AI tool in claims handling, credit decisions, payments, customer onboarding or core operations may well be; an internal marketing copy tool usually is not.

**2. Expect these in every contract (Art. 30(2))**
- [ ] Written service description + SLAs in one document
- [ ] Declared data processing and storage **locations**, with advance notice of changes (list your hosting regions and your model provider's)
- [ ] Data security clauses (overlaps with the GDPR DPA)
- [ ] Data return / export in accessible format on termination or insolvency
- [ ] **Incident assistance at no cost or pre-agreed cost**
- [ ] Cooperation with the customer's regulators
- [ ] Termination rights + notice periods
- [ ] Taking part in their security awareness training if asked

**3. If the service supports a critical or important function, also expect (Art. 30(3) + RTS 2025/532)**
- [ ] Quantified SLAs and service reporting
- [ ] Tested business continuity plan (have one and test it)
- [ ] **Unrestricted audit and on-site inspection rights** for the customer and its regulator. Negotiate pooled audits or third-party reports (SOC 2, ISO 27001) as "alternative assurance" where allowed, but do not refuse regulator access.
- [ ] Participation in their **TLPT on production**, or pooled testing
- [ ] Exit plan with a transition period where you keep serving them
- [ ] **Subcontractor disclosure and flow-down:** your cloud host, database provider, and **LLM API provider** are subcontractors. You must identify them, monitor them, flow down security and continuity terms, and pass through audit rights as far as possible. Big providers' standard terms may not give audit rights to your customer: flag this gap early, it is the most common blocker.
- [ ] **Material change notice:** you cannot swap your model provider, hosting region or other key subcontractor without advance notice and a chance to object. Build this into your roadmap process.

**4. Be ready for the register of information**
- [ ] The customer must record you (and your relevant subcontractors) in their register. Expect a questionnaire asking for your legal entity identifier (LEI), legal name, country, services, subcontractor chain and locations. Keep a standard answer pack.

**5. Incident support**
- [ ] Your incident process must let the customer meet **4h after classification / 24h after awareness** for initial reports. Contractually commit to notify them fast (many ask for 1-4 hours) and give them the facts they need for the intermediate (72h) and final (1 month) reports.
- [ ] One event can trigger several clocks: their DORA report, your GDPR processor notice to them, possibly your CRA report if you ship an installable product (see `cyber-resilience-act.md`), possibly NIS2.

**6. Security baseline they will check (Art. 28(5))**
- [ ] "Appropriate information security standards": in practice ISO 27001 or SOC 2 or a detailed questionnaire. For critical/important services, "most up-to-date and highest quality" standards get "due consideration".
- [ ] For AI: document model provenance, prompt injection controls, data isolation between tenants, no training on customer data, logging and human oversight. Map to `iso-42001.md` and `eu-ai-act.md`.

**7. Pricing and scope**
- [ ] Price the overhead: audits, TLPT participation, exit assistance, incident support at no cost. These are real costs a small supplier must plan for.

---

## Common misreadings

1. **"DORA applies to us because we sell to banks."** It applies to the bank. You feel it through Art. 30 contract terms. Only CTPPs are directly overseen.
2. **"Only critical providers have obligations."** Every ICT contract with a financial entity needs Art. 30(2) terms, whatever the supplier's size.
3. **"The subcontracting RTS makes us monitor the whole chain to the end."** The adopted RTS focuses on subcontractors that support critical or important functions or material parts of them; the provider monitors all such subcontracted services (Art. 4(1)(b)).
4. **"DORA has 2% / 10M fines."** No EU fine cap for financial entities; member states set penalties. The 1% daily turnover figure is for CTPP periodic penalty payments.
5. **"Incident reporting is 24h/72h like NIS2."** DORA adds a **4-hour-after-classification** trigger for the initial notification, and the 72h runs from the initial notification, not from awareness.
6. **"Cloud and AI giants are all CTPPs."** The first list (18 Nov 2025) has 19 providers; AI model providers are not on it.

---

## Sources

- [Regulation (EU) 2022/2554, official text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng): Art. 1, 2, 3, 5, 16, 17, 19, 25-31, 35, 45, 50, 64
- [Commission Delegated Regulation (EU) 2025/301 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg_del/2025/301/oj/eng): incident report content and time limits
- [Commission Delegated Regulation (EU) 2025/532 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg_del/2025/532/oj/eng): subcontracting RTS
- [EBA: Joint RTS on subcontracting (status page)](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/operational-resilience/joint-regulatory-technical-subcontracting)
- [EBA: Joint technical standards on major incident reporting](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/operational-resilience/joint-technical-standards-major-incident-reporting)
- [EBA: ITS on register of information templates](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/operational-resilience/implementing-technical-standards-establish-templates-register-information)
- [EBA: RTS on policy for ICT services supporting critical or important functions](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/operational-resilience/regulatory-technical-standards-policy-ict-services-supporting-critical-or-important-functions)
- [EBA: Joint RTS on TLPT](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/operational-resilience/joint-regulatory-technical-standards-specifying-elements-related-threat-led-penetration-tests)
- [EBA: DORA overview page](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act)
- [EBA: DORA oversight page (CTPPs, opt-in, Level 2 acts)](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act/dora-oversight)
- [ESAs press release: CTPP designation, 18 Nov 2025](https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital)
- [EIOPA: List of designated CTPPs (PDF)](https://www.eiopa.europa.eu/document/download/56b1ca78-5dd2-4d36-8377-47a538eb7558_en?filename=List%20of%20designated%20CTPPs.pdf)
- [EUR-Lex procedure 2025/0360/COD (Digital Omnibus): status "Ongoing"](https://eur-lex.europa.eu/procedure/EN/2025_360)
- [EPRS briefing: Digital Omnibus Single-Entry Point (March 2026)](https://www.europarl.europa.eu/RegData/etudes/BRIE/2026/785675/EPRS_BRI(2026)785675_EN.pdf)

**Last reviewed:** 2026-09-29 (primary sources checked this date).
