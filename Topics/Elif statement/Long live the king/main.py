h = int(input())
v = int(input())
if h > 1 and h < 8:
    if v > 1 and v < 8:
        print(8)
    elif v == 1 or v == 8:
        print(5)
elif h == 1 or h == 8:
    if v > 1 and v < 8:
        print(5)
    elif v == 1 or v == 8:
        print(3)
