years = int(input())
if 0 < years <= 2:
    print(years * 10.5)
elif years > 2:
    print(2 * 10.5 + (years - 2) * 4)