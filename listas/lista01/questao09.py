# Escreva uma função chamada maior que recebe um vetor e retorna o maior valor
# dentre os elementos do vetor.

def maior(arrayNumero):
  numeroMaior = 0
  for i in range(len(arrayNumero)):
    if(arrayNumero[i] > numeroMaior):
      numeroMaior = arrayNumero[i]
      
  return numeroMaior

print(maior(range(10)))