# Escreva uma função chamada somadiagonal que recebe uma matriz e calcula
# a soma dos elementos que estão na diagonal principal.

def somaDiagonal(matriz):
  soma = 0
  for linhaDiagonal in range(len(matriz)):
    soma += matriz[linhaDiagonal][linhaDiagonal]
      
  return soma

minha_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = somaDiagonal(minha_matriz)
print(resultado)