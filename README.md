# Claude Team Setup

An onboarding wizard that helps team members configure Claude AI with your company context, personal writing style, and role-specific prompts.

Built with Python (static HTML generator), Cloudflare Pages, and the Claude Code skill system.

![Screenshot placeholder](screenshot.png)

## Features

- 4-tab interface: Overview, Chat, Cowork, Code
- Guided wizard with progress tracking
- Personal writing style profiler (analyzes real writing samples)
- Role-specific prompt cheatsheets
- Company context file installation (brand, operating manual)
- Admin panel for managing tab access
- Install script for one-command setup

## What Users Get

After running the setup, each team member has:

1. `~/.claude/CLAUDE.md` - Personal Claude config
2. `~/.claude/memory/writingstyle.md` - Their writing voice profile
3. `~/.claude/memory/cheatsheet.md` - Role-specific prompts
4. `~/.claude/memory/company.md` - Company operating manual
5. `~/.claude/memory/brand.md` - Brand system reference

## Quickstart

1. Clone this repo
2. Edit content files (`company.md`, `brand.md`, `writing-style.md`, `config.json`)
3. Update `build.py` with your brand colors and title
4. Run `python3 build.py` to generate `index.html`
5. Deploy to Cloudflare Pages (or any static host)
6. Share the install URL with your team

See [DEPLOYING.md](DEPLOYING.md) for detailed setup.
See [CUSTOMIZATION.md](CUSTOMIZATION.md) to swap in your brand.

## How It Works

- `build.py` generates a self-contained `index.html`
- `install.sh` bootstraps a user's Claude environment via curl
- The `/team-setup` skill runs interactively in Claude to collect preferences and generate files
- Admin panel manages per-tab access via Cloudflare KV

## Built With

- [Python](https://python.org/) - Static HTML generator
- [Cloudflare Pages](https://pages.cloudflare.com/) - Hosting
- [Claude Code](https://claude.ai/claude-code) - Skill system

## License

MIT
