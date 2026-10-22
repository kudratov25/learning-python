# 🐍 Python Roadmap — AI · Google · General Engineering

> **Total estimate:** ~7–10 months at 2–3 hours/day

---

## Overview

| Phase | Topic | Duration |
|-------|-------|----------|
| 0 | Setup & Tooling | 1–2 days |
| 1 | Python Basics | 2–3 weeks |
| 2 | Intermediate Python | 3–4 weeks |
| 3 | Professional Python | 3–4 weeks |
| 4 | DSA & Interview Prep | 2–3 months |
| 5 | AI & Data Science | 2–3 months |
| 6 | System Design *(Google target)* | ongoing |

---

## Phase 0 — Setup (1–2 days)

- [ ] Install Python 3.12+
- [ ] Set up VS Code or PyCharm
- [ ] Learn the REPL (`python3` in terminal)
- [ ] Install `ruff`, `mypy` globally
- [ ] Create your first `hello.py`

---

## Phase 1 — Python Basics (2–3 weeks)

### Syntax & Core Concepts

- [ ] Variables and data types (`int`, `float`, `bool`, `str`)
- [ ] Strings (slicing, formatting, methods)
- [ ] Collections: `list`, `tuple`, `set`, `dict`
- [ ] Conditions: `if / elif / else`, `match`
- [ ] Loops: `for`, `while`, `break`, `continue`
- [ ] Functions: args, kwargs, return values, scope
- [ ] Modules and packages (`import`, `from`, `__init__.py`)

### Projects

- [ ] **Calculator** — arithmetic with user input
- [ ] **To-do CLI app** — add / remove / list tasks in terminal
- [ ] **File organizer script** — sort files in a folder by extension

---

## Phase 2 — Intermediate Python (3–4 weeks)

### OOP

- [ ] Classes and objects
- [ ] Inheritance and `super()`
- [ ] Composition over inheritance
- [ ] Magic methods: `__str__`, `__repr__`, `__len__`, `__eq__`
- [ ] `@property`, `@classmethod`, `@staticmethod`

### Error Handling

- [ ] `try / except / finally`
- [ ] Built-in exceptions
- [ ] Custom exception classes

### File I/O

- [ ] Read/write text files
- [ ] JSON (`json` module)
- [ ] CSV (`csv` module)

### Pythonic Features

- [ ] List / dict / set comprehensions
- [ ] Generators and `yield`
- [ ] Iterators and `__iter__` / `__next__`
- [ ] Decorators (basics)
- [ ] Context managers (`with`, `__enter__` / `__exit__`)

### Projects

- [ ] **Expense tracker** — OOP-based, saves to JSON
- [ ] **Note-taking app** — CRUD with file persistence
- [ ] **Simple web scraper** — `requests` + `BeautifulSoup`

---

## Phase 3 — Professional Python (3–4 weeks)

### Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b
```

- [ ] Basic type hints (`int`, `str`, `list[str]`, `dict[str, int]`)
- [ ] `Optional`, `Union`, `Any` from `typing`
- [ ] `mypy` basics — run type checks on your code

### Testing

- [ ] `pytest` fundamentals
- [ ] Writing unit tests
- [ ] Fixtures and parametrize
- [ ] Mocking with `unittest.mock`

### Environment & Packaging

- [ ] `venv` — create and activate virtual environments
- [ ] `pip` and `requirements.txt`
- [ ] `pyproject.toml` (modern standard)
- [ ] Publishing a package to PyPI (basic)

### Code Quality

- [ ] `ruff` — linting and formatting
- [ ] Proper project structure (`src/`, `tests/`, `pyproject.toml`)
- [ ] `pre-commit` hooks

### Projects

- [ ] **REST API client** — typed, tested, uses `httpx`
- [ ] **Small package/library** — installable via pip, with tests

---

## Phase 4 — DSA & Interview Prep (2–3 months)

### Python Tools for LeetCode

```python
from collections import Counter, defaultdict, deque
import heapq, bisect, itertools
```

- [ ] `Counter` — frequency maps
- [ ] `defaultdict` — safe dict with defaults
- [ ] `deque` — O(1) popleft for BFS
- [ ] `heapq` — min-heap operations
- [ ] `bisect` — binary search on sorted lists
- [ ] `itertools` — combinations, permutations, product

### Topics (in order)

- [ ] Arrays & strings
- [ ] Hash maps & sets
- [ ] Two pointers
- [ ] Sliding window
- [ ] Stacks & queues
- [ ] Binary search
- [ ] Trees (DFS, BFS)
- [ ] Graphs (BFS, DFS, union-find)
- [ ] Dynamic programming
- [ ] Heaps & priority queues

> **Target:** 150–200 LeetCode problems (easy → medium → hard)

---

## Phase 5 — AI & Data Science (2–3 months)

### Libraries

| Library | Purpose |
|---------|---------|
| `NumPy` | Arrays, linear algebra |
| `Pandas` | Data manipulation |
| `Matplotlib` / `Seaborn` | Visualization |
| `Scikit-learn` | Classical ML |
| `PyTorch` | Deep learning |

### Concepts

- [ ] Data cleaning and preprocessing
- [ ] Statistics basics (mean, variance, distributions)
- [ ] Linear algebra basics (vectors, matrices, dot product)
- [ ] ML fundamentals (supervised, unsupervised, evaluation)
- [ ] Neural networks (forward pass, backprop, gradients)
- [ ] LLM basics (tokens, embeddings, prompting, APIs)

### Projects

- [ ] **House price predictor** — regression with Scikit-learn
- [ ] **Image classifier** — CNN with PyTorch
- [ ] **Chatbot** — Claude or OpenAI API with conversation history

---

## Phase 6 — System Design (Ongoing — Google target)

> Start reading this during Phase 4, deepen it during Phase 5.

- [ ] How the web works (DNS, HTTP, TCP)
- [ ] APIs: REST vs GraphQL vs gRPC
- [ ] Databases: SQL vs NoSQL, indexing, transactions
- [ ] Caching (Redis), message queues (Kafka)
- [ ] Load balancing, horizontal scaling
- [ ] CAP theorem, eventual consistency
- [ ] Design classics: URL shortener, rate limiter, Twitter feed

**Resource:** *Designing Data-Intensive Applications* — Kleppmann

---

## Daily Schedule (2–3 hours)

```
1h    → Learn (video / book / docs for current phase)
1h    → Build (current phase project)
30min → LeetCode (1 easy or 1 medium problem)
```

> Skip LeetCode during Phase 1–2. Add it from Phase 3 onward so your Python is solid first.

---

## Recommended Learning Order

```
Phase 0 (setup)
    ↓
Phase 1 (basics)
    ↓
Phase 2 (OOP + files + exceptions + pythonic features)
    ↓
Phase 3 (professional tools + typing + testing)
    ↓
Phase 4 (DSA + LeetCode) ← start system design here
    ↓
Phase 5 (AI + data science)
    ↓
Phase 6 (system design — deepened)
```

---

## Progress Tracker

| Phase | Status | Started | Completed |
|-------|--------|---------|-----------|
| 0 | ⬜ Not started | — | — |
| 1 | ⬜ Not started | — | — |
| 2 | ⬜ Not started | — | — |
| 3 | ⬜ Not started | — | — |
| 4 | ⬜ Not started | — | — |
| 5 | ⬜ Not started | — | — |
| 6 | ⬜ Not started | — | — |
