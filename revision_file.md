# Python Practice Tracker — Rokkun.io Interview Prep

## Session Progress

### Level 1 — Syntax Muscle Memory
- [x] 1. Read a number, print if it is odd or even
- [x] 2. FizzBuzz (3 → Fizz, 5 → Buzz, both → FizzBuzz, else the number)
- [x] 3. Read a string, print it reversed
- [x] 4. Read a sentence, count how many words it has
- [x] 5. Read 5 numbers, print the largest

### Level 2 — Collections
- [x] 6. Read 5 numbers into a list, print only the even ones
- [x] 7. Given a list of words, print only words longer than 4 characters
- [x] 8. Count how many times each word appears in a sentence — use a dict
- [ ] 9. Given two lists, return elements that appear in both
- [ ] 10. Flatten this nested list: `[[1,2],[3,4],[5,6]]`

### Level 3 — Functions and Real Patterns
- [ ] 11. Filter a list of dicts by key=value
- [ ] 12. Read a JSON file and return it as a dict
- [ ] 13. Return the 3 most common words in a string
- [ ] 14. Retry an operation up to 3 times on exception
- [ ] 15. FastAPI POST endpoint — takes `{"query": "..."}`, returns `{"answer": "..."}`

### Level 2 (Advanced) — AI Engineering Core
- [ ] 16. Async Python — `asyncio.gather` running two coroutines in parallel
- [ ] 17. FastAPI — Pydantic model + dependency injection + async endpoint
- [ ] 18. RAG pipeline — chunk → embed → store in ChromaDB → retrieve top-k → build prompt
- [ ] 19. LangChain — prompt template + LLM + StrOutputParser using LCEL (`|` pipe)
- [ ] 20. LangGraph — TypedDict state + node function + compile and invoke a graph

### Level 3 — OOP and Classes (`level_3_oop/`)
- [ ] 21. Basic class — `Dog` with `__init__` and `bark()`
- [ ] 22. `__str__` and `__repr__` — human vs developer representation
- [ ] 23. BankAccount — `deposit`, `withdraw`, `@property`, `ValueError`
- [ ] 24. Inheritance — `Animal` base class, `Dog` and `Cat` subclasses (polymorphism)
- [ ] 25. `@classmethod` and `@staticmethod` — `Person.from_string()` and `Person.is_adult()`
- [ ] 26. `@dataclass` — rewrite a class using the dataclass decorator
- [ ] 27. `@property` getter/setter — `Temperature` with validation
- [ ] 28. Dunder collection methods — `__len__`, `__contains__` on a `Playlist` class
- [ ] 29. Abstract base class — `Shape`, `Circle`, `Rectangle` using `ABC`
- [ ] 30. Context manager — `__enter__`/`__exit__`, then `@contextmanager` version

### Level 4 — Python Power Features (`level_4_power_features/`)
- [ ] 31. List comprehension — filter, transform, combine in one line
- [ ] 32. Dict comprehension — `{word: len}`, filter by value
- [ ] 33. Decorator `@timer` — measure and print function execution time
- [ ] 34. Decorator `@log_calls` — print args and return value for any function
- [ ] 35. Generator — `fibonacci(n)` using `yield`
- [ ] 36. `*args` and `**kwargs` — flexible function signatures
- [ ] 37. Lambda + `sorted()` — sort list of dicts by key, multi-key sort
- [ ] 38. `zip()` and `enumerate()` — practical pairing and indexing patterns
- [ ] 39. Type hints — annotate existing functions with full type signatures
- [ ] 40. Advanced comprehensions — flatten, extract fields, set comprehension

### Level 5 — Production Patterns (`level_5_production/`)
- [ ] 41. File I/O — `read_file`, `write_file`, `append_file` with `with open`
- [ ] 42. JSON handling — `save_json`, `load_json`, `get_nested` safe accessor
- [ ] 43. Environment variables — `os.environ`, `python-dotenv`, required vs optional
- [ ] 44. Logging — logger setup with file + console handlers, log levels
- [ ] 45. HTTP requests — `requests` library, error handling, timeouts
- [ ] 46. Async HTTP — `aiohttp` + `asyncio.gather` for concurrent fetching
- [ ] 47. Pydantic models — validation, nested models, optional fields, `ValidationError`
- [ ] 48. FastAPI CRUD — full GET/POST/DELETE with in-memory store
- [ ] 49. SQLAlchemy — model definition, session, insert/query/delete
- [ ] 50. Production function — type hints + logging + async + Pydantic all together

### Level 6 — AI Engineering Core (`level_6_ai_engineering/`)
- [ ] 51. Nested JSON parsing — safe extraction from OpenAI-style API response payloads
- [ ] 52. Context window slicing — keep last N messages, trim to char/token limit
- [ ] 53. Prompt hydration — safe dict injection into multi-variable prompt templates
- [ ] 54. `copy.deepcopy()` vs shallow copy — LangGraph state mutation patterns
- [ ] 55. Network exceptions + exponential backoff retry — production LLM API calls
- [ ] 56. Text chunking — fixed size with overlap, by sentence, by paragraph
- [ ] 57. Token counting with `tiktoken` — count, check fit, trim messages to limit
- [ ] 58. MongoDB basics — insert, find, update, delete for AI document storage
- [ ] 59. Redis caching — cache LLM responses by query hash, TTL, invalidation
- [ ] 60. Vector DB with Qdrant — create collection, ingest, search, delete by metadata
- [ ] 61. LangGraph advanced — multi-node graph with conditional edges and branching
- [ ] 62. Streaming LLM responses — generator + FastAPI `StreamingResponse` + SSE
- [ ] 63. Multi-agent pattern — researcher + writer + critic with LangGraph loop
- [ ] 64. `pytest` — write unit tests, assert errors, parametrize
- [ ] 65. Docker — `Dockerfile` + `docker-compose.yml` for FastAPI + Redis + Qdrant

---

## Weak Spots (filled after session)

_To be added after problem 15._

---

## Extra Practice (added as session progresses)

- Q2: revisit — bare `except` vs `except ValueError`, and condition ordering (FizzBuzz must come first)
- Q3: revisit — `str(input())` is redundant; dead `except ValueError` on string input
- Q4: revisit — remember to use `input()`, don't hardcode the test string
- Q6: revisit — needed solution shown; rewrite from memory was clean ✓
- Q10: revisit — kept mixing up outer/inner loop variable names (`inner` vs `item`). Rewrite 3x until automatic.
- Q11: revisit — needed solution shown; concept of passing key/value as variables was confusing. Rewrite 3x until automatic.
