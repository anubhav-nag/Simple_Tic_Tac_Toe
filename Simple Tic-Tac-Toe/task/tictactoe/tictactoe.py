tic_tac = [" " for i in range(9)]
print("---------")
print("|" + " " + tic_tac[0] + " " + tic_tac[1] + " " + tic_tac[2] + " " + "|")
print("|" + " " + tic_tac[3] + " " + tic_tac[4] + " " + tic_tac[5] + " " + "|")
print("|" + " " + tic_tac[6] + " " + tic_tac[7] + " " + tic_tac[8] + " " + "|")
print("---------")

count = 0


def test():
    c = 0
    o = 0
    count_x = 0
    count_o = 0
    for i in tic_tac:
        if i == "X":
            count_x += 1
        elif i == "O":
            count_o += 1
    for i in range(0, 9, 3):
        if tic_tac[i] == tic_tac[i + 1] == tic_tac[i + 2]:  # horizontal check
            if tic_tac[i] == "X":
                c += 1
            elif tic_tac[i] == "O":
                o += 1
    for i in range(0, 3):
        if tic_tac[i] == tic_tac[i + 3] == tic_tac[i + 6]:  # vertical check
            if tic_tac[i] == "X":
                c += 1
            elif tic_tac[i] == "O":
                o += 1
    if tic_tac[0] == tic_tac[4] == tic_tac[8]:  # diagonal check 1
        if tic_tac[0] == "X":
            c += 1
        elif tic_tac[0] == "O":
            o += 1
    if tic_tac[2] == tic_tac[4] == tic_tac[6]:  # diagonal check 2
        if tic_tac[2] == "X":
            c += 1
        elif tic_tac[2] == "O":
            o += 1

    if c == 1 and o == 0:
        print("X wins")
    elif o == 1 and c == 0:
        print("O wins")
    elif " " not in tic_tac:
        print("Draw")
    else:
        coordinates()


def coordinates():
    global count
    v, h = input("Enter the coordinates: ").split()
    if h.isnumeric() and v.isnumeric():
        v = int(v)
        h = int(h)
        r = [i for i in range(1, 4)]
        if v not in r or h not in r:
            print("Coordinates should be from 1 to 3!")
            coordinates()
        else:
            x = (v - 1) * 3 + (h - 1)
            if tic_tac[x] == " ":
                tic_tac[x] = "X" if count % 2 == 0 else "O"
                count += 1
                print("---------")
                print("|" + " " + tic_tac[0] + " " + tic_tac[1] + " " + tic_tac[2] + " " + "|")
                print("|" + " " + tic_tac[3] + " " + tic_tac[4] + " " + tic_tac[5] + " " + "|")
                print("|" + " " + tic_tac[6] + " " + tic_tac[7] + " " + tic_tac[8] + " " + "|")
                print("---------")

                test()
            else:
                print("This cell is occupied! Choose another one!")
                coordinates()
    else:
        print("You should enter numbers!")
        coordinates()


coordinates()
