# ePrivacy: cookies, trackers and electronic marketing

**Citation:** Directive 2002/58/EC (the "ePrivacy Directive", ePD), as amended by Directive 2009/136/EC (the 2009 amendment rewrote Art. 5(3) and Art. 13). Consolidated text: 02002L0058-20091219.

**Nature:** It is a **Directive**, not a Regulation. It only binds businesses through each Member State's transposing law. Ireland transposed it with S.I. No. 336 of 2011 (the "ePrivacy Regulations"). Rules, regulators and penalties therefore vary country by country.

**Enforcement:** Member States lay down penalties, which must be "effective, proportionate and dissuasive", and may include criminal sanctions (ePD Art. 15a(1)). The **GDPR one-stop-shop does not apply** to ePrivacy matters (EDPB Cookie Banner Taskforce report, para. 4). Every national regulator can act on the cookie banner of a site aimed at its country. Ireland example: the DPC enforces the cookie rule (Reg. 5). Breaches of the marketing rule (Reg. 13) are criminal offences. **Each message counts as a separate offence**, with fines on indictment of up to **€250,000 for a company** and €50,000 for an individual (Reg. 13(13)(b), 13(15), S.I. 336/2011 as made).

---

## Scope: what the Directive covers

Two provisions matter to almost every business. The rest of the Directive (traffic data, location data, directories, call-line ID) targets telecoms providers.

1. **Art. 5(3): storing or reading information on a user's device.** This covers cookies and every similar technique. It applies to **any website, app or IoT operator**, not only telecoms.
2. **Art. 13: unsolicited direct marketing** by email, SMS, fax or automated calls.

**Art. 5(3) is not limited to personal data.** It protects "any information" on the terminal equipment. This rests on:
- the CJEU in *Planet49* (C-673/17, 1 Oct 2019, ruling point 2): the consent rule is "not to be interpreted differently according to whether or not the information stored or accessed ... is personal data"
- EDPB Guidelines 2/2023, paras. 9-12

Anonymous-sounding identifiers are still in scope.

---

## Art. 5(3): the consent rule

**The text (as amended 2009):** storing information, or gaining access to information already stored, on a subscriber's or user's terminal equipment is allowed only if the user "has given his or her consent, having been provided with clear and comprehensive information, in accordance with Directive 95/46/EC [now GDPR], inter alia, about the purposes of the processing."

**Consent standard = GDPR consent.** The Directive borrows its definition of consent from data protection law. The EDPB Cookie Banner Taskforce confirmed that this reference covers both:
- the definition of consent (GDPR Art. 4(11))
- the conditions for consent (GDPR Art. 7)

Consent must therefore be:
- freely given, specific, informed and unambiguous
- given by a clear affirmative act
- as easy to withdraw as to give

**Pre-ticked boxes are invalid** (*Planet49*, ruling point 1; Taskforce para. 10).

**The only two exemptions** (Art. 5(3), second sentence):
1. **Transmission exemption:** technical storage or access "for the sole purpose of carrying out the transmission of a communication over an electronic communications network". Example: load-balancer routing.
2. **Strictly-necessary exemption:** storage or access "strictly necessary in order for the provider of an information society service explicitly requested by the subscriber or user to provide the service".

Typical items that can qualify as strictly necessary:
- session and authentication cookies
- shopping cart cookies
- security and anti-fraud cookies tied to a service the user requested
- load balancing
- a cookie that stores the user's own consent choice or preferences (Taskforce para. 30, citing WP29 Opinion 04/2012)

Under the current Directive, **analytics, A/B testing, advertising, social plugins, session replay and heatmaps are not strictly necessary.** Some national regulators are reported to tolerate narrowly configured first-party audience measurement without consent. France's CNIL is the usual example. **UNVERIFIED this session:** the current CNIL conditions were not fetched. Treat this as a **national** position, check it per country, and never as an EU-wide exemption.

**Legitimate interests cannot justify placing or reading cookies.** The Taskforce said (para. 24) that "the legal basis for the placement/reading of cookies pursuant to Article 5(3) cannot be the legitimate interests of the controller". If Art. 5(3) consent is missing, the later GDPR processing also cannot be compliant.

---

## EDPB Guidelines 2/2023: technical scope of Art. 5(3)

**Status:** Version 2.0, adopted 7 October 2024 after public consultation. Version 1.0 was adopted on 14 November 2023 for consultation. The guidelines define **when Art. 5(3) applies**. They do **not** analyse the exemptions (para. 56).

**Three cumulative criteria:**
- **A:** "information": personal or non-personal, whoever stored it
- **B:** "terminal equipment" of a subscriber or user, connected to a public communications network
- **C:** "gaining access" or "storage"

**What the EDPB says falls within Art. 5(3):**

| Technique | EDPB position |
|---|---|
| **Tracking pixels** (web and email) | In scope. Distributing the pixel counts as storage, at least through the client cache. Collecting the identifier counts as "gaining access" (paras. 47-51). **Email open-tracking pixels are covered.** |
| **Tracking links / URL parameters** (affiliate IDs, click IDs) | In scope (paras. 49-51). |
| **JavaScript that makes the browser send data back** | In scope. The EDPB treats instructing the browser to send information as "gaining access" (paras. 33, 51). |
| **Local storage, IndexedDB, WebSQL, cache** | Using them purely on the device is not "access". Art. 5(3) applies as soon as the information, **"or any derivation of this information"**, leaves the device (para. 44). |
| **Fingerprinting** (HTTP headers, user agent, ETag, HSTS, etc.) | Using these mechanisms to collect information "can lead to the application of Article 5(3)" (para. 43; WP29 Opinion 9/2014). |
| **Local processing with results sent to a server** (e.g. on-device ad-auction APIs) | In scope once the result is sent off the device (paras. 52-53). |
| **IP-only tracking** | Can be in scope. Unless the entity can ensure the IP does not come from the user's device, it "has to take all the steps pursuant to Article 5(3)". IPv6 and static router IPv4 are named; CGNAT may fall outside (paras. 54-55). |
| **IoT devices** (direct or via a phone or gateway) | The device is terminal equipment. Streaming or cached reporting to a server is "gaining access" (paras. 57-60). |
| **Hashed email / "unique identifier" matching** | In scope. The collecting entity instructs the browser to send the identifier (paras. 61-63). |

**Practical consequence:** "cookieless" tracking is not a way around consent. Examples include server-side tagging fed by client JavaScript, pixels, fingerprinting, hashed-email IDs and IP-based tracking. The test is whether code you distribute makes the device send information back, not whether a cookie is written.

---

## EDPB Cookie Banner Taskforce: what regulators treat as non-compliant

**Source:** *Report of the work undertaken by the Cookie Banner Taskforce*, adopted **17 January 2023**. The report was written to coordinate responses to the noyb complaints. It states a "minimum threshold" agreed by the national regulators. National guidance still applies on top.

| Practice | Taskforce position |
|---|---|
| **Type A: no reject option on the layer that has "Accept"** | A **"vast majority"** of regulators consider it an infringement if the banner offers no refuse/reject option on the same layer as the consent button (para. 8). A few disagreed because Art. 5(3) does not literally require a reject button. **Treat reject-on-first-layer as the baseline.** |
| **Type B: pre-ticked boxes** (including on the second layer) | Invalid consent (para. 10). |
| **Type C: deceptive link design** | "Refuse" or "continue without accepting" hidden as a link in running text, or placed outside the banner without enough visual support, is invalid (para. 14). The banner must not suggest that consent is needed to access the content. |
| **Types D/E: deceptive colours and contrast** | Assessed case by case. There is no mandatory colour standard. A reject button whose text contrast is so low that it is unreadable is "manifestly misleading" (paras. 17-18). |
| **Type H: legitimate interest claimed in deeper layers** | Relying on legitimate interest for "personalised ads" or "content profiles" is doubtful. Making users refuse twice is confusing. Cookies themselves cannot rest on legitimate interest (paras. 22-24). |
| **Type I: misclassified "essential" cookies** | Many sites label non-essential cookies as essential. The site owner must keep a cookie list and **be able to demonstrate why each cookie is essential** (paras. 26-28). |
| **Type K: no way to withdraw** | Withdrawal must be possible at any time and **as easy as giving consent**. A floating icon or a link in a visible, standard place is an example. The specific mechanism is not mandated (paras. 31-35). |

---

## Art. 13: unsolicited communications (email and SMS marketing)

| Situation | Rule (ePD Art. 13) |
|---|---|
| Email, SMS, fax or automated calls to **natural persons** | **Prior consent** (Art. 13(1)). |
| **Soft opt-in** for existing customers | Allowed without consent when all of these hold (Art. 13(2)): (i) contact details were obtained "in the context of the sale of a product or a service"; (ii) the sender markets **its own similar** products or services; (iii) the customer was clearly offered a free, easy opt-out **at collection** and **in every message**. |
| **Legal persons / B2B** | Art. 13(5): paras. (1) and (3) apply to natural persons. For legal persons, Member States only have to protect their "legitimate interests". **B2B rules therefore differ by country.** |
| All marketing email | No disguised sender identity, and a valid address to send opt-outs to (Art. 13(4)). |

**B2B varies by Member State. Ireland (S.I. 336/2011, as made) as a worked example:**
- **Reg. 13(2):** an email to an address that "reasonably appears ... to be an email address used mainly by the subscriber or user in the context of their commercial or official activity", about that activity only, is **not** treated as marketing to a natural person. Consent is therefore not required.
- **Reg. 13(4):** marketing emails to a business (non-natural-person) subscriber are prohibited only once it has **notified you it does not consent**. This is an opt-out regime.
- **Reg. 13(11)(d):** Ireland adds a **12-month limit** to the soft opt-in. The sale must have happened no more than 12 months before the message, or the details must have been used for marketing within that period.
- **Reg. 13(14):** in a prosecution, the **sender must prove consent**.
- Other Member States are stricter. Several require consent even for B2B email. **UNVERIFIED this session:** a per-country B2B table. Check the national regulator before any cross-border campaign.

**GDPR still applies alongside.** A B2B email to a named person is personal data. It needs a GDPR lawful basis (usually legitimate interests backed by a written legitimate interests assessment, an LIA), an Art. 14 notice for data you collected indirectly, and an absolute right to object to direct marketing.

---

## The ePrivacy Regulation: withdrawn

- The proposal COM(2017) 10 was meant to replace the Directive with a directly applicable Regulation.
- The Commission's 2025 work programme announced it would be withdrawn: "no foreseeable agreement" and "outdated".
- The Commission approved the withdrawal at its 2533rd meeting on **16 July 2025**.
- The withdrawal was published in the Official Journal on **6 October 2025 (OJ C/2025/5423)** (European Parliament Legislative Train).
- **The 2002 Directive, as amended in 2009, remains the law**, through national transposing acts.

---

## The Digital Omnibus: proposed cookie reform (NOT law)

**What it is:** Commission proposal **COM(2025) 837**, dated **19 November 2025**, procedure **2025/0360(COD)**. It amends the GDPR, the ePD, the Data Act, NIS2 and others. The AI Act changes run in a separate file (see `eu-ai-act.md`).

**What the Commission proposed on cookies (proposal text, EUR-Lex):**

- **New GDPR Art. 88a.** Storing or accessing **personal data** on a natural person's device would be governed by the GDPR, not ePD Art. 5(3).
  - Consent stays the default (88a(1)).
  - **No consent needed** where strictly necessary for (88a(3)):
    - (a) transmission
    - (b) a service the data subject explicitly requested
    - (c) **aggregated audience measurement by the controller of the online service "solely for its own use"**
    - (d) security of the service or the device
  - **Single-click refusal** (88a(4)(a)).
  - **No new consent request for the same purpose for at least 6 months after a refusal** (88a(4)(c)).
  - No repeat request while an existing consent is still valid (88a(4)(b)).
  - Would apply **6 months after entry into force** (88a(5)).
- **New GDPR Art. 88b.** Controllers' interfaces must accept consent, refusal and objection given through **automated, machine-readable signals** (for example browser settings), with harmonised standards to follow.
  - Would apply 24 months after entry into force (88b(5)).
  - Non-SME **browser providers** must provide the technical means 48 months after entry into force (88b(6)-(7)).
  - Media service providers are exempt (88b(3)).
- **ePD Art. 5(3) amended.** A new subparagraph says Art. 5(3) "shall not apply if the subscriber or user is a natural person, and the information stored or accessed constitutes or leads to the processing of personal data". **Art. 5(3) would remain for non-personal data and for legal persons.**
- **ePD Art. 4 deleted.** Telecoms security and breach notification would move to GDPR and NIS2.
- **GDPR Art. 88c** (legitimate interests for AI development) is in the same package. It is not a cookie rule.

**Legislative status as of 29 September 2026: still a proposal. No change to cookie law is in force.**
- **Parliament:** first reading, not finished. The LIBE and ITRE committees discussed the draft report jointly on **13 July 2026**. The amendment deadline was 15 July, and **more than 1,750 amendments** were tabled. No committee vote is reported (EP Legislative Train, page updated 1 Aug 2026).
- **Council:** **no negotiating mandate.** The COREPER II vote planned for **26 June 2026** was cancelled because Member States disagreed (EP Legislative Train). The Cyprus Presidency handed the file to the Irish Presidency. The Irish Presidency circulated a compromise dated 3 September, examined by the Antici simplification group on 11 September. A further compromise was reportedly tabled around 18-21 September. It aims for a Council-Parliament deal by year-end.
- **Trilogues:** not started.
- **What the Council compromises did with cookies.** These texts are not public, so this rests on press reports (Agence Europe, 27 Jun, 16 Jul, 8 Sep 2026):
  - **Art. 88b** (automated browser signals) and **Art. 88c** (AI legitimate interest) were **deleted**.
  - Discussion has moved toward an **expanded "white list" of consent exemptions**, including fraud detection and prevention, contextual advertising, and audience measurement where data is "pseudonymised immediately after collection and anonymised before being shared with third parties".
  - **UNVERIFIED:** whether the current Council text keeps the move into GDPR Art. 88a or amends ePD Art. 5(3) in place. Several secondary sources say the relocation was removed in June 2026. Agence Europe describes the exemptions in ePrivacy terms. The primary texts are not available.
- **Bottom line:** do not design banners around single-click-reject-plus-6-month-moratorium or browser signals as legal requirements. Current law is ePD Art. 5(3) as transposed nationally, plus EDPB and national guidance.

---

## How ePrivacy, GDPR and the Data Act interact

| Layer | Governs | Key hook |
|---|---|---|
| **ePD Art. 5(3)** (national law) | The **act of storing or reading** information on a device, personal or not | Consent unless strictly necessary. No legitimate interests. No one-stop-shop. |
| **GDPR** | **All later processing** of personal data obtained that way, plus the definition and conditions of consent | Taskforce paras. 1-3; EDPB Opinion 5/2019 (cited there). If Art. 5(3) fails, the GDPR processing fails too (Taskforce para. 24). |
| **ePD Art. 13** + GDPR | Marketing channel rules (ePD) + lawful basis, transparency and the right to object (GDPR) | Both must be satisfied. |
| **Data Act** (Reg. 2023/2854) | Access to and portability of connected-product data, B2B data terms, cloud switching | Art. 1(5): "without prejudice to" the GDPR **and Directive 2002/58/EC**. In a conflict, data protection and privacy law **prevails**. |

**Where they collide in practice:**
- **Data Act Art. 4(12).** When a connected-product user asks for data that includes someone else's personal data, the data holder may release it only if there is a GDPR Art. 6 basis, Art. 9 where relevant, **"and of Article 5(3) of Directive 2002/58/EC"**. Reading data off a device to meet a Data Act request is still a terminal-equipment access.
- **EDPB Guidelines 2/2023 treat IoT devices as terminal equipment.** The IoT data flows the Data Act opens up are also subject to Art. 5(3) consent or exemption analysis.
- **Data Act access rights complement GDPR Arts. 15 and 20** (Art. 1(5)). They cover non-personal and passively observed data, and they apply regardless of the GDPR legal basis (Recital 35).
- **If the Omnibus passes in its Commission form,** personal-data device access moves to GDPR (Art. 88a) and gains one-stop-shop and GDPR-level fines. Non-personal device access stays in ePD. This creates a split regime. Not law yet.

---

## Website audit checklist

**1. What fires before consent** (test in a clean browser profile, EU IP, no interaction):
- [ ] DevTools > Application: list every cookie, localStorage, sessionStorage and IndexedDB entry **before** clicking anything. Every entry must be strictly necessary.
- [ ] DevTools > Network: list every third-party request before consent, including analytics, ad pixels, tag managers loading vendor tags, chat widgets, embedded video, fonts from third-party CDNs, and session replay. **A request that makes the browser send an identifier counts as access, even with no cookie written** (EDPB 2/2023).
- [ ] Check server-side tagging endpoints. First-party-domain collection that is fed by client JavaScript is still Art. 5(3) access.
- [ ] Check email templates for open-tracking pixels and click-tracking link IDs. These are in scope under EDPB 2/2023 paras. 47-51.

**2. Banner design:**
- [ ] "Reject all" appears on the **same layer** as "Accept all", with equal prominence. No link-only reject. No low-contrast reject.
- [ ] No pre-ticked categories on any layer.
- [ ] No "legitimate interest" toggles for tracking or ad purposes.
- [ ] Purposes and recipients are explained on the banner. There is a link to the full cookie list.
- [ ] No cookie wall and no wording implying that consent is required to use the site.

**3. After a choice:**
- [ ] After Reject, reload and navigate, then re-check the Network and Application tabs. Nothing non-essential appears.
- [ ] After Accept, then withdraw: tags stop, and non-essential cookies are deleted or expired where possible.
- [ ] A persistent, easy withdrawal route exists (footer link or floating icon). Withdrawal takes no more clicks than consent.

**4. Classification and documentation:**
- [ ] A cookie and tracker inventory with name, provider, purpose, duration, first or third party, and category. **Each "essential" label has a written justification** (Taskforce para. 28).
- [ ] Analytics treated as consent-required by default. Use a no-consent audience-measurement configuration only where the **national regulator** in that market explicitly allows it. Document which regulator and which configuration.
- [ ] Re-scan after every release that adds a tag.

**5. Consent logging (proof, GDPR Art. 7(1)):**
- [ ] Record: timestamp, banner/policy version, choices per purpose, and a pseudonymous consent ID. Do not log raw IPs unless justified.
- [ ] Keep enough to show what the user saw and chose. Retention matches the consent lifetime plus a reasonable evidence window.
- [ ] Consent and preference cookies are themselves exempt (Taskforce para. 30).

**6. Google Consent Mode caveats:**
- [ ] Consent Mode **is not a consent mechanism**. It signals consent states (`ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`) collected by your consent management platform (CMP).
- [ ] **Basic mode:** tags do not load until consent. Google: "No data is sent before a user consents - not even the default consent status."
- [ ] **Advanced mode:** tags load before consent and, when consent is denied, send **"cookieless pings"** to Google. These include a timestamp, user agent, referrer, consent state, a per-page random number, and GCLID/DCLID if present in the URL (Google developer docs). Under EDPB 2/2023 (JavaScript instructing the browser to send information; URL click IDs), **these pings are likely Art. 5(3) access without consent.** Hank's default is basic mode for EU traffic, unless a national regulator's position supports advanced mode.
- [ ] Google requires consent signals for EEA traffic to keep ad personalisation and measurement features (Google Ads Help "Updates to consent mode for traffic in EEA"; Customer Match requires both `ad_user_data` and `ad_personalization` granted from March 2024). This is a contractual requirement from Google, **not** a legal safe harbour.
- [ ] Default state for EEA visitors = all `denied`, set **before** any Google tag fires.

**7. Email marketing:**
- [ ] For each list: its source, lawful basis (consent or soft opt-in), date of the underlying sale (the Irish 12-month limit), and an opt-out in every message.
- [ ] B2B lists: identify the recipient's country and apply that country's Art. 13 rule.

---

## Applying this in practice

For a small agency that builds and hosts websites, apps and AI features for clients:

1. **The client is usually the party that places the cookies.** It decides the tags, so it answers for Art. 5(3) and is the GDPR controller. The agency is the processor or implementer. The agency is still the one in control of what fires, so run the checklist above **before every launch and after every tag change**, and put the result in the handover pack.
2. **Ship privacy-by-default templates.** Tag managers default to denied. Basic Consent Mode for EU traffic. Reject on the first layer. No third-party embeds until consent (click-to-load placeholders for video and maps). Fonts self-hosted.
3. **Do not sell "cookieless" as "consent-free".** Server-side tagging, fingerprint-based analytics and hashed-email matching are all in scope under EDPB 2/2023. Only a narrow first-party audience measurement set-up, where a national regulator permits it, avoids consent today.
4. **AI chat widgets and agents on websites.** Chat session IDs stored in localStorage and sent back are strictly necessary only for a chat the user actually opened. Loading a third-party widget script that sets identifiers or phones home **on page load, before the user interacts**, needs consent. Load it on click.
5. **Do not re-architect for the Omnibus yet.** Single-click reject is already expected under the Taskforce view, so build it now. The 6-month re-ask moratorium and browser-signal compliance are proposals. Re-check the Omnibus status every quarter until trilogues conclude.
6. **Outbound email for the agency itself.** Check the recipient's country B2B rule, keep an LIA for GDPR, include an opt-out and sender identity in every email, and keep a suppression list. In Ireland, business-address emails about the recipient's role are workable without consent. Elsewhere they may not be.
7. **Contract wording.** In client contracts, make the client responsible for approving the cookie list and banner text, and the agency responsible for implementing the configuration exactly as documented.

---

## Sources

- [Directive 2002/58/EC, consolidated 19.12.2009 (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02002L0058-20091219): Arts. 5(3), 13, 15a
- [CJEU C-673/17 *Planet49*, 1 Oct 2019 (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62017CJ0673)
- [EDPB Guidelines 2/2023 on Technical Scope of Art. 5(3) ePD, v2.0, 7 Oct 2024 (PDF)](https://www.edpb.europa.eu/system/files/2024-10/edpb_guidelines_202302_technical_scope_art_53_eprivacydirective_v2_en_0.pdf)
- [EDPB Report of the Cookie Banner Taskforce, 17 Jan 2023 (PDF)](https://www.edpb.europa.eu/system/files/2023-01/edpb_20230118_report_cookie_banner_taskforce_en.pdf)
- [European Parliament Legislative Train: ePrivacy Regulation (withdrawn, OJ C/2025/5423)](https://www.europarl.europa.eu/legislative-train/theme-connected-digital-single-market/file-jd-e-privacy-reform)
- [Commission proposal COM(2025) 837, Digital Omnibus, 19 Nov 2025 (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52025PC0837): Arts. 3 (GDPR 88a-88c), 5 (ePD amendments)
- [European Parliament Legislative Train: Digital Omnibus 2025/0360(COD), updated 1 Aug 2026](https://www.europarl.europa.eu/legislative-train/theme-a-new-plan-for-europe-s-sustainable-prosperity-and-competitiveness/file-digital-package)
- Agence Europe (press, secondary): [27 Jun 2026, Cyprus Presidency hands Omnibus to Ireland](https://agenceurope.eu/en/bulletin/article/13897/15/cyprus-presidency-of-eu-council-hands-digital-omnibus-over-to-ireland-for-lack-of-agreement-between-member-states); [16 Jul 2026, Irish consultation](https://agenceurope.eu/en/bulletin/article/13910/11/digital-omnibus-irish-presidency-consults-eu-countries-on-pseudonymisation-data-processing-for-ai-and-cookies); [8 Sep 2026, Irish compromise options](https://agenceurope.eu/en/bulletin/article/13933/12/pseudonymised-data-cookies-irish-presidency-of-eu-council-sets-out-compromise-options-on-digital-omnibus)
- [S.I. No. 336/2011 (Ireland), Irish Statute Book, as made](https://www.irishstatutebook.ie/eli/2011/si/336/made/en/print): Regs. 5, 13, 27
- [Google Tag Platform: Consent mode concepts (basic vs advanced)](https://developers.google.com/tag-platform/security/concepts/consent-mode)
- [Google Ads Help: Updates to consent mode for EEA traffic](https://support.google.com/google-ads/answer/13695607?hl=en)
- [Regulation (EU) 2023/2854 Data Act (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R2854): Arts. 1(5), 4(12)

**Last reviewed:** 2026-09-29 (primary sources checked this date).
