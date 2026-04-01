#!/usr/bin/env python3
"""Sensitivity test - scans all repo files for blocklisted terms.

Run: python3 test_sensitivity.py
Exit code 0 = clean, 1 = matches found.
"""
import os
import sys
import re

# Each entry is either a plain string (substring match) or a tuple ("term", True) for word-boundary match.
# Use word-boundary for short terms that could appear as substrings in common words (e.g., "dme" in "README").
BLOCKLIST = [
    # Company
    "cubby", "cubbybeds", "cubby beds", "dreamteam",
    # People
    "caleb", "polley", "crpolley",
    "emilie", "rosalee", "alexis w",
    "brittany", "trevor k", "megan d",
    "irvin c", "justin o", "katie k", "matt m",
    "zoe s", "tom f", "alex w",
    # Contact
    "720-829", "3282 w 19th", "crpolley@gmail",
    "caleb@cubbybeds",
    # Domains
    "cubbybeds.com", "dreamteam.cubbybeds",
    # Brand (exact Cubby hex values)
    "#444963", "#facd7a", "#108474",
    # Business context
    "medtech", "safety bed", ("dme", True), "medicaid",
    "hipaa", "protected health information",
    "fda class", "complex care", ("e1399", True),
    "autism", "epilepsy", "cerebral palsy",
    "enclosed safety bed",
    # Infrastructure
    "34d792cf", "caleb-0bc.workers.dev",
    # API keys (patterns)
    "sk-ant-",
    # Email domain
    "@cubbybeds.com",
]

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".pytest_cache"}
SKIP_FILES = {"test_sensitivity.py"}  # Don't flag ourselves
BINARY_EXTS = {".xlsx", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2", ".ttf", ".pdf"}


def _match(term, text_lower):
    """Check if a blocklist entry matches in text. Supports word-boundary tuples."""
    if isinstance(term, tuple):
        word, _ = term
        return bool(re.search(r'\b' + re.escape(word.lower()) + r'\b', text_lower))
    return term.lower() in text_lower


def _term_str(term):
    """Get display string for a blocklist entry."""
    return term[0] if isinstance(term, tuple) else term


def scan_file(filepath, patterns):
    """Scan a single file for blocklist matches. Returns list of (line_num, term, line_text)."""
    matches = []
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line_num, line in enumerate(f, 1):
                line_lower = line.lower()
                for pattern in patterns:
                    if _match(pattern, line_lower):
                        matches.append((line_num, _term_str(pattern), line.strip()))
    except (OSError, UnicodeDecodeError):
        pass
    return matches


def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    patterns = BLOCKLIST
    total_matches = 0
    files_scanned = 0

    for dirpath, dirnames, filenames in os.walk(repo_root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

        for filename in filenames:
            if filename in SKIP_FILES:
                continue
            ext = os.path.splitext(filename)[1].lower()
            if ext in BINARY_EXTS:
                continue

            filepath = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(filepath, repo_root)

            # Check filename itself
            fname_lower = filename.lower()
            for pattern in patterns:
                if _match(pattern, fname_lower):
                    print(f"FILENAME: {rel_path} matches '{_term_str(pattern)}'")
                    total_matches += 1

            # Check file contents
            matches = scan_file(filepath, patterns)
            files_scanned += 1
            for line_num, term, line_text in matches:
                print(f"{rel_path}:{line_num}: '{term}' -> {line_text[:120]}")
                total_matches += 1

    print(f"\n{'PASS' if total_matches == 0 else 'FAIL'}: {total_matches} blocklist matches found across {files_scanned} files.")
    sys.exit(0 if total_matches == 0 else 1)


if __name__ == "__main__":
    main()
