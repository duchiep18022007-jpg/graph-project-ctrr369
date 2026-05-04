import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

graph = {}

# ====== ĐỌC FILE ======
def read_graph_from_file(filename="data.txt"):
    global graph
    graph = {}

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 3:
                    continue

                u, v, w = parts
                w = int(w)

                graph.setdefault(u, []).append((v, w))
                graph.setdefault(v, []).append((u, w))

        print("✅ Đã đọc đồ thị từ file")

    except FileNotFoundError:
        print("❌ Không tìm thấy file data.txt")


# ====== VẼ ĐỒ THỊ ======
def draw_graph(title="Graph"):
    G = nx.Graph()

    for u in graph:
        for v, w in graph[u]:
            G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)

    nx.draw(G, pos,
            with_labels=True,
            node_color="lightblue",
            node_size=2000,
            font_size=12)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title(title)
    plt.show()


# ====== BFS ======
def bfs(start):
    visited = set()
    queue = deque([start])

    print("BFS:", end=" ")

    while queue:
        u = queue.popleft()
        if u not in visited:
            print(u, end=" ")
            visited.add(u)

            for v, _ in graph[u]:
                if v not in visited:
                    queue.append(v)

    print()
    draw_graph("BFS")


# ====== DFS ======
def dfs(start):
    visited = set()

    def dfs_util(u):
        print(u, end=" ")
        visited.add(u)

        for v, _ in graph[u]:
            if v not in visited:
                dfs_util(v)

    print("DFS:", end=" ")
    dfs_util(start)
    print()

    draw_graph("DFS")


# ====== MENU ======
def main():
    while True:
        print("\n===== MENU =====")
        print("1. Đọc đồ thị từ file")
        print("2. BFS")
        print("3. DFS")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            read_graph_from_file()
        elif choice == "2":
            bfs(input("Start: "))
        elif choice == "3":
            dfs(input("Start: "))
        elif choice == "0":
            print("👋 Thoát")
            break
        else:
            print("❌ Không hợp lệ")


if __name__ == "__main__":
    main()