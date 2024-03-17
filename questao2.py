def sequencia_fibonacci(n):
    fibonacci = [0,1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci
    
def check_fibinacci(num):

    fibonacci = sequencia_fibonacci(num)
    if num in fibonacci:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência Fibonacci."
    

numero = int(input("Digite um numero para verificar se pertence à sequência Fibonacci: "))
print(check_fibinacci(numero))
