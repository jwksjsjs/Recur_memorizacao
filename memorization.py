from functools import lru_cache
from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

#Recursivamente calcula o número de partições de n usando valores até k
@lru_cache(maxsize=None)
def particoes(n, k):
    if n == 0:
        return 1
    if n < 0 or k == 0:
        return 0
    return particoes(n - k, k) + particoes(n, k - 1)


def numero_particoes(n):
    return particoes(n, n)

# Função para rodar em paralelo
def calcular_particao(n):
    inicio = perf_counter()
    total = numero_particoes(n)
    duracao = perf_counter() - inicio
    return (n, total, round(duracao, 3))


# Roda cálculos em paralelo para uma lista de valores de n
def executar_particoes_em_paralelo(lista_n):
    with ProcessPoolExecutor() as executor:
        resultados = executor.map(calcular_particao, lista_n)
    return list(resultados)
    

# Execuçã
if __name__ == "__main__":
    lista = [50, 60, 70, 80, 90]

    print("Calculando número de partições em paralelo...")
    saidas = executar_particoes_em_paralelo(lista)

    for n, total, tempo in saidas:
        print(f"n = {n}: {total} partições (tempo: {tempo}s)")
