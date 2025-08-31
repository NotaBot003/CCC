time = int(input())
edm, win, hal, john = 0, 0, 0, 0
print(time, "in Ottawa")
if time - 300 <= 0:
    vic = 2400 - (300 - time)
else:
    vic = time - 300
if time - 200 <= 0:
    edm = 2400 -  (200 - time)
else:
    edm = time - 200
if time - 100 <= 0:
    win = 2400 -  (100 - time)
else:
    win = time - 100
tor = time
if time + 100 >= 2400:
    hal = 2400 - (100 + time)
else:
    hal = time + 100
if time + 130 >= 2400:
    john = 2400 - (130 + time)
else:
    if time + 130 == 275:
        john = 315
    else:
        john = time + 130
print(vic, "in Victoria")
print(edm, "in Edmonton")
print(win, "in Winnipeg")
print(time, "in Toronto")
print(hal, "in Halifax")
print(john, "in St. John's")
