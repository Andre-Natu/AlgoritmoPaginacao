def calcular_fifo(quadros_memoria, sequencia_referencia):
    faltas = 0
    fila_quadros = []

    for referencia in sequencia_referencia:
        # Se a referência já estiver na fila, não precisa fazer nada.
        if referencia not in fila_quadros:
            # Se a fila de quadros já estiver cheia, remove a página mais antiga
            if len(fila_quadros) >= quadros_memoria:
                fila_quadros.pop(0)

            # Adiciona a nova referência na fila
            fila_quadros.append(referencia)
            faltas += 1

    return faltas
