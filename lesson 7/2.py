a = float(input())
b = float(input())
c = float(input())
if a == b == c:
    print('Равносторонний')
elif a == b or a == c or b == c:
    print('Равнобедренный')
elif a != b != c:
    print('Разносторонний')