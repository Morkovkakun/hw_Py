"""Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве. """

x = input('Please enter first floating point value:\n')
x = float(x)

y = input('Please enter second floating point value:\n')
y = float(y)

length = ((x - y) ** 2 + (x - y) ** 2) ** (0.5)

print(f"the distance is {length}")