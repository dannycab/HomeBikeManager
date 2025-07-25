# Project Status (July 2025)

| Feature                        | Status      | Notes                                             |
|--------------------------------|-------------|---------------------------------------------------|
| sync_docs_to_wiki.py           | Built       | Automates copying docs/ to the Wiki repo           |
| Other automation scripts       | Planned     | More scripts may be added in the future            |

**Summary:**
- sync_docs_to_wiki.py is built and automates copying docs/ to the Wiki repo.
- More automation scripts may be added in the future.
# Automation Scripts

This project includes helper scripts for common development and maintenance tasks.

## sync_docs_to_wiki.py
Copies all markdown files from docs/ to the sibling HomeBikeManager.wiki/ directory. Run this script from the project root after updating docs/ to keep the GitHub Wiki in sync.

### Usage
1. Ensure you have cloned the wiki repo as a sibling directory:
   git clone https://github.com/dannycab/HomeBikeManager.wiki.git ../HomeBikeManager.wiki
2. Run the script:
   python scripts/sync_docs_to_wiki.py
3. Review, commit, and push changes in the wiki repo as needed.

---

More automation scripts may be added in the future. See this file for updates.
