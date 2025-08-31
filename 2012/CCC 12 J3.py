n = int(input())
for line in ('*x*', ' xx', '* *'):
    for i in range(n):
        for l in line:
            print(l * n, end='')
        print()