import a_star
import dijkstra
import bfs
import a_star_biblioteka
import dijkstra_biblioteka
import networkx as nx

from maze import generate_maze

# porównanie jakościowe algorytmów

w = 50
h = 50

start = (1,1)
end = (w-1, h-1)

maze = generate_maze(w+1, h+1)

# Dijkstra

print("Dijkstra")
print("-------------")
dijkstra_maze_graph = dijkstra.generate_maze_graph_from_matrix(maze)

dijkstra.dijkstra(maze, dijkstra_maze_graph, start, end)

# A*

print("A*")
print("-------------")

astar_path = a_star.astar(maze, start, end)
a_star.visualize_path(maze, astar_path)

# BFS

print("BFS")
print("-------------")

bfs_maze_graph = bfs.generate_maze_graph_from_matrix(maze)

bfs.bfs(maze, bfs_maze_graph, start, end)

# A* z networkx

print("A* - networkx")
print("-------------")

G = nx.grid_2d_graph(len(maze), len(maze[0]))

    
for i in range(len(maze)):
  for j in range(len(maze[0])):
    if maze[i][j] == 1:
      G.remove_node((i, j))

a_star_biblioteka.astar_with_networkx(maze, G, start, end)

# Dijsktra z networkx

print("Dijkstra - networkx")
print("-------------")

d_graph = dijkstra_biblioteka.generate_maze_graph_from_matrix(maze)

dijkstra_biblioteka.dijkstra_with_networkx(maze, d_graph, start, end)