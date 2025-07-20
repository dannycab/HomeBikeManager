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
WIKI_SRC_DIR = os.path.join(PROJECT_ROOT, 'wiki')
WIKI_DST_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, '../HomeBikeManager.wiki'))

if not os.path.isdir(WIKI_DST_DIR):
    print(f"Wiki directory not found at {WIKI_DST_DIR}. Please clone the wiki repo as a sibling directory.")
    exit(1)

# Copy all files from wiki/ to the wiki repo (HomeBikeManager.wiki/)
for filename in os.listdir(WIKI_SRC_DIR):
    src = os.path.join(WIKI_SRC_DIR, filename)
    dst = os.path.join(WIKI_DST_DIR, filename)
    if os.path.isfile(src):
        shutil.copy2(src, dst)
        print(f"Copied {filename} to wiki.")

# Git add, commit, and push
os.chdir(WIKI_DST_DIR)
subprocess.run(["git", "add", "."])
commit_msg = f"update to wiki {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocess.run(["git", "commit", "-m", commit_msg])
subprocess.run(["git", "push"])
print("All wiki pages copied and pushed to wiki repo.")
