
import numpy as np

class Lista:
    def __init__(self):
        self.max = 10
        self.tam = 0
        self.elems = np.zeros(self.max)
        
    def setMaximo(self, m):
        self.max = m
        self.elems = np.zeros(self.max)

    def verificaListaVazia(self):
        if self.tam == 0:
            return True
        else:
            return False
    
    def imprimir(self):
        for i in np.range(self.tam):
            print(f"{self.elems[i]}")

    def inserir(self, novoElemento):
        if self.tam == self.max:
            print('lista cheia')
        else:
            self.elems[self.tam] = novoElemento
            self.tam +=1

    def limparLista(self):
        self.tam = 0
    

def main():
    listinha = Lista(4)
    listinha.verificaListaVazia()
    for i in range(3):
        listinha.inserir(i)
    
    listinha.verificaListaVazia()
    listinha.imprimir()
    listinha.verificaListaVazia()
    listinha.imprimir()

if __name__ == "__main__":
    main()
