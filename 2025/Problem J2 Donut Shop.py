total = int(input())
events = int(input())

for i in range(events):
    symbol = input()
    if symbol == '+':
        total += int(input())
    elif symbol == '-':
        total -= int(input())
print(total)