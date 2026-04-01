#!/bin/bash
# Acme Corp Claude Setup - Bootstrap Script
# Run: curl -sL team.acmecorp.com/claude-setup/install.sh | bash

set -e

BASE_URL="https://team.acmecorp.com/claude-setup"
CLAUDE_DIR="$HOME/.claude"
SKILLS_DIR="$CLAUDE_DIR/skills"
MEMORY_DIR="$CLAUDE_DIR/memory"

echo ""
echo "  Setting up Claude for Acme Corp..."
echo ""

# Check for curl
if ! command -v curl &> /dev/null; then
    echo "  Error: curl is required but not installed."
    echo "  On Mac: it should be pre-installed. Try restarting Terminal."
    exit 1
fi

# Create directories
mkdir -p "$SKILLS_DIR/team-setup/references"
mkdir -p "$SKILLS_DIR/team-update"
mkdir -p "$MEMORY_DIR"

echo "  Downloading files..."

# Download /team-setup skill + references
curl -sfL "$BASE_URL/skill/SKILL.md" -o "$SKILLS_DIR/team-setup/SKILL.md" || {
    echo "  Error: Could not download team-setup skill. Check your internet connection."
    exit 1
}
curl -sfL "$BASE_URL/skill/references/cheatsheets.md" -o "$SKILLS_DIR/team-setup/references/cheatsheets.md"
curl -sfL "$BASE_URL/skill/references/claude-md-template.md" -o "$SKILLS_DIR/team-setup/references/claude-md-template.md"
curl -sfL "$BASE_URL/skill/references/writingstyle-template.md" -o "$SKILLS_DIR/team-setup/references/writingstyle-template.md"

# Download /team-update skill
curl -sfL "$BASE_URL/skill-update/SKILL.md" -o "$SKILLS_DIR/team-update/SKILL.md"

# Download company files
curl -sfL "$BASE_URL/company.md" -o "$MEMORY_DIR/company.md"
curl -sfL "$BASE_URL/brand.md" -o "$MEMORY_DIR/brand.md"

echo ""
echo "  Done. Here's what was installed:"
echo ""
echo "    ~/.claude/skills/team-setup/       - Onboarding skill"
echo "    ~/.claude/skills/team-update/      - Company file updater"
echo "    ~/.claude/memory/company.md        - Acme Corp operating manual"
echo "    ~/.claude/memory/brand.md          - Brand reference"
echo ""
echo "  Next steps:"
echo "    1. Open Terminal"
echo "    2. Type: claude"
echo "    3. Type: /team-setup"
echo ""
echo "  Claude will walk you through the rest."
echo ""
