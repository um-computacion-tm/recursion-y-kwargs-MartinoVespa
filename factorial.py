def factorial(n):

    if n == 1:

        return 1

    resultado = n * factorial(n-1)
    
    print("-" *30)
    
    print("Factorial de ", n, " == ", resultado)
    
    return resultado