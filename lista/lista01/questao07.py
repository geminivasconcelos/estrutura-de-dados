#  Escreva uma função chamada fibonacci que receba um número e retorne a soma da sua sequência de Fibonacci.

from questao05 import *

def somaSequenciaFibonacci(numero):
  sequenciaFibonacci = fibonacci(numero)
  totalSomaSequenciaFibonacci = 0
  for i in range(len(sequenciaFibonacci)):
    totalSomaSequenciaFibonacci += sequenciaFibonacci[i]
    
  return totalSomaSequenciaFibonacci

print(f"Total da soma da sequência é: {somaSequenciaFibonacci(5)}")