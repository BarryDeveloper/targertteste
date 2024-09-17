def fibonacci_sequencia(n):
    fib_seq = [0, 1] 
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def fibonacci(n):
    fib_seq = fibonacci_sequencia(n)
    if n in fib_seq:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = fibonacci(numero)
print(resultado)
