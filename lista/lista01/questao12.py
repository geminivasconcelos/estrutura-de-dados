# Escreva uma função chamada somamatriz que recebe uma matriz e soma todos os elementos da matriz.


def somamatriz(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma


minha_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
resultado = somamatriz(minha_matriz)
print(resultado)