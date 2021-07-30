s=input("Enter the sentence:")
l=k=""
a=[]
for i in s:
  if i==" ":
    a.append(l)
    l=""
  else:
    l+=i
k=s.replace("and",",")
print(k)