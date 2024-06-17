#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import time
from maze import generate_maze
import numpy as np

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

class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # Koszt drogi od punktu startowego do bie��cego w�z�a
        self.h = 0  # Przybli�ony koszt odleg�o�ci od bie��cego w�z�a do celu
        self.f = 0  # Ca�kowity koszt, suma g i h

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    clock_start = time.time()
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while open_list:
        # Wybierz bieżący węzeł z listy otwartej, kt�ry ma najni�szy koszt ca�kowity
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Usuń bieżący węzeł z listy otwartej i dodaj go do listy zamkni�tej
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Sprawdź, czy osi�gni�to cel
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            clock_stop = time.time()

            print(f"Czas działania: {clock_stop - clock_start}")
            print(f"Długość ścieżki: {len(path)}")

            return path[::-1]  # Zwróć odwróconą ścieżkę

        # Wygeneruj dzieci
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
        
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or \
                    node_position[1] > (len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                # print(maze[node_position[0]][node_position[1]])
                # print(node_position)
                # print("tak")
                continue

            new_node = Node(current_node, node_position)
     
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            # Oblicz koszty dla dziecka
            child.g = current_node.g + 1

            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)

            child.f = child.g + child.h

            child_open = False
            for open_node in open_list:
                if child == open_node and child.g < open_node.g:
                    child_open = True
                    break

            if not child_open:
                open_list.append(child)
     
    


def run():
    
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

    w = 50
    h = 50

    maze = generate_maze(w+1, h+1)

    start = (1, 1)
    end = (w-1, h-1)

    clock_start = time.time()
    path = astar(maze, start, end)
    clock_end = time.time()

    # wizualizacja
    visualize_path(maze, path)


# run()


# Przykład trudny dla algorytmu A*
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


# Przykład łatwy dla algorytmu A*
    # maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    #         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
