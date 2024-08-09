x = int(input('Digite um número inteiro: '))

teste1 = x % 2
teste2 = x % 3
cond1 = teste1 == 0
cond2 = teste2 == 0

if cond1 and cond2 or x <= 1:
    print('não primo')
else:
    print('primo')