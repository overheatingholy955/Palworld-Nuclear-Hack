"""Structural checks for the Hank plugin. Standard library only.

- plugin.json and marketplace.json parse and agree on the plugin name
- every SKILL.md and agent file has name + description frontmatter
- every references/*.md path mentioned in SKILL.md exists, and every
  reference file is mentioned (no orphans)
- every reference brief carries a Sources section and a Last reviewed date
- relative links in any markdown file point at files that exist
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "hank" / "SKILL.md"
REFS = ROOT / "skills" / "hank" / "references"
errors = []


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
        return {}
    keys = dict(
        line.split(":", 1) for line in m.group(1).splitlines() if ":" in line and not line.startswith(" ")
    )
    for key in ("name", "description"):
        if key not in keys:
            errors.append(f"{path.relative_to(ROOT)}: frontmatter has no {key}")
    return keys


plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
if plugin["name"] not in {p["name"] for p in market["plugins"]}:
    errors.append("marketplace.json does not list the plugin named in plugin.json")

frontmatter(SKILL)
for agent in sorted((ROOT / "agents").glob("*.md")):
    frontmatter(agent)

skill_text = SKILL.read_text(encoding="utf-8")
mentioned = set(re.findall(r"references/([a-z0-9-]+\.md)", skill_text))
present = {p.name for p in REFS.glob("*.md")}
for name in sorted(mentioned - present):
    errors.append(f"SKILL.md points at references/{name}, which does not exist")
for name in sorted(present - mentioned):
    errors.append(f"references/{name} is never mentioned in SKILL.md")

for md in sorted(ROOT.rglob("*.md")):
    if ".git" in md.parts:
        continue
    for target in re.findall(r"\]\((?!https?:|mailto:|#)([^)\s]+)\)|`(\.\./[^`\s]+\.md)`", md.read_text(encoding="utf-8")):
        rel = next(t for t in target if t)
        if not (md.parent / rel.split("#")[0]).exists():
            errors.append(f"{md.relative_to(ROOT)}: link to missing file {rel}")

for ref in sorted(REFS.glob("*.md")):
    text = ref.read_text(encoding="utf-8")
    if "## Sources" not in text:
        errors.append(f"references/{ref.name}: no Sources section")
    if not re.search(r"Last reviewed:\*?\*?\s*\d{4}-\d{2}-\d{2}", text):
        errors.append(f"references/{ref.name}: no Last reviewed date")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: skill, {len(list((ROOT / 'agents').glob('*.md')))} agent(s), {len(present)} reference briefs")
