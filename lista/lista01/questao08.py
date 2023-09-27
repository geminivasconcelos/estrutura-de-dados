# Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5,
# temos 3, 5, 6, 9, cuja soma é 23. Escreva uma função chamada multiplos que recebe
# um número y e retorna a soma de todos os múltiplos de 3 e 5 abaixo desse número y.

def multiplos(numero):
  totalSomaMultiplos = 0
  for i in range(numero):
    if i % 3 == 0 or i % 5 == 0:
      totalSomaMultiplos += i
      
  return totalSomaMultiplos

print(multiplos(10))