"""Prasības:
•	Katrai funkcijai — docstring ar aprakstu, parametriem, atgriežamo vērtību un piemēru
•	Vismaz 2 funkcijām — noklusējuma parametru vērtības
•	Funkcijas ir "tīras" (pure): nav blakusefektu, nav print() iekšpusē (izņemot demonstrācijai)
•	Katra funkcija validē ievadi: piem., factorial(-1) met ValueError
•	Faila beigās: if __name__ == "__main__": bloks ar demonstrācijas izsaukumiem
"""

import math

#-----Virkņu funkcija------

# Piemērs: capitalize("hello") -> "Hello"
def capitalize(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Ievadei jābūt virknei (str)")
    return text.capitalize()

def truncate(text: str, max_len : int = 20) -> str:
    if not isinstance(text, str):
        raise TypeError("Ievadei jābūt virknei (str)")
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."

def count_words(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("Ievadei jābūt virknei (str)")
    return len(text.split())


#----- Skaitļu funkcijas -----

def clamp(num: float, low: float = 0.0, hight: float = 100.0) -> float:
    if low > hight:
        raise ValueError("Minimālā robeža nevar būt lielāka par maksimālo")
    return max(low, min(num, hight))
def is_prime(num: int) -> bool:
    if not isinstance(num, int):
        raise TypeError("Jāievada vesels skaitlis")
    if num < 2:
        return False
    for i in range (2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Faktoriālam nepieciešams vesels skaitlis")
    if n < 0:
        raise ValueError("Faktoriāls nav definēts negatīviem skaitļiem")

    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

#----- Sarakstu funkcijas -----

def total(numbers: list) -> float:
    if not isinstance(numbers, list):
        raise TypeError("Jāiesniedz saraksts (list)")
    
    kopa = 0
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise ValueError("Saraksts drīkst būt tikai skaitļi")
        kopa += n
    return kopa

def average(numbers: list) -> float:
    if not numbers:
        return 0.0
    return total(numbers) / len(numbers)

print("----- demonstrācija -----")

if __name__ == "__main__":
    print("---- Virkņu funkciju tests ----")
    txt = "python ir foršs"
    print(f"Capitalize: {capitalize(txt)}")
    print(f"Truncate: {truncate(txt, 6)}")
    print(f"Vārdi:    {count_words(txt)}")

    print("\n --- Sarakstu funkciju tests ---")
    cipari = [10, 20, 30, 40]
    print(f"Saraksts: {cipari}")
    print(f"Summa: {total(cipari)}")
    print(f"Vidējais: {average(cipari)}")
