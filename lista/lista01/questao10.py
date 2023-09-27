# Escreva uma função chamada menor que recebe um vetor e retorna o maior
# valor dentre os elementos do vetor.

def menor(arrayNumero):
  numeroMenor = float('inf')
  for i in range(len(arrayNumero)):
    if(arrayNumero[i] < numeroMenor):
      numeroMenor = arrayNumero[i]
      
  return numeroMenor

print(menor([5, 3, 4, 1]))