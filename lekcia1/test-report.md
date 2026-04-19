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
3 passed, 1 warning
```

Integračný beh:

```bash
uv run --with-requirements lekcia1/requirements.txt python lekcia1/main.py
```

Výsledok:

```text
Druhá mocnina čísla 4 je 16.
```

## Čo bolo overené

- funkcia `square_number(4)` vracia hodnotu `16`
- načítanie `GEMINI_API_KEY` z `.env` súboru funguje
- základný manual tool use tok funguje:
  - prvé volanie modelu
  - zachytenie tool callu `square_number`
  - vykonanie nástroja v Pythone
  - odoslanie tool response späť modelu
  - získanie finálnej odpovede
- reálne volanie Gemini API vrátilo správnu finálnu odpoveď pre číslo `4`

## Poznámka

Unit testy používajú mockovaný klient a nerobia skutočné volanie Gemini API.

Samostatne bol overený aj ostrý integračný beh proti Gemini API.

Počas behu unit testov sa objavilo 1 deprecation warning z knižnice `google-genai`, ale testy prešli bez chyby.
