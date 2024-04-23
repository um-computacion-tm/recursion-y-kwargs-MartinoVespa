def fibonacci(fibo):

    if fibo == 0:
        return 0
    
    elif fibo == 1:
    
        return 1
    
    else:
        
        resultado =  fibonacci(fibo-1) + fibonacci(fibo-2)
        
        return resultado