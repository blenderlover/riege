k = 0
reshenie = ''
for x in range (1, 777):
    for y in range (1, 777):
        if 13 * x + 12 * y == 777:
            reshenie += f'({x}, {y})\n'
            k += 1
print(k, reshenie, sep='\n')
