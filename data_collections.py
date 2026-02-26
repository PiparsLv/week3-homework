print("--------A daļa Saraksti-----------")
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
print(f"Saraksta summa: {summa}, Saraksta vidējais rezultāts: {videjais}")


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

print("-------B daļa Vārdnīcas--------")

"""B daļa — Vārdnīcas:
•	Izveido vārdnīcu ar 3+ studentiem: {"Anna": 85, "Jānis": 72, "Līga": 95}
•	Pievieno jaunu studentu; maina esošu atzīmi
•	Iterē ar for name, grade in studenti.items(): un izvada katru
•	Atrod studentu ar augstāko atzīmi (for cikls pa vārdnīcu)
"""
studenti = {"Anna": 85, "Jānis": 72, "Līga": 95}  #izveidota vārdnīca
print(studenti)

studenti["Aldis"] = 70                             #pievienots papildus elements vārdnīcai
print(f"Pievienojies jauns students: {studenti}")

studenti["Anna"] = 75                               #tiek izmainīts vārdnīcā esošs elements izmantojot key
print(f"Annai samazināts vērtējums: {studenti}")

for name, grade in studenti.items():                
    print(f"Students: {name}, Atzīme: {grade}")

top_students = ""
top_atzime = 0

for name, grade in studenti.items():
    if grade > top_atzime:
        top_atzime = grade
        top_students = name
print(f"Labākais students: {top_students}  ({top_atzime})")

print("-------C Daļa Kombinācija---------")

"""•	Izveido sarakstu ar vārdnīcām: [{"name": "Anna", "grade": 85}, ...]
•	Filtrē: tikai studenti ar atzīmi >= 80
•	Izmanto enumerate() un f-strings formatētai izvadei: "1. Anna — 85"
"""
"""studenti1 = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 72},
    {"name": "Līga", "grade": 95},
    {"name": "Aldis", "grade": 70}
    ]

for  i, students in enumerate(studenti1, start = 1):
    if students["grade"] >= 80:
        print(f" {i}{students["name"]} - {students["grade"]}")"""

#Mi piedāvājums
studenti1 = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 72},
    {"name": "Līga", "grade": 95},
    {"name": "Aldis", "grade": 70}
]

# 1. Izveidojam sarakstu tikai ar tiem, kam ir 80+ (List Comprehension)
labie_studenti = [s for s in studenti1 if s["grade"] >= 80]

# 2. Izmantojam enumerate, lai sanumurētu tikai atlasītos
for i, students in enumerate(labie_studenti, start=1):
    print(f"{i}. {students['name']} — {students['grade']}")