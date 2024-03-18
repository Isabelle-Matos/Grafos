import networkx as nx
import re

def grafos():
    grafo = nx.Graph()
    grafo = nx.read_gml("sjdr.gml")

    return grafo

def sjrd(g):

    esquinas = set()

    edgelist = list(g.edges(data=True))
    graus = dict(g.degree())
    vertices_ordenados = sorted(graus, key=graus.get, reverse=True)

    f = open('saida.txt', 'w')

    while g.edges:
        for v in vertices_ordenados:
            for i in edgelist:
                if g.has_edge(i[0], i[1]):
                    if v == i[0] or v == i[1]:
                        esquinas.add(v)
                        g.remove_edge(i[0], i[1])
                        nome = i[2]['name']
                        f.write(f'{nome} monitorada pela câmera na esquina {v}')
                        f.write('\n')
                        # print(f'{nome} monitorada pela câmera na esquina {v}')
                        graus = dict(g.degree())
                        vertices_ordenados = sorted(graus, key=graus.get, reverse=True)

    f.write('\n')
    f.write("Lista de esquinas onde serão colocadas as câmeras:")
    # print("Lista de esquinas onde serão colocadas as câmeras:")
    for k in esquinas:
        f.write(k)
        f.write('\n')
        print(k)
    f.close()

G = grafos()
esq = sjrd(G)





