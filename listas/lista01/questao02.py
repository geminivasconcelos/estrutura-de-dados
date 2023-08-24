# Escreva uma função chamada divide que faça divisão de dois números inteiros utilizando subtrações.

def divide(divisor, dividendo):
  if divisor == 0:
        raise ValueError("Divisor não pode ser zero!")
    
  quociente = 0
  while dividendo >= divisor:
    dividendo -= divisor
    quociente += 1
    
  return quociente
  
  

print(divide(9, 3))