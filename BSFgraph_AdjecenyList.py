from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)  # For undirected graph
        else:
            print(f"Invalid route! Nodes must be between 0 and {self.vertices - 1}.")


    def display(self):
        print("\nAdjacency List Representation:")
        for i in range(self.vertices):
            print(f"Location {i} -> {self.adj_list[i]}")

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque([start])
        visited[start] = True
        bfs_order = []

        while queue:
            node = queue.popleft()
            bfs_order.append(node)

            for neighbour in self.adj_list[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

        print(f"\nBFS Traversal starting from location {start}: {bfs_order}")

# Main Program (Menu Driven)


n = int(input("Enter number of locations (nodes): "))
g = Graph(n)

while True:
    print("\n==== Graph Operations Menu ====")
    print("1. Add a route (edge)")
    print("2. Display adjacency list")
    print("3. Perform BFS traversal")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        u = int(input("Enter starting location: "))
        v = int(input("Enter ending location: "))
        g.add_edge(u, v)
        print(f"Route added between {u} and {v}.")
    elif choice == 2:
        g.display()
    elif choice == 3:
        start = int(input("Enter starting node for BFS: "))
        g.bfs(start)
    elif choice == 4:
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
