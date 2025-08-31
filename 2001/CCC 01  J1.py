height = int(input())
for half in (range(1, height, 2), range(height, -1, -2)):
    for i in half:
        print('*' * i + ' ' * ((height-i)*2) + '*' * i)