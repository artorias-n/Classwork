import networkx as nx
import matplotlib.pyplot as plt

class Graph(): 
    def __init__(self, vertices): 
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)] 
        self.V = vertices 
        self.all_cycles = set()

    def isSafe(self, v, pos, path): 
        if self.graph[path[pos-1]][v] == 0: 
            return False
        if v in path: 
            return False
        return True

    def hamCycleUtil(self, path, pos): 
        if pos == self.V: 
            if self.graph[path[pos-1]][path[0]] == 1: 
                cycle = tuple(path + [path[0]])
                normalized = self.normalize_cycle(cycle)
                self.all_cycles.add(normalized)
            return

        for v in range(1, self.V): 
            if self.isSafe(v, pos, path): 
                path[pos] = v 
                self.hamCycleUtil(path, pos + 1) 
                path[pos] = -1

    def normalize_cycle(self, cycle):
        min_index = cycle.index(min(cycle[:-1]))
        rotated = cycle[min_index:-1] + cycle[1:min_index+1]
        reversed_rotated = tuple(reversed(rotated))
        return tuple(min(rotated, reversed_rotated))

    def hamCycle(self): 
        path = [-1] * self.V 
        path[0] = 0
        self.all_cycles.clear()
        self.hamCycleUtil(path, 1)

        if not self.all_cycles:
            print("Solution does not exist\n")
            return False

        self.printAndDrawAllSolutions() 
        return True

    def printAndDrawAllSolutions(self): 
        print(f"Found {len(self.all_cycles)} Hamiltonian cycle(s):")
        for i, cycle in enumerate(sorted(self.all_cycles), 1):
            print(f"Cycle {i}: {' -> '.join(map(str, cycle))}")
            self.draw_cycle(cycle, i)

    def draw_cycle(self, cycle, index):
        G = nx.Graph()
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] == 1:
                    G.add_edge(i, j)

        pos = nx.circular_layout(G)
        edge_colors = ['red' if (u, v) in zip(cycle, cycle[1:]) or (v, u) in zip(cycle, cycle[1:]) else 'lightgray'
                       for u, v in G.edges()]

        plt.figure(figsize=(5, 5))
        nx.draw(G, pos, with_labels=True, node_color='lightblue',
                edge_color=edge_colors, node_size=800, font_weight='bold')
        plt.title(f"Hamiltonian Cycle {index}")
        plt.show()


# Example usage:
g3 = Graph(5) 
g3.graph = [ 
    [0, 1, 1, 0, 1], 
    [1, 0, 1, 1, 1], 
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
] 

print("Graph 3:")
g3.hamCycle()
