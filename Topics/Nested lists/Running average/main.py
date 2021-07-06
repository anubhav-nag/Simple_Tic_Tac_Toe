a = input()
t = [(int(a[i]) + int(a[i + 1])) / 2 for i in range(len(a) - 1)]
print(t)
