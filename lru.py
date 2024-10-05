def calcular_lru(quadros_memoria, sequencia_referencia):
    faltas = 0
    fila_quadros = []

    for referencia in sequencia_referencia:
        # Se a referência não estiver fila, precisa adicionar ela a fila.
        if referencia not in fila_quadros:
            # Se a fila de quadros já estiver cheia, remove a página menos recentemente usada
            if len(fila_quadros) >= quadros_memoria:
                # a página do início da lista sempre vai ser a menos recentemente usada.
                fila_quadros.pop(0)

            # Adiciona a nova referência na fila
            fila_quadros.append(referencia)
            faltas += 1
        else:
            # Se a referência já estiver na fila, significa que ela foi a mais usada recentemente(agora)
            # logo tiramos ela da posição que ela estiver na fila e adicionamos ela no final.
            fila_quadros.remove(referencia)
            fila_quadros.append(referencia)

    return faltas
