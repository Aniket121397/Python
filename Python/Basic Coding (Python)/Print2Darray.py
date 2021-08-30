# Write a program to accept the input from a user in a 2D array, and then print the array in a 2D format only

list = []

n = int(input("Enter no. of elements: "))

for i in range(0,n):
    ele = int(input("Enter a element: "))
    list.append(ele)

print(list)