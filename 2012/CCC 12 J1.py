a = int(input())
b = int(input())

if 0 < b - a < 21:
    print("You are speeding and your fine is $100.")
elif 20 < b - a < 31:
    print("You are speeding and your fine is $270.")
elif 30 < b - a:
    print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")