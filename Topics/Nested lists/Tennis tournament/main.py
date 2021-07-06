n = int(input())
x = [input().split(" ") for i in range(n)]
c = 0
a = []
for i in x:
    if i[1] == "win":
        c += 1
        a.append(i[0])
print(a)
print(c)
