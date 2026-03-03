# src/calculatrice.py

def division(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division par zéro interdite.")
    return float(a / b)


def puissance(a: float, n: int) -> float:
    if n < 0:
        raise ValueError("L'exposant ne peut pas être négatif.")
    return float(a ** n)


def moyenne(notes: list[float]) -> float:
    if len(notes) == 0:
        raise ValueError("La liste des notes est vide.")
    return float(sum(notes) / len(notes))