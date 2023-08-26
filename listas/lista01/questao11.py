# Escreva uma função chamada media que recebe um vetor e retorna sua
# média.

def media(arrayNumeros):
  totalSomaArray = 0
  for i in range(len(arrayNumeros)):
    totalSomaArray += arrayNumeros[i]
    
  media = totalSomaArray/len(arrayNumeros)
  return media

print(media([3,5,2,1]))