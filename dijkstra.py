#!/usr/bin/env python3

import heapq
import matplotlib.pyplot as plt
import time

def dijkstra(graph, start, end):
    clock_start = time.time()
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0 
    queue = [(0, start)]
    previous = {}  # słownik przechowujący poprzedników dla każdego wierzchołka

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_vertex == end:
            break

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex  # zapisz poprzednika
                heapq.heappush(queue, (distance, neighbor))

    # Odtwórz ścieżkę zakończoną
    path = []
    current = end
    while current in previous:
        path.insert(0, current)
        current = previous[current]
    path.insert(0, start)

    clock_end = time.time()
    
    print("Minimalna liczba kroków od punktu startowego do punktu końcowego:", distances[end])
    print(f"Czas działania: {clock_end - clock_start}")
    print("Ścieżka:",path)
    
    visualize_path(maze, path)

def generate_maze_graph_from_matrix(maze):
    rows = len(maze)
    cols = len(maze[0])
    graph = {}
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:  # Pomijamy ściany
                continue
            vertex = (i, j)
            neighbors = {}
            if i > 0 and maze[i-1][j] == 0:
                neighbors[(i-1, j)] = 1
            if i < rows - 1 and maze[i+1][j] == 0:
                neighbors[(i+1, j)] = 1
            if j > 0 and maze[i][j-1] == 0:
                neighbors[(i, j-1)] = 1
            if j < cols - 1 and maze[i][j+1] == 0:
                neighbors[(i, j+1)] = 1
            graph[vertex] = neighbors
    return graph

def visualize_path(maze, path):
    # Utwórz obiekt do rysowania
    fig, ax = plt.subplots()
    
    # Przetwórz labirynt
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                # Jeśli jest ściana, dodaj prostokąt koloru czarnego
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='black'))
            elif (i, j) in path:
                # Jeśli punkt jest na ścieżce, oznacz go kolorem czerwonym
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='red'))
            else:
                # W przeciwnym razie, dodaj prostokąt koloru białego
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='white'))
    
    # Ustaw granice i etykiety osi
    ax.set_xlim(0, len(maze[0]))
    ax.set_ylim(-len(maze), 0)
    ax.set_aspect('equal')
    ax.set_xticks(range(len(maze[0])))
    ax.set_yticks(range(-len(maze), 0))

    # Pokaż rysunek
    plt.grid(True)
    plt.show()


maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (0, 0)
end = (9, 9)

maze_graph = generate_maze_graph_from_matrix(maze)


dijkstra(maze_graph, start, end)

# Przykład trudny dla algorytmu Dijkstry
# maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#             [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
#             [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Przykład łatwy dla algorytmu Dijkstry
    # maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    #         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]