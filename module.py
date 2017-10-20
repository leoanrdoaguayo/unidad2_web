from math import pi
"""Funcion que calcula el area de un cilindro"""
def area_cilindro(R: float, h: float) -> float:
     area = (2* pi * R) * (h + R)
     return area
"""Funcion que calcula el volumen de un cilindro"""
def volumen_cilindro(h: float, R: float)-> float:
    volumen = (pi * R**2) * h
    return volumen
