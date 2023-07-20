"""

Escribe un programa que imprima los números del 1 al 100. Pero para los múltiplos de 3 imprime "Fizz" 
en lugar del número, y para los múltiplos de 5 imprime "Buzz". Para los números que son múltiplos tanto de 3
como de 5, imprime "FizzBuzz".


"""

num = 1

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

    