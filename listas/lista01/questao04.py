# Escreva uma função chamada primo que recebe um número inteiro e retorne 1, se primo, ou 0, caso contrário.

def primo(numero):
  if(numero <= 1 ):
    return 'não é primo'
  if(numero <= 3):
    return 'é primo'
  if numero % 2 == 0 or numero % 3 == 0:
    return 'não é primo'
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      return 'não é primo'
    i += 6
  return 'é primo'

print(primo(31))