burger = int(input())
side = int(input())
drink = int(input())
des = int(input())
cal = 0
if burger == 1:
    cal = 461
elif burger == 2:
    cal = 431
elif burger == 3:
    cal = 420
elif burger == 4:
    cal = 0

if side == 1:
    cal = cal + 100
elif side == 2:
    cal = cal + 57
elif side == 3:
    cal = cal + 70
elif side == 4:
    cal = cal + 0

if drink == 1:
    cal = cal + 130
elif drink == 2:
    cal = cal + 160
elif drink == 3:
    cal = cal + 118
elif drink == 4:
    cal = cal + 0

if des == 1:
    cal = cal + 167
elif des == 2:
    cal = cal + 266
elif des == 3:
    cal = cal + 75
elif des == 4:
    cal = cal + 0
print("Your total Calorie count is", str(cal) + ".")