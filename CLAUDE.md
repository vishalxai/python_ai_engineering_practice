# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Interview practice repo for Vishal — a Full-Stack AI Engineer preparing for interviews. The goal is building hand-writing muscle memory for Python, FastAPI, RAG pipelines, LangChain, and LangGraph. Vishal can read Python fluently but freezes writing from a blank page.

## Environment

- Python 3.13, virtual environment at `.venv/`
- Activate: `source .venv/bin/activate`
- Install deps: `pip install -r requirements.txt`

## Running practice files

```bash
# Run any standalone script
python q01_odd_even.py

# Run FastAPI questions (q15, q17)
uvicorn q15_fastapi_endpoint:app --reload
uvicorn level_2/q17_fastapi_advanced:app --reload
```

## Repo structure

```
q01–q15.py              # Level 1 — Python fundamentals (syntax, collections, functions)
level_2/                # Level 2 (q16–q20) — async, FastAPI, RAG, LangChain, LangGraph
level_3_oop/            # Level 3 (q21–q30) — classes, inheritance, decorators, ABC, context managers
level_4_power_features/ # Level 4 (q31–q40) — comprehensions, generators, *args, lambda, type hints
level_5_production/     # Level 5 (q41–q50) — file I/O, logging, env vars, requests, Pydantic, SQLAlchemy
level_6_ai_engineering/ # Level 6 (q51–q65) — nested JSON, chunking, tokens, Redis, Qdrant, LangGraph advanced, Docker
revision_file.md        # Progress checklist — 65 questions total, mark done as completed
requirements.txt        # Currently contains Vishal's first attempt at q01 (misplaced)
```

## Total question count: 65
- Q1–Q15:  Python fundamentals
- Q16–Q20: AI engineering basics (interview priority)
- Q21–Q30: OOP and classes
- Q31–Q40: Python power features
- Q41–Q50: Production patterns
- Q51–Q65: AI engineering deep dive (RAG, LangGraph, streaming, Docker)

## Practice session rules (coach mode)

When Vishal pastes a solution for review, evaluate on exactly three things:
1. Does it work correctly
2. Is it Pythonic
3. What edge case did he miss

Keep feedback to 3 lines max. If he is stuck, give one hint only — never the full solution unless he has genuinely tried. After he gets the hint, if still stuck, show the solution and immediately ask him to close it and rewrite from memory.

After all 20 questions are done, fill in the **Weak Spots** section in `revision_file.md`.

## Target role context

Rokkun.io — Full-Stack AI Engineer. Must-haves per JD: Python production proficiency, FastAPI, RAG pipelines, LangChain/LangGraph, vector DBs (Chroma/Qdrant/Pinecone), PostgreSQL. Interview is 2026-05-28.
