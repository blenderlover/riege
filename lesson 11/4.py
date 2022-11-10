m = int(input())
p = int(input())
n = int(input())
for i in range(n):
    m = m + m * (p / 100)
    print(i + 1, m)