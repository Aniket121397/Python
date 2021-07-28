word = input("Enter a word: ")
vowels = "AEIOUaeiou"
output = ""

for letters in word :
    if letters not in vowels:
        output += letters
print(output ,end=" ")



