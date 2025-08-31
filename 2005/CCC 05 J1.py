day = int(input())
eve = int(input())
nit = int(input())
planA = 0.00
planB = 0.00

if day >= 100:
    planA = (day - 100)*25
planA = planA + (15*eve) + (20*nit)
planA = planA * 0.01

float = planA
format_floata = "{:.2f}".format(float)


print("Plan A costs", format_floata)
if day >= 250:
    planB = (day - 250)*45
planB = planB + (35*eve) + (25*nit)
planB = planB * 0.01
float = planB
format_floatb = "{:.2f}".format(float)
print("Plan B costs", format_floatb)
if planA > planB:
    print("Plan B is cheapest.")
if planB > planA:
    print("Plan A is cheapest.")
if planA == planB:
    print("Plan A and B are the same price.")
