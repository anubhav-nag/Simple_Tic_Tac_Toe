s = input()
for i in s:
    if i.isupper():
        if s[0] == i:
            s = s.replace(i, i.lower())
        else:
            s = s.replace(i, "_" + i.lower())
print(s)
