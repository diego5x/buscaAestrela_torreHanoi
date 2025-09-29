import heapq

def heuristica(estado, haste_final=3):
    return sum(1 for disco in estado if disco != haste_final)

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

def a_star_iniciar(n_discos):
    estado_inicial = [list(range(n_discos, 0, -1)), [], []]  
    estado_objetivo = [[], [], list(range(n_discos, 0, -1))]  

    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0 + heuristica(estado_inicial), 0, estado_inicial, []))

    visitados = set()
    visitados.add(tuple(tuple(h) for h in estado_inicial))  

    while fila_prioridade:
        _, custo_atual, estado_atual, caminho = heapq.heappop(fila_prioridade)

        if estado_atual == estado_objetivo:
            return caminho

        for sucessor in gerar_sucessores(estado_atual):
            if tuple(tuple(h) for h in sucessor) not in visitados:
                visitados.add(tuple(tuple(h) for h in sucessor))
                heapq.heappush(fila_prioridade, (custo_atual + 1 + heuristica(sucessor), custo_atual + 1, sucessor, caminho + [sucessor]))

    return None

caminho = a_star_iniciar(6)
for passo in caminho:
    print(passo)
