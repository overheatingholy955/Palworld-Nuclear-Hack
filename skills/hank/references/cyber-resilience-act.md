# CRA: Cyber Resilience Act

**Citation:** Regulation (EU) 2024/2847 on horizontal cybersecurity requirements for products with digital elements. Signed 23 October 2024. In force since December 2024.

**Status on 2026-09-29:** **The reporting obligations have applied since 11 September 2026.** ENISA's Single Reporting Platform (SRP) went live the same day. Everything else (Annex I essential requirements, conformity assessment, CE marking) applies from **11 December 2027**.

**Enforcement:** National market surveillance authorities (product-safety style, not DPAs). Reporting goes to the national CSIRT designated as coordinator plus ENISA. Maximum fine: **€15M or 2.5% of worldwide annual turnover**, whichever is higher (Art. 64(2)).

---

## Key dates (Art. 71, Art. 69)

| Date | What applies |
|---|---|
| 11 Jun 2026 | Chapter IV (Art. 35-51): notification of conformity assessment bodies |
| **11 Sep 2026** | **Art. 14 reporting of actively exploited vulnerabilities and severe incidents. LIVE NOW.** |
| 11 Dec 2027 | Full application: Annex I requirements, conformity assessment, CE marking, everything else |
| 11 Jun 2028 | Old EU type-examination certificates under other harmonisation laws stop being valid (Art. 69(1)) |

**Legacy products (Art. 69(2)-(3)):** products placed on the market before 11 Dec 2027 only fall under the full CRA if they are substantially modified after that date. **But Art. 14 reporting applies to them anyway.** Commission guidance (C(2026) 5252, para. 210) adds that reporting keeps applying after the support period ends, while Part II vulnerability handling does not apply to pre-Dec-2027 products or to products past end of support.

---

## Scope: what is a "product with digital elements"

**Definition (Art. 3(1)):** "a software or hardware product and its remote data processing solutions, including software or hardware components being placed on the market separately."

**Scope trigger (Art. 2(1)):** made available on the EU market, with an intended purpose or reasonably foreseeable use that includes a direct or indirect logical or physical data connection to a device or network.

**"Made available on the market" = supplied in the course of a commercial activity, paid or free** (Art. 3(22)). Recital 15 says commercial activity includes charging for the product, charging for support beyond cost recovery, monetising through a platform, or requiring personal data processing for purposes other than security/compatibility.

### In or out: the practical map

| Thing | CRA? | Basis |
|---|---|---|
| Installed desktop app, mobile app, CLI, SDK, library sold or monetised | **IN** | Guidance paras 18-20, Examples 3-4 |
| Browser extension, Electron-style app installed locally | **IN** | Guidance para 20, Example 4 |
| Firmware / IoT device and its companion cloud | **IN** (cloud as remote data processing) | Recital 12 |
| Pure SaaS / web app used only in a browser | **OUT on its own** | Guidance para 21, Example 5; Recital 12 |
| Progressive web app accessed only through the browser | **OUT on its own** | Guidance para 21 |
| Informational website | **OUT** | Recital 12, Guidance Example 6 |
| Backend API that an in-scope app needs to work, built by or for the manufacturer | **IN as remote data processing solution (RDPS)** | Art. 3(2), Recital 11, Guidance §8 |
| Third-party SaaS the manufacturer plugs into its product (e.g. chat widget) | **Not RDPS**, but treat as a third-party component: risk-assess + due diligence | Guidance paras 200-202, §8.3.1 |
| Medical devices, IVDs, vehicles, certified aviation, marine equipment | **OUT** (own regimes) | Art. 2(2)-(4) |
| National security / defence-only products | **OUT** | Art. 2(7) |
| Non-monetised FOSS, individual contributors | **OUT** | Recital 18 |

**Remote data processing (Art. 3(2)):** processing "at a distance" whose software is designed and developed by or under the responsibility of the manufacturer, and without which the product could not perform one of its functions. Both tests must be yes (Guidance para 202). Who operates it does not matter; who designed it does (para 196). IaaS/PaaS-hosted code you wrote can be RDPS; a third-party SaaS you licence is not (paras 198-200).

**SaaS is covered by NIS2, not the CRA.** Recital 12 says so explicitly: NIS2 applies to cloud computing services including SaaS, PaaS, IaaS, for providers that are medium-sized or larger.

**Worked example from the guidance (§8.3.1, mobile banking app):** the app is the product. The bank's API gateway the app talks to is RDPS and in scope. The ledger and account systems behind it are not RDPS (the app does not talk to them directly) but must still be covered in the risk assessment. A third-party chat SaaS embedded in the app is a component, not RDPS.

---

## Roles

- **Manufacturer** (Art. 3(13)): develops or has developed a product and markets it under its own name or trademark, paid or free. Carries almost all obligations.
- **Importer / distributor** (Art. 3(16)-(17), Art. 19-20): verification and cooperation duties.
- **Open-source software steward** (Art. 3(14), Art. 24): a legal person (foundation, company) that systematically supports FOSS intended for commercial activities on a sustained basis. Light-touch regime:
  - Documented cybersecurity policy covering vulnerability handling (Art. 24(1)).
  - Cooperate with market surveillance authorities (Art. 24(2)).
  - Art. 14(1) reporting of actively exploited vulnerabilities to the extent involved in development; Art. 14(3) incident reporting only for their own development infrastructure (Art. 24(3)).
  - **No fines for stewards** (Art. 64(10)(b)). Cannot affix CE marking (Recital 19).
- **Hosting on GitHub / npm / PyPI** is not itself making available on the market (Recital 20).
- **FOSS integrated by a manufacturer:** the manufacturer owns due diligence on that component (Art. 13(5)) and must report vulnerabilities it finds upstream and share fixes (Art. 13(6)).

---

## Manufacturer obligations (Art. 13 + Annex I)

### Process obligations (Art. 13)

- **Cybersecurity risk assessment**, documented, updated during the support period, in the technical file (Art. 13(2)-(4)).
- **Due diligence on third-party components**, including FOSS (Art. 13(5)).
- **Support period** at least **5 years**, unless expected use is shorter (Art. 13(8)). Guidance para 126: 5 years is a floor, **not a default**. Longer-lived products need longer support.
- End date of support (month + year) shown at time of purchase (Art. 13(19)).
- Each security update stays available for **10 years** or the rest of the support period, whichever is longer (Art. 13(9)).
- For software: may only patch the latest version if users can upgrade free and without extra costs (Art. 13(10); Guidance paras 129-131). Each substantially modified version needs its own declared support period.
- **Single point of contact** for vulnerability reports; cannot be automated-only (Art. 13(17)).
- Technical documentation + EU declaration of conformity kept **10 years** or the support period, whichever is longer (Art. 13(13)).
- Tell authorities and users before ceasing operations (Art. 13(23)).

### Annex I Part I: product properties

Based on the risk assessment, the product must:
- (a) ship **without known exploitable vulnerabilities**
- (b) be **secure by default**, with reset to original state
- (c) support security updates, **automatic by default where applicable**, with opt-out
- (d) protect against unauthorised access (authn, identity/access management)
- (e) encrypt data at rest and in transit with state-of-the-art mechanisms
- (f) protect integrity of data, commands, programs, config
- (g) data minimisation
- (h) protect availability, including DoS resilience
- (i) not degrade other devices/networks
- (j) limit attack surface
- (k) exploitation mitigation
- (l) security logging and monitoring, with user opt-out
- (m) secure, permanent deletion of user data and settings

### Annex I Part II: vulnerability handling

1. **SBOM** in a commonly used, machine-readable format, covering **at least top-level dependencies**. The Commission may set format by implementing act (Art. 13(24)).
2. Remediate without delay; security updates separate from feature updates where feasible.
3. Regular security testing and review.
4. Publicly disclose fixed vulnerabilities once a fix is out (may delay in justified cases).
5. **Coordinated vulnerability disclosure (CVD) policy.**
6. Contact address for vulnerability reports.
7. Secure update distribution, automatic where applicable.
8. Security updates free of charge (unless agreed otherwise for tailor-made B2B products), with advisories.

---

## Art. 14 reporting (live since 11 Sep 2026)

**What triggers it:**
- **Actively exploited vulnerability**: reliable evidence a malicious actor exploited it without permission (Art. 3(42)). Not every CVE; only exploited ones.
- **Severe incident** affecting product security (Art. 14(5)): affects the ability to protect availability, authenticity, integrity or confidentiality of sensitive or important data or functions, OR has led or could lead to malicious code in the product or in users' systems.

**Clock (from becoming aware):**

| Step | Actively exploited vulnerability | Severe incident |
|---|---|---|
| Early warning | **24 hours** | **24 hours** (include whether malicious/unlawful suspected) |
| Notification | **72 hours** | **72 hours** |
| Final report | **14 days after a fix or mitigation is available** | **1 month after the 72h notification** |

**"Becoming aware"** (Guidance paras 211-214, aligned with NIS2 implementing reg 2024/2690 and EDPB breach guidelines): when, after prompt initial assessment, the manufacturer has a reasonable degree of certainty. The emphasis is on starting that assessment immediately.

**Where:** via the ENISA **Single Reporting Platform** (portal.cra-srp.enisa.europa.eu), using the endpoint of the CSIRT in the member state of the manufacturer's main EU establishment (where cybersecurity decisions are mainly taken). Non-EU manufacturers follow the fallback order in Art. 14(7): authorised representative, then importer, then distributor, then the state with the most users.

**Also:** inform impacted users, in machine-readable format where appropriate (Art. 14(8)). Micro and small enterprises cannot be fined for missing the **24h early warning** specifically (Art. 64(10)(a)); the 72h and final report deadlines still bind them. Reporting alone does not create extra liability (Art. 17(4)). CSIRTs provide helpdesk support, especially to SMEs (Art. 17(6)).

---

## Important and critical products (Art. 7-8, Annex III-IV)

Classification is by **core functionality**. Integrating an important component does not make the whole product important (Art. 7(1)).

**Class I (Annex III)** includes: identity management and privileged access management; browsers; password managers; anti-malware; VPNs; network management systems; SIEM; boot managers; PKI software; network interfaces; operating systems; routers/modems/switches; security-relevant microprocessors/microcontrollers/ASIC/FPGA; smart home virtual assistants; smart home security products; connected toys; health or children's wearables.

**Class II (Annex III)**: hypervisors and container runtimes; firewalls and IDS/IPS; tamper-resistant microprocessors and microcontrollers.

**Critical (Annex IV)**: hardware security boxes; smart meter gateways and secure cryptoprocessing devices; smartcards and secure elements.

Technical descriptions of each category: **Commission Implementing Regulation (EU) 2025/2392** (28 Nov 2025).

**AI note:** plain AI apps, chatbots and LLM wrappers are not listed categories. They are default-class products if installed or distributed as software. An AI agent sold as an identity/access tool or SIEM would pick up that class.

---

## Conformity assessment (Art. 32)

| Product class | Allowed route |
|---|---|
| Default (most software) | **Self-assessment** (Module A, internal control), or B+C, H, or an EU scheme |
| Class I | Self-assessment **only if** harmonised standards / common specs / EU scheme applied in full. Otherwise third-party (B+C or H) |
| Class II | Third-party mandatory (B+C, H, or EU scheme at "substantial") |
| Critical | EU cybersecurity certificate where a delegated act requires it, otherwise Class II routes |

FOSS in Class I/II may self-assess if the technical documentation is public (Art. 32(5)). SME fees must be proportionate (Art. 32(6)). The Commission expects the first standardisation deliverables in Q3 2026 and more by 30 Oct 2027.

---

## Fines (Art. 64)

| Breach | Max |
|---|---|
| Annex I essential requirements, Art. 13 (manufacturer), **Art. 14 (reporting)** | **€15M or 2.5%** worldwide turnover |
| Other operator obligations, CE marking, docs, conformity procedure, notified-body rules | €10M or 2% |
| Incorrect / misleading info to authorities or notified bodies | €5M or 1% |

Member states set the actual penalty rules. Size and SME status must be taken into account (Art. 64(5)(c)).

---

## Interaction with other regimes

- **AI Act (Art. 12 CRA):** a high-risk AI system that is also a CRA product is **deemed compliant with AI Act Art. 15 cybersecurity** if it meets Annex I Parts I and II and the CRA declaration of conformity says so. AI Act conformity assessment (Art. 43 AI Act) governs, except Class I/II/critical products under AI Act internal control, which follow CRA procedures for the cyber part. AI Act high-risk timelines: see `eu-ai-act.md` (not re-verified here).
- **NIS2:** covers SaaS/cloud as services (Recital 12). CRA "incident" and "near miss" reuse NIS2 definitions (Art. 3(43), (45)). A vendor can be under both: NIS2 for its service operations, CRA for the installable product.
- **DORA:** a financial entity that ships a mobile banking app is a CRA manufacturer for that app (Guidance §8.3.1). DORA governs the entity's ICT risk; CRA governs the product.
- **GDPR:** Annex I Part I (e), (g), (m) overlap with Art. 25 and 32 GDPR. A severe incident can also be a personal data breach. Separate clocks, separate recipients.
- **Digital Omnibus (COM(2025) 837, procedure 2025/0360/COD):** proposes a single-entry point for incident reporting built on the CRA SRP. **Still "Ongoing" on EUR-Lex on 2026-09-29. Not law.**

---

## Implementing acts, delegated acts and guidance (2025-2026)

| Date | Act | Content |
|---|---|---|
| 28 Nov 2025 | Implementing Regulation (EU) 2025/2392 | Technical descriptions of important and critical product categories |
| Adopted 11 Dec 2025 | Delegated Regulation (EU) 2026/881 | When CSIRTs may delay disseminating notifications (Art. 14(9) / 16(2)). Commission page listed it as "publication pending objection period"; final OJ publication date UNVERIFIED |
| 27 Jul 2026 | Commission guidance C(2026) 5252 + annex | Scope (incl. RDPS and FOSS), substantial modification, support period, reporting, risk assessment. 67 examples. Non-binding |
| 11 Sep 2026 | ENISA SRP launch | Initial operating capability; ENISA says it will expand features "over the coming months" |
| Q4 2026 (planned) | Delegated act | EUCC presumption of conformity with the CRA (Commission roadmap) |
| Not yet adopted | SBOM format implementing act (Art. 13(24)) | Optional power; none found this session: UNVERIFIED |

---

## Applying this in practice

For a small software or AI supplier. Decide scope per product line, not per company.

**Step 1: are we a manufacturer of a CRA product?**
- [ ] List every artefact shipped to customers: installers, mobile apps, desktop apps, browser extensions, SDKs, CLIs, on-prem containers, self-hosted agents, plugins, MCP servers distributed as packages.
- [ ] Browser-only SaaS with no installable client: **out of the CRA on its own.** Check NIS2 instead (medium-sized or larger cloud provider).
- [ ] SaaS with an installable client (mobile app, desktop app, extension, on-prem connector): **the client is the product and the backend it needs is RDPS.** Both in scope.
- [ ] Bespoke software built for one client under contract: likely the client is the manufacturer if it markets it under its own name (Art. 3(13) "has products designed, developed"). If we market it under our name, we are. Confirm per contract. (Hank's reading of the definition, not stated in the guidance.)
- [ ] Open-source repos: out if not monetised. If we monetise them (paid support beyond cost, paid tier, data-for-access), we are a manufacturer for them.

**Step 2: reporting, now (in force since 11 Sep 2026)**
- [ ] Register on the ENISA SRP and name primary + backup reporters before anything happens.
- [ ] Identify our coordinating CSIRT (main EU establishment; for an Irish company, Ireland's national CSIRT).
- [ ] Write a runbook: triage → "reasonable certainty" decision → 24h early warning → 72h notification → final report. Log the awareness timestamp.
- [ ] Map overlaps: the same event may also be a GDPR breach (72h to the DPA), a NIS2 significant incident, or a DORA major incident for a financial-entity client. Different recipients, different clocks.
- [ ] User notification template (Art. 14(8)).
- [ ] Applies to products already on the market today, even though Annex I does not bite until Dec 2027.

**Step 3: by 11 Dec 2027**
- [ ] Documented cybersecurity risk assessment per product.
- [ ] SBOM generated in CI (CycloneDX or SPDX), top-level dependencies at minimum, full tree preferred.
- [ ] Zero known exploitable vulns at release: dependency scanning gate in CI, documented exceptions.
- [ ] CVD policy published + `security.txt` + single point of contact.
- [ ] Declared support period (≥5 years unless justified shorter) with month/year end date shown at purchase.
- [ ] Security updates separable from feature updates, free, with advisories; auto-update on by default where applicable.
- [ ] Secure defaults, encryption, access control, logging, full data wipe.
- [ ] Check Annex III: if a product's core function is identity/access, password management, VPN, SIEM, network management, it is Class I and may need a notified body unless harmonised standards are applied in full.
- [ ] Technical file + EU declaration of conformity + CE marking, kept 10 years.

**AI-specific notes**
- An LLM feature inside an installable product is part of the product. Prompt injection leading to code execution in the user's environment is squarely a "severe incident" candidate (Art. 14(5)(b)).
- The model API we call (Anthropic, OpenAI) is a third-party SaaS, not our RDPS. Treat it as a component: risk-assess, due diligence, isolate.
- If a product is also a high-risk AI system, doing CRA Annex I properly gives presumption of conformity for AI Act Art. 15 cybersecurity (Art. 12 CRA).

---

## Common misreadings

1. **"CRA starts in 2027."** Reporting started 11 Sep 2026 and covers products already on the market.
2. **"All SaaS is in scope."** Browser-only SaaS is not a product with digital elements. Its backend is only caught as RDPS of an in-scope product.
3. **"All SaaS is out of scope."** The backend of an in-scope app is caught as RDPS if you designed it.
4. **"Five years support is the standard."** It is a floor, and the Commission says it is not a default.
5. **"Report every CVE."** Only actively exploited vulnerabilities and severe incidents are mandatory. Others are voluntary (Art. 15).
6. **"Open source is exempt."** Only if not monetised. Stewards have light duties; integrating manufacturers carry full responsibility for components.
7. **"The Digital Omnibus changed CRA reporting."** It is a proposal, still ongoing.

---

## Sources

- [Regulation (EU) 2024/2847, official text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng): Art. 2, 3, 7, 8, 12, 13, 14, 16, 17, 24, 32, 64, 69, 71; Annex I, III, IV; Recitals 11-20
- [European Commission: CRA implementation page (last update 27 Jul 2026)](https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation): timeline, implementing/delegated acts
- [European Commission: guidance publication, 27 Jul 2026](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation)
- [Commission guidance C(2026) 5252 annex (PDF)](https://ec.europa.eu/newsroom/dae/redirection/document/131456): §2.2, §2.7, §5, §8, §9.1
- [European Commission: CRA reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)
- [ENISA: The CRA Single Reporting Platform is launched (11 Sep 2026)](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched)
- [ENISA: Single Reporting Platform page + FAQ](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)
- [EUR-Lex procedure 2025/0360/COD (Digital Omnibus): status "Ongoing"](https://eur-lex.europa.eu/procedure/EN/2025_360)
- [EPRS briefing: Digital Omnibus Single-Entry Point (March 2026)](https://www.europarl.europa.eu/RegData/etudes/BRIE/2026/785675/EPRS_BRI(2026)785675_EN.pdf)

**Last reviewed:** 2026-09-29 (primary sources checked this date).
