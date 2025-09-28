import uuid
from collections import deque
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, val, color="skyblue"):
        self.left = None
        self.right = None
        self.val = val
        self.color = color
        self.id = str(uuid.uuid4())

    def __lt__(self, other):
        return self.val < other.val


def build_heap_graph(graph, heap, pos):
    graph.add_node(heap[0].id, color=heap[0].color, label=heap[0].val)
    queue = deque([(0, 0, 0, 1)])
    visited = {heap[0].id}

    while queue:
        index, x, y, layer = queue.popleft()
        node = heap[index]

        left_index = 2 * index + 1
        right_index = left_index + 1

        if left_index < len(heap):
            left = heap[left_index]
            if left.id not in visited:
                lx = x - 1 / 2**layer
                ly = y - 1
                graph.add_node(left.id, color=left.color, label=left.val)
                pos[left.id] = (lx, ly)
                visited.add(left.id)
                queue.append((left_index, lx, ly, layer + 1))
            graph.add_edge(node.id, left.id)

        if right_index < len(heap):
            right = heap[right_index]
            if right.id not in visited:
                rx = x + 1 / 2**layer
                ry = y - 1
                graph.add_node(right.id, color=right.color, label=right.val)
                pos[right.id] = (rx, ry)
                visited.add(right.id)
                queue.append((right_index, rx, ry, layer + 1))
            graph.add_edge(node.id, right.id)


def draw_heap(heap):
    if not heap:
        return

    graph = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}
    build_heap_graph(graph, heap, pos)
    colors = [n[1]["color"] for n in graph.nodes(data=True)]
    labels = {n[0]: n[1]["label"] for n in graph.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(
        graph,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


def main():
    heap = [Node(0), Node(4), Node(5), Node(10), Node(1), Node(3)]
    heapq.heapify(heap)
    draw_heap(heap)


if __name__ == "__main__":
    main()
