from math import sqrt

inputs = int(input())
while inputs > 0:
    for i in range(int(sqrt(inputs)), 0, -1):
        if inputs % i == 0:
            dimensions = (i, inputs // i)
            print(f"Minimum perimeter is {sum(dimensions) * 2}"
                  f" with dimensions {dimensions[0]} x {dimensions[1]}")
            break
    inputs = int(input())