# Security policy

## Reporting a vulnerability

Please report security issues privately by email to **diego@aiwithdiego.com**. Do not open a public issue or pull request for a vulnerability.

For a prompt-only plugin like this one, the likely issues are instructions in `SKILL.md` or the agent file that could make Claude act unsafely, for example following instructions found in the files it reviews, or running something it should only read. Include the file, the line, and a reproduction.

I'll acknowledge your report within 5 working days.

## Supported versions

Only the latest commit on `main` is supported.
