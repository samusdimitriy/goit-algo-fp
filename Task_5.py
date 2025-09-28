import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def bfs_nodes(root):
    nodes = []
    queue = deque([root])
    visited = set()

    while queue:
        node = queue.popleft()
        if node.id in visited:
            continue
        visited.add(node.id)
        nodes.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return nodes


def build_graph(root):
    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    queue = deque([(root, 0, 0, 1)])
    graph.add_node(root.id, label=root.val)

    while queue:
        node, x, y, layer = queue.popleft()

        if node.left:
            left = node.left
            lx = x - 1 / 2**layer
            ly = y - 1
            graph.add_node(left.id, label=left.val)
            pos[left.id] = (lx, ly)
            queue.append((left, lx, ly, layer + 1))
            graph.add_edge(node.id, left.id)

        if node.right:
            right = node.right
            rx = x + 1 / 2**layer
            ry = y - 1
            graph.add_node(right.id, label=right.val)
            pos[right.id] = (rx, ry)
            queue.append((right, rx, ry, layer + 1))
            graph.add_edge(node.id, right.id)

    return graph, pos


def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def generate_palette(count):
    if count <= 0:
        return []

    start = (0x12, 0x30, 0x5A)
    end = (0xC6, 0xE0, 0xFF)

    if count == 1:
        return [rgb_to_hex(start)]

    palette = []
    for index in range(count):
        factor = index / (count - 1)
        color = tuple(int(start[i] + (end[i] - start[i]) * factor) for i in range(3))
        palette.append(rgb_to_hex(color))

    return palette


def traversal_colors(root, palette, strategy):
    colors = {}
    visited = set()
    index = 0
    container = deque([root]) if strategy == "breadth" else [root]

    while container:
        node = container.popleft() if strategy == "breadth" else container.pop()
        if node.id in visited:
            continue
        visited.add(node.id)
        colors[node.id] = palette[index]
        index += 1

        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        if strategy == "breadth":
            container.extend(children)
        else:
            container.extend(reversed(children))

    return colors


def draw_tree(root, traversal_type):
    graph, pos = build_graph(root)
    nodes = bfs_nodes(root)
    palette = generate_palette(len(nodes))
    color_map = traversal_colors(root, palette, traversal_type)

    node_colors = [color_map[node_id] for node_id in graph.nodes()]
    labels = {node: data["label"] for node, data in graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        graph,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=node_colors,
        font_color="white",
    )
    plt.show()


def main():
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(11)
    root.right.left.right = Node(12)
    root.right.right.left = Node(13)
    root.right.right.right = Node(14)

    draw_tree(root, traversal_type="depth")
    draw_tree(root, traversal_type="breadth")


if __name__ == "__main__":
    main()
