a = int(input())
b = int(input())
for i in range(a, b+1):
    cube = i**3
    if cube % 10 == 4 or cube % 10 == 9:
        print(i)