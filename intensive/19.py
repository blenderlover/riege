a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 - 1 == a2 or a1 + 1 == a2) and (b1 - 2 == b2 or b1 + 2 == b2):
    print ('YES')
elif (a1 - 2 == a2 or a1 + 2 == a2) and (b1 - 1 == b2 or b1 + 1 == b2):
    print ('YES')
else:
    print ('NO')