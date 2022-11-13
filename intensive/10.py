a = int(input())
if 1000 <= a <= 9999 and a % 7 == 0 or 1000 <= a <= 9999 and a % 17 == 0:
    print('YES')
else:
    print('NO')