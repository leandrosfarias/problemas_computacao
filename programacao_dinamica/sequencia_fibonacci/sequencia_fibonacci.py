# finbonacci
def fibonacci_recursivo(n):
    if n <= 2:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_recursivo_top_down(n):
    if n <= 2:
        return 1
    vetor = inicializa_vetor(n)
    if vetor[n - 1] == -1:
        vetor[n - 1] = fibonacci_recursivo_top_down(n - 1) + fibonacci_recursivo_top_down(n - 2)
    return vetor[n - 1]


def fibonacci_recursivo_bottom_up(n):
    if n <= 2:
        return 1
    vetor = inicializa_vetor(n)
    # vetor[0] = 1
    # vetor[1] = 1
    for i in range(2, n):
        vetor[i] = vetor[i - 1] + vetor[i - 2]
    return vetor[n - 1]


def inicializa_vetor(n):
    vetor = [0 for i in range(n)]
    vetor[0] = 1
    vetor[1] = 1
    for i in range(2, n):
        vetor[i] = -1
    return vetor


print(fibonacci_recursivo_bottom_up(6))
