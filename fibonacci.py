def fibonacci(n):
    a, b = 0, 1
    seq = []
    while b <= n:
        seq.append(b)
        a, b = b, a + b
    print("Sequência de Fibonacci:", seq)
    if n in seq:
        print(n, "pertence à sequência de Fibonacci.")
    else:
        print(n, "não pertence à sequência de Fibonacci.")


numero = int(input("Digite um número: "))
fibonacci(numero)
