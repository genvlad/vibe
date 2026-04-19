# Test report: lekcia1

## Výsledok

PASS

## Spustené testy

Príkaz:

```bash
uv run --with pytest --with-requirements lekcia1/requirements.txt pytest lekcia1/tests -q
```

Výsledok:

```text
2 passed, 1 warning
```

Integračný beh:

```bash
uv run --with-requirements lekcia1/requirements.txt python lekcia1/main.py
```

Výsledok:

```text
--- Response Tool call: ---
id=None args={'number': 4} name='square_number' partial_args=None will_continue=None
--- Final response: ---
Druhá mocnina čísla 4 je 16.
```

## Čo bolo overené

- funkcia `square_number(4)` vracia hodnotu `16`
- skript načíta `GEMINI_API_KEY` cez `load_dotenv()`
- jednoduchý tool use tok funguje:
  - prvé volanie modelu
  - zachytenie tool callu `square_number`
  - vykonanie nástroja v Pythone
  - odoslanie tool response späť modelu
  - získanie finálnej odpovede
- reálne volanie Gemini API vrátilo správnu finálnu odpoveď pre číslo `4`

## Poznámka

Skript:
- `load_dotenv()`
- zoznam `tools`
- priame `generate_content(...)`
- výpis tool callu aj finálnej odpovede

Samostatne bol overený aj ostrý integračný beh proti Gemini API.

Počas behu unit testov sa objavilo 1 deprecation warning z knižnice `google-genai`, ale testy prešli bez chyby.
