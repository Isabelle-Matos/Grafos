import queue
import networkx as nx


def grafo():
    g = nx.DiGraph()

    with open("entrada.txt", "r") as file:
        for i in file.readlines():
            partes = i.split() 
            source, target, peso = int(partes[0]), int(partes[1]), int(partes[2])
            g.add_edge(source, target, weight = peso)
               
        
    return g

def pert(g):
    vertices = list(g.nodes())
    fifo = queue.Queue()
    fifo.put(vertices[0])
    
    ti = dict()
    tf = dict()
    critico = list()

    for i in vertices:
        ti[i] = 0
        tf[i] = 0

    while not fifo.empty():
        v = fifo.get()
        num_mais_v = list(g.neighbors(v))

        for i in num_mais_v:
            if g.has_edge(v, i):
                weight = g.get_edge_data(v, i)['weight']
                peso_final = weight + ti[v]

            if ti[i] < peso_final:
                ti[i] = peso_final

            fifo.put(i)

    fifo.put(vertices[-1])
    tf[vertices[-1]] = ti[vertices[-1]]

    while not fifo.empty():
        v = fifo.get()
        num_menos_v = list(g.predecessors(v))

        for i in num_menos_v:
            #print(v, i)
            weight = g.get_edge_data(i, v)['weight']
            peso_final = tf[v] - weight
            #print(v, i)
            #print(weight)
            #print(peso_final)
            if tf[i] !=0 and tf[i] > peso_final:
                tf[i] = peso_final
            elif tf[i] == 0:
                tf[i] = peso_final

            fifo.put(i)

    for i in ti.keys():
        if ti[i] == tf[i]:
            critico.append(i)

    print(f"ES: {ti}")
    print(f"LS: {tf}")
    print(f"Caminho Critico: {critico}")


g = grafo()
pert(g)

