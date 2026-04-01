# Customization Guide

## 1. Company Context (`company.md`)

Replace the Acme Corp example with your company info:
- Who you are and what you build
- Org structure and department leads
- Values and working norms
- Tools and tech stack
- Data privacy / compliance rules

## 2. Brand System (`brand.md`)

Replace with your design tokens:
- Color palette (primary, semantic, extended)
- Typography (fonts, weights, sizes)
- Spacing and radius tokens
- Voice and tone guidelines

## 3. Writing Style (`writing-style.md`)

Replace with your exec/founder's writing voice. The `/team-setup` skill uses this as a reference when profiling team members.

## 4. Config (`config.json`)

Update company name, domain, departments, and admin emails.

## 5. Brand Colors in `build.py`

Find the `:root` CSS custom properties block and replace the color values. See the comments for which variable maps to which UI element.

Key variables: `--navy`, `--gold`, `--teal`, `--blue`, `--cream`

## 6. Skill Content

Update the prompts in `skill/references/cheatsheets.md` to match your team's actual workflows and tools.

Update the compliance section in `skill/references/claude-md-template.md` to match your industry requirements.

## 7. Install Script (`install.sh`)

Update the `BASE_URL` to point to your deployed instance.

## 8. Rebuild

```bash
python3 build.py
python3 -m pytest test_build.py -v
python3 test_sensitivity.py
```
