"""
The output of Q.1 will be :
4 is maximum

The output of Q.2 will be :
x is 50
Changed local x to 2
x is now 50

"""
def trainglepattern(noOfRows):
    for stars in range(1, noOfRows + 1):
        print(" " * noOfRows, end=" ")
        print("* " * stars)
        noOfRows -= 1


def patternwithnumbers(noOfrows):
    num = 1
    for i in range(1,noOfrows + 1):
      for x in range(1,i + 1):
        print(num, end=" ")
        num = num+1
      print()

noOfRows = int(input("Enter no. of rows: "))
trainglepattern(noOfRows)
print()
patternwithnumbers(noOfRows)





