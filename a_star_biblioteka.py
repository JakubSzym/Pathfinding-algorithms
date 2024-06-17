#!/usr/bin/env python3
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time
from maze import generate_maze

def visualize_path(maze, path):
    fig, ax = plt.subplots()
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='black'))
            elif (i, j) in path:
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='red'))
            else:
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='white'))

    ax.set_xlim(0, len(maze[0]))
    ax.set_ylim(-len(maze), 0)
    ax.set_aspect('equal')
    ax.set_xticks(range(len(maze[0])))
    ax.set_yticks(range(-len(maze), 0))

    plt.grid(True)
    plt.show()

def astar_with_networkx(maze, graph, start, end):
    start_clock = time.time()
    path = nx.astar_path(graph, start, end)
    end_clock = time.time()

    print(f"Czas działania: {end_clock-start_clock}")
    print(f"Długość ściezki: {len(path)}")

    visualize_path(maze, path)



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

def run():
    w = 1000
    h = 1000

    maze = generate_maze(w+1, h+1)

    start = (1,1)
    end = (w-1, h-1)

    # Tworzenie grafu na podstawie labiryntu
    G = nx.grid_2d_graph(len(maze), len(maze[0]))

    # Usunięcie krawędzi odpowiadających ścianom labiryntu
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                G.remove_node((i, j))

    # Znalezienie najkrótszej ścieżki za pomocą algorytmu A*
    start_clock = time.time()
    path = nx.astar_path(G, start, end)
    end_clock = time.time()

    print(f"Czas działania: {end_clock - start_clock}")

    # Wizualizacja labiryntu
    visualize_path(maze, path)

# run()
