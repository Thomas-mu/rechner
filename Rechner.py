# Taschenrechner nach V-Modell
# Azubi-Projekt mit Notizen (Protokoll der Eingaben und Ergebnisse)
NOTIZDATEI = "notizen.txt"
def schreibe_notiz(text):
    """Speichert Textzeilen in der Notizen-Datei"""
    with open(NOTIZDATEI, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def eingabe():
    """Fragt Benutzer nach zwei Zahlen und einem Operator"""
    try:
        a = float(input("Geben Sie die erste Zahl ein: "))
        b = float(input("Geben Sie die zweite Zahl ein: "))
        op = input("Wählen Sie einen Operator (+, -, *, /): ")

        # Eingaben in Notizen speichern
        schreibe_notiz(f"Eingaben: {a} {op} {b}")
        return a, b, op
    except ValueError:
        print("Ungültige Eingabe, bitte nur Zahlen eingeben!")
        schreibe_notiz("Ungültige Eingabe erkannt.")
        return eingabe()  # Eingabe wiederholen

def berechne(a, b, op):
    """Führt die Berechnung aus"""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Fehler: Division durch 0 ist nicht erlaubt!"
        return a / b
    else:
        return "Ungültiger Operator"

def ausgabe(ergebnis):
    """Zeigt das Ergebnis an"""
    print("Ergebnis:", ergebnis)
    # Ergebnis in Notizen speichern
    schreibe_notiz(f"Ergebnis: {ergebnis}")
    schreibe_notiz("-" * 30)  # Trenner

def main():
    """Hauptprogramm – steuert den Ablauf"""
    a, b, op = eingabe()
    ergebnis = berechne(a, b, op)
    ausgabe(ergebnis)

if __name__ == "__main__":
    main()
