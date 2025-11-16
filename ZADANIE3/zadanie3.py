import requests, re, time, sys
from collections import Counter

URL = "https://pl.wikipedia.org/api/rest_v1/page/random/summary"
N = 100  # liczba losowań
HEADERS = {
    "User-Agent": "wp-edu-wiki-stats/0.1 (kontakt: twoj-email@domena)",
    "Accept": "application/json",
}

# przygotowanie wyrażenia regularnego wyłapującego słowa (litery)
WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


def selekcja(text: str):
    # znajdź tylko słowa składające się z liter
    slowa = WORD_RE.findall(text)
    # zamień na małe litery i filtruj długość > 3
    return [s.lower() for s in slowa if len(s) > 3]


def ramka(text: str, width: int = 80) -> str:
    max_len = width - 2
    if len(text) > max_len:
        # przycinamy i dodajemy wielokropek
        text = text[:max_len - 1] + "…"
    # wyśrodkowanie i ramka
    centered = text.center(max_len)
    return f"[{centered}]"


def main():
    cnt = Counter()
    licznik_slow = 0
    pobrane = 0

    # linia statusu
    print(ramka("Start"), end="", flush=True)

    while pobrane < N:
        try:
            data = requests.get(URL, headers=HEADERS, timeout=10).json()
        except Exception:
            time.sleep(0.1)
            continue

        title = data.get("title") or ""
        print("\r" + ramka(title, 80), end="", flush=True)

        extract = data.get("extract", "")
        lista_slow = selekcja(extract)
        cnt.update(lista_slow)
        licznik_slow += len(lista_slow)
        pobrane += 1

        time.sleep(0.05)  # opcjonalnie, żeby nie obciążać API

    print("\n")
    print(f"Pobrano: {pobrane}")
    print(f"#Słowa:  {licznik_slow}")
    print(f"Unikalne:  {len(cnt)}\n")

    print("Najczęstsze 15 słów:")
    for slowo, ile in cnt.most_common(15):
        print(f"{slowo}: {ile}")


if __name__ == "__main__":
    main()
