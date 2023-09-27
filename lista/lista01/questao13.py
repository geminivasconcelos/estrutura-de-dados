# Escreva uma função chamada somacoluna que recebe uma matriz, calcula sua
# transposta e soma os elementos da primeira coluna.

#append concatena 2 matrizes

def somaColuna(matriz):
  transposta = []  # Inicializa a matriz transposta
  for j in range(len(matriz[0])):
    coluna = []
    for i in range(len(matriz)):
      coluna.append(matriz[i][j])
    transposta.append(coluna)
    
  soma = sum(transposta[0])
  return soma


minha_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = somaColuna(minha_matriz)
print(resultado) 





