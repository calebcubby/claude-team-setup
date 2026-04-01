# Personal CLAUDE.md Template

> The /team-setup skill fills in placeholders based on onboarding answers. Sections marked {{PLACEHOLDER}} are replaced during generation.

---

```markdown
# {{NAME}} - Claude Config

## Identity

- **Name:** {{NAME}}
- **Role:** {{ROLE}}
- **Department:** {{DEPARTMENT}}
- **Email:** {{EMAIL}}

---

## How I Work

{{WORKING_STYLE}}

---

## Reference Files

These files live in `~/.claude/memory/` and load automatically:

- **company.md** - Company operating manual. How the company works, values, decisions, guardrails. Updated quarterly by leadership. Don't edit - run `/team-update` to get the latest.
- **brand.md** - Colors, fonts, logos, design tokens. Full brand reference for any design or content work.
- **writingstyle.md** - Your personal writing voice profile. Edit anytime. Add more writing samples to refine it.
- **cheatsheet.md** - Starter prompts for your role. Open when you're not sure what to ask.

---

## Data Privacy - Non-Negotiable

**NEVER put sensitive customer data into Claude.** This includes:
- Customer names, addresses, phone numbers, emails, dates of birth
- Account numbers, payment details, Social Security numbers
- Device serial numbers linked to customers
- Any data that could identify a specific customer or individual

**Safe to discuss:** Anonymized/aggregated data, fake/test data marked as such, code, schemas, UI designs, business logic, general product categories.

Your company may have additional data handling policies. Follow them. When in doubt, anonymize first.

---

## Anti-Patterns

- Don't summarize what I said back to me. Skip to analysis.
- Don't hedge when I ask for a recommendation. Pick a side.
- Don't be verbose. If it can be said in 2 sentences, don't use 5.
- Don't use filler words: "just," "really," "very," "actually," "basically."
- Refer to company.md for company context, brand.md for design, writingstyle.md for my voice.
```

---

## Placeholder Reference

| Placeholder | Source | Example |
|-------------|--------|---------|
| `{{NAME}}` | Step 2: name | Jordan Rivera |
| `{{ROLE}}` | Step 2: role | VP Growth |
| `{{DEPARTMENT}}` | Step 2: department | Growth |
| `{{EMAIL}}` | Step 2: email | jordan@acmecorp.com |
| `{{WORKING_STYLE}}` | Step 3: generated from answers | See below |

### Working Style Generation

Based on Step 3 answers, generate a `{{WORKING_STYLE}}` block like:

**If direct + concise + push back:**
```
- Be direct and blunt with feedback. Don't soften bad news.
- Default to concise output. Shortest path to the answer.
- Push back on my ideas. Play devil's advocate. Tell me what's wrong before what's right.
```

**If diplomatic + thorough + execute:**
```
- Give context with feedback. Explain the reasoning.
- Default to thorough output. Full context and supporting details.
- Execute what I ask. Save pushback for when something is clearly wrong.
```

**If mixed:** Combine relevant lines from each. Most people are mixed.
