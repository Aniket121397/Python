
def split_into_list(words):
    word=""
    res=list()
    for c in words:
        if c==" ":
            res.append(word)
            word=""
        else:
            word+=c
    res.append(word)
    return res
b=input("Enter sentences:")
split_into_list(b)
A=b[::-1]
ans=""
for r in A:
    ans += r + ""
print(ans)

