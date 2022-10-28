a = int(input())
b = int(input())
c = int(input())
if a + b > c or b + a > c or c + a > b or a + c > b or b + c > a or c + b > a:
    print('Yes')
else:
    print('No')
