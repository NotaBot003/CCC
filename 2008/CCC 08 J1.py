w = int(input())
h = float(input())

s = w/(h*h)
if s >= 18.5 and s <= 25: print("Normal weight")
if s < 18.5 print ("Underweight")
if s > 25 print ("Overweight")
