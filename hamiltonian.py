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
        # Rotate to start from the smallest vertex to avoid duplicates
        min_index = cycle.index(min(cycle[:-1]))  # exclude the last which is same as first
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

        self.printAllSolutions() 
        return True

    def printAllSolutions(self): 
        print(f"Found {len(self.all_cycles)} Hamiltonian cycle(s):")
        for cycle in sorted(self.all_cycles):
            print(" -> ".join(map(str, cycle)))


# Example usage:
g1 = Graph(5) 
g1.graph = [ 
    [0, 1, 0, 1, 0], 
    [1, 0, 1, 1, 1], 
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1], 
    [0, 1, 1, 1, 0], 
] 

g2 = Graph(5) 
g2.graph = [ 
    [0, 1, 0, 1, 0], 
    [1, 0, 1, 1, 1], 
    [0, 1, 0, 0, 1], 
    [1, 1, 0, 0, 0], 
    [0, 1, 1, 0, 0], 
] 

g3 = Graph(5) 
g3.graph = [ 
    [0, 1, 1, 0, 1], 
    [1, 0, 1, 1, 1], 
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
] 

# Run and print all Hamiltonian cycles
print("Graph 1:")
g1.hamCycle()
print("\nGraph 2:")
g2.hamCycle()
print("\nGraph 3:")
g3.hamCycle()
