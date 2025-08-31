first = int(input())
last = int(input())
year = first
print("All positions change in year", first)
while year <= last:
    year += 60
    if year <= last:
        print("All positions change in year", year)