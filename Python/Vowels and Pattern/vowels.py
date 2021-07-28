word = input("Enter a word: ")
vowels = "aeiouAEIOU"

output = ""
for i in word:
    if i in vowels:
        output += i


if output == "":
    print("No vowels found!")
else:
    print(output)








