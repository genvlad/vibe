# Špecifikácia úlohy: lekcia1

## Cieľ

Vytvoriť jednoduchý Python skript, ktorý demonštruje základný tool use pri volaní LLM API.

Skript má:

1. zavolať Gemini API,
2. sprístupniť modelu jednoduchý nástroj `square_number`,
3. nechať model požiadať o výpočet druhej mocniny čísla 4,
4. vykonať nástroj v Pythone,
5. vrátiť výsledok späť modelu,
6. vypísať finálnu textovú odpoveď do konzoly.

## Rozsah

Úloha má byť zámerne jednoduchá a krátka:

- jeden vstupný prompt napevno v kóde,
- jeden nástroj,
- bez CLI argumentov,
- bez zložitých abstrakcií,
- bez frameworkov,
- bez ukladania histórie,
- bez webového rozhrania.

## Funkčné požiadavky

### 1. Vstupný prompt

Skript po spustení odošle modelu prompt s významom:

`Daj mi druhú mocninu čísla 4.`

Text promptu môže byť formulovaný prirodzene po slovensky alebo česky.

### 2. Nástroj

Implementovať jednu Python funkciu:

- názov: `square_number`
- vstup: celé číslo `number`
- výstup: druhá mocnina čísla

Príklad:

- vstup `4`
- výstup `16`

### 3. Tool use tok

Skript musí ukázať celý základný cyklus:

1. odoslanie používateľského promptu modelu,
2. prijatie požiadavky modelu na použitie nástroja,
3. vykonanie funkcie `square_number(4)`,
4. odoslanie výsledku nástroja späť modelu,
5. získanie finálnej odpovede modelu.

### 4. Výstup programu

Program vypíše do konzoly finálnu odpoveď modelu.

Očakávaný význam výstupu:

- model oznámi, že druhá mocnina čísla 4 je 16.

Presná formulácia odpovede nemusí byť striktne fixná.

## Technické požiadavky

- Jazyk: Python 3.11+
- Závislosť: `google-genai`
- Model: `gemini-2.5-flash`
- API kľúč čítať z `GEMINI_API_KEY`
- Použiť lokálny `.env` súbor v priečinku úlohy
- Kód má byť ľahko čitateľný pre začiatočníka

## Súbory, ktoré má pripraviť programátor

V priečinku `lekcia1/` majú vzniknúť:

- `main.py`
- `requirements.txt`
- `.env.example`

Voliteľne:

- `tests/test_main.py`

## Odporúčaná štruktúra implementácie

Implementácia má zostať plochá a jednoduchá:

- načítanie API kľúča,
- definícia funkcie `square_number`,
- vytvorenie klienta,
- prvé volanie modelu s deklarovaným nástrojom,
- spracovanie tool call,
- druhé volanie modelu s výsledkom nástroja,
- výpis finálnej odpovede.

Nie je potrebné vytvárať viacero modulov ani tried.

## Validácia

Za splnenú sa úloha považuje, keď:

- skript sa spustí cez `uv run --with-requirements requirements.txt python main.py`,
- model použije nástroj alebo je implementovaný tok pre tool call podľa SDK,
- výsledok nástroja je `16`,
- finálna odpoveď zodpovedá zadaniu.
