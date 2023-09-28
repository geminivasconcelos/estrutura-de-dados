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

  def removeItemPorPosicaoLista(self, posicao):
    if(posicao >= 0 and posicao <= self.tamanho):
        # self.elemento[posicao] = 0
        for i in range(self.tamanho):
          if(i > posicao):
              self.elemento[i-1] = self.elemento[i]
        self.tamanho -= 1
    else:
      print(f"Posição inválida")

  def removeItemListaPorValor(self, numero):
    numeroNaLista = False
    posicaoNaLista = 0
    for i in range(self.tamanho):
      if(round(self.elemento[i])  == round(numero)):
        numeroNaLista = True
        posicaoNaLista = i

    if(numeroNaLista == True):
      for i in range(self.tamanho):
        if(i > posicaoNaLista):
          self.elemento[i-1] = self.elemento[i]
      self.tamanho -= 1
    else:
      print(f"Numero não encontrado")


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
  print("insere valores")
  lista.inserir(5)
  lista.inserir(15)
  lista.inserir(20)
  lista.inserir(25)
  print("busca por valor")
  lista.buscaValorLista(150)
  print("adiciona valor em determinada posicao")
  lista.inserirPosicaoLista(24, 2)
  lista.imprimirLista()
  print("remove pela posicao")
  lista.removeItemPorPosicaoLista(4)
  lista.imprimirLista()
  print("remove pelo valor")
  lista.removeItemListaPorValor(5)
  lista.imprimirLista()


if __name__ == "__main__":
  main()