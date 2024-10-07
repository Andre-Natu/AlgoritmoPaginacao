import fifo
import lru
import otm

nome_arquivo = "entrada.txt"


# Alunos: Andre Lopes e Antonio Rocha

def ler_entrada():
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Armazena o primeiro valor na variável quadros_memoria
    memoria = int(linhas[0].strip())

    # Armazena o restante dos valores em uma lista
    valores = [int(linha.strip()) for linha in linhas[1:]]

    return memoria, valores


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    quadros_memoria, sequencia_referencia = ler_entrada()

    faltas_fifo = fifo.calcular_fifo(quadros_memoria, sequencia_referencia)
    print("FIFO ", faltas_fifo)

    faltas_otm = otm.calcular_otm(quadros_memoria, sequencia_referencia)
    print("OTM ", faltas_otm)

    faltas_lru = lru.calcular_lru(quadros_memoria, sequencia_referencia)
    print("LRU ", faltas_lru)
