#  Write a program to accept a number from a user and print the table of the number.

n = int(input("Enter a number: "))

for i in range (1,11):
    print(n , "x", i, "=" ,n * i)