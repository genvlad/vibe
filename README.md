# Vibe

Zbierka Python úloh z kurzu programovania s umelou inteligenciou (Anthropic API).

## Štruktúra

Každá úloha je v samostatnom priečinku v rôte repa:

```
<nazov-ulohy>/
├── spec.md             # zadanie
├── main.py             # implementácia
├── requirements.txt
├── .env.example
├── tests/
└── test-report.md
```

## Spustenie úlohy

```bash
cd <nazov-ulohy>
cp .env.example .env        # doplň ANTHROPIC_API_KEY
uv run --with-requirements requirements.txt python main.py
```

## Zoznam úloh

| Úloha | Popis | Spustenie |
| --- | --- | --- |
| _(zatiaľ žiadna)_ | | |
