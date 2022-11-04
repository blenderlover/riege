city1 = input()
city2 = input()
city3 = input()
len1 = len(city1)
len2 = len(city2)
len3 = len(city3)
minimum = min(city1, city2, city3, key=len)
maximum = max(city1, city2, city3, key=len)
if len1 == len2 or len1 == len3 or len2 == len3:
    print('Длины всех городов должны быть различны')
else:
    print(minimum)
    print(maximum)