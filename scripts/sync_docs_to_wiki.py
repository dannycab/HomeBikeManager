#!/usr/bin/env python3
"""
Script to copy all markdown files from docs/ to the sibling HomeBikeManager.wiki/ directory.
Usage: Run this script from the project root after updating docs/.
"""
import os
import shutil
import subprocess
from datetime import datetime

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(PROJECT_ROOT, 'docs')
WIKI_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, '../HomeBikeManager.wiki'))

if not os.path.isdir(WIKI_DIR):
    print(f"Wiki directory not found at {WIKI_DIR}. Please clone the wiki repo as a sibling directory.")
    exit(1)

for filename in os.listdir(DOCS_DIR):
    if filename.endswith('.md'):
        src = os.path.join(DOCS_DIR, filename)
        dst = os.path.join(WIKI_DIR, filename)
        shutil.copy2(src, dst)
        print(f"Copied {filename} to wiki.")

# Git add, commit, and push
os.chdir(WIKI_DIR)
subprocess.run(["git", "add", "."])
commit_msg = f"update to wiki {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocess.run(["git", "commit", "-m", commit_msg])
subprocess.run(["git", "push"])
print("All docs copied and pushed to wiki.")
