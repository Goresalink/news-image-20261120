#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261120.

Copies the repository's front-page image summing up Friday
20 November 2026's world news to the output path.
Deterministic, standard library only, no network: the same
bytes are written on every run, so the two grading runs agree.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    # The image lives beside this program in the repository; the
    # grader mounts that directory read-only, so copy, never move.
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
