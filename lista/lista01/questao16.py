# Escreva uma função chamada somaacumulativa que recebe um vetor e
# retorna um outro vetor resultante de uma soma acumulativa. Exemplo:
# Entrada: 1 2 3 4 5
# Saída: 1 3 6 10 15

def somaCumulativa(arrayNumeros):
  arrayTotalSoma = []
  soma = 0
  for numero in range(len(arrayNumeros)):
    soma += arrayNumeros[numero] 
    arrayTotalSoma.append(soma)
    
  return arrayTotalSoma

print(somaCumulativa([1, 2, 3, 4, 5]))