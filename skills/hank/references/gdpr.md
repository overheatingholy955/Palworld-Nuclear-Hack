# GDPR: General Data Protection Regulation

**Citation:** Regulation (EU) 2016/679 (OJ L 119, 4.5.2016). Applies since 25 May 2018. Procedural complement: Regulation (EU) 2025/2518 on cross-border enforcement (applies from 2 April 2027, see below).

**Enforcement:** National Data Protection Authorities (DPAs / supervisory authorities) per Member State. Lead authority for cross-border processing is the DPA of the controller's main EU establishment (one-stop-shop, Art. 56). Administrative fines (Art. 83): up to **€20M or 4%** of global annual turnover, whichever is higher, for breaches of principles, lawful basis, data subject rights and transfers; up to **€10M or 2%** for most controller/processor obligations (Arts. 8, 11, 25–39, 42, 43). Data subjects can also claim compensation (Art. 82).

**UK note:** the UK runs a separate regime (UK GDPR + Data Protection Act 2018, as amended by the Data (Use and Access) Act 2025), enforced by the ICO. It is no longer "functionally identical" to the EU GDPR. See the separate **UK notes** section at the end; do not mix UK guidance into EU conclusions.

---

## Scope: who it applies to

GDPR applies to:

1. **Any organisation established in the EU/EEA** processing personal data in the context of that establishment, regardless of where processing happens (Art. 3(1)).
2. **Any organisation outside the EU** offering goods/services to people in the EU OR monitoring their behaviour in the EU (Art. 3(2) extraterritoriality).
3. **Any information relating to an identified or identifiable natural person** (Art. 4(1)). Pseudonymised data is personal data *for whoever can re-identify it*; anonymous data is outside scope. Since the CJEU's *EDPS v SRB* judgment (C-413/23 P, 4 Sep 2025) identifiability is assessed from the perspective of the entity concerned: see "Recent developments".

---

## The seven principles (Art. 5)

1. **Lawfulness, fairness, transparency**: must have a lawful basis, must be fair, must tell people what you're doing.
2. **Purpose limitation**: collected for specified, explicit, legitimate purposes; not further processed incompatibly.
3. **Data minimisation**: adequate, relevant, limited to what's necessary.
4. **Accuracy**: kept up to date; inaccurate data corrected/erased without delay.
5. **Storage limitation**: kept no longer than necessary for the purpose.
6. **Integrity + confidentiality**: appropriate security (encryption, access control, resilience).
7. **Accountability**: controller must demonstrate compliance with all six above (Art. 5(2)).

**The accountability principle is the one Hank reaches for most often**: every other principle gets enforced via "show your work." Document the lawful basis, document the retention period, document the breach response plan.

---

## Lawful bases (Art. 6): pick one per purpose

| Basis | When to use | Typical example |
|---|---|---|
| **Consent** | User actively opts in to a specific purpose; freely given, specific, informed, unambiguous | Newsletter signup, non-essential cookies, lead-magnet downloads |
| **Contract** | Necessary to perform a contract with the data subject or pre-contract steps they asked for | Processing billing details to issue invoices |
| **Legal obligation** | Required by EU/Member State law (not your own contract) | Retaining invoices for tax law |
| **Vital interests** | Necessary to protect someone's life | Rare in commercial settings |
| **Public task** | Public-authority processing for an official function | Public bodies only |
| **Legitimate interests** | Necessary for your or a third party's legitimate interest, not overridden by data subject's rights | B2B prospecting, website analytics (non-cookie parts), fraud prevention, security |

**No hierarchy.** Pick the most appropriate for the purpose. **Don't plan to swap bases later** (regulator guidance, e.g. ICO and EDPB consent guidelines: if consent is withdrawn you cannot silently fall back on legitimate interests). Get it right first time; document the choice.

**Legitimate interests needs a documented Legitimate Interest Assessment (LIA)**: purpose test, necessity test, balancing test (EDPB Guidelines 1/2024 on Art. 6(1)(f), adopted for consultation Oct 2024; ICO also publishes a template). Without an LIA the basis rarely survives scrutiny.

**Special category data** (racial/ethnic origin, political opinions, religious/philosophical beliefs, trade union membership, genetic, biometric-for-identification, health, sex life, sexual orientation) needs an Art. 6 lawful basis **PLUS** an Art. 9(2) condition. Most common: explicit consent, employment/social-security law, vital interests, manifestly made public, legal claims.

**Note:** cookies and similar device access are governed by the ePrivacy Directive (2002/58/EC, Art. 5(3)) as transposed nationally, not by Art. 6 alone. The Digital Omnibus proposal would move this into the GDPR (Art. 88a/88b); that is **not law** (see below).

---

## Controllers vs processors (Art. 4(7), 4(8), 26, 28)

- **Controller** decides the purposes + means of processing.
- **Processor** processes on behalf of and under instruction from the controller.
- **Joint controllers** decide together (requires an Art. 26 arrangement).

A controller–processor relationship requires a **Data Processing Agreement** per Art. 28(3) covering: subject-matter, duration, nature + purpose of processing, categories of data + data subjects, controller obligations + rights, confidentiality, security measures (Art. 32), sub-processor conditions, assistance with data subject rights + DPIAs + breach notification, end-of-engagement deletion/return, audit rights.

**Sub-processors:** processor needs the controller's prior specific or general written authorisation; under general authorisation the controller must be informed of changes and able to object (Art. 28(2)). The same data-protection obligations flow down the chain (Art. 28(4)).

---

## Data subject rights (Chapter III)

| Right | Article | What it means in practice |
|---|---|---|
| Information | 13, 14 | Privacy notice covers all required disclosures |
| Access (DSAR) | 15 | "What data do you have on me?": response within 1 month |
| Rectification | 16 | Correct inaccurate data without undue delay |
| Erasure (RTBF) | 17 | Delete when no longer necessary, consent withdrawn, etc. |
| Restriction | 18 | Store but don't otherwise process while a dispute is pending |
| Portability | 20 | Structured, commonly used, machine-readable export (consent/contract + automated processing) |
| Object | 21 | Object to legitimate-interests/public-task processing; absolute right for direct marketing |
| Automated decisions | 22 | Right not to be subject to decisions based solely on automated processing (incl. profiling) with legal/similarly significant effects, save for contract necessity, law, or explicit consent. **Major AI-system implication.** |

**DSAR clock = 1 month, extendable by 2 further months for complex/numerous requests** (Art. 12(3)). Manifestly unfounded or excessive requests may be refused or charged for (Art. 12(5)); the controller bears the burden of proof. Failure to respond is an enforceable infringement. Build a DSAR process before you need one.

---

## International transfers (Chapter V)

EU → non-EU transfers need a legal mechanism:

1. **Adequacy decision** (Art. 45): Commission has ruled the destination provides essentially equivalent protection. Includes e.g. UK (renewed December 2025), Switzerland, Israel, Japan, South Korea, Canada (commercial), and the **US for organisations certified under the EU-US Data Privacy Framework (DPF)**. Check the Commission's live list before relying on it.
2. **Standard Contractual Clauses (SCCs)** (Commission Implementing Decision (EU) 2021/914): used for non-DPF US recipients and other non-adequate countries.
3. **Binding Corporate Rules (BCRs)**: intra-group, approved via the EDPB consistency mechanism.
4. **Derogations (Art. 49)**: explicit consent, contract performance, important public interest, legal claims. Narrow; not for routine transfers.

**Post-Schrems II (C-311/18, 16 July 2020):** SCCs/BCRs require a Transfer Impact Assessment (TIA) showing the destination's law doesn't undermine the safeguards, plus supplementary measures where needed. Transfers to DPF-certified US organisations rely on the adequacy decision and need no TIA; the Commission's DPF assessment of US law can be referenced in TIAs for SCC-based US transfers.

**DPF status (verified 2026-09-29):** Commission Implementing Decision (EU) 2023/1795 of 10 July 2023. The **General Court dismissed** the annulment action in *Latombe v Commission* (T-553/23, judgment 3 Sep 2025), holding the US Data Protection Review Court and bulk-collection safeguards adequate. **Appeal pending** before the Court of Justice: *Latombe v Commission*, **C-703/25 P**, lodged 31 Oct 2025; an order was issued 4 Jun 2026 (reported as admitting Microsoft as intervener); no hearing, AG opinion or judgment found. DPF remains valid until the CJEU rules otherwise. Keep SCCs available as a fallback in contracts with US sub-processors.

---

## Breach notification (Art. 33, 34)

- **To DPA:** without undue delay and, where feasible, within **72 hours** of becoming aware of a personal data breach, **unless the breach is unlikely to result in a risk** to rights/freedoms. Late notifications must give reasons.
- **To data subjects:** without undue delay, if the breach is likely to result in a **high risk** to rights/freedoms (Art. 34), subject to the Art. 34(3) exceptions (e.g. data was encrypted).
- **Processor → controller:** without undue delay after becoming aware (Art. 33(2)).

Breach = "a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data" (Art. 4(12)). Includes lost laptops, misdirected emails, ransomware, exposed storage buckets, prompt/data leakage through an AI system.

**Document every breach even if not reportable**: Art. 33(5) requires an internal record.

**Proposed, not law:** the Digital Omnibus would raise the DPA threshold to "high risk" and the deadline to 96 hours via a single entry point (see below). Until adopted, **72 hours / "risk" threshold stands.**

---

## Records of processing (Art. 30)

The Art. 30(5) exemption for organisations under 250 employees does **not** apply if processing is likely to result in a risk to rights/freedoms, is not occasional, or includes special category / criminal-offence data. In practice every B2B SaaS keeps a ROPA. Contents: name + contact of controller/DPO, purposes, categories of subjects + data, recipients, transfers, retention, security measures.

**Proposed, not law:** the Commission's "Omnibus IV" (21 May 2025) proposes raising the threshold to 750 employees and limiting the record duty to high-risk processing. Adoption status as of Sep 2026: **UNVERIFIED**.

---

## Data Protection Impact Assessment (DPIA: Art. 35)

Required when processing is **likely to result in high risk** to rights/freedoms. Always required for (Art. 35(3)):
- Systematic + extensive evaluation of personal aspects based on automated processing, incl. profiling, with legal/similarly significant effects
- Large-scale special category or criminal-offence data
- Systematic monitoring of a publicly accessible area on a large scale

Plus each national DPA's published list of processing requiring a DPIA (Art. 35(4)); innovative technology such as AI is a listed criterion in EDPB/WP29 guidance (WP248 rev.01). A DPIA covers: description of processing, necessity + proportionality, risk assessment, mitigation measures; prior consultation with the DPA if residual risk remains high (Art. 36).

**AI Act link:** a deployer's Fundamental Rights Impact Assessment (AI Act Art. 27) may cross-reference the DPIA (Art. 27(4) as amended by Reg. (EU) 2026/1744).

---

## Common AI-specific GDPR issues

1. **Provider training on user inputs.** Consumer-tier LLM services may use inputs for training. For personal/confidential data, use business/enterprise terms with contractual no-training commitments and a DPA.
2. **Vector stores containing personal data.** Embeddings can leak or partially reconstruct source text. Treat embedding stores as personal-data stores: same retention, access control, DSAR and erasure handling.
3. **Automated decisions (Art. 22).** CV screening, credit scoring, risk scoring: human involvement must be meaningful, and data subjects get the right to human intervention, to express their view and to contest (Art. 22(3)). The CJEU read "decision" broadly in *SCHUFA* (C-634/21, 7 Dec 2023).
4. **Is the model itself personal data?** EDPB Opinion 28/2024 (18 Dec 2024): models trained on personal data are not automatically anonymous. A model is anonymous only if it is very unlikely that (1) individuals whose data was used can be identified, directly or indirectly, and (2) such data can be extracted through queries. DPAs assess case by case.
5. **Legitimate interest for AI development/deployment.** Opinion 28/2024 confirms it can be a valid basis, subject to the three-step test (legitimate interest, necessity, balancing), considering data subjects' reasonable expectations and mitigating measures.
6. **Unlawfully trained models.** Per Opinion 28/2024, unlawful processing in development can affect the lawfulness of later deployment (whether by the same or another controller), unless the model has been duly anonymised. Deployers should check the provider's lawful-basis story ("appropriate assessment").
7. **Right to erasure vs model weights.** Erasure from trained weights is hard. Safest approaches: don't train on personal data; use providers with no-training terms; apply output filtering; document the residual risk.
8. **Indirect collection (Art. 14).** Scraping or enrichment (LinkedIn, lead-enrichment APIs, public data) requires Art. 14 information within a reasonable period, at the latest within one month; at the latest at first communication if used to contact the person; at the latest on first disclosure if shared. Defend the legitimate-interests basis with a written LIA.

---

## Recent developments (2025–2026)

### Digital Omnibus: GDPR amendments (PROPOSAL, not law)

- **Instrument:** Commission proposal COM(2025) 837 final, 19 Nov 2025 ("Digital Omnibus Regulation"). Separate from the AI track (the AI Omnibus is now law as Reg. (EU) 2026/1744; see the EU AI Act brief).
- **Status as of 2026-09-29:** first reading. Parliament: ITRE + LIBE jointly (rapporteurs Aura Salla, Marina Kaljurand); draft report 22 Jun 2026, 1,750+ amendments tabled by 15 Jul 2026; no committee vote found. Council: no general approach/negotiating mandate; a planned COREPER vote (26 Jun 2026) was cancelled and work continues under the Irish Presidency (EP Legislative Train, update of 1 Aug 2026). **No trilogue, no adopted text.** Final wording will differ from the proposal.
- **What the Commission text proposes** (verified against COM(2025) 837):
  - **Personal data definition (Art. 4(1)):** adds an entity-relative test: information isn't personal data for an entity that cannot identify the person with means reasonably likely to be used by *that* entity, and doesn't become personal merely because a later recipient could identify. New **Art. 41a** lets the Commission adopt implementing acts on when pseudonymised data stops being personal data for certain entities. (Reported: the Council Presidency moved away from redefining Art. 4(1) towards a new pseudonymisation article; **UNVERIFIED** against Council documents.)
  - **AI and legitimate interest (new Art. 88c):** processing "in the context of the development and operation of an AI system … or an AI model" may rely on Art. 6(1)(f), unless other law requires consent or data subjects' interests override (especially children). Safeguards include data minimisation in source selection and training, protection against disclosure of residually retained data, enhanced transparency, and an **unconditional right to object**.
  - **Special categories (Art. 9(2)(k) + 9(5)):** new derogation for residual special-category data in AI development/operation, with a duty to avoid collecting it, remove it when found, or, where removal is disproportionate, protect it from outputs and disclosure. New **Art. 9(2)(l)** for biometric verification under the data subject's sole control.
  - **DSAR abuse (Art. 12(5)):** controllers may refuse or charge for access requests where the data subject "abuses the rights … for purposes other than the protection of their data"; the burden of proof stays with the controller.
  - **Breach notification (Art. 33):** notify the DPA only where the breach is **likely to result in a high risk**, within **96 hours** where feasible, via the **single entry point** under new NIS2 Art. 23a (direct DPA notification continues until the single entry point exists). The EDPB would draft a common template and a list of high-risk circumstances.
  - **Information duty (Art. 13(4)):** exemption for clear, circumscribed, non-data-intensive relationships.
  - **Automated decisions (Art. 22):** rewritten as a permission list: contract necessity "regardless of whether the decision could be taken otherwise than by solely automated means", law, or explicit consent.
  - **DPIA (Art. 35):** EU-wide lists (required / not required) plus a common template and methodology, proposed by the EDPB and adopted by Commission implementing act.
  - **Cookies (new Arts. 88a/88b):** device storage/access rules move into the GDPR; consent exemptions for first-party aggregated audience measurement and security; one-click refusal; no re-asking for 6 months after refusal; machine-readable browser-based consent signals (browser-provider obligation 48 months after entry into force).
  - **Scientific research:** new definition (Art. 4(38)), which may include commercial research; further processing for research deemed compatible.

### GDPR Procedural Regulation (ADOPTED)

- **Regulation (EU) 2025/2518** of 26 Nov 2025 laying down additional procedural rules on the enforcement of Regulation (EU) 2016/679. OJ L, 2025/2518, 12.12.2025. **Entered into force 1 Jan 2026; applies from 2 April 2027** (to ex officio investigations opened, and complaints lodged, after that date).
- Harmonises admissibility of cross-border complaints, gives complainants and investigated parties rights to be heard and to see preliminary findings, and sets time limits (Council press release, 17 Nov 2025: ~15 months for regular investigations, extendable for complex cases; ~12 months for simple cooperation).

### Case law

- ***EDPS v SRB*, C-413/23 P (CJEU, 4 Sep 2025):** set aside General Court T-557/20. Personal opinions/comments are personal data of their authors. Pseudonymised data may be non-personal for a recipient that cannot reasonably re-identify (technical, organisational, legal means), but remains personal data for the controller holding the key. The controller's transparency duty (who the recipients are) is assessed **at collection, from the controller's perspective**, so it applies even if the data is not personal for the recipient. (Case decided under Reg. 2018/1725 for EU institutions; applied by analogy to the GDPR.)
- ***Quirin Privatbank*, C-655/23 (CJEU, 4 Sep 2025):** the GDPR does not itself give a preventive injunction remedy against future unlawful processing (absent an erasure request), but Member States may provide one. Under Art. 82(1), the **degree of the controller's fault may not be taken into account** in assessing non-material damages, and an injunction obtained under national law may not reduce or replace compensation. (Consistent with earlier case law: no de minimis threshold for non-material damage, but damage must be proven.)
- ***Latombe v Commission*, T-553/23 (General Court, 3 Sep 2025):** DPF upheld; appeal C-703/25 P pending (see Transfers).

### EDPB

- **Opinion 28/2024** on AI models (18 Dec 2024): anonymity, legitimate interest, unlawfully trained models (summarised above).
- Guidelines 01/2025 on pseudonymisation (adopted for consultation January 2025); status of the final version after *SRB* is **UNVERIFIED**.

---

## UK notes (separate regime, not EU law)

- **Data (Use and Access) Act 2025** received Royal Assent **19 June 2025**; commenced in stages via commencement regulations (Commencement No. 1: 20 Aug 2025; main Part 5 data-protection changes planned ~6 months after Royal Assent; the controller complaints-handling duty (s.103) planned ~12 months after Royal Assent). Exact commencement date of each provision: check legislation.gov.uk; not individually verified here.
- UK-specific changes include recognised legitimate interests, relaxed rules on some automated decision-making, cookie-consent exemptions and a data-subject complaints process. ICO guidance applies to UK GDPR only.
- **EU → UK transfers:** the Commission renewed the UK adequacy decisions in December 2025 (Commission press release IP/25/3059); per the draft renewal, valid until December 2031.

---

## Applying this in practice

For an agency or SaaS team that builds and runs systems for clients.

**Roles.** For client websites and systems, the client is normally the controller and the agency the processor. The agency becomes a joint controller, or a controller in its own right, if it decides purposes or means (for example, reusing client data to improve its own product).

**Per-deployment checklist (every engagement that touches personal data)**

- [ ] Roles confirmed per processing activity
- [ ] DPA signed before any production data flows
- [ ] Sub-processor list disclosed in the DPA, with change notice and a right to object; every model API provider included
- [ ] Lawful basis documented for every distinct purpose
- [ ] Privacy notice updated for the data flow: sources, AI processing, retention, sub-processors, transfer mechanism
- [ ] Cookie consent: nothing non-essential fires before consent; granular; withdrawable (see `eprivacy.md`)
- [ ] Retention period per data category, enforced by a deletion job
- [ ] Data subject request process documented and tested
- [ ] Breach path defined: who calls whom inside 72 hours; processor notifies the controller without undue delay
- [ ] Transfer mechanism in place for every non-EU recipient (Data Privacy Framework certification check, or SCCs plus a transfer impact assessment)
- [ ] DPIA done where AI processing is likely high risk
- [ ] Records of processing (Art. 30) updated

**For your own business**

- [ ] Privacy notice current and listing all processors
- [ ] Cookie banner verified in a clean browser profile
- [ ] Legitimate interests assessment on file for B2B outreach; Art. 14 notice at first contact
- [ ] Marketing consent captured and withdrawable; suppression list kept
- [ ] Internal data subject request and breach process documented, even for a one-person company
- [ ] LLM provider plans set to no training on inputs

**Watch list**

- Digital Omnibus GDPR amendments: still a proposal; do not advise on them as if in force.
- C-703/25 P (appeal against the General Court's Data Privacy Framework ruling): if the Court of Justice annuls the DPF, US transfers must move to SCCs plus a transfer impact assessment.
- Regulation (EU) 2025/2518 on cross-border enforcement applies from 2 April 2027.

---

## Sources

- [Regulation (EU) 2016/679: official text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [Regulation (EU) 2025/2518: GDPR procedural rules (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2025/2518/oj/eng): checked 2026-09-29
- [Council press release, 17 Nov 2025: cross-border complaints regulation adopted](https://www.consilium.europa.eu/en/press/press-releases/2025/11/17/council-adopts-new-eu-law-to-speed-up-handling-cross-border-data-protection-complaints/)
- [COM(2025) 837: Digital Omnibus Regulation proposal (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025PC0837): GDPR amendments read 2026-09-29
- [European Parliament Legislative Train: Digital Omnibus Regulation](https://www.europarl.europa.eu/legislative-train/theme-a-new-plan-for-europe-s-sustainable-prosperity-and-competitiveness/file-digital-package): status update 1 Aug 2026
- [CJEU C-413/23 P, EDPS v SRB, 4 Sep 2025 (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0413)
- [CJEU C-655/23, Quirin Privatbank, 4 Sep 2025 (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0655)
- [General Court T-553/23, Latombe v Commission, 3 Sep 2025 (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A62023TJ0553)
- [InfoCuria: C-703/25 P Latombe v Commission (pending)](https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?language=en&td=ALL&num=C-703/25)
- [EDPB Opinion 28/2024 on AI models](https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en) and [EDPB press release, 18 Dec 2024](https://www.edpb.europa.eu/news/news/2024/edpb-opinion-ai-models-gdpr-principles-support-responsible-ai_en)
- [EDPB: European Data Protection Board](https://www.edpb.europa.eu/): guidelines + opinions
- [Commission: adequacy decisions list](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en)
- [Commission press release IP/25/3059: UK adequacy renewed](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_3059)
- [Schrems II ruling (CJEU C-311/18)](https://curia.europa.eu/): international transfer case law
- UK only: [GOV.UK: DUAA 2025 commencement plans](https://www.gov.uk/guidance/data-use-and-access-act-2025-plans-for-commencement); [ICO: lawful basis guide](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/); ICO accountability framework: `https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/`

**Last reviewed:** 2026-09-29 (primary sources checked this date).
