import math

# Creating the data structure for the ontology:
class WeightedOntology:
    def __init__(self):
        self.edges = {}

    def add_edge(self, parent, child, weight):
        """Add a bidirectional edge with a weight"""
        self.edges.setdefault(parent, []).append((child, weight))
        self.edges.setdefault(child, []).append((parent, weight))


    def distance(self, a, b):
        """Find shortest distance between a and b"""

        def dfs(current, target, visited, current_dist):
            if current == target:
                return current_dist

            visited.add(current)
            shortest = float("inf")

            for neighbor, weight in self.edges.get(current, []):
                if neighbor not in visited:
                    dist = dfs(neighbor, target, visited, current_dist + weight)
                    shortest = min(shortest, dist)

            visited.remove(current)
            return shortest
        
        return dfs(a, b, set(), 0)

    def similarity(self, a, b, alpha=1.0):
        """Convert distance to similarity score using exponential decay"""
        d = self.distance(a, b)
        if d == float("inf"):
            return 0.0
        return math.exp(-alpha * d)