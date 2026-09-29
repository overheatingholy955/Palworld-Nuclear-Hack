# Ireland: national regime for data protection, ePrivacy, cybersecurity, AI and accessibility

**Scope of this brief:** the Irish layer on top of the EU frameworks covered in `gdpr.md`, `nis2.md` and `eu-ai-act.md`. Read those first; this file covers only what Ireland adds, changes or enforces differently.

**Main instruments:**
- Data Protection Act 2018 (No. 7 of 2018): gives further effect to GDPR, establishes the Data Protection Commission.
- S.I. No. 336/2011: European Communities (Electronic Communications Networks and Services) (Privacy and Electronic Communications) Regulations 2011 (the "ePrivacy Regulations": cookies and electronic marketing).
- S.I. No. 360/2018: NIS1 transposition, still in force because NIS2 has not been transposed.
- Regulation of Artificial Intelligence Act 2026 (No. 31 of 2026) + S.I. No. 366/2025 (AI Act designation regulations).
- S.I. No. 636/2023: European Union (Accessibility Requirements of Products and Services) Regulations 2023 (European Accessibility Act).

---

## 1. Data Protection Commission (DPC)

**Role:** Ireland's GDPR supervisory authority, and **lead supervisory authority (one-stop-shop) for most large US tech companies**, whose EU headquarters are in Dublin. Also enforces the ePrivacy Regulations (S.I. 336/2011, Regs 17 and 26) and, since 2025, is an AI Act market surveillance authority (see section 4).

**Contact:**
- Web: https://www.dataprotection.ie, complaints and queries via "Contact Us Online"; **breach notifications only via "Report a Breach" on the homepage** (not by phone).
- Post: Data Protection Commission, 6 Pembroke Row, Dublin 2, D02 X963. Second office: Canal House, Station Road, Portarlington, R32 AP23, Co. Laois.
- Phone (general information only, 9.30–13.00 Mon–Fri): (01) 765 01 00 / 1800 437 737.

### Cookies guidance (April 2020, still the operative guidance)

The DPC's *Guidance note on cookies and other tracking technologies* (6 April 2020) gave controllers six months to comply before enforcement. Its positions:

- **Consent is required** for cookies unless strictly necessary for a service the user explicitly requested (Reg. 5(3) and 5(5) of S.I. 336/2011). Consent must meet the GDPR standard.
- **No pre-ticked boxes, sliders or toggles set to "on"** by default.
- **Equal prominence:** if the banner has an "accept" button, it must give equal prominence to "reject" or to a "manage" option that leads to granular choices by cookie type and purpose. Banners with only "OK, got it!" or "I understand" are not acceptable.
- **No implied consent:** "by continuing to browse / scroll / click you agree" is not permissible; banners that vanish on scroll are non-compliant.
- **Analytics cookies require consent.** The DPC adds that first-party analytics limited to aggregated statistics, with clear information and an easy opt-out, is "unlikely" to be an enforcement priority. Unlikely is not exempt.
- **Re-ask after at most six months** where a stored consent record is used.

### DPC activity on AI and LLM training (relevant to anyone deploying or training models)

- **Meta AI training (statement 21 May 2025):** after the DPC raised concerns, Meta paused EU training in June 2024. The DPC then sought an EDPB Opinion (issued December 2024 on AI models). Meta restarted training on EU users' public content from 27 May 2025 after implementing DPC recommendations: a clearer objection form, longer notice period, objection form available for over a year, de-identification, dataset filtering and output filters. This is a **supervision outcome, not a decision or approval**.
- **X / Grok:** in July 2024 X (then Twitter International) refused to stop training Grok on EU user data without key mitigations. The DPC applied to the **High Court under s.134 of the Data Protection Act 2018 on 8 August 2024** (urgent-action power). X undertook to stop processing that data and delete the affected datasets. The DPC opened an inquiry into Grok training on **11 April 2025** and a further investigation into Grok functionality on the X platform, including children's data, on **17 February 2026**.
- **Google PaLM 2:** inquiry opened 12 September 2024 into whether a **DPIA (Art. 35)** was carried out before processing EU personal data to develop the model. Ongoing.
- **LinkedIn €310M (decision notified 22 October 2024):** often cited in AI discussions, but it concerned **behavioural analysis and targeted advertising** (lawfulness, fairness, transparency), not LLM training.
- **DPC AI Insights Report (September 2026)**, "Responsible Artificial Intelligence Innovation: Insights from the DPC's Supervision of AI (2021–2025)". Key positions:
  - Most-cited issue in AI recommendations is **transparency** (135 citations), well ahead of technical and organisational measures (30), Art. 25 (29), data minimisation (28) and legal basis (25).
  - Controllers planning to train AI on existing user data must give **clear notification plus a reasonable notice period** before training starts, so people can object (Arts. 5(1)(a), 12, 13/14). The same applies when a user's data first becomes eligible later, e.g. on turning 18.
  - **Private messages:** the DPC considers it "unlikely" a controller can show users expect their private messages or other private data to be used for AI training, so legitimate interests will be very hard to rely on.
  - The DPC will use s.134 High Court applications where risks are not mitigated.

### Data Protection Act 2018: points that differ from or add to GDPR

| Section | Rule | Practical effect |
|---|---|---|
| **s.31** | **Digital age of consent = 16** for information society services (GDPR Art. 8 default range 13–16) | Consent-based processing of under-16s' data for online services needs parental consent. Preventative/counselling services excluded. |
| **s.29** | "Child" in the GDPR means **under 18** in Ireland | Child-specific GDPR protections (e.g. transparency aimed at children) apply up to 18. |
| **s.30** | Offence for companies to process children's data for direct marketing, profiling or micro-targeting | **Not commenced** (per the Irish Statute Book commencement table, checked 2026-09-29). Do not cite it as law in force. |
| **s.117** | Data protection actions (tort) in Circuit Court or High Court, for injunction, declaration and compensation | Private litigation route alongside DPC complaints. |
| **s.134** | DPC can apply to the High Court for urgent suspension/restriction/prohibition of processing | Used against X in August 2024. |
| **s.141(4)** | Fines on public authorities/bodies (not acting as undertakings) capped at **€1,000,000** | Private companies face the full GDPR Art. 83 ranges. |
| **ss.144–145** | Criminal offences: processor disclosing data without controller authority; obtaining and disclosing data without authority. Up to €50,000 and/or 5 years on indictment | Personal criminal exposure for staff and subcontractors who leak client data. |

---

## 2. ePrivacy Regulations: S.I. No. 336/2011

### Cookies and device access (Reg. 5(3)–(5))
- No storing of, or access to, information on a user's device **unless** the user has consented **and** has been given clear and comprehensive information, prominently displayed and easily accessible, including the purposes (Reg. 5(3)).
- Exemption only for storage/access that is for the sole purpose of transmitting a communication or is **strictly necessary** for a service explicitly requested by the user (Reg. 5(5)).
- Reg. 5(4) mentions browser settings as a possible consent method "where technically possible and effective"; any such consent must still meet the GDPR standard (clear affirmative act), which default browser settings will rarely satisfy.
- Covers any "information" stored on the device: cookies, local storage, pixels, fingerprinting scripts, SDKs in apps.

### Electronic direct marketing (Reg. 13)

| Target | Email / SMS | Phone |
|---|---|---|
| **Individual (natural person), B2C** | **Prior consent** required (Reg. 13(1)), unless the "soft opt-in" applies | Landline: not if they objected or are on the National Directory Database (NDD) opt-out. **Mobile: prior consent** (Reg. 13(6)). |
| **Individual at a work address, B2B** | Consent **not** required if the address "reasonably appears" to be used mainly in their **commercial or official activity** and the message **relates solely to that activity** (Reg. 13(2)) | As above |
| **Company / non-natural person** | Allowed unless the recipient has **told you it does not consent** (Reg. 13(4)) | Not if objected or recorded on the NDD (Reg. 13(3), (5)) |

**Soft opt-in (Reg. 13(11)), all four conditions:** (a) you obtained the email in the context of a **sale** to that customer; (b) you market your **own similar** products or services; (c) the customer was given a free, easy opt-out at collection **and** in every message; (d) the sale, or your last marketing email to them, was **within the previous 12 months**. The 12-month limit is stricter than in many other Member States.

**Every marketing message must:** not disguise the sender, include a valid address for opt-out requests (Reg. 13(10), (12)). **Onus of proving consent is on the sender** (Reg. 13(14)).

**Penalties:** each unsolicited message is a **separate offence** (Reg. 13(13)(b)). Summary conviction: class A fine (up to €5,000, Fines Act 2010) per offence. On indictment: up to **€250,000** for a body corporate, **€50,000** for an individual (Reg. 13(15)). Other ePrivacy offences (including cookie breaches under Reg. 5): class A fine on summary conviction (Reg. 27). The DPC prosecutes summarily (Reg. 26); separately, GDPR administrative fines apply to the personal-data processing involved.

**Enforcement:** DPC for Regs. 5 and 13 (investigation and prosecution); ComReg monitors other parts (Reg. 30), including the NDD.

---

## 3. NIS2 in Ireland: National Cyber Security Bill

**Status as of 2026-09-29: not transposed. No Bill published.**

- The General Scheme of the National Cyber Security Bill was published in **August/September 2024** (DECC); pre-legislative scrutiny on 17 October 2024, but no PLS report before the 2024 dissolution.
- Responsibility has moved to the **Minister for Justice, Home Affairs and Migration** (the NCSC now sits in that Department). On **16 July 2026** the Minister told the Dáil that drafting "is close to finalisation … with a view to its publication in the autumn", after which the Bill "will then commence its passage through the Houses of the Oireachtas" (PQ 390, ref 54126/26).
- The Oireachtas bills database (checked 2026-09-29, entries up to Bill No. 92 of 2026) contains **no National Cyber Security Bill**.
- **The Commission referred Ireland to the CJEU in July 2026** (IP/26/1499) for failing to notify transposition, requesting a lump sum and daily penalties.
- **Until enactment, NIS1 applies:** S.I. 360/2018 remains in full effect for designated operators of essential services and NIS1 digital service providers. The NCSC's NIS2 registration and incident-reporting portals are not live (NCSC NIS2 page, last updated 24 June 2025).

**What the General Scheme proposed (may change in the published Bill):**
- NCSC placed on a statutory footing; CSIRT-IE as national CSIRT.
- Competent authorities by sector (Head 17): CRU (energy, drinking water, waste water); **ComReg (digital infrastructure, ICT service management, space, digital providers)**; Central Bank (banking, financial market infrastructure); IAA (aviation); Commission for Railway Regulation (rail); Minister for Transport (maritime); NTA (road); an agency under the Minister for Health (health); **NCSC for all other sectors**.
- Maximum fines matching NIS2 Art. 34 (essential: greater of €10M or 2% of worldwide turnover).

**Preparatory material already published:** NIS2 Risk Management Measures guidance (draft, June 2025); Ireland is co-owner of the **Cyber Fundamentals (CyFun)** framework, which the NCSC recommends to help essential and important entities organise and evidence their NIS2 measures; NCA forum launched 2024; draft third National Cyber Security Strategy out for consultation (per the July 2026 PQ answer).

**NCSC contact:**
- Web: https://www.ncsc.gov.ie · NIS2 queries: nis2@ncsc.gov.ie · general: contact@ncsc.gov.ie · phone +353 1 678 2333
- Address: National Cyber Security Centre, Department of Justice, Home Affairs and Migration, Tom Johnson House, Haddington Road, Dublin 4, D04 K7X4.
- CSIRT-IE incident response is limited to government and critical national infrastructure constituents; others report cybercrime to An Garda Síochána.

---

## 4. EU AI Act in Ireland: distributed model

**Status as of 2026-09-29: national framework enacted and commenced.**

- **S.I. No. 366/2025**, European Union (Artificial Intelligence) (Designation) Regulations 2025 (made 25 July 2025):
  - The **Minister for Enterprise, Tourism and Employment** designated as a national competent authority and originally as single point of contact.
  - **Central Bank of Ireland** = market surveillance authority for the purposes of Art. 74(6) (the AI Office describes this as "certain prohibited practices and … high-risk AI systems", i.e. those of financial institutions).
  - **Data Protection Commission** = market surveillance authority for the purposes of Art. 74(8) (AI Office: "certain prohibited AI practices and certain High-Risk AI use cases"). The exact Annex III areas are set by AI Act Art. 74(8), see `eu-ai-act.md`.
  - Annex I (product-embedded AI) sector authorities: Health and Safety Authority, CCPC, Marine Survey Office, ComReg, Commission for Railway Regulation, HPRA (medical devices / IVD).
- **Regulation of Artificial Intelligence Act 2026 (No. 31 of 2026)**, signed 21 July 2026:
  - Establishes **Oifig IS na hÉireann (AI Office of Ireland)**. Establishment day **31 July 2026** (S.I. No. 404/2026).
  - The Office replaces the Minister as **single point of contact** for Art. 70(2) (s.42). It coordinates the sectoral authorities, runs AI regulatory sandboxes, maintains a national **AI register** of prohibited-practice incidents and serious incidents, and promotes AI literacy.
  - Enforcement stays with the sectoral market surveillance authorities: authorised officers, contravention and prohibition notices, and an **adjudication model** for administrative fines (independent adjudicators; fines confirmed by the High Court). Fine ceilings follow AI Act Art. 99; public bodies capped at €1,000,000 (s.105).
  - Fundamental-rights bodies with Art. 77 powers include the DPC, Coimisiún na Meán, IHREC, the Ombudsman and others (s.53).
  - **Commencement:** ss.1–77 and 79–139 from **31 July 2026** (S.I. No. 403/2026). Part of s.78 (two limbs of the "applicable market surveillance authority" definition) not yet commenced.
- The AI Office website (https://aioffice.gov.ie/national-competent-authorities) lists **13** national competent authorities, adding the Commission for Regulation of Utilities, Coimisiún na Meán, the HSE, the National Transport Authority and the **Workplace Relations Commission** (AI in the labour market) to those above. The designation of each body for specific Annex III areas beyond S.I. 366/2025 is **UNVERIFIED**: check the current designation regulations before naming the authority for a given use case.
- EU-level application dates (including the AI Omnibus shift of Annex III high-risk obligations) are in `eu-ai-act.md` and are not re-verified here.

**Contact:** AI Office of Ireland, https://aioffice.gov.ie. Department of Enterprise, Tourism and Employment AI Act pages: https://enterprise.gov.ie.

---

## 5. European Accessibility Act in Ireland: S.I. No. 636/2023

**In force from 28 June 2025** (Reg. 1(2)). Made 12 December 2023.

**Services in scope (Reg. 3(2)), provided to consumers:** electronic communications; access to audiovisual media services; websites, apps, e-tickets, travel information and terminals for air, bus, rail and waterborne passenger transport; consumer banking; e-books and dedicated software; **e-commerce services**. Products (Reg. 3(1)): consumer computers and operating systems, payment terminals, ATMs, ticketing/check-in and information kiosks, consumer smartphones and TV-access equipment, e-readers.

**Microenterprise exemption (Reg. 5(4)):** service accessibility requirements **do not apply to services provided by a microenterprise** (fewer than 10 staff **and** turnover or balance sheet ≤ €2M). No exemption for products, and no exemption for SMEs above micro size.

**Other key rules:**
- Content exemptions (Reg. 3(4)): pre-recorded time-based media and office files published before 28 June 2025, archived website content not updated after that date, among others.
- Transitional (Reg. 38): services may keep using products lawfully used before 28 June 2025 until **28 June 2030**; service contracts agreed before 28 June 2025 may run unchanged until expiry, max 5 years; self-service terminals until end of economic life, max 20 years.
- Disproportionate-burden and fundamental-alteration exceptions exist (Reg. 15), based on a documented assessment; microenterprises have lighter documentation and notification duties under that Regulation.

**Authorities (Reg. 4):**

| Area | Authority |
|---|---|
| Products (market surveillance) | Competition and Consumer Protection Commission (CCPC) |
| **E-commerce services**, e-books | **CCPC** |
| Electronic communications, 112 | ComReg |
| Audiovisual media access services | Coimisiún na Meán |
| Air passenger transport services | Irish Aviation Authority |
| Bus, rail, waterborne transport services | National Transport Authority |
| Consumer banking | Central Bank of Ireland |
| Advisory role to all authorities | National Disability Authority |

**Penalties (Reg. 32):** failing to comply with the accessibility requirements (Reg. 5(1)) and certain other duties is an offence. Summary conviction: class A fine (up to €5,000) and/or up to 6 months' imprisonment. On indictment: up to **€60,000** and/or up to 18 months. Directors and managers can be personally liable where the offence is attributable to their consent, connivance or wilful neglect (Reg. 33). Due-diligence defence (Reg. 34).

**Contacts:** CCPC https://www.ccpc.ie · ComReg https://www.comreg.ie · Coimisiún na Meán https://www.cnam.ie · National Disability Authority https://nda.ie.

---

## Regulator contact sheet

| Regulator | Remit here | URL |
|---|---|---|
| Data Protection Commission | GDPR, DPA 2018, ePrivacy cookies + marketing, AI Act MSA (Art. 74(8)) | https://www.dataprotection.ie |
| National Cyber Security Centre / CSIRT-IE | NIS1 now, NIS2 lead once transposed | https://www.ncsc.gov.ie (nis2@ncsc.gov.ie) |
| ComReg | ePrivacy (non-DPC parts, NDD); proposed NIS2 authority for ICT service management and digital providers; EAA e-comms | https://www.comreg.ie |
| AI Office of Ireland (Oifig IS na hÉireann) | AI Act single point of contact and coordinator | https://aioffice.gov.ie |
| Dept. of Enterprise, Tourism and Employment | AI Act policy; national competent authority | https://enterprise.gov.ie |
| CCPC | EAA e-commerce + products; AI Act MSA for certain product areas | https://www.ccpc.ie |
| Central Bank of Ireland | AI Act MSA for financial institutions; EAA consumer banking | https://www.centralbank.ie |

---

## Checklist: Irish-specific items on any web or AI project

- [ ] Cookie banner: reject has equal prominence with accept; no pre-ticked toggles; nothing non-essential (including analytics) fires before consent; consent re-asked within 6 months
- [ ] Any service aimed at or likely used by under-16s: parental-consent path for consent-based processing (s.31); treat under-18s as children for GDPR purposes (s.29)
- [ ] Marketing emails to individuals: consent or valid soft opt-in (sale-based, own similar products, opt-out every time, 12-month window); B2B work-address emails relate solely to the recipient's role; unsubscribe in every message; consent records kept
- [ ] AI training on user data: notice plus a real notice period before training; no private messages; DPIA done before processing
- [ ] Consumer-facing e-commerce, banking, transport or e-comms service: EAA compliance unless the provider is a microenterprise
- [ ] NIS2: assume the client's Irish obligations are not yet law, but its obligations in other Member States and its group procurement policies probably are

---

## Applying this in practice

For a small Dublin-based agency building websites, apps and AI features:

**1. The agency's own position.** It is an Irish-established controller for its own operations and a processor for clients; the DPC is its supervisory authority. It is too small for NIS2 as an entity (see `nis2.md`). Under the EAA the agency is not the "service provider"; its clients are. But if the agency itself has fewer than 10 staff and under €2M turnover, its *own* consumer-facing services would fall under the microenterprise exemption anyway.

**2. Cookies are the most likely enforcement exposure on client sites.** Ship every Irish-facing site with a consent management setup that meets the DPC's 2020 guidance by default: reject-all at the first layer, granular categories, no analytics or marketing tags before opt-in (verify in the browser network tab, not the CMP dashboard), six-month re-consent. Do not rely on the "first-party analytics is not a priority" line as a legal basis.

**3. Outbound email.** Cold email to named individuals at their work address is permitted under Reg. 13(2) only if the message relates solely to their professional role; add an unsubscribe route and honour objections immediately. Anything consumer-facing needs consent. Each non-compliant email is a separate offence, and the burden of proving consent is on the sender, so keep consent logs.

**4. AI features.** If a client wants to fine-tune or train on its existing customer data, build in a notification and notice-period step, an objection mechanism, and a DPIA before any data leaves production, reflecting the DPC's September 2026 report. Rule out private messages and support-chat transcripts as training data unless the client can show a separate, clear basis. For deployed AI in regulated areas, identify the relevant Irish market surveillance authority early (Central Bank for financial institutions, DPC for the Art. 74(8) uses, and check the AI Office list for employment and other Annex III uses).

**5. Accessibility.** For clients running e-commerce or other in-scope consumer services who are not microenterprises, treat WCAG 2.1 AA as the build baseline (its link to the EAA harmonised standard EN 301 549 was not re-verified this session: UNVERIFIED) and document an accessibility statement. The CCPC is the authority for e-commerce. Criminal liability can reach the client's directors, which makes accessibility a sales-relevant point, not a nice-to-have. Confirm microenterprise status in writing before scoping accessibility out.

**6. NIS2 timing.** When the National Cyber Security Bill is published (promised for autumn 2026), check which competent authority ends up covering clients' sectors (ComReg vs NCSC in the General Scheme) and the registration deadline. Until then, prepare the supplier security pack described in `nis2.md` for clients with operations elsewhere in the EU.

---

## Sources

- [Data Protection Act 2018 (No. 7 of 2018), Irish Statute Book, enacted text](https://www.irishstatutebook.ie/eli/2018/act/7/enacted/en/print): ss.29–31, 117, 134, 141, 144–145
- [Data Protection Act 2018 commencement table, Irish Statute Book](https://www.irishstatutebook.ie/eli/isbc/2018_7.html): s.30 not commenced
- [S.I. No. 336/2011 ePrivacy Regulations, Irish Statute Book](https://www.irishstatutebook.ie/eli/2011/si/336/made/en/print): Regs. 5, 13, 17, 26, 27, 30
- [Fines Act 2010, Irish Statute Book](https://www.irishstatutebook.ie/eli/2010/act/8/enacted/en/print): class A fine
- [DPC, Guidance on Cookies and Other Tracking Technologies](https://www.dataprotection.ie/en/dpc-guidance/guidance-cookies-and-other-tracking-technologies)
- [DPC, Guidance note on cookies and other tracking technologies (PDF, April 2020)](https://www.dataprotection.ie/sites/default/files/uploads/2020-04/Guidance%20note%20on%20cookies%20and%20other%20tracking%20technologies.pdf)
- [DPC statement on Meta AI (21 May 2025)](http://www.dataprotection.ie/en/news-media/latest-news/dpc-statement-meta-ai)
- [DPC, LinkedIn Ireland €310M decision press release](https://www.dataprotection.ie/en/news-media/press-releases/irish-data-protection-commission-fines-linkedin-ireland-eu310-million)
- [DPC AI Insights Report (September 2026)](https://www.dataprotection.ie/sites/default/files/uploads/2026-09/DPC-AI-Insights-Report-AC.pdf)
- [DPC, How to contact us](https://www.dataprotection.ie/en/contact/how-contact-us)
- [NCSC, NIS2 page](https://www.ncsc.gov.ie/nis2/) and [NCSC contact page](https://www.ncsc.gov.ie/contact/)
- [Dáil written answer, PQ 390, 16 July 2026 (EU Directives / NIS2)](https://www.oireachtas.ie/en/debates/question/2026-07-16/390/)
- [Oireachtas Library & Research Service briefing on the National Cyber Security Bill (12 June 2025)](https://data.oireachtas.ie/ie/oireachtas/libraryResearch/2025/2025-06-12_briefing-paper-national-cyber-security-bill-2024_en.pdf)
- [Oireachtas bills API (legislation since 2024, queried 2026-09-29)](https://api.oireachtas.ie/v1/legislation?date_start=2024-01-01&limit=1000&lang=en)
- [Commission press release IP/26/1499 (July 2026), NIS2 referral of Ireland](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1499)
- [S.I. No. 366/2025 AI Act Designation Regulations, Irish Statute Book](https://www.irishstatutebook.ie/eli/2025/si/366/made/en/print)
- [Regulation of Artificial Intelligence Act 2026 (No. 31 of 2026), Irish Statute Book](https://www.irishstatutebook.ie/eli/2026/act/31/enacted/en/print) and [commencement table](https://www.irishstatutebook.ie/eli/isbc/2026_31.html)
- [S.I. No. 404/2026 Establishment Day Order](https://www.irishstatutebook.ie/eli/2026/si/404/made/en/print)
- [AI Office of Ireland, National Competent Authorities](https://aioffice.gov.ie/national-competent-authorities)
- [S.I. No. 636/2023 EAA Regulations, Irish Statute Book](https://www.irishstatutebook.ie/eli/2023/si/636/made/en/print)

**Last reviewed:** 2026-09-29 (primary sources checked this date).
