# Python AI Engineering Practice

A structured 65-question coding curriculum for Full-Stack AI Engineers — built to develop real muscle memory writing Python from scratch, without autocomplete.

Covers everything from Python fundamentals to production-grade RAG pipelines, LangGraph agents, vector databases, and Docker.

---

## Structure

| Level | Folder | Topics | Questions |
|-------|--------|--------|-----------|
| 1 | root | Syntax, I/O, conditionals, loops | Q1–Q5 |
| 2 | root | Lists, dicts, sets, collections | Q6–Q10 |
| 3 | root | Functions, JSON, FastAPI basics | Q11–Q15 |
| 4 | `level_2/` | Async, FastAPI advanced, RAG, LangChain, LangGraph | Q16–Q20 |
| 5 | `level_3_oop/` | Classes, inheritance, decorators, ABC, context managers | Q21–Q30 |
| 6 | `level_4_power_features/` | Comprehensions, generators, `*args`, lambda, type hints | Q31–Q40 |
| 7 | `level_5_production/` | File I/O, logging, env vars, requests, Pydantic, SQLAlchemy | Q41–Q50 |
| 8 | `level_6_ai_engineering/` | RAG deep dive, LangGraph advanced, vector DBs, streaming, Docker | Q51–Q65 |

---

## Topics Covered

**Python Fundamentals**
- Conditionals, loops, exception handling, user input
- String manipulation, list/dict/set operations
- Functions, return values, variable scope

**OOP**
- Classes, `__init__`, dunder methods (`__str__`, `__repr__`, `__len__`, `__contains__`)
- Inheritance, polymorphism, abstract base classes
- `@property`, `@classmethod`, `@staticmethod`, `@dataclass`
- Context managers (`__enter__`/`__exit__` and `@contextmanager`)

**Python Power Features**
- List, dict, and set comprehensions
- Decorators (`@timer`, `@log_calls`)
- Generators with `yield`
- `*args` / `**kwargs`, lambda, `zip()`, `enumerate()`
- Type hints and annotations

**Production Patterns**
- File I/O, JSON read/write, environment variables (`.env`)
- Structured logging with file + console handlers
- HTTP requests (`requests`, `aiohttp`, async concurrent fetching)
- Pydantic models with validation
- SQLAlchemy ORM: model, session, CRUD
- `pytest`: unit tests, error assertions, parametrize

**FastAPI**
- Basic POST endpoint with Pydantic request/response models
- Dependency injection, async endpoints
- Full CRUD with in-memory store
- `StreamingResponse` + Server-Sent Events (SSE)

**AI Engineering**
- RAG pipeline: chunking → embedding → ChromaDB → retrieval → prompt → LLM
- LangChain: prompt templates, LCEL pipe operator (`|`), `StrOutputParser`
- LangGraph: `TypedDict` state, node functions, `StateGraph`, conditional edges
- Multi-agent pattern: researcher → writer → critic loop
- Text chunking: fixed size with overlap, by sentence, by paragraph
- Token counting with `tiktoken`, context window management
- Nested JSON parsing from OpenAI-style API responses
- Exponential backoff retry for LLM API calls
- Prompt hydration with safe variable injection

**Databases & Infrastructure**
- MongoDB: insert, find, update, delete
- Redis: LLM response caching with TTL and query hash keys
- Qdrant: create collection, ingest vectors, similarity search, metadata filtering
- Docker: `Dockerfile`, `docker-compose.yml` (FastAPI + Redis + Qdrant)

---

## Running the Code

```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run any standalone script
python q01_odd_even.py

# Run FastAPI apps
uvicorn q15_fastapi_endpoint:app --reload
uvicorn level_2/q17_fastapi_advanced:app --reload

# Run tests
pytest level_6_ai_engineering/q64_pytest_basics.py -v
```

---

## Stack

Python 3.13 · FastAPI · LangChain · LangGraph · ChromaDB · Qdrant · Redis · MongoDB · Pydantic · SQLAlchemy · tiktoken · aiohttp · pytest · Docker
