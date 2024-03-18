import queue as queue
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def grafo():
    g = nx.DiGraph()

    with open("entrada.txt", "r") as file:
        for i in file.readlines():
            partes = i.split()
            source, target, peso = partes[0], partes[1], int(partes[2])
            g.add_edge(source, target, weight=peso)

    pos = nx.spring_layout(g, seed=11)
    nx.draw(g, pos, )
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    nx.draw_networkx_labels(g, pos, font_size=10, font_family="sans-serif")
    plt.savefig("path.png")

    return g
def encontra_caminho(g):
    caminho = []
    pilha = deque()
    torneira = 's'
    pilha.append(torneira)
    menor_peso = -1

    while pilha[-1] != 't' and len(pilha) != 0:
        torneira = pilha.pop()
        #print(torneira)
        caminho.append(torneira)

        vizinho = list(g.successors(torneira))
        #print(vizinho)
        for i in vizinho:
            if i not in caminho:
                pilha.append(i)

        if (len(pilha) == 0):
            break

        if g.has_edge(torneira, pilha[-1]):
            peso = g.get_edge_data(torneira, pilha[-1])['weight']

        if menor_peso == -1 or peso < menor_peso:
            menor_peso = peso

    if len(pilha) == 0:
        return [], 0

    if pilha[-1] == 't':
        caminho.append('t')

    return caminho, menor_peso
def grafo_folgas(g, caminho, folga):
    if caminho == []:
        return

    for i in range(len(caminho) - 1):
        if g.has_edge(caminho[i], caminho[i + 1]):
            g[caminho[i]][caminho[i + 1]]['weight'] -= folga

            if g[caminho[i]][caminho[i + 1]]['weight'] == 0:
                g.remove_edge(caminho[i], caminho[i + 1])

        if g.has_edge(caminho[i + 1], caminho[i]):
            g.add_edge(caminho[i + 1], caminho[i], weight=folga)


    return g
def ford(g):
    g_folga = g
    fluxo_maximo = 0
    caminho, folga = encontra_caminho(g)

    while caminho != [] and folga != 0:
        grafo_folgas(g, caminho, folga)
        fluxo_maximo += folga
        caminho, folga = encontra_caminho(g)

    return fluxo_maximo


G = grafo()
f_maximo = ford(G)
print(f'Fluxo máximo: {f_maximo}')

