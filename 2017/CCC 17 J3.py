start_x, start_y = (int(i) for i in input().split())
end_x, end_y = (int(i) for i in input().split())
squares = int(input())
distance = abs(start_x - end_x) + abs(start_y - end_y)
if squares >= distance and (distance % 2 == 0 and squares % 2 == 0 or
                                distance % 2 != 0 and squares % 2 != 0):
    print('Y')
else:
    print('N')