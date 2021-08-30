# Write a program to accept a number from a user and print its Square root and cube root
import math

n = int(input("Enter a number: "))

sqr = math.sqrt(n)
sqr2 = n ** (1/2)
cuberoot = n ** (1/3)

print(sqr)
print(sqr2)
print(cuberoot)