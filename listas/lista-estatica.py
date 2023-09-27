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