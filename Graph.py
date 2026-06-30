import networkx as nx
import matplotlib.pyplot as plt


def are_isomorphic(graph1, graph2):
    return nx.is_isomorphic(graph1, graph2)
go="y"
while go=="y":
    G1 = nx.Graph()
    G2 = nx.Graph()
    print("Please give me the edges for the graph G1")
    print("Enter exit to quit")
    flag=True
    while flag:
        x=input("Please enter the first vertice :  ")
        if x=="exit":
            flag=False
        if flag:
            y=input("Please enter the vertice it connects to:  ")
            G1.add_edge(x,y)
    print("Please give me the edges for the graph G2")
    print("Enter exit to quit")
    flag=True
    while flag:
        x=input("Please enter the first vertice :  ")
        if x=="exit":
            flag=False
        if flag:
            y=input("Please enter the vertice it connects to:  ")
            G2.add_edge(x,y)
        
    print("Are G1 and G2 isomorphic?", are_isomorphic(G1, G2))
    G1_C = nx.complement(G1) 
    G2_C = nx.complement(G2) 
    print("Are G1 and the complement of G1 self-complementary", are_isomorphic(G1, G1_C))
    print("Are G2 and the complement of G2 self-complementary", are_isomorphic(G2, G2_C))

    is_G1_bipartite = nx.is_bipartite(G1)
    print("Is the graph G1 bipartite?", is_G1_bipartite)

    is_G2_bipartite = nx.is_bipartite(G2)
    print("Is the graph G2 bipartite?", is_G2_bipartite)

    is_G1_C_bipartite = nx.is_bipartite(G1_C)
    print("Is the graph G1_C bipartite?", is_G1_C_bipartite)

    is_G2_C_bipartite = nx.is_bipartite(G2_C)
    print("Is the graph G2_C bipartite?", is_G2_C_bipartite)
    print("Would you like to go again?")
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))  # 2x2 grid for G1, G2, G1_C, G2_C

    pos1 = nx.spring_layout(G1)
    nx.draw(G1, pos1, ax=axs[0, 0], with_labels=True, node_color='lightblue', edge_color='gray')
    axs[0, 0].set_title("Graph G1")

    pos2 = nx.spring_layout(G2)
    nx.draw(G2, pos2, ax=axs[0, 1], with_labels=True, node_color='lightgreen', edge_color='gray')
    axs[0, 1].set_title("Graph G2")

    pos1c = nx.spring_layout(G1_C)
    nx.draw(G1_C, pos1c, ax=axs[1, 0], with_labels=True, node_color='lightcoral', edge_color='gray')
    axs[1, 0].set_title("Complement of G1")

    pos2c = nx.spring_layout(G2_C)
    nx.draw(G2_C, pos2c, ax=axs[1, 1], with_labels=True, node_color='plum', edge_color='gray')
    axs[1, 1].set_title("Complement of G2")

    for ax in axs.flat:
        ax.axis('off')

    plt.tight_layout()
    plt.show()
    go=input("Press y to go again anything else to stop:  ")

    
