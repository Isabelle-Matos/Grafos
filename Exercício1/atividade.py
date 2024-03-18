from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def grafo():
    g = nx.DiGraph()


    with open("entrada.txt", "r") as file:
            for i in file:
                partes = i.strip().split() 
                if len(partes) == 2:
                    source, target = partes[0], partes[1]
                    g.add_edge(source, target)
       
    return g

def componentes(g):
    vertices = set(g.nodes)
    k = 0
    componentes = []
    while vertices:
        v = list(vertices)[0]
        r_mais = {v}
        r_menos = {v}

        n_mais = set(g.neighbors(v))
        n_mais.add(v)

        while (n_mais - r_mais) != set():
            wk = n_mais - r_mais
            r_mais.update(wk)
            for i in r_mais:
                n_mais = n_mais.union(set(g.neighbors(i)))

        n_menos = set(g.predecessors(v))
        n_menos.add(v)

        while (n_menos - r_menos) != set():
            wk = n_menos - r_menos
            r_menos.update(wk)
            for i in r_menos:
                n_menos = n_menos.union(set(g.predecessors(i)))

        wk = r_mais.intersection(r_menos)
        vertices = vertices - wk
        k += 1
        componentes.append(list(wk))

    return componentes
            

g = grafo()
componentes_f = componentes(g)
print(componentes_f)
