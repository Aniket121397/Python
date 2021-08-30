#  Write a program to find  number is Even Or Odd .

n = int(input("Enter a number: "))

if n == 0:
    print("The number is neither even nor odd")

elif n % 2 == 0:
    print("The number is even")

else:
    print("The number is odd")