def sumofmulti(limit):
    for i in range(1,limit+1):
        if (i % 3 == 0 or i % 5 == 0):
            print(i,end=" ")

limit = int(input("Enter a number: "))
print("The multiples of 3 and 5 of",limit,"is ")
sumofmulti(limit)