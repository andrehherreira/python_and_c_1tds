num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
num3 = int(input('Digite um terceiro número: '))

#Se num1 for o maior
if num1 > num2 and num1 > num3:
    print(f'Seu maior número é o {num1}.')
#Se num2 for o maior
elif num2 > num3:
    print(f'Seu maior número é o {num2}.')
#Se num3 for o maior
else:
    print(f'Seu maior número é o {num3}.')

#Se num1 é menor
if num1 < num2 and num1 < num3:
    print(f'Seu menor número é o {num1}.')
#Se num2 é menor
elif num2 < num3:
    print(f'Seu menor número é o {num2}')
#Se num3 é menor
else:
    print(f'Seu menor número é o {num3}.')