StopPoint = int(input())
cases = int(input())
CasesPerPerson = int(input())

output = 0
PreviousCases = 0
totalCases = 0
day = 0

while totalCases < StopPoint:
    cases = cases*CasesPerPerson

    output = output + 1
    day = day + 1
    if day != 0:
        PreviousCases = PreviousCases + cases
    totalCases = PreviousCases
    #print(PreviousCases)
print(output)
