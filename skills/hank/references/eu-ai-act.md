# EU AI Act: Regulation (EU) 2024/1689

**Citation:** Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). Published OJ L, 2024/1689, **12.7.2024**. Entered into force **1 August 2024**. **Amended by Regulation (EU) 2026/1744** (Digital Omnibus on AI) of 8 July 2026, OJ L, 2026/1744, 24.7.2026, in force **27 July 2026**. Always read the consolidated text.

**Enforcement:** national market surveillance authorities per Member State; the **AI Office** (Commission) for GPAI models and, since the Omnibus, for AI systems built on a GPAI model by the same provider and AI systems in/constituting VLOPs/VLOSEs (Art. 75(1) as amended, with carve-outs where national authorities stay competent: Annex I products, critical infrastructure, law enforcement, border management, financial institutions, administration of justice). Maximum fines (Art. 99): **€35M or 7%** of global annual turnover for prohibited practices; **€15M or 3%** for most other obligations (incl. high-risk and Art. 50 transparency); **€7.5M or 1%** for incorrect/misleading information to authorities. For **SMEs/start-ups and, since the Omnibus, small mid-caps (SMCs)**, the lower of the two amounts applies (Art. 99(6), new 99(6a)). GPAI provider fines (Art. 101): up to €15M or 3%, enforceable from 2 Aug 2026.

---

## Scope: who it applies to

**Extraterritorial.** Applies to (Art. 2(1)):

1. **Providers** placing AI systems or GPAI models on the EU market or putting AI systems into service in the EU, **regardless of where the provider is established**
2. **Deployers** of AI systems established or located in the EU
3. **Providers + deployers outside the EU** where the AI system's output is used in the EU
4. **Importers, distributors, product manufacturers**, authorised representatives, affected persons in the EU

**Excluded (Art. 2(3)–(12)):** military/defence/national security; AI developed and used solely for scientific R&D; R&D/testing before placing on the market (real-world testing excepted); purely personal non-professional use; **AI systems under free and open-source licences, unless** placed on the market as high-risk, falling under Art. 5, or subject to Art. 50. (GPAI models under open-source licences get partial relief under Art. 53(2), but not if they carry systemic risk.)

**Definition of "AI system" (Art. 3(1))**: see Commission Guidelines on the AI system definition (6 Feb 2025). Plain rule-based software without inference generally falls outside.

---

## The four risk tiers

### Tier 1: Unacceptable risk (PROHIBITED, Art. 5)

Applies since **2 February 2025.** Original eight prohibited practices:

1. Subliminal, manipulative or deceptive techniques materially distorting behaviour and causing significant harm
2. Exploiting vulnerabilities (age, disability, social/economic situation) causing significant harm
3. Social scoring (by public **or private** actors) leading to detrimental/unjustified treatment
4. Predicting criminal-offence risk based solely on profiling or personality traits
5. Untargeted scraping of facial images from the internet/CCTV to build facial recognition databases
6. Emotion recognition in workplaces + education institutions (except medical or safety reasons)
7. Biometric categorisation to infer race, political opinions, trade union membership, religious/philosophical beliefs, sex life or sexual orientation
8. Real-time remote biometric identification in publicly accessible spaces for law enforcement (narrow exceptions)

**Added by Reg. (EU) 2026/1744, applies from 2 December 2026:**
- **Art. 5(1)(ba)**: AI systems that generate or manipulate realistic images, video, audio or similar material of an identifiable person's intimate parts or of an identifiable person engaged in sexually explicit activities **without that person's explicit consent** ("nudification").
- **Art. 5(1)(bb)**: AI systems that generate or manipulate child sexual abuse material (Directive 2011/93/EU).
- **Art. 5(1a)** scope rule: placing on the market is prohibited only if that output is the **intended purpose**, or is a **reasonably foreseeable and reproducible outcome** without significant modification **and** the system lacks reasonable and adequate safeguards to reliably prevent it (and to correct observed misuse). Use is prohibited only where the deployer uses the system for that purpose. Art. 5(1b): edits that don't increase exposure of intimate parts don't count.

Guidance: Commission Guidelines on prohibited AI practices (February 2025; non-binding).

### Tier 2: High-risk

The compliance-heavy tier. Two paths (Art. 6):

**Path A: Annex III use cases** (stand-alone high-risk):
1. **Biometrics** (remote identification, categorisation by sensitive attributes, emotion recognition, outside the prohibited contexts)
2. **Critical infrastructure** (safety components for critical digital infrastructure, road traffic, water, gas, heating, electricity)
3. **Education + vocational training** (admission, evaluation, steering learning, proctoring)
4. **Employment + workers management** (recruitment, candidate filtering, targeted job ads, promotion/termination decisions, task allocation, monitoring)
5. **Essential private + public services** (public benefits eligibility, creditworthiness/credit scoring, life/health insurance risk + pricing, emergency call triage)
6. **Law enforcement**
7. **Migration, asylum, border control**
8. **Administration of justice + democratic processes** (judicial decision support, influencing elections)

**Art. 6(3) filter:** an Annex III system is *not* high-risk if it doesn't pose a significant risk of harm (narrow procedural task, improving a prior human activity, detecting patterns without replacing human assessment, preparatory task). Never available if the system profiles natural persons. The provider must document the assessment before placing on the market and **register** the system (Art. 49(2)); the Omnibus kept registration but slimmed Annex VIII Section B (points 7 and 9 deleted).

**Path B: Annex I products** (Art. 6(1)): AI that is a safety component of, or is itself, a product under listed EU harmonisation legislation requiring third-party conformity assessment (medical devices, toys, lifts, radio equipment, etc.). The Omnibus narrowed this: AI used solely for non-safety user assistance, performance optimisation, efficiency, automation, convenience or quality control is **not** a safety component (new Art. 6(1a)–(1c)); **machinery** moved from Annex I Section A to Section B (handled via the Machinery Regulation instead); a new Art. 2(13) lets delegated acts limit duplicative AI Act requirements where sectoral law already covers them (delegated acts due by 2 Aug 2027).

**High-risk provider obligations** (apply from the dates in the timeline below):
- Risk management system (Art. 9): lifecycle-long
- Data + data governance (Art. 10): quality, relevance, bias controls on training/validation/test sets. Special-category data for bias detection now sits in **new Art. 4a** (Omnibus), with strict conditions (necessity, no synthetic/anonymised alternative, pseudonymisation, no third-party access, deletion, ROPA justification); Art. 4a(2) extends the permission to other AI systems/models and deployers.
- Technical documentation (Art. 11 + Annex IV): **SMEs and SMCs may use a simplified form** (Commission to publish)
- Automatic event logging (Art. 12)
- Transparency + instructions to deployers (Art. 13)
- Human oversight (Art. 14)
- Accuracy, robustness, cybersecurity (Art. 15): deemed met for cybersecurity where CRA (Reg. 2024/2847) essential requirements are met (new Art. 42(3))
- Quality management system (Art. 17): proportionate to size, esp. SMEs/SMCs
- Conformity assessment (Art. 43), EU declaration of conformity + CE marking (Arts. 47, 48)
- Registration in EU database (Arts. 49, 71)
- Post-market monitoring (Art. 72), serious incident reporting (Art. 73)

**Value chain (Art. 25, as amended):** when a deployer/distributor becomes the provider (e.g. substantial modification, own branding, repurposing into high-risk), the initial provider must cooperate (technical documentation, known limitations/failure modes, targeted technical access) unless it clearly specified the system is not to be turned into high-risk. Suppliers of components/models to a high-risk provider must agree the needed information in writing (Art. 25(4)); breaches now fall under Art. 99(4)(da) fines.

**Deployer obligations** (Art. 26): use per instructions, assign competent human oversight, monitor, keep logs, ensure input data relevance, inform workers/affected persons, and **Fundamental Rights Impact Assessment (Art. 27)** where applicable.

**Legacy systems (Art. 111(2) as amended):** high-risk systems placed on the market before the relevant Chapter III application date are covered only if significantly changed in design after that date; systems intended for public authorities must comply by **2 August 2030**.

### Tier 3: Transparency obligations (Art. 50)

Apply from **2 August 2026** (unchanged by the Omnibus):
- **Providers, AI interacting with people**: design so people are informed they are interacting with an AI system, unless obvious from context (Art. 50(1))
- **Providers, synthetic content** (audio, image, video, text): outputs marked in a **machine-readable format and detectable** as AI-generated/manipulated (Art. 50(2)). **Grace period:** systems placed on the market **before 2 Aug 2026** must comply by **2 December 2026** (new Art. 111(4); Council describes this as cutting the originally proposed 6-month grace to 3 months)
- **Deployers, emotion recognition / biometric categorisation**: inform exposed persons (Art. 50(3))
- **Deployers, deepfakes**: disclose that content is artificially generated/manipulated (lighter touch for evidently artistic/satirical works) (Art. 50(4))
- **Deployers, AI-generated text published to inform the public on matters of public interest**: disclose, unless human review/editorial control and editorial responsibility (Art. 50(4))

**Guidance (both published, non-binding):**
- **Code of Practice on Transparency of AI-generated Content**: final published **10 June 2026**; Section 1 providers (marking + detection), Section 2 deployers (labelling deepfakes and AI text). Voluntary. The amended Art. 50(7) lets the Commission assess its adequacy and, if inadequate, adopt implementing acts with common rules. Whether a formal adequacy assessment has been issued: **UNVERIFIED**.
- **Commission Guidelines on Art. 50 transparency obligations**: C(2026) 5054, **20 July 2026**.

### Tier 4: Minimal / no risk

Everything else. No AI Act obligations beyond Art. 4 AI literacy (for providers/deployers). Voluntary codes of conduct encouraged (Art. 95).

---

## AI literacy (Art. 4)

Applies since 2 Feb 2025. **Rewritten by the Omnibus (in force 27 Jul 2026):** providers and deployers "shall take measures to support the development of AI literacy" of their staff and others operating AI on their behalf, considering their knowledge, experience, training and context. It expressly **does not require guaranteeing any specific level of literacy** of any individual. The Commission and Member States must support compliance, especially for SMEs, and the Commission will publish practical examples. The obligation was softened, not removed: evidence of measures taken is still needed.

---

## General-Purpose AI (GPAI) models: separate regime (Chapter V)

Applies since **2 August 2025.** Commission enforcement powers (incl. Art. 101 fines) from **2 August 2026.** Models placed on the market **before 2 Aug 2025** must comply by **2 August 2027** (Art. 111(3)).

**All GPAI model providers must (Art. 53):**
- Maintain technical documentation (Annex XI) and provide information to downstream providers (Annex XII)
- Put in place a copyright-compliance policy (incl. respecting text-and-data-mining opt-outs)
- Publish a sufficiently detailed summary of training content (Commission template, July 2025)

**GPAI with systemic risk** (presumed above 10^25 FLOPs training compute, or designated) (Art. 55):
- Model evaluation incl. adversarial testing; systemic risk assessment + mitigation; serious incident reporting; adequate cybersecurity

**Supporting instruments:**
- **General-Purpose AI Code of Practice**: published **10 July 2025**; three chapters (Transparency, Copyright, Safety & Security); Commission and AI Board assessed it as an adequate voluntary tool (1 Aug 2025). The amended Art. 56(6) requires the Commission to publish its adequacy assessment.
- **Guidelines on the scope of obligations for GPAI providers**: **18 July 2025** (what counts as a GPAI model, who is a provider, modifications, open-source exemptions).
- **Training-data summary template**: July 2025.

**Downstream integrators** (building products on third-party GPAI) are not GPAI model providers unless they substantially modify the model (see the GPAI guidelines for the compute-based modification threshold). They are still **AI system providers/deployers** with their own Art. 50, Art. 4 and (if applicable) high-risk obligations.

---

## Application timeline (verified against Reg. 2024/1689 Art. 113 and Reg. 2026/1744, 2026-09-29)

| Date | What applies |
|---|---|
| 1 Aug 2024 | AI Act entered into force |
| 2 Feb 2025 | Chapters I + II: definitions, **AI literacy (Art. 4)**, **prohibited practices (Art. 5)** |
| 2 Aug 2025 | Notified bodies (Ch. III Sec. 4), **GPAI obligations (Ch. V)**, **governance (Ch. VII)**, **penalties regime (Ch. XII, except Art. 101)**, confidentiality (Art. 78); Member States to designate authorities + lay down penalty rules |
| 27 Jul 2026 | **Digital Omnibus on AI (Reg. 2026/1744) in force**; amended Art. 4 AI literacy, SMC relief, AI Office powers etc. take effect |
| 2 Aug 2026 | **General application date**: **Art. 50 transparency**, Art. 101 GPAI fines / Commission GPAI enforcement, remaining provisions not otherwise dated |
| **2 Dec 2026** | **New prohibitions Art. 5(1)(ba)/(bb)** (non-consensual intimate content, CSAM); deadline for Art. 50(2) marking for generative systems placed on the market before 2 Aug 2026 |
| 2 Aug 2027 | GPAI models placed on the market before 2 Aug 2025 must comply; national AI regulatory sandboxes operational (moved from 2 Aug 2026) |
| **2 Dec 2027** | **High-risk, Annex III (Art. 6(2))**: Chapter III Sections 1–3 apply (was 2 Aug 2026) |
| **2 Aug 2028** | **High-risk, Annex I products (Art. 6(1))** (was 2 Aug 2027) |
| 2 Aug 2030 | Legacy high-risk systems used by public authorities must comply |

**How the Omnibus got here:** Commission proposal COM(2025) 836, 19 Nov 2025 → Council mandate 13 Mar 2026 → **provisional political agreement 7 May 2026** → Parliament plenary vote → **Council final adoption 29 Jun 2026** → signed 8 Jul 2026 → OJ 24 Jul 2026 → in force 27 Jul 2026. The high-risk dates are **fixed**, not linked to standards availability (the Commission's original proposal had proposed a standards-linked trigger; the final text sets fixed dates). The date of the EP plenary vote was not individually verified.

---

## Guidance + standards status (as of 2026-09-29)

| Instrument | Status |
|---|---|
| Guidelines on AI system definition | Published 6 Feb 2025 |
| Guidelines on prohibited practices | Published February 2025 |
| GPAI Code of Practice | Published 10 Jul 2025; assessed adequate |
| GPAI provider guidelines | Published 18 Jul 2025 |
| Transparency Code of Practice (Art. 50) | Final published 10 Jun 2026 |
| Art. 50 guidelines | Adopted 20 Jul 2026 (C(2026) 5054) |
| High-risk classification guidelines (Art. 6(5)) | **Draft only.** Legal deadline was 2 Feb 2026 (missed); draft published, targeted consultation closed 23 Jul 2026; final expected by end 2026 (Commission page, not independently confirmed) |
| Harmonised standards (CEN-CENELEC JTC 21, M/593 + M/613) | CEN/CENELEC adopted exceptional acceleration measures in Oct 2025 targeting key deliverables by **Q4 2026**. **EN 18286:2026** (QMS for AI Act regulatory purposes) **published July 2026**, the first AI Act standard. **No AI Act harmonised standard cited in the OJ found**, so no presumption of conformity yet (Art. 40). Other deliverables (risk management, data quality, logging, accuracy, robustness, cybersecurity, conformity assessment): in progress; exact status **UNVERIFIED** |
| Simplified technical documentation form (SME/SMC) + FRIA questionnaire template | Required by the Omnibus; publication **UNVERIFIED** |

---

## Conformity assessment paths (high-risk)

1. **Internal control (Annex VI)**: provider self-assesses. Default for Annex III points 2–8.
2. **Notified body (Annex VII)**: QMS + technical documentation assessed by a third party. Required for **Annex III point 1 (biometrics)** where the provider hasn't fully applied harmonised standards/common specifications. For Annex I products, follow the sectoral procedure (Art. 43(3) as amended); sectoral notified bodies must apply for AI Act designation by 28 Jan 2028.

Output: **EU declaration of conformity** + **CE marking** + registration in the **EU database** (Art. 71).

---

## Fundamental Rights Impact Assessment (FRIA, Art. 27)

Required before first use, for **deployers** of Annex III high-risk systems (except point 2, critical infrastructure) that are **bodies governed by public law or private entities providing public services**, and for **all deployers** of systems under Annex III **point 5(b) (creditworthiness/credit scoring)** and **5(c) (life/health insurance risk + pricing)**. Covers:
- Deployer's processes in which the system is used
- Period + frequency of use
- Categories of natural persons affected
- Specific risks of harm
- Human oversight measures
- Measures if risks materialise (incl. governance + complaints)

The Omnibus lets the FRIA **cross-reference or reuse the GDPR DPIA** (Art. 27(4)) and requires the AI Office to provide a questionnaire template, including an automated tool (Art. 27(5)).

---

## EU AI Act vs other frameworks

| | EU AI Act | ISO/IEC 42001 | NIST AI RMF |
|---|---|---|---|
| Mandatory? | Yes (in EU) | Voluntary | Voluntary |
| Geography | EU + extraterritorial | Global | US-rooted, global use |
| Scope | AI systems + GPAI models on EU market | AI management system | AI risk management |
| Risk model | Fixed tiers | Org-defined | Org-defined |
| Penalty? | Up to €35M / 7% turnover | Loss of cert | None |
| Audit? | Notified body for some | Accredited cert body | Self-assessment |

**Stack play:** ISO 42001 (management system) + NIST AI RMF (risk method) + AI Act conformity for in-scope systems. Note that EN 18286 (not ISO 42001) is the European QMS standard written for AI Act Art. 17. ISO 42001 certification alone gives no presumption of conformity.

---

## Common EU AI Act mistakes (Hank's reviewer lens)

1. **"We use Anthropic/OpenAI so we're fine."** GPAI provider compliance covers their Chapter V duties only. Integrators have their own provider/deployer obligations.
2. **No AI literacy evidence (Art. 4).** Softened by the Omnibus ("take measures to support"), but still an obligation since Feb 2025.
3. **Chatbot without an AI-interaction notice.** Art. 50(1) applies from 2 Aug 2026.
4. **Synthetic content not machine-readably marked (Art. 50(2)).** Needs watermarking/metadata/provenance (e.g. C2PA-style) per the Transparency Code. Existing generative systems: deadline 2 Dec 2026.
5. **Annex III classification missed.** Employment covers CV screening, candidate filtering, targeted job ads, task allocation and monitoring.
6. **Relying on Art. 6(3) without documentation + registration.** The exemption needs a written assessment and EU-database registration.
7. **Treating the delay as cancellation.** High-risk moved to 2 Dec 2027 / 2 Aug 2028 (fixed), but prohibitions, AI literacy, GPAI and Art. 50 already apply, and the new nudification/CSAM prohibitions apply from 2 Dec 2026.
8. **Generative image/video tools without safeguards against intimate deepfakes.** Under Art. 5(1a), a general-purpose image tool can fall under the new prohibition if such output is reasonably foreseeable and reproducible and it lacks reasonable and adequate safeguards.
9. **GPAI copyright stance unclear.** Art. 53(1)(c): choose providers that publish copyright policies and training-data summaries.

---

## Applying this in practice

For a team that builds AI features on top of general-purpose models (Claude, GPT, Gemini) for itself or for clients.

**Your role.** Integrating a GPAI model through an API does not make you a GPAI model provider. It does make you the provider of an AI system when you ship it under your name, with Art. 4 and Art. 50 duties, and high-risk duties if the use case falls in Annex III. The client using what you built is normally the deployer.

**Per product**

- [ ] Tier assigned (prohibited, high-risk, transparency, minimal)
- [ ] If an Annex III area is touched: Art. 6(3) assessment written and registration planned, or the full high-risk path
- [ ] Provider obligations checked against the current build
- [ ] Gap list with a remediation plan against the applicable deadline

**Per client deployment with AI features**

- [ ] Tier assigned (most chatbots, agents and content generation land in the transparency tier)
- [ ] If high-risk: stop and scope the full conformity workload and cost with the client before building further
- [ ] Art. 50(1) AI-interaction notice live (applies since 2 Aug 2026)
- [ ] Art. 50(2) machine-readable marking on generated images, video, audio and text; generators placed on the market before 2 Aug 2026 compliant by 2 Dec 2026
- [ ] Art. 50(4) deepfake and public-interest text labelling handled by the client as deployer
- [ ] Image and video generation: safeguards against non-consensual intimate content and CSAM before 2 Dec 2026
- [ ] If the client deploys a high-risk Annex III system: client's FRIA done before use; you supply the Art. 13 information; reuse the DPIA
- [ ] GPAI provider recorded, and its Code of Practice signatory status checked
- [ ] Logging sufficient to reconstruct what the system did
- [ ] Human oversight pattern documented and effective
- [ ] Incident path for AI-specific failures (harmful output, bias, drift)
- [ ] If you supply a component to a client's high-risk system: the Art. 25(4) written agreement covers information, access and assistance

**Your own organisation (quarterly)**

- [ ] AI literacy measures documented for everyone building or running AI systems (Art. 4, as amended)
- [ ] Register of AI systems in use and their tiers
- [ ] AI-generated marketing assets labelled where Art. 50 applies
- [ ] Standards and guidance refresh: high-risk classification guidelines, harmonised standards from CEN-CENELEC JTC 21, any Official Journal citations

**FRIA note.** An ISO 42001 AI impact assessment plus a GDPR DPIA cover most FRIA evidence, and Art. 27(4) as amended allows cross-referencing the DPIA. What remains is the FRIA-specific framing: affected groups, fundamental-rights risks, complaint routes.

---

## Sources

- [Regulation (EU) 2024/1689: official text (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689): Art. 113 checked 2026-09-29
- [Regulation (EU) 2026/1744: Digital Omnibus on AI (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1744): full amending text read 2026-09-29
- [Council press release, 29 Jun 2026: final adoption](https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/)
- [Council press release, 7 May 2026: provisional agreement](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)
- [Commission press release IP/26/1024: agreement, nudification ban](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1024)
- [European Commission: AI Act overview + timeline](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Commission: Code of Practice on marking and labelling AI-generated content (10 Jun 2026)](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content)
- [Commission: Guidelines on Art. 50 transparency obligations (20 Jul 2026)](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-guidelines-transparency-obligations-providers-and-deployers-certain-ai-systems)
- [Commission: General-Purpose AI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)
- [Commission: Guidelines for GPAI providers (18 Jul 2025)](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers)
- [Commission: Guidelines on AI system definition (6 Feb 2025)](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-ai-system-definition-facilitate-first-ai-acts-rules-application)
- [Commission: Guidelines on prohibited AI practices (Feb 2025)](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-prohibited-artificial-intelligence-ai-practices-defined-ai-act)
- [Commission: Draft guidelines on high-risk classification](https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems)
- [CEN-CENELEC: acceleration of AI standards (23 Oct 2025)](https://www.cencenelec.eu/news-events/news/2025/brief-news/2025-10-23-ai-standardization/) and [EN 18286 in the spotlight (Jul 2026)](https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-07-30-ai-quality-management/)
- [AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en): official EC Q&A
- [AI Act Explorer (Future of Life Institute)](https://artificialintelligenceact.eu/): convenience only; may lag the Omnibus amendments

**Last reviewed:** 2026-09-29 (primary sources checked this date).
