def heuristica(estado, haste_final=3):
    return sum(1 for i, haste in enumerate(estado) for disco in haste if disco != haste_final)

def gerar_sucessores(estado):
    sucessores = []
    for i in range(3):
        for j in range(3):
            if i != j:
                if estado[i]:
                    disco = estado[i][-1]
                    if not estado[j] or estado[j][-1] > disco:
                        novo_estado = [list(h) for h in estado]
                        novo_estado[j].append(novo_estado[i].pop())
                        sucessores.append(novo_estado)
    return sucessores

def inserir_fila_prioridade(fila, item):
    """Insere item na fila de prioridade mantendo a ordem pelo primeiro elemento da tupla (f(n))"""
    f_n = item[0]
    for idx, elem in enumerate(fila):
        if f_n < elem[0]:
            fila.insert(idx, item)
            return
    fila.append(item)

def a_star_iniciar(n_discos):
    estado_inicial = [list(range(n_discos, 0, -1)), [], []]
    estado_objetivo = [[], [], list(range(n_discos, 0, -1))]

    fila_prioridade = []
    inserir_fila_prioridade(fila_prioridade, (heuristica(estado_inicial), 0, estado_inicial, []))

    visitados = set()
    visitados.add(tuple(tuple(h) for h in estado_inicial))

    while fila_prioridade:
        f_atual, custo_atual, estado_atual, caminho = fila_prioridade.pop(0)

        if estado_atual == estado_objetivo:
            return caminho

        for sucessor in gerar_sucessores(estado_atual):
            estado_tuple = tuple(tuple(h) for h in sucessor)
            if estado_tuple not in visitados:
                visitados.add(estado_tuple)
                f_sucessor = custo_atual + 1 + heuristica(sucessor)
                inserir_fila_prioridade(fila_prioridade, (f_sucessor, custo_atual + 1, sucessor, caminho + [sucessor]))

    return None

caminho = a_star_iniciar(12)
for passo in caminho:
    print(passo)
