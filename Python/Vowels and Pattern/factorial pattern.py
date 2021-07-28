def printpattern(number):
    for i in range(1,number + 1):
       print("* " * i,end=" ")
       print()

def printfactors(number):
    for i in range(1, number + 1):
        if number % i == 0:
           print(i,end=" ")
    print()

def printfactorial(number):
    fact = 1
    for i in range(1,number + 1):
        fact = i * fact
    print(fact)

number = int(input("Enter a number: "))

print("The pattern is :")
printpattern(number)

print()

print("The factors of",number,"are :")
printfactors(number)

print()

print("The factorial of the",number,"is:")
printfactorial(number)

