def showstars(number):
    for i in range(1,number + 1):
       print("* " * i,end=" ")
       print()

number = int(input("Enter no. of rows: "))
showstars(number)