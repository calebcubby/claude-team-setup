---
name: team-update
description: Check for and install the latest company files (company.md, brand.md). Run /team-update to pull the latest versions from the team portal. Use when leadership announces an update, when starting a new quarter, or when prompted by Claude that files may be stale.
---

# Team Update

Checks the team portal for the latest company.md and brand.md, compares versions, and updates local copies if newer versions are available.

## Workflow

### Step 1: Check Local Versions

Read the first line of these files to get the current version tag:
- `~/.claude/memory/company.md` - look for `<!-- version: YYYY-QN -->`
- `~/.claude/memory/brand.md` - look for `<!-- version: YYYY-QN -->`

If either file is missing, note it for download in Step 3.

### Step 2: Check Remote Versions

Fetch the latest versions from the team portal:

```bash
curl -sL "team.acmecorp.com/claude-setup/company.md" | head -1
curl -sL "team.acmecorp.com/claude-setup/brand.md" | head -1
```

Compare remote version tags to local version tags.

### Step 3: Update If Needed

**If remote is newer (or local file is missing):**

Download and replace:
```bash
curl -sL "team.acmecorp.com/claude-setup/company.md" -o ~/.claude/memory/company.md
curl -sL "team.acmecorp.com/claude-setup/brand.md" -o ~/.claude/memory/brand.md
```

Report what was updated:

> Updated company.md from [old version] to [new version].
> Updated brand.md from [old version] to [new version].

**If already current:**

> Your company files are up to date (version [version]).

### Step 4: Review Mode (Optional)

If the user runs `/team-update review` (admin only - for writing quarterly updates):

1. Read the current `company.md` in full
2. Walk through each section and ask what changed this quarter:
   - What We're Building Toward (goal progress)
   - Annual Goals (progress, any changes)
   - Key Projects (status updates, new/killed projects)
   - Our Team (new hires, role changes, departures)
   - What We're Solving (retired challenges, new priorities)
   - Guardrails (any new approved/prohibited language)
3. Skip sections that are stable (Who We Are, How We Think, How We Decide, etc.)
4. Generate an updated company.md with the new version tag bumped
5. Show the diff and ask for approval before writing

## Error Handling

- If the team portal is unreachable, report the error and tell the user to try again later
- If curl is not available, provide manual download instructions
- Never silently fail - always report what happened
