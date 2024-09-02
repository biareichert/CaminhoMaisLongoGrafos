#Busca por exaustão
def caminhoMaximo(grafo, inicial, final):
    #Iniciando variaveis
    distanciaMax = -1
    pilha = [([inicial], 0)]
    #enquanto a pilha nao estiver vazia
    while pilha:
        caminho, distancia = pilha.pop()
        vertice = caminho[-1]

        if vertice == final:
            if distancia > distanciaMax:
                distanciaMax = distancia
                caminhoMax = caminho
            continue
        #percorre o grafo no vertice selecionado e empilha
        for destino, peso in grafo[vertice]:
            pilha.append( (caminho+[destino], peso+distancia) )

    return caminhoMax

def verificarValores(grafo):
    for i in range(len(grafo)):
        for destino, peso in grafo[i]:
            if(peso < 0):
                return 1
    return 0

def main():

    grafo = {0:[(1, 11), (2, 10)],
             1:[(3, 2), (4, 2)],
             2:[(3, 5),(4, 1)],
             3:[(5, 20)],
             4:[(6, 3), (7, 4)],
             5:[(6, 5), (7, 30)],
             6:[(8, 2)],
             7:[(8, 5)],
             8:[(9, 30)],
             9:[]}

    if(verificarValores(grafo) == 1):
        print("O grafo possui valores negativos.")
    else:

        #calcular os caminhos entre todos os vertices do grafo
        #caminhos de U até U sao ignorados automaticamente
        for i in range(len(grafo)):
            for j in range(len(grafo)):
                if not i==j:
                    try:
                        caminhoMax = caminhoMaximo(grafo, i, j)
                        print("O caminho máximo entre {} e {} é: ".format(i,j),caminhoMax)
                    except:
                        #print("nao existe caminho valido entre {} e {}".format(i,j))
                        pass

        print("Desenha desenhar o grafo? digite 1 caso queira")
        aux = int(input(">>"))
        if aux == 1:
            try:
                import matplotlib.pyplot as plt
                import networkx as nx
            except ImportError:
                print('\nA biblioteca networkx não esta instalada')
            else:

                G = nx.DiGraph()
                for vertice in grafo:
                    for i in range(len(grafo[vertice])):
                        origem = vertice
                        peso = grafo[vertice][i][1]
                        destino = grafo[vertice][i][0]
                        G.add_edge(origem,destino,weight=peso)

                arestas = [(u,v) for (u,v,w) in G.edges(data=True)]
                pos = nx.shell_layout(G, scale=1) #spectral,circular,shell
                edge_labels = nx.get_edge_attributes(G, 'weight')

                nx.draw_networkx_nodes(G, pos, node_size=750, node_color='white', linewidths=1, edgecolors='black')
                nx.draw_networkx_edges(G, pos, edgelist=arestas, width=2, alpha=1, edge_color="red", arrowsize=20, arrowstyle= '->')

                nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='black', label_pos=0.5)
                nx.draw_networkx_labels(G, pos, font_size=12,font_color='black')

                plt.axis('off')
                plt.show()

if __name__ == "__main__":
    main()
