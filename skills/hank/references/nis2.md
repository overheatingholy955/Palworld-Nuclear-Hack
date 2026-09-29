# NIS2: Directive on a high common level of cybersecurity across the Union

**Citation:** Directive (EU) 2022/2555 (OJ L 333, 27.12.2022, p. 80). Replaces NIS1 (Directive (EU) 2016/1148). It is a **directive**, so the obligations reach companies through each Member State's transposing law, not directly.

**Key implementing act:** Commission Implementing Regulation (EU) 2024/2690 of 17 October 2024 (published OJ 18.10.2024; in force on the 20th day after publication). Directly applicable to the digital-infrastructure and ICT-service-management entity types listed below.

**Enforcement:** National competent authorities + national CSIRTs + a single point of contact per Member State. Maximum fines (Art. 34): essential entities at least €10M or 2% of worldwide annual turnover, whichever is higher; important entities at least €7M or 1.4%, whichever is higher. These are *minimum maxima*: Member States may set higher caps.

**Deadlines in the text:** transposition by **17 October 2024**, national measures applied from **18 October 2024** (Art. 41(1)). Member State lists of essential and important entities by **17 April 2025** (Art. 3(3)). Entities in the Art. 27 registry (DNS, cloud, data centres, CDNs, MSPs, MSSPs, online marketplaces, search engines, social networks) had to submit registration details by **17 January 2025** (Art. 27(2)), in practice only where national law was in place.

---

## Scope: who is in

NIS2 applies to an entity when **both** tests are met:

1. **Sector test.** The entity is of a type listed in **Annex I** (sectors of high criticality) or **Annex II** (other critical sectors). 18 sectors in total.
2. **Size-cap rule (Art. 2(1)).** The entity **qualifies as a medium-sized enterprise or exceeds the medium-sized ceilings** under Commission Recommendation 2003/361/EC. Put the other way round: **micro and small enterprises are out by default.**

Size ceilings from Recommendation 2003/361/EC, Annex Art. 2:

| Category | Staff | Turnover | Balance sheet |
|---|---|---|---|
| Micro | < 10 | ≤ €2M | or ≤ €2M |
| Small | < 50 | ≤ €10M | or ≤ €10M |
| Medium | < 250 | ≤ €50M | or ≤ €43M |
| Large | exceeds the medium ceilings | | |

Gotchas on the size test:
- Headcount and financials are counted with **partner (25%+) and linked (majority/control) enterprises** per the Recommendation. A 20-person subsidiary of a large group is usually not "small". Recital 16 lets Member States take an entity's operational independence from its group into account.
- NIS2 disapplies Art. 3(4) of the Recommendation's Annex (the "25% public-body ownership" rule), so publicly owned bodies are sized on their own numbers.

**Size-independent inclusions (Art. 2(2)–(4)):** providers of public electronic communications networks/services, trust service providers, TLD name registries, DNS service providers, domain name registration services, entities that are the **sole provider** of an essential service in a Member State, entities whose disruption would have significant public-safety/health or systemic impact, entities a Member State identifies as critical, central-government public administration, and critical entities under the CER Directive (EU) 2022/2557.

**Out of scope:** public administration in national security, public security, defence or law enforcement (Art. 2(7)); entities exempted from DORA (Art. 2(10)). Where a sector-specific EU act imposes at least equivalent measures and reporting (DORA for finance is the main one), that act takes precedence (Art. 4).

### Annex I: sectors of high criticality (11)
Energy (electricity, district heating/cooling, oil, gas, hydrogen) · Transport (air, rail, water, road) · Banking · Financial market infrastructures · **Health** (healthcare providers, EU reference labs, pharma R&D and manufacturing, critical medical devices) · Drinking water · Waste water · **Digital infrastructure** (IXPs, DNS, TLD registries, cloud computing, data centres, CDNs, trust services, public electronic communications) · **ICT service management (business-to-business)** · Public administration · Space.

### Annex II: other critical sectors (7)
Postal and courier · Waste management · Chemicals · Food (wholesale distribution, industrial production/processing) · Manufacturing (medical devices/IVD, computer/electronic/optical, electrical equipment, machinery, motor vehicles, other transport equipment) · **Digital providers** · Research organisations.

### The two sectors most often misread

**ICT service management (B2B)** (Annex I, point 9) contains exactly two entity types:
- **Managed service provider (MSP)**: Art. 6(39): "an entity that provides services related to the installation, management, operation or maintenance of ICT products, networks, infrastructure, applications or any other network and information systems, via assistance or active administration carried out either on customers' premises or remotely."
- **Managed security service provider (MSSP)**: Art. 6(40): an MSP "that carries out or provides assistance for activities relating to cybersecurity risk management."

The MSP definition is broad. An agency that hosts, operates and maintains client applications under an ongoing arrangement can fall within the *type* of entity. It is still only in scope if it passes the size-cap rule (medium or larger), unless a Member State designates it individually.

**Digital providers** (Annex II, point 6) is **only** three types: providers of **online marketplaces**, **online search engines**, and **social networking services platforms**. "Digital provider" does not mean "any company doing digital work". A web or AI agency is not a digital provider under NIS2. (Cloud, data-centre and CDN providers sit in Annex I "digital infrastructure" instead.)

### Essential vs important (Art. 3)

**Essential entities** (Art. 3(1)):
- (a) Annex I entities that **exceed** the medium-sized ceilings (i.e. large Annex I entities);
- (b) qualified trust service providers, TLD registries and DNS providers, any size;
- (c) public electronic communications providers that are medium-sized;
- (d) central-government public administration;
- (e) other Annex I/II entities a Member State identifies as essential;
- (f) CER critical entities;
- (g) optionally, former NIS1 operators of essential services.

**Important entities** (Art. 3(2)): every other Annex I or II entity in scope. In practice: **medium-sized Annex I entities and all in-scope Annex II entities.** A medium-sized MSP is important; a large MSP is essential.

**Why the category matters:** same Art. 21 and Art. 23 obligations for both. The difference is supervision (essential = ex ante and ex post, Art. 32; important = **ex post only**, triggered by evidence of non-compliance, Art. 33), fine ceilings, and the Art. 32(5) sanctions that apply only to essential entities.

**Jurisdiction (Art. 26):** DNS, TLD, domain registration, cloud, data centres, CDNs, **MSPs, MSSPs**, online marketplaces, search engines and social networks fall under the Member State of their **main establishment** in the EU (where cybersecurity risk-management decisions are predominantly taken). Other entities fall under every Member State where they are established.

---

## Governance and management-body liability (Art. 20)

- Management bodies of essential and important entities must **approve** the Art. 21 risk-management measures, **oversee** their implementation, and **"can be held liable for infringements by the entities of that Article"** (Art. 20(1)). The detailed liability rules are set nationally.
- Members of management bodies are **required to follow training** (Art. 20(2)); entities are encouraged to offer similar training to staff regularly.
- For **essential entities only**, where earlier enforcement fails, authorities can request a court or competent body to **temporarily prohibit any person discharging managerial responsibilities at CEO or legal-representative level from exercising managerial functions** (Art. 32(5)(b)), and to suspend certifications or authorisations (Art. 32(5)(a)). These last until the entity remedies the deficiency.
- Member States must ensure that a natural person who represents or controls an essential entity has the power to ensure its compliance (Art. 32(6)); Art. 33(5) applies Art. 32(6)–(8) to important entities mutatis mutandis.

---

## Cybersecurity risk-management measures (Art. 21)

**Standard (Art. 21(1)):** "appropriate and proportionate technical, operational and organisational measures", taking account of the state of the art, relevant European/international standards, cost of implementation, the entity's exposure, **size**, and the likelihood and severity of incidents. **All-hazards approach**, including physical environment.

**The ten minimum measures (Art. 21(2)):**

1. **(a)** Policies on risk analysis and information system security.
2. **(b)** Incident handling.
3. **(c)** Business continuity, such as backup management and disaster recovery, and crisis management.
4. **(d)** Supply chain security, including security-related aspects concerning the relationships between each entity and its **direct suppliers or service providers**.
5. **(e)** Security in network and information systems acquisition, development and maintenance, including **vulnerability handling and disclosure**.
6. **(f)** Policies and procedures to assess the effectiveness of cybersecurity risk-management measures.
7. **(g)** Basic cyber hygiene practices and cybersecurity training.
8. **(h)** Policies and procedures regarding the use of cryptography and, where appropriate, encryption.
9. **(i)** Human resources security, access control policies and asset management.
10. **(j)** Multi-factor authentication or continuous authentication, secured voice/video/text communications and secured emergency communication systems, where appropriate.

**Supply-chain specifics (Art. 21(3)):** when choosing supply-chain measures, entities must take into account "the vulnerabilities specific to each direct supplier and service provider and the overall quality of products and cybersecurity practices of their suppliers and service providers, including their **secure development procedures**", plus any EU coordinated risk assessments of critical supply chains (Art. 22).

**Corrective duty (Art. 21(4)):** an entity that finds it does not comply must take corrective measures without undue delay.

---

## Implementing Regulation (EU) 2024/2690: digital infrastructure and MSPs

Adopted under Art. 21(5) and 23(11). **Applies to:** DNS service providers, TLD name registries, cloud computing service providers, data centre service providers, CDN providers, **managed service providers, managed security service providers**, providers of online marketplaces, online search engines and social networking platforms, and trust service providers. As a regulation it applies directly, but only to entities that are in NIS2 scope in the first place.

**What it does:**
- Annex sets detailed technical and methodological requirements for each Art. 21(2) point (a)–(j): e.g. 1. security policy; 2. risk management; 3. incident handling (monitoring and logging, event reporting, classification, response, post-incident review); 4. business continuity and backups; 5. supply chain; 6. secure acquisition, SDLC, configuration, change, testing, patch management, network security; and so on.
- Where a requirement applies "where appropriate / where applicable / to the extent feasible" and the entity decides it does not, it **must document its reasoning** (Art. 2(2)).
- **Significant incident criteria (Art. 3):** any one of: direct financial loss above **€500,000 or 5% of annual turnover, whichever is lower**; exfiltration of trade secrets; death; considerable damage to health; a successful, suspectedly malicious and unauthorised access capable of causing severe operational disruption; recurring incidents (Art. 4: at least twice in 6 months, same apparent root cause, jointly meeting the financial threshold); or the entity-type criteria in Arts. 5–14. Scheduled maintenance does not count.
- **MSP/MSSP-specific criteria (Art. 10):** the managed service is completely unavailable for **more than 30 minutes**; availability limited for more than 5% of EU users or 1 million EU users (whichever is smaller) for **more than one hour**; data integrity, confidentiality or authenticity compromised **as a result of suspectedly malicious action**; or compromised with impact on more than 5% / 1 million EU users.

**Supply-chain contract clauses (Annex, point 5.1.4):** in-scope entities must ensure their contracts with suppliers and service providers specify, where appropriate (including via SLAs):
- (a) cybersecurity requirements for the supplier, including for acquisition of ICT services/products;
- (b) awareness, skills, training and, where appropriate, certification requirements for supplier staff;
- (c) background verification of supplier staff;
- (d) an obligation to **notify the entity without undue delay of incidents** that present a risk to the entity's systems;
- (e) **right to audit or right to receive audit reports**;
- (f) an obligation to handle vulnerabilities that present a risk to the entity;
- (g) subcontracting requirements, with the same cybersecurity requirements flowing to subcontractors;
- (h) termination obligations, such as retrieval and disposal of information.

Plus (point 5.2) a maintained **directory of direct suppliers** with contact points and the ICT products/services each provides, and (point 8.1) awareness programmes offered to direct suppliers where appropriate.

**ENISA Technical Implementation Guidance** (v1.0, June 2025) maps each requirement of 2024/2690 to guidance, examples of evidence, and standards mappings. Useful as an audit checklist even for entities outside the regulation's formal scope.

---

## Incident reporting (Art. 23)

**What must be reported:** "significant incidents", meaning an incident that (a) has caused or is capable of causing **severe operational disruption** of the services or **financial loss** for the entity, or (b) has affected or is capable of affecting other natural or legal persons by causing **considerable material or non-material damage** (Art. 23(3)). For the entity types covered by 2024/2690, use the thresholds above.

**To whom:** the national CSIRT or, where applicable, the competent authority. Where appropriate, entities must also notify **the recipients of their services** of significant incidents likely to adversely affect those services (Art. 23(1)), and tell recipients potentially affected by a significant cyber threat what measures they can take (Art. 23(2)).

**Timeline (Art. 23(4)), clock starts on becoming aware of the significant incident:**

| Step | Deadline | Content |
|---|---|---|
| **Early warning** | Without undue delay, **within 24 hours** | Whether suspected unlawful/malicious; whether cross-border impact possible |
| **Incident notification** | Without undue delay, **within 72 hours** | Update of early warning; initial assessment incl. severity, impact and, where available, indicators of compromise |
| **Intermediate report** | On request of CSIRT/authority | Relevant status updates |
| **Final report** | **Not later than one month** after the incident notification | Detailed description, severity and impact; threat type or root cause; applied and ongoing mitigation; cross-border impact |
| **Progress report** | If still ongoing at the one-month mark | Progress report then; final report within one month of handling the incident |

Trust service providers: incidents affecting trust services must be notified within **24 hours** (Art. 23(4) derogation).

The CSIRT/authority must respond within 24 hours of the early warning where possible (Art. 23(5)). "The mere act of notification shall not subject the notifying entity to increased liability" (Art. 23(1)).

**Interaction with GDPR:** a NIS2 incident that is also a personal data breach triggers the separate GDPR Art. 33 notification to the data protection authority. NIS2 authorities must inform the DPA (Art. 35(1)), and cannot fine under NIS2 for the same conduct where the DPA has already fined under GDPR Art. 58(2)(i) (Art. 35(2)).

---

## Fines and enforcement (Arts. 32–34)

| | Essential entities | Important entities |
|---|---|---|
| Supervision | Ex ante + ex post (Art. 32): on-site inspections, regular and targeted audits, security scans, information requests | **Ex post only** (Art. 33), on evidence or indication of non-compliance |
| Max fine for Art. 21/23 breaches | At least **€10M or 2%** of total worldwide annual turnover of the undertaking, whichever higher (Art. 34(4)) | At least **€7M or 1.4%**, whichever higher (Art. 34(5)) |
| Management sanctions | Temporary ban on CEO/legal-representative-level manager; suspension of certification/authorisation (Art. 32(5)) | Not available |
| Other powers | Warnings, binding instructions, orders to comply, orders to inform affected recipients, monitoring officer, public disclosure of infringements (Art. 32(4)) | Same list minus monitoring officer (Art. 33(4)) |

Member States may add periodic penalty payments (Art. 34(6)). Turnover is that of "the undertaking to which the entity belongs", i.e. group-level.

---

## Transposition status (as of 2026-09-29)

- Deadline 17 October 2024 was missed by most Member States. The Commission sent letters of formal notice on **28 November 2024** and reasoned opinions to 19 Member States on **7 May 2025**.
- **July 2026 infringement package (IP/26/1499):** the Commission referred **Ireland, Spain, France and the Netherlands** to the Court of Justice for failing to notify complete transposition, **with a request for financial sanctions** (lump sum plus daily penalties). The press release states that the other Member States had complied ("most complied").
- The Commission's per-country transposition tracker page was last updated 1 July 2025, so it lags; rely on the infringement decisions instead.
- For Ireland specifically see `ireland.md` (National Cyber Security Bill still unpublished at the date of review; NIS1 regime under S.I. 360/2018 remains in force).
- **Practical rule:** until a Member State has transposed, NIS2 obligations are not enforceable against companies there, but clients operating in several Member States are already bound in most of them, and their procurement teams apply NIS2 clauses group-wide.

---

## Pending changes: the 2025–2026 simplification packages

**1. Targeted NIS2 amendments: COM(2026) 13, procedure 2026/0012(COD).** Published by the Commission on 20 January 2026 alongside the proposed Cybersecurity Act revision ("CSA2"). Status: **proposal only.** In Parliament: ITRE lead committee, rapporteur Markéta Gregorová (Greens/EFA); committee draft report PE792.221 tabled **24 September 2026**; stage "Awaiting committee decision". Council progress report discussed 9 June 2026. **Nothing adopted.** Main contents:
- New **small mid-cap** category (defined by Commission Recommendation (EU) 2025/1099: not an SME, fewer than 750 staff, turnover ≤ €150M or balance sheet ≤ €129M). Small mid-caps would "as a main rule" be designated **important**, not essential.
- **Commission guidelines on supply-chain requests** to suppliers, recommending an appropriate level of detail, structure and format, explicitly to "prevent the undue passing on of obligations on entities not in scope". Directly relevant to small suppliers drowning in questionnaires.
- Entities able to demonstrate compliance through **organisational cybersecurity certification** under the European Cybersecurity Certification Framework.
- **Maximum harmonisation** for Art. 21(5) implementing acts; stronger ENISA role for cross-border entities; micro and small DNS providers removed from scope; post-quantum cryptography migration policies in national strategies; harmonised ransomware data collection.
- Proposed transposition window: 12 months after entry into force.

**2. Digital Omnibus: COM(2025) 837, procedure 2025/0360(COD).** Published 19 November 2025. Status: **proposal only**, joint ITRE/LIBE committee, draft report filed 22 June 2026, amendments July 2026, stage "Awaiting committee decision". Relevant to NIS2:
- **Single-Entry Point (SEP)** run by ENISA: one incident report to satisfy NIS2, CER, GDPR breach notification, DORA and eIDAS obligations ("report once, share many"). Per the EPRS briefing (March 2026), SEP obligations would apply 18 months after entry into force (extendable to 24 months).
- **NIS2's 24h / 72h / one-month deadlines are unchanged** by the Omnibus.
- For GDPR (not NIS2) it proposes extending breach notification to **96 hours** and raising the DPA-notification threshold to "likely to result in a **high** risk". Proposal only.
- Six Member States (France, Germany, Italy, Netherlands, Spain, Sweden) opposed the SEP in a joint non-paper (per EPRS).

Neither package changes current obligations. Re-check both procedure files at the next review.

---

## Checklist: is this organisation in scope?

- [ ] Is the organisation's activity an entity type listed in Annex I or II? (Map it to the exact entity type, not the sector label.)
- [ ] Group-level size, counting partner and linked enterprises: medium-sized or larger? If micro/small, out of scope unless one of the Art. 2(2)–(4) size-independent grounds applies.
- [ ] If in scope: essential (large Annex I, or special category) or important (everything else)?
- [ ] Which Member State(s) have jurisdiction (Art. 26 main-establishment rule for MSPs, cloud, digital providers)?
- [ ] Has that Member State transposed? What is the national registration route and deadline?
- [ ] Is a sector-specific regime (DORA) displacing NIS2 under Art. 4?
- [ ] Does Implementing Regulation 2024/2690 apply (entity-type list above)?

## Checklist: minimum evidence for an in-scope entity

- [ ] Management body approval of the risk-management measures, minuted; management training records (Art. 20)
- [ ] Documented policies covering all ten Art. 21(2) measures, with an all-hazards risk assessment
- [ ] Supplier register and supply-chain security policy; security clauses in supplier contracts
- [ ] Incident classification against Art. 23(3) (and 2024/2690 thresholds if applicable); 24h/72h/1-month runbook with named owners
- [ ] Customer-notification procedure for significant incidents and significant cyber threats (Art. 23(1)–(2))
- [ ] Parallel GDPR breach path (72h to the DPA) wired into the same runbook
- [ ] MFA, encryption policy, access control, asset inventory, backups tested, vulnerability handling and disclosure process
- [ ] Periodic effectiveness review (Art. 21(2)(f)); documented reasoning wherever a 2024/2690 "where appropriate" requirement is not applied

---

## Applying this in practice

For a small agency (under 50 staff and under €10M, so a small enterprise) that builds and maintains websites, apps and AI features for clients:

**1. The agency itself is almost certainly not an NIS2 entity.** Even if its hosting-and-maintenance work fits the MSP definition, the size-cap rule excludes small and micro enterprises unless a Member State designates them individually (sole provider, significant systemic impact, etc.). Do not tell clients "we are NIS2-compliant" as if it were a status; say the agency supports clients' NIS2 supply-chain obligations. Re-check the size test if the agency joins a group or passes 50 staff / €10M.

**2. NIS2 reaches the agency through client contracts.** In-scope clients (medium or large healthcare providers, manufacturers, food wholesalers, energy, transport, any medium-plus MSP or cloud provider) must manage supply-chain risk under Art. 21(2)(d) and 21(3), and, if they are 2024/2690 entities, must put specific clauses into supplier contracts (Annex 5.1.4). That is the most common way a small supplier "meets NIS2". Expect and be ready to accept, with sensible limits:
- security requirements schedule (MFA, encryption, patching, secure development, logging);
- **incident notification to the client "without undue delay"**. Push for a concrete window you can actually meet (e.g. initial notice within 24 hours of confirming an incident that affects the client's systems or data), because the client's own 24-hour early-warning clock may start when *you* tell them;
- right to audit, or right to receive audit reports / a completed questionnaire annually (offer the report route first);
- vulnerability handling obligations and timelines;
- flow-down of the same requirements to your subcontractors (hosting, LLM API providers, email, monitoring);
- staff training and, where the client insists, background checks;
- exit clause: return and secure deletion of client data and credentials.

**3. Build a reusable supplier pack once.** A short security statement mapped to the ten Art. 21(2) headings, a subprocessor and hosting list, an incident-response summary with contact points, MFA/access-control and backup descriptions, secure-development practices (code review, dependency scanning, secrets management), and a vulnerability-disclosure contact. This answers most client questionnaires and lines up with the Commission's proposed supply-chain guidelines.

**4. Watch the liability allocation, not just the clauses.** Clients will try to pass their NIS2 fine exposure down. Cap liability, exclude regulatory fines imposed for the client's own failures, and make notification duties conditional on the agency actually becoming aware of an incident affecting the client.

**5. Know which clients are likely in scope.** Sector plus size. A small private clinic or a 20-person online shop is out; a medium-sized private hospital group, medical-device manufacturer, or industrial food producer is in (Annex I health or Annex II). A client that only *runs an online shop* is not a "digital provider"; operating an **online marketplace** for third-party sellers might be, if medium-sized.

**6. Align with GDPR work already done.** The same client usually needs an Art. 28 DPA from the agency. Merge the NIS2 security schedule and the GDPR Art. 32 security annex into one document with one incident-notification clause, so there is a single clock and a single contact path.

**7. Track the simplification packages.** If COM(2026) 13 passes with the supply-chain guidelines, expect standardised supplier questionnaires; if the Digital Omnibus SEP is adopted, client incident reports may move to one ENISA portal. Neither changes anything today.

---

## Sources

- [Directive (EU) 2022/2555 (NIS2), EUR-Lex consolidated HTML](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555): Arts. 2, 3, 6, 20, 21, 23, 26, 27, 32–35, 41, Annexes I–II, recital 16
- [Commission Implementing Regulation (EU) 2024/2690, EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R2690): Arts. 1–4, 10, 16; Annex points 5.1, 5.2, 8.1
- [Commission Recommendation 2003/361/EC (SME definition), EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32003H0361)
- [Commission Recommendation (EU) 2025/1099 (small mid-caps), EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32025H1099)
- [Commission press release IP/26/1499, referral of Ireland, Spain, France and the Netherlands (July 2026)](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1499)
- [Commission, NIS2 transposition in EU countries](https://digital-strategy.ec.europa.eu/en/policies/nis-transposition)
- [COM(2026) 13 final, proposal amending NIS2](https://www.europarl.europa.eu/RegData/docs_autres_institutions/commission_europeenne/com/2026/0013/COM_COM(2026)0013_EN.pdf)
- [EP Legislative Observatory, 2026/0012(COD)](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2026/0012(COD))
- [EP Legislative Train, targeted amendments to NIS2 (updated 01/08/2026)](https://www.europarl.europa.eu/legislative-train/theme-a-new-plan-for-europe-s-sustainable-prosperity-and-competitiveness/file-targeted-amendments-to-the-nis2-directive)
- [EP Legislative Observatory, 2025/0360(COD) Digital Omnibus](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0360(COD))
- [EPRS briefing PE 785.675, "Simplifying cybersecurity reporting" (March 2026)](https://www.europarl.europa.eu/RegData/etudes/BRIE/2026/785675/EPRS_BRI(2026)785675_EN.pdf)
- [ENISA, NIS2 Technical Implementation Guidance](https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance)

**Last reviewed:** 2026-09-29 (primary sources checked this date).
