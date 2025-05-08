produto1 = int(input(f'Qual o preço do primeiro produto? '))
produto2 = int(input(f'Qual o preço do segundo produto? '))
produto3 = int(input(f'Qual o preço do terceiro produto? '))

if produto1 < produto2 and produto1 < produto3:
    print('Compre o primeiro produto.')
elif produto2 < produto3:
    print('Compre o segundo produto.')
else:
    print('Compre o terceiro produto.')