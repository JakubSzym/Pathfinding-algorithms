#!/usr/bin/env python3

import matplotlib.pyplot as plt
import time
import networkx as nx
from maze import generate_maze

def visualize_path(maze, path):
    # Utwórz obiekt do rysowania
    fig, ax = plt.subplots()
    
    # Przetwórz labirynt
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                # Je�li jest ściana, dodaj prostokąt koloru czarnego
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='black'))
            elif (i, j) in path:
                # Jeśli punkt jest na ścieżce, oznacz go kolorem czerwonym
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='red'))
            else:
                # W przeciwnym razie, dodaj prostokąt koloru bia�ego
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='white'))
    
    # Ustaw granice i etykiety osi
    ax.set_xlim(0, len(maze[0]))
    ax.set_ylim(-len(maze), 0)
    ax.set_aspect('equal')
    ax.set_xticks(range(len(maze[0])))
    ax.set_yticks(range(-len(maze), 0))

    plt.grid(True)
    plt.show()

def generate_maze_graph_from_matrix(maze):
    rows = len(maze)
    cols = len(maze[0])
    graph = {}
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:  # Pomijamy �ciany
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

def dijkstra_with_networkx(maze, graph, start, end):
    clock_start = time.time()
    G = nx.Graph(graph)  # Tworzymy graf z naszego słownika
    path = nx.dijkstra_path(G, source=start, target=end)  # Znajdujemy najkrótszą ścieżkę
    clock_end = time.time()
    
    print("Minimalna liczba krokow od punktu startowego do punktu koncowego:", len(path))
    print(f"Czas dzialania: {clock_end - clock_start}")

    visualize_path(maze, path)

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

def run():

    w = 100
    h = 100

    maze = generate_maze(w+1, h+1)

    start = (1, 1)
    end = (w-1, h-1)

    maze_graph = generate_maze_graph_from_matrix(maze)

    dijkstra_with_networkx(maze, maze_graph, start, end)

# run()