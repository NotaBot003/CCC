n = int(input())
scoville = 0

for i in range(n):
    pepper = input()
    if pepper == "Poblano":
        scoville += 1500
    if pepper == "Mirasol":
        scoville += 6000
    if pepper == "Serrano":
        scoville += 15500
    if pepper == "Cayenne":
        scoville += 40000
    if pepper == "Thai":
        scoville += 75000
    if pepper == "Habanero":
        scoville += 125000
print(scoville)