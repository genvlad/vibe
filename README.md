# Vibe

Collection of Python tasks from a course on AI-assisted programming (Google Gemini API).

## Structure

Each task lives in its own folder at the repo root:

```
<task-name>/
├── main.py             # implementation
├── requirements.txt
├── .env.example
├── tests/
└── test-report.md
```

## Running a task

```bash
cd <task-name>
cp .env.example .env        # fill in GEMINI_API_KEY
uv run --with-requirements requirements.txt python main.py
```

## Tasks

| Task | Description | Run |
| --- | --- | --- |
| `lekcia1` | Simple Gemini tool use example that squares the number 4 via a Python function. | `cd lekcia1 && uv run --with-requirements requirements.txt python main.py` |
