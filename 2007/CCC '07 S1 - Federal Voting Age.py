Repetition = int(input())
for i in range(Repetition):
    birthdays = input()
    year, month, day = list(map(int, birthdays.split()))
    if year <= 1989:
        if year == 1989:
            if month <= 2:
                if month == 2:
                    if day <= 27:
                        print("Yes")
                    else: print("No")
                else: print("Yes")
            else: print("No")
        else: print("Yes")
    else: print("No")