# Hank

**An AI security and EU compliance analyst for Claude Code.**

Hank is the reviewer I use on my own work and on client projects. He does two jobs:

- **Security review** of anything with an AI surface: LLM calls, prompts, RAG pipelines, MCP servers, agents. Checked against the OWASP Top 10 for LLM Applications (2025) and the OWASP Top 10 for Agentic Applications, with findings mapped to MITRE ATLAS techniques.
- **EU compliance review** of any project, AI or not. A brochure site with a contact form and analytics counts. He works out which laws apply, checks the project against them, and names the article behind every finding.

He reads and reports. He edits no files unless you ask, active security tests only run against a staging environment you own, and his compliance output is analysis, not legal advice.

## Install

Inside Claude Code:

```text
/plugin marketplace add aiwithdiego/hank
/plugin install hank@hank-security
```

Or from a shell: `claude plugin marketplace add aiwithdiego/hank`, then `claude plugin install hank@hank-security`.

This installs a skill (`hank`) and a subagent (`hank`). The subagent runs the same method in its own context, statically: it reads and reports, and leaves any active testing to you.

## Use

Ask in plain language:

> "Hank, review the chatbot endpoint for prompt injection."
> "Check our MCP server before we publish it."
> "Does this site need a cookie banner, and is ours compliant?"
> "We're pitching an insurer. What will DORA mean for our contract?"
> "Is our AI feature high-risk under the AI Act?"
> "Review this DPA."

## What he covers

| Area | Frameworks |
|---|---|
| AI security | OWASP LLM Top 10 (2025), OWASP Agentic Top 10, MITRE ATLAS mapping, MCP-specific checks (tool poisoning, rug pulls, cross-server shadowing) |
| Data protection | GDPR, UK GDPR notes, ePrivacy (cookies, tracking, e-marketing) |
| AI regulation | EU AI Act as amended by Regulation (EU) 2026/1744 |
| Cybersecurity law | NIS2, Cyber Resilience Act, DORA |
| Data and cloud | Data Act (switching, egress charges, unfair B2B terms) |
| Standards | ISO/IEC 27001, ISO/IEC 42001, SOC 2, NIST AI RMF |
| National example | Ireland: Data Protection Commission, Data Protection Act 2018, S.I. 336/2011 |

Every compliance review starts with the same question: which of these actually apply to this project? One incident can start four reporting clocks with four different regulators, and one website can owe consent under ePrivacy even when no personal data is involved. Hank maps that first, then opens only the rules that apply.

## How it's built

```text
skills/hank/SKILL.md        the working method: both modes, checklists, report format
skills/hank/references/     one brief per framework, with sources and a review date
agents/hank.md              subagent that runs the review in an isolated context
```

`SKILL.md` stays short enough to load on every review. The briefs hold the detail and get read only when a question needs it.

Every brief ends with its sources and a "Last reviewed" date. The EU briefs were checked against EUR-Lex, the Commission, the EDPB, ENISA and national regulators on 29 September 2026. EU law moved a lot in 2025 and 2026: the AI Act was amended, and the Digital Omnibus proposals on GDPR, cookies and the Data Act are still going through Parliament and Council. Hank separates what is law from what is only proposed, and he is told to check a primary source when a question depends on something newer than a brief.

## Limits

- **Not legal advice.** Hank tells you which rule applies, what the gap is and what to fix. For anything material he writes the exact question to take to a lawyer or DPO.
- **Dated knowledge.** The briefs are as good as their review date. Check the date on the brief before relying on a deadline.
- **Security testing needs a target you own.** Mode 1 sends real attack payloads. Point it at your own dev or staging environment.

## License

[MIT](LICENSE) © 2026 Diego Bauer
