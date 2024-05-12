#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def visualize_path(maze, path):
    # Utw�rz obiekt do rysowania
    fig, ax = plt.subplots()
    
    # Przetw�rz labirynt
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                # Je�li jest �ciana, dodaj prostok�t koloru czarnego
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='black'))
            elif (i, j) in path:
                # Je�li punkt jest na �cie�ce, oznacz go kolorem czerwonym
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='red'))
            else:
                # W przeciwnym razie, dodaj prostok�t koloru bia�ego
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='white'))
                    # Ustaw granice i etykiety osi
    ax.set_xlim(0, len(maze[0]))
    ax.set_ylim(-len(maze), 0)
    ax.set_aspect('equal')
    ax.set_xticks(range(len(maze[0])))
    ax.set_yticks(range(-len(maze), 0))

    # Poka� rysunek
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
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    # Tworzenie w�z�a startowego i ko�cowego
    start_node = Node(None, start)
    end_node = Node(None, end)

    # Inicjalizacja listy otwartej i zamkni�tej
    open_list = []
    closed_list = []

    # Dodanie w�z�a startowego do listy otwartej
    open_list.append(start_node)

    # P�tla g��wna algorytmu A*
    while open_list:
        # Wybierz bie��cy w�ze� z listy otwartej, kt�ry ma najni�szy koszt ca�kowity
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Usu� bie��cy w�ze� z listy otwartej i dodaj go do listy zamkni�tej
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Sprawd�, czy osi�gni�to cel
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Zwr�� odwr�con� �cie�k�

        # Wygeneruj dzieci
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            # Pobierz pozycj� w�z�a
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            
            # Sprawd�, czy w�ze� jest poza granicami labiryntu
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or \
                    node_position[1] > (len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Sprawd�, czy w�ze� jest na przeszkodzie
            if maze[node_position[0]][node_position[1]] != 0:
                # print(maze[node_position[0]][node_position[1]])
                # print(node_position)
                # print("tak")
                continue

            # Utw�rz nowy w�ze�
            new_node = Node(current_node, node_position)
            

            # Dodaj nowy w�ze� do listy dzieci
            children.append(new_node)

        # Przetw�rz dzieci
        for child in children:
            # Sprawd�, czy dziecko znajduje si� na li�cie zamkni�tej
            if child in closed_list:
                continue

            # Oblicz koszty dla dziecka
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + \
                      ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Sprawd�, czy dziecko znajduje si� ju� na li�cie otwartej
            child_open = False
            for open_node in open_list:
                if child == open_node and child.g < open_node.g:  # Zmiana warunku
                    child_open = True
                    break

            # Dodaj dziecko do listy otwartej, je�li nie jest tam jeszcze
            if not child_open:
                open_list.append(child)
     
    


def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (9, 9)

    path = astar(maze, start, end)
    print(path)
    # Wywo�aj funkcj� do wizualizacji
    visualize_path(maze, path)


if __name__ == '__main__':
    main()

