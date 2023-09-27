#Escreva uma função chamada potencia que calcule a potência de dois números x e y (xy) utilizando multiplicações

def potencia(numero1, numero2):
  resultado = 1
  for _ in range(numero2):
    resultado *= numero1
  return resultado

print(potencia(2,4))