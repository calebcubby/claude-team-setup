---
name: team-setup
description: Team onboarding for Claude Code. Run /team-setup to set up a new team member's Claude environment with company context, brand guide, personal writing style profile, role-specific cheatsheet, and recommended plugins. Use when onboarding a new employee to Claude, when someone says "set up Claude," or when running first-time Claude Code setup for a team member.
---

# Team Setup - Claude Onboarding

Interactive skill that configures a new team member's Claude environment in one session. Generates personal config files, installs role-specific plugins, and teaches the system.

## Prerequisites

Before running, verify these files exist (install.sh should have placed them):
- `~/.claude/memory/company.md` - Company operating manual
- `~/.claude/memory/brand.md` - Brand reference

If missing, inform the user to run the install script first:
```
curl -sL team.acmecorp.com/claude-setup/install.sh | bash
```

## Workflow

Execute these steps sequentially. Do not skip steps. Ask questions conversationally, not as a form.

### Step 1: Welcome

Display this message:

> Welcome to Acme Corp's Claude setup. I'm going to get you fully configured in about 10 minutes.
>
> When we're done, you'll have:
> - Claude loaded with your company's operating manual, brand, and guardrails
> - A personal writing style profile so Claude sounds like you
> - Role-specific skills and starter prompts
>
> Let's go.

### Step 2: Identity

Ask these questions naturally (not as a numbered list):

- What's your name?
- What's your role/title at Acme Corp?
- What department are you in?
- What's your @acmecorp.com email?

Store all answers for file generation.

### Step 3: Working Style

Ask these three questions. Present options but accept freeform answers:

1. **Communication style** - "When you get feedback, do you prefer people to be direct and blunt, or do you like more context and diplomacy?"
2. **Output length** - "When Claude writes something for you, should it default to concise (shortest path to the answer) or thorough (full context and reasoning)?"
3. **Autonomy** - "Should Claude push back on your ideas and play devil's advocate, or mostly execute what you ask?"

### Step 4: Work Type

Ask: "What best describes your work at Acme Corp?"

- **I build software or apps** (engineering, data, technical)
- **I work with customers or do marketing** (growth, marketing, sales, CS, content)
- **Both**

This determines which plugins to install in Step 8.

### Step 5: Writing Style Questions

Say: "Now let's build your writing voice so Claude sounds like you, not a robot. Seven quick questions."

Ask these one or two at a time, conversationally:

1. "How do you typically open emails to colleagues?" (First name only / "Hi [name]," / "Hey [name]," / Varies by relationship)
2. "How do you sign off?" (Just my name / Thanks, [name] / Best, [name] / No signoff)
3. "How long are your typical emails?" (2-3 sentences / A short paragraph / Multiple paragraphs)
4. "Bullet points or prose?" (Bullets when possible / Paragraphs / Mix depending on content)
5. "How do you deliver bad news or say no?" (Direct, rip the band-aid / Soften it with context first / Depends on the audience)
6. "Do you use humor in professional writing?" (Often / Sometimes with people I know / Rarely)
7. "When you're excited about something, how does it show in your writing?" (Short punchy sentences, maybe caps / Exclamation marks / More detail and energy / Stays pretty even)

### Step 6: Optional Writing Samples

Say:

> Want to paste 3-5 real emails or Slack messages you've written? The more variety the better - a quick reply, a longer update, something where you said no.
>
> **Data privacy reminder:** Do NOT paste anything containing customer PII, financial account numbers, or any data that could identify a specific customer. Internal strategy emails, vendor comms, team updates, and Slack messages are all fine.

If they provide samples, analyze:
- Average sentence length
- Vocabulary patterns (casual vs. formal, jargon usage)
- Greeting and closing patterns
- Tone markers (humor, directness, hedging)
- Punctuation habits (em dashes, exclamation marks, ellipses)
- How they structure arguments (bottom-line first vs. build-up)

Merge sample analysis with question answers. Samples take priority over self-reported answers when they conflict (people are bad at describing their own voice).

If they skip, that's fine. Generate the profile from questions alone.

### Step 7: Generate and Review Writing Style

Generate `writingstyle.md` using the template in [references/writingstyle-template.md](references/writingstyle-template.md).

Show the full generated profile to the user. Say: "Here's your writing style profile. Read it and tell me what's off - I'll adjust."

Iterate until they're satisfied. Then save to `~/.claude/memory/writingstyle.md`.

### Step 8: Install Plugins

Based on Step 4 answer:

**Builds software:**
```
/install-plugin obra/superpowers
```
Tell them: "Installing Superpowers - 13 development skills including test-driven development, systematic debugging, code review, and planning workflows. These activate automatically when relevant."

**Customer/marketing:**
```
/install-plugin coreyhaines31/marketingskills
```
Tell them: "Installing Marketing Skills - 34 skills including copywriting, SEO audit, ad creative, email sequences, and conversion optimization. These activate automatically when relevant."

**Both:** Install both plugins with both messages.

If plugin installation fails, don't block the flow. Note the error and provide manual instructions at the end.

### Step 9: Write Files

Generate and write all files:

1. **Personal CLAUDE.md** - Generate from template in [references/claude-md-template.md](references/claude-md-template.md). Fill in identity, working style, and references. Write to `~/.claude/CLAUDE.md`.
   - **IMPORTANT:** If a CLAUDE.md already exists, read it first. Ask the user if they want to replace it or merge their existing preferences with the company config. Never silently overwrite.

2. **writingstyle.md** - Already saved in Step 7.

3. **cheatsheet.md** - Extract the role-appropriate section from [references/cheatsheets.md](references/cheatsheets.md) based on their department. Write to `~/.claude/memory/cheatsheet.md`.

4. Verify `company.md` and `brand.md` exist in `~/.claude/memory/`. If missing, download from `team.acmecorp.com/claude-setup/`.

### Step 10: Wow Moment

Say: "You're set up. Let's test it. Give me a quick scenario and I'll draft something in your voice."

Suggest options based on their role:
- **Growth/Marketing:** "Draft a Slack message to the team about a campaign win"
- **Product:** "Write a quick feature brief for something you're working on"
- **Engineering:** "Draft a PR description for a recent change"
- **Operations:** "Write a process change announcement"
- **Sales:** "Draft a follow-up email to a prospect"
- **General:** "Write a Slack message declining a meeting request"

Draft the response using their writingstyle.md + company.md context. This proves the system works.

### Step 11: Teach

Walk them through what was installed. Keep it brief:

> Here's what's now in your setup:
>
> 1. **company.md** - Company operating manual. Updated quarterly by leadership. Don't edit this - run `/team-update` to get the latest version.
> 2. **brand.md** - Colors, fonts, logos, design tokens. Full brand reference.
> 3. **writingstyle.md** - Your personal voice profile. Edit this anytime. Add more writing samples later to refine it.
> 4. **CLAUDE.md** - Your personal preferences and config. Edit anytime to change how Claude works with you.
> 5. **cheatsheet.md** - Starter prompts for your role. Open it when you're not sure what to ask.
> 6. **Plugins** - Skills that activate automatically based on what you're working on.
>
> All of these live in `~/.claude/`. They work in every Claude Code conversation, not just this one.

Then show 3 role-specific starter prompts from their cheatsheet and say: "Try one of these next time you open Claude."

End with: "You're good to go. If anything feels off, edit your writingstyle.md or CLAUDE.md. Run `/team-update` anytime to check for company updates."
