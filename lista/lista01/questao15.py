# Escreva uma função chamada pertence que recebe dois vetores e retorna a
# soma dos elementos que fazem parte dos dois conjuntos (vetores).

def pertence(vetorUm, vetorDois):
  somaNumeroPertence = 0
  
  for i in range(len(vetorUm)):
    for j in range(len(vetorDois)):
      if(vetorUm[i] == vetorDois[j]):
        somaNumeroPertence += vetorUm[i] + vetorDois[j]
        
  return somaNumeroPertence


vetorUm = [0 ,2, 3, 4, 7]
vetorDois = [2, 6, 7]
print(pertence(vetorUm, vetorDois ))