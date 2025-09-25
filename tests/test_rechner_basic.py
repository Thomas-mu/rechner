# Minimaler Komponententest für die Funktion berechne() in Rechner.py

from Rechner import berechne

def test_addition():
    assert berechne(2, 3, "+") == 5

def test_subtraktion():
    assert berechne(5, 2, "-") == 3

def test_multiplikation():
    assert berechne(4, 3, "*") == 12

def test_division_ok():
    assert berechne(10, 2, "/") == 5

def test_division_durch_null():
    res = berechne(1, 0, "/")
    assert isinstance(res, str) and "Division" in res

def test_ungueltiger_operator():
    res = berechne(2, 3, "x")
    assert isinstance(res, str) and "Ungültig" in res
