n = int(input())
maximum = 0
minimum = 9
while n != 0:
    if n % 10 > maximum:
        maximum = n % 10
    if n % 10 < minimum:
        minimum = n % 10
    n = n // 10
print('Максимальная', maximum)
print('Минимальная', minimum)