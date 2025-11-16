import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    # Rozdzielamy wejście: wzór funkcji i zakres liczb
    wzor, zakres = wejscie.split(",")
    x_min, x_max = map(float, zakres.split())
    
    # Generujemy wartości x
    x_val = np.linspace(x_min, x_max, 200)
    
    # Definiujemy zmienną x w środowisku eval
    x = x_val
    
    # Użycie eval do obliczenia wartości funkcji
    y_val = eval(wzor)
    
    # Rysowanie wykresu
    plt.figure()
    plt.plot(x_val, y_val)
    plt.title(f"Funkcja: {wzor}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)

    # Zwracamy wartości brzegowe
    return y_val[0], y_val[-1]


# Funkcja rysująca wykres na podstawie SymPy i lambdify()
def rysuj_wielomian_sympy(wejscie):
    # Rozdzielamy wejście: wzór funkcji i zakres liczb
    wzor, zakres = wejscie.split(",")
    x_min, x_max = map(float, zakres.split())

    # Definicja symbolu i funkcji SymPy
    x = symbols('x')
    expr = sympify(wzor)  # tworzymy wyrażenie SymPy
    f = lambdify(x, expr, 'numpy')  # konwertujemy do funkcji numerycznej

    # Generowanie danych
    x_val = np.linspace(x_min, x_max, 200)
    y_val_sympy = f(x_val)

    # Rysowanie wykresu
    plt.figure()
    plt.plot(x_val, y_val_sympy)
    plt.title(f"SymPy: {wzor}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)

    # Zwracamy wartości brzegowe
    return y_val_sympy[0], y_val_sympy[-1]


if __name__ == '__main__':
    # Przykładowe wywołanie pierwszej funkcji
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    
    # Pierwszy wykres z eval
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)
    
    # Drugie wejście dla funkcji SymPy - bardziej złożona funkcja 
    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"  
    
    # Drugi wykres z SymPy
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)
    
    # Wyświetlanie obu wykresów
    plt.savefig("wykres.png")
    print("Wykres zapisany jako wykres.png")
