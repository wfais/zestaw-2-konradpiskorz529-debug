import os
import time
import threading
import sys

# Stałe konfiguracyjne
LICZBA_KROKOW = 80_000_000
LICZBA_WATKOW = sorted({1, 2, 4, os.cpu_count() or 4})


def policz_fragment_pi(pocz: int, kon: int, krok: float, wyniki: list[float], indeks: int) -> None:
    suma = 0.0
    for i in range(pocz, kon):
        x = (i + 0.5) * krok
        suma += 4.0 / (1.0 + x * x)
    wyniki[indeks] = suma * krok  # zapis do własnego slotu w liście


def main():
    print(f"Python: {sys.version.split()[0]}  (tryb bez GIL? {getattr(sys, '_is_gil_enabled', lambda: None)() is False})")
    print(f"Liczba rdzeni logicznych CPU: {os.cpu_count()}")
    print(f"LICZBA_KROKOW: {LICZBA_KROKOW:,}\n")

    krok = 1.0 / LICZBA_KROKOW

    # Wstępne rozgrzanie środowiska
    wyniki = [0.0]
    w = threading.Thread(target=policz_fragment_pi, args=(0, LICZBA_KROKOW, krok, wyniki, 0))
    w.start()
    w.join()

    # Mierzymy wydajność dla różnych liczby wątków
    wyniki_czasow = {}

    for liczba_w in LICZBA_WATKOW:
        print(f"\nLiczba wątków: {liczba_w}")

        # Przygotowanie listy na wyniki
        wyniki = [0.0 for _ in range(liczba_w)]
        watki = []

        # Podział pracy na zakresy
        rozmiar = LICZBA_KROKOW // liczba_w
        start_czas = time.perf_counter()

        for indeks in range(liczba_w):
            pocz = indeks * rozmiar
            kon = (indeks + 1) * rozmiar if indeks < liczba_w - 1 else LICZBA_KROKOW
            w = threading.Thread(target=policz_fragment_pi, args=(pocz, kon, krok, wyniki, indeks))
            watki.append(w)
            w.start()

        # Czekamy aż wszystkie wątki się zakończą
        for w in watki:
            w.join()

        # Sumowanie wyników i pomiar czasu
        pi = sum(wyniki)
        czas = time.perf_counter() - start_czas
        wyniki_czasow[liczba_w] = czas

        print(f"  π ≈ {pi:.10f}")
        print(f"  Czas: {czas:.3f} s")

    print("\nPrzyspieszenie:")
    czas_1 = wyniki_czasow[1]
    for liczba_w, czas in wyniki_czasow.items():
        speedup = czas_1 / czas
        print(f"  {liczba_w} wątków: {speedup:.2f}×")


if __name__ == "__main__":
    main()
