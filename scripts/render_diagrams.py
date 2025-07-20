#!/usr/bin/env python3
"""
Render all .d2 files in scripts/diagrams/ to SVG images in docs/diagrams/ and, if present, ../HomeBikeManager.wiki/diagrams/.
Requires the D2 CLI: https://d2lang.com/tour/installation/
"""

import os
import subprocess
import logging
import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D2_SRC = os.path.join(PROJECT_ROOT, 'scripts', 'diagrams')
DOCS_OUT = os.path.join(PROJECT_ROOT, 'docs', 'diagrams')
WIKI_OUT = os.path.abspath(os.path.join(PROJECT_ROOT, '../HomeBikeManager.wiki/diagrams'))


LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOGS_DIR, 'render_diagrams.log')

logger = logging.getLogger("render_diagrams")
DEBUG_MODE = os.environ.get("DEBUG", "0") == "1"

logger.setLevel(logging.DEBUG if DEBUG_MODE else logging.INFO)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG if DEBUG_MODE else logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

# File handler (overwrite log file each run)
fh = logging.FileHandler(LOG_FILE, mode='w')
fh.setLevel(logging.DEBUG if DEBUG_MODE else logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)

os.makedirs(DOCS_OUT, exist_ok=True)
if os.path.isdir(os.path.dirname(WIKI_OUT)):
    os.makedirs(WIKI_OUT, exist_ok=True)

success = 0
fail = 0
skipped = 0
for fname in os.listdir(D2_SRC):
    if fname.endswith('.d2'):
        src = os.path.join(D2_SRC, fname)
        svg_name = os.path.splitext(fname)[0] + '.svg'
        docs_svg = os.path.join(DOCS_OUT, svg_name)
        try:
            result_docs = subprocess.run(['d2', src, docs_svg], check=True, capture_output=True, text=True)
            logger.info(f"Rendered {fname} to docs/diagrams/{svg_name}")
            if DEBUG_MODE and result_docs.stdout:
                logger.debug(f"d2 stdout for {fname} (docs): {result_docs.stdout}")
            if DEBUG_MODE and result_docs.stderr:
                logger.debug(f"d2 stderr for {fname} (docs): {result_docs.stderr}")
            if os.path.isdir(os.path.dirname(WIKI_OUT)):
                wiki_svg = os.path.join(WIKI_OUT, svg_name)
                result_wiki = subprocess.run(['d2', src, wiki_svg], check=True, capture_output=True, text=True)
                logger.info(f"Rendered {fname} to wiki/diagrams/{svg_name}")
                if DEBUG_MODE and result_wiki.stdout:
                    logger.debug(f"d2 stdout for {fname} (wiki): {result_wiki.stdout}")
                if DEBUG_MODE and result_wiki.stderr:
                    logger.debug(f"d2 stderr for {fname} (wiki): {result_wiki.stderr}")
            success += 1
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to render {fname}: {e}")
            if e.stdout:
                logger.error(f"d2 stdout for {fname}: {e.stdout}")
            if e.stderr:
                logger.error(f"d2 stderr for {fname}: {e.stderr}")
            skipped += 1

logger.info(f"Summary: {success} diagrams rendered, {skipped} skipped due to errors.")
