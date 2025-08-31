while True:
    inputs = input()
    if inputs == "X":
        break
    while True:
        anas = inputs.count("ANA")
        bases = inputs.count("BAS")
        inputs = inputs.replace("ANA", "A")
        inputs = inputs.replace("BAS", "A")
        if anas == 0 and bases == 0:
            break
    if inputs == "A":
        print("YES")
    else:
        print("NO")
