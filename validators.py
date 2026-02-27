# ---Modulis datu validācijai ---
#Ietver e-pasta, tālruņa numura, vecuma, paroles un datuma pārbaudi.

from datetime import datetime
def is_email(text: str) -> bool:
    if not isinstance(text, str):
        return False
    if "@" not in text:
        return False
    
    parts = text.split("@")
    #pārbaudam vai pēc @ ir vismaz viena daļa ar punktu
    return len(parts) == 2 and "." in parts[1]

def is_phone_number(text: str) -> bool:
    if not isinstance(text, str):
        return False
    prefix = "+371 "
    if not text.startswith(prefix):
        return False
    number_part = text[len(prefix):]
    return len(number_part) == 8 and number_part.isdigit()

def is_valid_age(age: int) -> bool:
    if type(age) is not int:
        return False
    return 0 <= age <= 150

def is_strong_pasword(text: str) -> bool:
    #pārbauda paroles stiprumu, vismaz 8 simboli, satur burtus un ciparus
    if not isinstance(text, str) or len(text) < 8:
        return False
    
    has_alpha = any(c.isalpha() for c in text)
    has_digit = any(c.isalpha() for c in text)

    return has_alpha and has_digit

def is_valid_date(text: str) -> bool:
    if not isinstance(text, str):
        return False
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
# --- Demonstrācija un Testēšana ---

if __name__ == "__main__":
    print("--- Moduļa validators.py testi ---")

    #1. e-pasta testi

    print(f"E-pasts (anna@inbox.lv): {is_email("anna@inbox.lv")}") #True
    print(f"E-pasts (bez punkta): {is_email("anna@inbox.lv")}")    #False
    print(f"E-pasts (tikai teksts): {is_email("anna")}")           #False

    #2. telefona testi
    print(f"\nTelefons (+371 26123456): {is_phone_number("+371 26123456")}") #true
    print(f"Telefons (bez koda): {is_phone_number("26123456")}" ) #false
    print(f"Telefons (par īsu): {is_phone_number ("+371 2612")}") #false

    #3.vecuma testi
    print(f"\nVecums(25): {is_valid_age(25)}") #true
    print(f"Vecums (151): {is_valid_age(151)}") #false
    print(f"Vecums (teksts): {is_valid_age("25")}") #false

    #4. paroles testi
    print(f"\nParole (Saule20024): {is_strong_pasword("Saule20024")}")#true
    print(f"Parole (tikai burti): {is_strong_pasword("tikai burti")}")#false
    print(f"Parole (par īsu): {is_strong_pasword("S24")}")#false
    
    #5. datuma testi
    print(f"\nDatums (2024-12-31): {is_valid_date("2024-12-31")}")#true
    print(f"Datums (31-12-2024): {is_valid_date("31-12-2024")}")#false
    print(f"Datums (2024-02-30): {is_valid_date("2024-02-30")}")#false




