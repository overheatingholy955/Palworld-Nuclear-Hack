# Data Act: Regulation (EU) 2023/2854

**Citation:** Regulation (EU) 2023/2854 of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act).
- Entered into force 11 January 2024.
- **Applies from 12 September 2025** (Art. 50).
- It is a Regulation, so it is directly applicable. No national transposition is needed, except for penalties and the choice of authorities.

**Enforcement:**
- Each Member State designates **competent authorities** and, if it has more than one, a **data coordinator** (Recital 107; Art. 37).
- The authority enforcing the cloud-switching rules (Arts. 23-31, 34-35) must have experience in data and electronic communications services (Art. 37).
- For **personal data**, the GDPR supervisory authorities are responsible within their competence.
- **UNVERIFIED this session:** which body each Member State (including Ireland) has designated. Check the Commission's public register.

**Penalties** (Art. 40):
- Set nationally. They must be "effective, proportionate and dissuasive".
- Member States had to notify their penalty rules by 12 September 2025.
- Criteria include the **infringing party's annual turnover in the Union**.
- **For breaches of Chapters II, III and V, GDPR supervisory authorities may impose fines "in accordance with Article 83" GDPR, up to the Art. 83(5) ceiling.** That ceiling is the higher of €20M or 4% of worldwide annual turnover (per GDPR, see `gdpr.md`).
- Competent authorities may impose periodic penalties and penalties with retroactive effect (Art. 37(5)(d)).

---

## Scope: who it applies to (Art. 1(3))

It reaches beyond the EU, much as the GDPR does. It applies to:
- manufacturers of connected products placed on the EU market, and providers of related services, **wherever they are established**
- users of those products and services in the Union
- data holders that make data available to recipients in the Union
- public-sector requesters
- **providers of data processing services, wherever established, that serve customers in the Union**
- data-space participants and smart-contract vendors

Virtual assistants count when they interact with a connected product (Art. 1(4)).

**It covers personal and non-personal data** (Art. 1(2)).

**The GDPR and ePrivacy prevail in any conflict** (Art. 1(5)). The Regulation is "without prejudice to" the GDPR, EUDPR and Directive 2002/58/EC. For users who are data subjects, the Chapter II rights *complement* the GDPR rights of access (Art. 15) and portability (Art. 20).

**Chapter map:**

| Chapter | Topic | Who it bites |
|---|---|---|
| II (Arts. 3-7) | B2C and B2B access to connected-product and related-service data | Manufacturers, related-service providers, data holders |
| III (Arts. 8-12) | General terms when a law obliges a data holder to share (FRAND terms, compensation, dispute settlement) | Data holders under a legal sharing duty |
| IV (Art. 13) | Unfair terms in B2B data contracts | **Any business drafting data terms** |
| V (Arts. 14-22) | Access by public bodies on "exceptional need" | Data holders that are legal persons |
| VI (Arts. 23-31) | **Switching between data processing services** (cloud, PaaS, **SaaS**) | **Cloud and SaaS providers** |
| VII (Art. 32) | Unlawful third-country government access to non-personal data | Data processing service providers |
| VIII (Arts. 33-36) | Interoperability, data spaces, smart contracts | Data-space participants, smart-contract vendors |
| IX-XI | Enforcement, delegated acts, final provisions | |

---

## Key dates (Art. 50, Art. 29)

| Date | What happens |
|---|---|
| 11 Jan 2024 | Entry into force. Art. 29(2) period starts: switching charges limited to **cost-based reduced charges** |
| **12 Sep 2025** | General application. Chapter IV applies to contracts concluded **after** this date |
| **12 Sep 2026** | **Art. 3(1) design obligation** applies to connected products and related services **"placed on the market after 12 September 2026"** |
| **12 Jan 2027** | **Switching charges, including egress, banned** for switching (Art. 29(1)) |
| **12 Sep 2027** | Chapter IV extends to contracts concluded **on or before** 12 Sep 2025 if they are of indefinite duration or due to expire at least 10 years from 11 Jan 2024 |

**Precise reading of the 12 Sep 2026 date:** Art. 3(1) is not retroactive. Products already on the market before that date do not have to be redesigned. **The rest of Chapter II has applied since 12 Sep 2025.** That includes Art. 3(2)-(3) pre-contract information, Art. 4 access on request, and Art. 5 sharing with third parties. For products where the user cannot access data directly, the data holder must provide it on request (Art. 4(1)).

---

## Chapter II: connected-product and related-service data

**Definitions (Art. 2):**
- **Connected product:** an item that obtains, generates or collects data about its use or environment, can communicate product data, and whose primary function is not storing or processing data for others.
- **Related service:** a digital service, other than an electronic communications service and including software, that is connected with the product when it is bought, rented or leased, such that its absence would prevent the product from performing one or more of its functions. Also covers a service connected later by the manufacturer or a third party to add to, update or adapt the product's functions.
- **Readily available data:** product and related-service data the data holder can obtain "without disproportionate effort going beyond a simple operation".

**Core duties:**
- **Access by design (Art. 3(1)):** products and related services must make product data, related-service data and the metadata needed to use them available **by default**, easily, securely, free of charge, in a structured, commonly used, machine-readable format. Where relevant and technically feasible, access must be **direct** to the user. Applies to products placed on the market after 12 Sep 2026.
- **Pre-contract transparency (Art. 3(2)-(3)):**
  - the type, format and volume of data
  - whether data is generated continuously or in real time
  - whether it is stored on the device or remotely, and for how long
  - how the user can access, retrieve or erase it
  - for related services, the provider must give additional information
- **User access on request (Art. 4(1)):** where direct access is impossible, provide readily available data and metadata "without undue delay", of the same quality the data holder has, free of charge, and continuously or in real time where feasible.
- **Sharing with third parties at the user's request (Art. 5):** the third party receives the data free of charge **to the user**. **Gatekeepers under the Digital Markets Act are not eligible third parties** (Art. 5(3)).
- **Limits on the data holder (Art. 4(13)-(14)):**
  - It may use non-personal readily available data **only on the basis of a contract with the user**.
  - It may not use the data to derive insights that undermine the user's commercial position.
  - It may not share non-personal product data with third parties beyond fulfilling the user contract.
- **Limits on the user (Art. 4(10)):** the user may not use the data to develop a **competing connected product**.
- **Personal data (Art. 4(12)):** where the requesting user is not the data subject, personal data may be released only with a GDPR Art. 6 basis, Art. 9 where relevant, and **ePrivacy Art. 5(3)** satisfied.
- **Micro and small enterprise exemption (Art. 7(1)):** Chapter II does not apply to products made or related services provided by a micro or small enterprise. The exemption is lost if the enterprise has a partner or linked enterprise that does not qualify, or if it is **subcontracted** to manufacture or design the product or provide the related service. Newly medium-sized firms get a one-year grace period.
- **No contracting out (Art. 7(2)):** terms that exclude or vary the user's Chapter II rights are not binding on the user.

---

## Chapter III: when a law obliges data sharing (Arts. 8-12)

When Union or national law requires a data holder to make data available to a data recipient:
- terms must be fair, reasonable and non-discriminatory (FRAND)
- the data holder may ask for **reasonable compensation**, which may include a margin. **No margin is allowed toward SMEs and not-for-profit research organisations** (Recital 47).
- dispute settlement bodies are available

Chapter III applies only to sharing obligations in laws **entering into force after 12 Sep 2025** (Art. 50).

---

## Chapter IV: unfair B2B contract terms (Art. 13)

**Scope:** a term about **access to and use of data, or liability and remedies for breach or termination of data-related obligations**, that one enterprise **unilaterally imposed** on another. An unfair term is **not binding**. The rest of the contract survives if the term is severable (Art. 13(7)).

**General test (Art. 13(3)):** the term "grossly deviates from good commercial practice in data access and use, contrary to good faith and fair dealing".

**Blacklist, always unfair (Art. 13(4)):** a term whose object or effect is to:
- (a) exclude or limit the imposing party's liability for **intentional acts or gross negligence**
- (b) exclude the other party's remedies for non-performance, or the imposing party's liability for breach
- (c) give the imposing party the **exclusive right** to decide whether the data conforms to the contract, or to interpret any term

**Grey list, presumed unfair (Art. 13(5)):** a term whose object or effect is to:
- (a) inappropriately limit remedies or liability, or extend the other party's liability
- (b) let the imposing party **access and use the other party's data** in a way significantly detrimental to its legitimate interests, especially trade secrets, IP or commercially sensitive data
- (c) prevent or limit the other party from using the data **it provided or generated** during the contract
- (d) prevent termination within a reasonable period
- (e) prevent the other party from **getting a copy of its data** during the contract or within a reasonable period after it ends
- (f) allow termination by the imposing party at unreasonably short notice
- (g) allow a substantial change to price or data conditions without a valid reason and without a right to terminate. Unilateral changes to indefinite-term contracts are allowed if the reason is specified, reasonable notice is given, and the other party can terminate at no cost.

**Other rules:**
- **"Unilaterally imposed"** means supplied by one party where the other could not influence it **despite an attempt to negotiate**. **The party that supplied the term bears the burden of proof** (Art. 13(6)).
- **Excluded:** terms defining the **main subject matter** and the **adequacy of the price** (Art. 13(8)).
- **Cannot be contracted out of** (Art. 13(9)).
- **Protects enterprises of any size.** The adopted text says "another enterprise" and sets no size threshold, so a large client can also invoke Art. 13 against a small supplier's standard terms.

---

## Chapter V: public-sector access (Arts. 14-22)

- Public sector bodies, the Commission, the ECB and Union bodies may require data holders that are **legal persons** to provide data where they show an **exceptional need**.
- **Public emergency:** personal data can be requested if necessary (Art. 15(1)(a)).
- **Other specific public-interest tasks provided for by law:** **non-personal data only**, and only after all other means are exhausted, including buying the data at market rates (Art. 15(1)(b)).
- Micro and small enterprises are exempt from the non-emergency limb (Art. 15(2)).
- Criminal enforcement, customs and tax are outside this Chapter (Art. 16(2)).

---

## Chapter VI: switching between data processing services (Arts. 23-31)

**This is the part that catches SaaS providers.**

**Definition (Art. 2(8)):** a "data processing service" is a digital service provided to a customer that enables "ubiquitous and on-demand network access to a shared pool of configurable, scalable and elastic computing resources", rapidly provisioned and released with minimal management effort or provider interaction.
- **Recital 81 names IaaS, PaaS and SaaS.**
- The **Commission FAQ (v1.4, 22 Jan 2026, Q58a)** confirms that Chapter VI "does not make a distinction between different types of SaaS, and thus applies to all SaaS types which display the characteristics listed in the definition".
- The FAQ adds a **customer test**: ask whether the user has contracted to use a data processing service **as such**, or only uses a functionality it enables, such as listening to music or watching video.

**What a provider must do:**
- **Remove obstacles** (Art. 23): no pre-commercial, commercial, technical, contractual or organisational barriers to:
  - terminating
  - contracting with a new provider
  - porting exportable data and digital assets, **including after a free tier**
  - achieving functional equivalence (IaaS)
  - unbundling
- **Written contract with minimum switching terms** (Art. 25(2)):
  - **notice period of at most 2 months** to start switching
  - **transitional period of at most 30 days** for the switch, during which the provider must assist, keep the service running, disclose known continuity risks and keep data secure
  - if 30 days is technically unfeasible, notify within **14 working days**, justify, and offer an alternative of at most **7 months** (Art. 25(4))
  - the customer may extend the transitional period once (Art. 25(5))
  - an **exhaustive list of exportable data and digital assets**, and of any internal-functioning data excluded on trade-secret grounds
  - **data retrieval period of at least 30 days** after the transitional period
  - **full erasure** of exportable data and assets after the retrieval period
  - an exit-strategy support obligation
  - termination triggers
  - the switching charges applicable under Art. 29
- **Information duties** (Art. 26): switching procedures, methods, formats and known limitations, plus an **up-to-date online register** of data structures, formats and standards.
- **Good faith** (Art. 27): all parties, including the destination provider, must cooperate.
- **Transparency on international access** (Art. 28): publish on your website, and keep up to date:
  - the jurisdiction of the ICT infrastructure used for each service
  - a general description of the measures that prevent unlawful third-country government access to **non-personal** data
  - list those web pages in every contract

**Switching and egress charges** (Art. 29):
- 11 Jan 2024 to 12 Jan 2027: only **reduced** charges, not exceeding the provider's **direct costs** of the switch.
- **From 12 Jan 2027: no switching charges at all, egress included.**
- Standard service fees, early termination penalties and reduced switching charges must be disclosed **before** contracting (Art. 29(4)).
- **Exception, parallel multi-cloud use (Art. 34(2)):** providers may still pass on egress **costs** incurred, with no margin, even after 12 Jan 2027 (FAQ Q54).

**Technical duties differ by delivery model** (Art. 30):
- **IaaS:** facilitate **functional equivalence** at the destination (Art. 30(1)).
- **PaaS/SaaS:**
  - provide **open interfaces**, free of charge and to an equal extent to all customers and destination providers (Art. 30(2))
  - comply with common specifications or harmonised interoperability standards **12 months after** their reference is published in the EU repository (Art. 30(3))
  - until then, **export all exportable data in a structured, commonly used, machine-readable format** on request (Art. 30(5))
- No duty to develop new technology or to disclose IP or trade secrets (Art. 30(6)).
- The source provider does not have to rebuild the service at the destination (Art. 24; FAQ Q58b).

**Lighter regimes** (Art. 31):
- **Custom-built services** (Art. 31(1)): the majority of main features custom-built for one customer, or all components developed for that customer, **and** not offered at broad commercial scale through the service catalogue. These are exempt only from Art. 23(d), **Art. 29** and Art. 30(1) and (3).
  - They are still subject to the Art. 25 contract terms, Art. 30(2) open interfaces and Art. 30(5) export (FAQ Q52).
  - **Common misreading:** "custom" does **not** mean "out of scope".
- **Non-production test or evaluation versions for a limited period** (Art. 31(2)) are fully outside Chapter VI.
- **The customer must be told in advance which obligations do not apply** (Art. 31(3)).

**No SME exemption in Chapter VI today.** Chapter II's micro/small exemption (Art. 7) does not extend here. A two-person SaaS company is caught if its service fits Art. 2(8). The Digital Omnibus would add limited relief (below). That relief is not law.

---

## Chapter VII: international government access (Art. 32)

- Providers must take **adequate technical, organisational and legal measures, including contracts**, to prevent third-country government access to or transfer of **non-personal data** held in the EU where that would conflict with EU or Member State law (Art. 32(1)).
- A third-country court or authority order is enforceable **only on the basis of an international agreement**, such as a mutual legal assistance treaty (Art. 32(2)).
- **Without such an agreement,** comply only if all of these hold (Art. 32(3)):
  - the foreign system requires the order to be reasoned, proportionate and specific
  - the provider's objection can be reviewed by a competent foreign court
  - that court can weigh the EU-protected interests
- The provider may seek the view of the national authority. With no reply within 1 month, it may refuse.
- **Provide the minimum data permissible** (Art. 32(4)).
- **Inform the customer before complying**, except for law-enforcement requests while secrecy is needed (Art. 32(5)).
- This parallels GDPR Chapter V, which covers personal data. Art. 32 covers **non-personal** data, such as client business data, logs and model artefacts.

---

## Chapter VIII: interoperability (Arts. 33-36)

- **Data spaces** (Art. 33): participants offering data must describe the following, where applicable in machine-readable form:
  - dataset content, licences and quality
  - formats and vocabularies
  - API access terms
  - smart-contract interoperability
- Harmonised standards or Commission common specifications give a presumption of conformity.
- **Parallel use of data processing services** (Art. 34): switching duties apply *mutatis mutandis*.
- **Interoperability of data processing services** (Art. 35): open specifications and standards feed the Art. 30(3) duty.
- **Smart contracts for executing data-sharing agreements**: essential requirements in Art. 36.

---

## Commission model contractual terms (Art. 41)

- Art. 41 required the Commission, before 12 Sep 2025, to recommend **non-binding** model contractual terms (MCTs) on data access and use, and **standard contractual clauses (SCCs) for cloud computing contracts**.
- **Status:** the Commission published a **Recommendation** with the MCTs and SCCs on **19 November 2025**. On its page it is still titled "Draft Recommendation", and it was released in English first, with translations to follow.
- The annex carries reference **C(2025) 7750 final**, dated 19.11.2025. This was seen on a third-party mirror of the Commission document, not on the Commission site itself.
- **UNVERIFIED:** Official Journal publication and completion of the translations.
- **MCTs:** sets for data holder↔user, data holder↔data recipient and user↔data recipient under Chapters II and III, plus one set for **voluntary** data sharing designed to pass the Chapter IV unfairness test (Commission FAQ Q74; Commission library page).
- **Cloud SCCs:** switching and exit, term and termination, non-dispersion, non-amendment, security and business continuity, and liability (FAQ Q74).
- **Use:** voluntary and adaptable. The Commission says they are aimed mainly at B2B and can be used B2C if consumer-law terms are added.

---

## Pending change: Digital Omnibus (proposal only)

The Commission's Digital Omnibus proposal (**COM(2025) 837, 19 Nov 2025, procedure 2025/0360(COD)**) would amend the Data Act. **As of 29 Sep 2026 it is not adopted.** The Council has no negotiating mandate, Parliament's committees are still working through more than 1,750 amendments, and no trilogue has started (EP Legislative Train, updated 1 Aug 2026; see `eprivacy.md` for detail).

Proposed Data Act changes:
- **Chapter V narrowed** to "public emergencies" only. Arts. 14 and 15 would be replaced by a new Art. 15a.
- **New Art. 31(1a):** custom-made services other than IaaS, where the majority of features have been adapted to the customer, **provided under contracts concluded on or before 12 Sep 2025**, would be exempt from Chapter VI and Art. 34, **except Art. 29 (charges phase-out)**. Terms contrary to Art. 29(1)-(3) would be null and void.
- **New Art. 31(1b):** the same exemption for **SMEs and small mid-caps** providing non-IaaS services under contracts concluded on or before 12 Sep 2025. Such providers would not need to renegotiate those contracts before they expire. Recital 18 would also confirm that **proportionate early-termination penalties** in fixed-term contracts are allowed if they do not obstruct switching.
- **Trade-secret refusal:** data holders could refuse disclosure where there is a high risk of it reaching jurisdictions with weaker protection (Arts. 4(8), 5(11)).
- **Consolidation into the Data Act** of the Data Governance Act (data intermediation would become voluntary), the Free Flow of Non-Personal Data Regulation and the Open Data Directive.
- **Small mid-caps** would get the SME relief in several places.

**Note:** even if adopted, the Omnibus relief covers only **legacy contracts** (on or before 12 Sep 2025). New SaaS contracts would remain fully in scope, and the egress-charge ban on 12 Jan 2027 would be untouched.

---

## Common assumptions that are wrong

1. **"The Data Act is about IoT, so SaaS isn't affected."** Chapter VI covers SaaS that fits the Art. 2(8) definition (Recital 81; FAQ Q58a).
2. **"We're a small company, so we're exempt."** Only Chapter II (connected products) and parts of Chapter V have micro/small exemptions. Chapters IV and VI have none.
3. **"Custom builds are out of scope."** The Art. 31(1) custom-built regime removes only Arts. 23(d), 29, 30(1) and 30(3). Contract terms, open interfaces and data export still apply.
4. **"Egress fees are fine until 2027."** Since 11 Jan 2024 they have been limited to the provider's direct costs (Art. 29(2)-(3)).
5. **"Everything in the Data Act starts on 12 Sep 2026."** Most of it has applied since 12 Sep 2025. Only the Art. 3(1) design duty is tied to products placed on the market after 12 Sep 2026.
6. **"Data Act fines are small, national fines."** Chapter II, III and V breaches can draw **GDPR-scale fines** from data protection authorities (Art. 40(4)).

---

## Applying this in practice

For a small agency or SaaS builder that hosts client data or offers data-processing services:

1. **Classify each offering.**
   - Is it a self-service, on-demand, scalable service sold from a catalogue? Then it is probably a "data processing service" under Chapter VI.
   - Is it a bespoke build run for one client and not sold at scale? Then it is probably in the lighter Art. 31(1) regime, but still subject to the Art. 25 terms and the export duty.
   - Are pilots and time-limited test deployments clearly labelled non-production? Then they fall under Art. 31(2).
   - Write the classification down, and **tell the client before signing which obligations don't apply** (Art. 31(3)).
2. **Put switching terms in the master services agreement or terms of service.**
   - Notice of at most 2 months.
   - Transition of at most 30 days, with continuity and assistance.
   - A list of exportable data and assets, and any trade-secret carve-outs.
   - Retrieval of at least 30 days.
   - Erasure afterwards.
   - The switching charge position (cost-based now, zero from 12 Jan 2027).
   - The Commission cloud SCCs are a ready starting point.
3. **Build the exit path into the product.** Provide a documented export in structured, machine-readable formats (JSON/CSV/SQL dump plus a schema description). Include configuration, prompts, workflows and embeddings metadata where they are the customer's "digital assets". Publish a register of formats (Art. 26(b)). Offer an API the destination provider can use (Art. 30(2)).
4. **Remove lock-in fees.** Stop charging for exports or egress when a customer leaves, before **12 Jan 2027**. Until then, charge only documented direct costs. Parallel-use egress can still be passed on at cost.
5. **Publish an international-access page** (Art. 28): where the infrastructure sits and under which jurisdiction (including US-parent sub-processors), and the measures against third-country access to non-personal data. Link it from every contract. Keep a playbook for foreign government requests (Art. 32(3)-(5)): legal review, minimum data, and notify the customer first.
6. **Review your standard terms against Art. 13** for every B2B contract that touches data. Watch especially for:
   - clauses letting you use client data (including for **model training or product improvement**) in a way significantly detrimental to the client, which is presumed unfair (Art. 13(5)(b))
   - clauses restricting the client's access to or copies of its own data (13(5)(c) and (e))
   - liability caps that also cover gross negligence (13(4)(a))
   - unilateral price or data-condition changes without a right to exit (13(5)(g))

   Keep evidence of genuine negotiation. The supplier bears the burden of proving a term was not unilaterally imposed.
7. **If you build for connected-product clients** (devices, apps that control devices, virtual assistants interacting with them):
   - Products placed on the market after 12 Sep 2026 need **data access by design**.
   - Prepare Art. 3(2)-(3) disclosures.
   - Support Art. 4 and Art. 5 access requests.
   - Check GDPR **and ePrivacy Art. 5(3)** before releasing any personal data.
   - The micro/small exemption is lost when you are **subcontracted** to design the product or service (Art. 7(1)). An agency building for a larger client does not bring its own exemption with it.
8. **GDPR still governs personal data.** A Data Act switching or export request never overrides the controller/processor roles, DPAs, retention or transfer rules. Where they conflict, data protection law prevails (Art. 1(5)).
9. **Track the Omnibus** for legacy-contract relief. Do not rely on it for new contracts.

---

## Sources

- [Regulation (EU) 2023/2854 (Data Act), official text (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R2854): Arts. 1-7, 13-16, 23-35, 37, 40-41, 50; Recitals 35, 47, 80-81, 107
- [European Commission, Data Act policy page (updated 2 Jul 2026)](https://digital-strategy.ec.europa.eu/en/policies/data-act)
- [European Commission, Data Act FAQ v1.4, 22 Jan 2026](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-frequently-asked-questions-about-data-act): Q52, Q54, Q58a, Q58b, Q74 ([PDF](https://ec.europa.eu/newsroom/dae/redirection/document/108144))
- [European Commission, Recommendation on non-binding MCTs and cloud SCCs (19 Nov 2025)](https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding)
- [Commission proposal COM(2025) 837, Digital Omnibus (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52025PC0837): Art. 1 (Data Act amendments), Recitals 15, 17-18
- [European Parliament Legislative Train: Digital Omnibus 2025/0360(COD)](https://www.europarl.europa.eu/legislative-train/theme-a-new-plan-for-europe-s-sustainable-prosperity-and-competitiveness/file-digital-package)
- [Directive 2002/58/EC, consolidated (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02002L0058-20091219): interaction with Art. 4(12)

**Last reviewed:** 2026-09-29 (primary sources checked this date).
