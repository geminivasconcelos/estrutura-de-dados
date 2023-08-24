# Escreva uma função chamada multiplica que faça multiplicação de dois números inteiros utilizando somas.

def multiplica(numero1, numero2):
  resultado = 0
  for _ in range(numero2):
    resultado += numero1
  return resultado

print(multiplica(10, 3))
