CurrentSquare = 1
while True:
    roll = int(input())
    if roll < 2 or roll > 12:
        break
    if CurrentSquare + roll <= 100:
        CurrentSquare += roll
    if CurrentSquare == 54:
        CurrentSquare = 19
    if CurrentSquare == 90:
        CurrentSquare = 48
    if CurrentSquare == 99:
        CurrentSquare = 77
    if CurrentSquare == 9:
        CurrentSquare = 34
    if CurrentSquare == 40:
        CurrentSquare = 64
    if CurrentSquare == 67:
        CurrentSquare = 86
    print("You are now on square", CurrentSquare)
    if CurrentSquare == 100:
        break
if CurrentSquare == 100:
    print("You Win!")
else:
    print("You Quit!")