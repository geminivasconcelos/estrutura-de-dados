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
      
  def inserirPosicaoLista(self, numero, posicao):
    if(posicao >= 0 and posicao <= self.tamanho):
      if(self.tamanho < self.max):
        for i in range(self.tamanho, posicao, -1):
            self.elemento[i] = self.elemento[i-1]
        self.elemento[posicao] = numero                
        self.tamanho += 1
    else:
      print(f"Posição inválida")
      
  def buscaValorLista(self, numero):
    numeroEncontrado = False
    for i in range(self.tamanho):
      if(self.elemento[i] == numero):
        print(f"Numero encontrado")
        numeroEncontrado = True
        break
    if(numeroEncontrado == False):
      print(f"Esse numero não está na lista")
      
  # def removeItemPosicaoLista(self, numero):
    
      
  def limparLista(self):
    self.tamanho = 0
    
  def imprimirLista(self):
    if(self.tamanho == 0):
      print(f"Lista esta vazia")
    else:
      for i in np.arange(self.tamanho):
        print(f"{self.elemento[i]}")  
  
  

def main():
  numero = int(sys.argv[1])
  lista = Lista(numero)
  lista.inserir(5)
  lista.inserir(15)
  lista.inserir(20)
  lista.inserir(25)
  # lista.buscaValorLista(150)
  lista.inserirPosicaoLista(24, 10)
  # lista.inserirPosicaoLista(1, 4)
  lista.imprimirLista()
  # lista.limpar()
  # lista.imprimir()
  # lista.inserir(50)
  # lista.imprimir()

if __name__ == "__main__":
  main()