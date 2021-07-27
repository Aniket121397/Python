num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))

op_1 = "+"
op_2 = "-"
op_3 = "*"
op_4 = "/"

op = input("Enter a operator: ")

if op == op_1:
    print(num_1 + num_2)

elif op == op_2:
    print(num_1 - num_2)

elif op == op_3:
    print(num_1 * num_2)

elif op == op_4:
    print(num_1 * num_2)

else:
    print("Invalid Operator")







