def calcular_otm(quadros_memoria, sequencia_referencia):
    faltas = 0
    fila_quadros = []

    for i in range(len(sequencia_referencia)):
        referencia = sequencia_referencia[i]

        # Se a referência já estiver na fila, não precisa fazer nada.
        if referencia not in fila_quadros:

            # substitui uma pagina se a fila estiver cheia
            if len(fila_quadros) >= quadros_memoria:
                # Encontrar a página na fila que não será usada por mais tempo no futuro
                distancias = []
                for pagina in fila_quadros:
                    try:
                        # percorre todos os elementos posteriores a i e armazena a primeira posição que foi encontrada.
                        distancia = sequencia_referencia[i + 1:].index(pagina)
                    except ValueError:
                        # Se a página não for encontrada no futuro, definimos a distância como infinita
                        distancia = float('inf')
                    distancias.append(distancia)

                # Encontrar a página com a maior distância (ou que não será usada mais)
                pagina_a_remover = fila_quadros[distancias.index(max(distancias))]
                fila_quadros.remove(pagina_a_remover)

            # Adicionar a nova referência na fila
            fila_quadros.append(referencia)
            faltas += 1

    return faltas
