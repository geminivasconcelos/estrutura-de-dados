import numpy as np
import sys

class Lista:
  def __init__(self, numero):
    self.max = numero
    self.elemento = np.zeros(self.max)
    self.tamanho = 0

  def inserir(self, numeroInserir):
    if(self.tamanho < self.max):
      self.elemento[self.tamanho] = numeroInserir
      self.tamanho += 1
    else:
      print(f"Lista está cheia")

  def imprimirLista(self):
    if(self.tamanho == 0):
      print(f"Lista esta vazia")
    else:
      for i in np.arange(self.tamanho):
        print(f"{self.elemento[i]}")  
  
  def limparLista(self):
    self.tamanho = 0

def main():
  numero = 2
  lista = Lista(numero)
  lista.inserir(5)
  lista.inserir(15)
  lista.inserir(20)
  lista.inserir(25)
  lista.imprimir()
  # lista.limpar()
  # lista.imprimir()
  # lista.inserir(50)
  # lista.imprimir()

if __name__ == "__main__":
  main()