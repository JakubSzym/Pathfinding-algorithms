import matplotlib.pyplot as plt

x = [50, 100, 200, 300, 400, 500, 800, 1000]

# wykres dla A*

xa = [10, 30, 50, 70, 90, 120]
y = [0.0001, 0.0044, 0.0047, 0.23, 1.05, 1.65 ]

plt.figure(1)
plt.title("A*")
plt.plot(xa, y)
plt.xlabel("rozmiar")
plt.ylabel("czas [s]")

# wykres dla A* z networkx

y = [0.0013, 0.006, 0.032, 0.061, 0.17, 0.29, 0.8, 1.1]

plt.figure(3)
plt.title("A* --- networkx")
plt.plot(x, y)
plt.xlabel("rozmiar")
plt.ylabel("czas [s]")

# wykres dla Dijkstry

y = [0.0007, 0.0033, 0.015, 0.029, 0.061, 0.11, 0.37, 0.52]

plt.figure(4)
plt.title("Dijkstra")
plt.plot(x, y)
plt.xlabel("rozmiar")
plt.ylabel("czas [s]")

# wykres dla Dijkstry z networkx

y = [0.003, 0.02, 0.14, 0.52, 1.2, 2.0, 12.8, 20.6]

plt.figure(5)
plt.title("Dijkstra --- networkx")
plt.plot(x, y)
plt.xlabel("rozmiar")
plt.ylabel("czas [s]")

# wykres dla BFS

y = [0.0002, 0.0009, 0.005, 0.018, 0.04, 0.09, 0.19, 0.41]

plt.figure(6)
plt.title("BFS")
plt.plot(x, y)
plt.xlabel("rozmiar")
plt.ylabel("czas [s]")

plt.show()