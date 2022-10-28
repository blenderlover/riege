a = int(input())
b = int(input())
znak = input()
if znak != '*' and znak != '/' and znak != '+' and znak != '-':
    print('Неверная операция')
elif znak == '*':
    print(a * b)
elif znak == '/':
    print(a / b)
elif znak == '+':
    print(a + b)
elif znak == '-':
    print(a - b)

