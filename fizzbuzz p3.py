numero = int(input("Digite um número inteiro:"))

teste1 = numero % 3
teste2 = numero % 5

if teste1 == 0 and teste2 == 0:
   print("FizzBuzz")
else:
   print(numero)