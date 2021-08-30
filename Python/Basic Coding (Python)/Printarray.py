# Write a program to accept n numbers from user in an array and print all of them

list = []

n = int(input("Enter no. of elements: "))

for i in range(0,n):
    ele = int(input("Enter a element: "))
    list.append(ele)

print(list)