"""Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится)."""

x = int(input("Enter x:"))
y = int(input("Enter y:"))

def check(x,y):
    pos = 4
    if x > 0 and y > 0:
        pos = 1
    elif x < 0 and y > 0:
        pos = 2
    elif x < 0 and y < 0:
        pos = 3
    print(f"Coordinate now in {pos} position cartesian coordinate system")

check(x,y)