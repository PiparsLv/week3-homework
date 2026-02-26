"""•	Izveido sarakstu ar 5+ skaitļiem; pievieno elementu ar .append(), dzēš ar .pop()
•	Aprēķina saraksta summu un vidējo vērtību ar for ciklu (nelietojot sum()/len() — lai saprastu mehāniku)
•	Filtrē sarakstu: izveido jaunu sarakstu tikai ar pāra skaitļiem (for + if)
•	Demonstrē šķēlumu (slice): pirmie 3, pēdējie 2, katrs otrais elements
"""
import math
saraksts = [1, 2, 3, 4, 5, 6]
print(saraksts)

saraksts.append(7)
print(f"Elementa pievienošana: {saraksts}")

saraksts.pop(0)
print(f"Dzēšanas funkcija: {saraksts}")

summa = 0               #summa ir sākumā 0, lai katrā cikla aplī būtu iespēja pievienot klāt
skaits = 0

for vertiba in saraksts:                # summas funkcija
    summa += vertiba                    # sasummējam skaitli
    skaits += 1                         # katrā solī pieskaitamām 1 

if skaits > 0:                          # jānorāda ka skaitlis nedrīkst būt mazāks par 0, lai ar to nedalītu
    videjais = summa / skaits
else:
    videjais = 0
print(f"Saraksta summa: {summa}")
print(f"Saraksta vidējais rezultāts: {videjais}")

para_skaitli = []

for paris in saraksts:
    if paris % 2 == 0:          # dalot ar divi varam noteikt ka ir pāra skaitlis
        para_skaitli.append(paris)
print(f"Pilnais saraksts: {saraksts}")
print(f"Tikai pāra skaitļi: {para_skaitli}")


saraksts2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Pirmie 3 skaitļi: {saraksts2[0:3]}")
print(f"pēdējie 2 skaitļi: {saraksts2[-2:]}")
print(f"Katrs otrais elements: {saraksts2[1::2]}")