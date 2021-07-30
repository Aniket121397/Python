def fizz_fuzz(x):
    if (x%3==0 and x%5==0):
        return "fizz_buzz"
    elif (x%3==0):
        return "fizz"
    elif (x%5==0):
        return "Buzz"
    else:
        return x
a=int(input("Enter the number:"))
print(fizz_fuzz(a))
