def rzymskie_na_arabskie(rzymskie):
    rzym_to_arab = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    if not isinstance(rzymskie, str) or not rzymskie:
        raise ValueError("Podano niepoprawny format – oczekiwany łańcuch znaków.")

    wartosc = 0
    i = 0
    while i < len(rzymskie):
        if rzymskie[i] not in rzym_to_arab:
            raise ValueError("Niepoprawny format liczby rzymskiej.")

        if (i + 1 < len(rzymskie) and
            rzym_to_arab[rzymskie[i]] < rzym_to_arab[rzymskie[i + 1]]):
            wartosc += rzym_to_arab[rzymskie[i + 1]] - rzym_to_arab[rzymskie[i]]
            i += 2
        else:
            wartosc += rzym_to_arab[rzymskie[i]]
            i += 1

    # Walidacja końcowa: konwersja w obie strony powinna dać to samo
    if arabskie_na_rzymskie(wartosc) != rzymskie:
        raise ValueError("Niepoprawny format liczby rzymskiej.")
    return wartosc


def arabskie_na_rzymskie(arabskie):
    if not isinstance(arabskie, int) or not (1 <= arabskie <= 3999):
        raise ValueError("Liczba musi być całkowita z zakresu 1–3999.")

    arab_to_rzym = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    rzymskie = ""
    for value, symbol in arab_to_rzym:
        while arabskie >= value:
            rzymskie += symbol
            arabskie -= value
    return rzymskie


if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)

