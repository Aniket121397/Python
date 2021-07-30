# def reverse(s):
#         str=""
#         for i in s:
#             str=i+str
#             if str==s:
#                 return str
# s=input("Enter:")
# print("The original string is:",end=" ")
# print(s)
# print("Palindrome of string :",end="")
# print(reverse(s))

def palindrome(s):
    return s==s[::-1]
s=input("Enter word:")
ans=palindrome(s)
if ans:
    print("YES ",s,"is palindrome")
else:
    print("NO")
