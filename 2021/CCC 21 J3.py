while True:
    inputs = input()
    [aa, ab, ac, ad, ae] = ([*inputs])
    rl = int(aa) + int(ab)
    if int(inputs) == 99999:
        break
    if (rl % 2) == 0:
        print("right" + " " + ac + ad + ae)
    elif (rl % 2) == 1:
        print("left" + " " + ac + ad + ae)
