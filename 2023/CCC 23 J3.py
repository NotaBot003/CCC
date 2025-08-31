n = int(input())

dayone = 0
daytwo = 0
daythree = 0
dayfour = 0
dayfive = 0
days = 0
maxone = 0
maxtwo = 0
maxthree = 0
maxfour = 0
maxfive = 0
for i in range(n):
    inputs = input()
    [aa, ab, ac, ad, ae] = inputs
    if aa == "Y":
        dayone = dayone + 1
    if ab == "Y":
        daytwo = daytwo + 1
    if ac == "Y":
        daythree = daythree + 1
    if ad == "Y":
        dayfour = dayfour + 1
    if ae == "Y":
        dayfive = dayfive + 1
a = (dayone, daytwo, daythree, dayfour, dayfive)
x = max(a)
if dayone == x:
    days = days + 1
    maxone = "1"
else: maxone = ""
if daytwo == x:
    days = days + 1
    if maxone == "1":
        maxtwo = (","+"2")
    else: maxtwo = "2"
else: maxtwo = ""
if daythree == x:
    days = days + 1
    if maxone == "1" or maxtwo == "2":
        maxthree = (","+"3")
    else: maxthree = "3"
else: maxthree = ""
if dayfour == x:
    days = days + 1
    if maxone == "1" or maxtwo == "2" or maxthree == "3":
        maxfour = (","+"4")
    else: maxfour = "4"
else: maxfour = ""
if dayfive == x:
    days = days + 1
    if maxone == "1" or maxtwo == "2" or maxthree == "3" or maxfour == "4":
        maxfive = (","+"5")
    else: maxfive = "5"
else: maxfive = ""
print(maxone + maxtwo + maxthree + maxfour + maxfive)
