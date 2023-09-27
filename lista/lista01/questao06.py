# Escreva uma função chamada inteiros que recebe um número inteiro positivo x e retorne a soma de todos os inteiros positivos entre 1 e x.

def inteiro(numero):
  resultado = 0;
  if(numero > 0 and isinstance(numero, int)):
    for i in range(1, numero):
      if(i > 0 and isinstance(i, int)):
        resultado += i
      
  return resultado

print(inteiro(10))
    