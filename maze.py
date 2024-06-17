import random

# DisjointSet - zbiór rozłączny

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


# Algorytm Kruskala do generowania dużych labiryntów

def generate_maze(width, height):
    maze = [[1] * width for _ in range(height)]
    walls = []
    ds = DisjointSet(width * height)

    for y in range(1, height, 2):
        for x in range(1, width, 2):
            maze[y][x] = 0
            if x < width - 2:
                walls.append((x, y, x + 2, y))
            if y < height - 2:
                walls.append((x, y, x, y + 2))

    random.shuffle(walls)

    for x1, y1, x2, y2 in walls:
        cell1 = y1 * width + x1
        cell2 = y2 * width + x2
        if ds.find(cell1) != ds.find(cell2):
            ds.union(cell1, cell2)
            maze[(y1 + y2) // 2][(x1 + x2) // 2] = 0
            maze[y2][x2] = 0

    return maze