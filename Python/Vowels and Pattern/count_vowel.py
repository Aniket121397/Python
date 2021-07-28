s=input("Enter word:")
vowels="AEIOUaeiou"
count=0
for x in s:
    if x in vowels:
        count +=1
print("Vowels:",count)