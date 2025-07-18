import time
import os

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def ler_instancia(caminho):
    with open(caminho, 'r') as f:
        return list(map(int, f.read().split()))

def main():
    pasta = 'instancias-num'
    arquivos = sorted(os.listdir(pasta))

    print(f"{'Arquivo':<25} {'Selection Sort (s)':<20} {'Insertion Sort (s)'}")
    print('-' * 65)

    for arquivo in arquivos:
        try:
            caminho = os.path.join(pasta, arquivo)
            dados = ler_instancia(caminho)

            print(f"Processando {arquivo}...")

            # Selection Sort
            dados1 = dados.copy()
            start1 = time.time()
            selection_sort(dados1)
            end1 = time.time()
            tempo_selection = end1 - start1

            # Insertion Sort
            dados2 = dados.copy()
            start2 = time.time()
            insertion_sort(dados2)
            end2 = time.time()
            tempo_insertion = end2 - start2

            print(f"{arquivo:<25} {tempo_selection:<20.6f} {tempo_insertion:.6f}")

        except Exception as e:
            print(f"{arquivo:<25} ERRO AO PROCESSAR: {e}")

if __name__ == '__main__':
    main()
