while True:
    ama = input()
    if ama == "quit!":
        break
    ama = ama.replace("bor", "bour")
    ama = ama.replace("tor", "tour")
    print(ama)
