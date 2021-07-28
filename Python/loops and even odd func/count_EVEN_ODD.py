A=[23,54,22,98,45,65,37,31,82,64]
even=0
odd=0
for x in A:
    if x%2==0:
        even +=1
    else:
        odd +=1

print("There are:",even,"even numbers")
print("There are:",odd,"odd numbers")
