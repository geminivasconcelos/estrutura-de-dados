# Escreva uma função chamada fatorial que recebe um número e retorne seu fatorial.


def fibonacci(numero):
  fib_sequence = [0, 1]
  while len(fib_sequence) < numero:
    next_num = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_num)
  return fib_sequence

print(f"A sequência é: {fibonacci(5)}")    

    