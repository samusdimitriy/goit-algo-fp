import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if weight is None:
            weight = 0
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))

    def dijkstra(self, start_vertex):
        distances = {vertex: float("infinity") for vertex in self.vertices}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


def main():
    metro_graph = Graph()

    metro_graph.add_vertex("Alexanderplatz")
    metro_graph.add_vertex("Friedrichstrasse")
    metro_graph.add_vertex("Hauptbahnhof")
    metro_graph.add_vertex("Brandenburger Tor")
    metro_graph.add_vertex("Potsdamer Platz")
    metro_graph.add_vertex("Ostkreuz")
    metro_graph.add_vertex("Prenzlauer Allee")
    metro_graph.add_vertex("Gesundbrunnen")
    metro_graph.add_vertex("Wedding")
    metro_graph.add_vertex("Frankfurter Allee")
    metro_graph.add_vertex("Treptower Park")
    metro_graph.add_vertex("Schlesisches Tor")
    metro_graph.add_vertex("Spittelmarkt")

    metro_graph.add_edge("Alexanderplatz", "Friedrichstrasse", 1)
    metro_graph.add_edge("Friedrichstrasse", "Hauptbahnhof", 1)
    metro_graph.add_edge("Alexanderplatz", "Brandenburger Tor", 2)
    metro_graph.add_edge("Brandenburger Tor", "Potsdamer Platz", 1)
    metro_graph.add_edge("Potsdamer Platz", "Hauptbahnhof", 2)
    metro_graph.add_edge("Hauptbahnhof", "Gesundbrunnen", 3)
    metro_graph.add_edge("Gesundbrunnen", "Wedding", 1)
    metro_graph.add_edge("Alexanderplatz", "Frankfurter Allee", 3)
    metro_graph.add_edge("Frankfurter Allee", "Ostkreuz", 1)
    metro_graph.add_edge("Ostkreuz", "Treptower Park", 2)
    metro_graph.add_edge("Treptower Park", "Schlesisches Tor", 2)
    metro_graph.add_edge("Alexanderplatz", "Prenzlauer Allee", 2)
    metro_graph.add_edge("Prenzlauer Allee", "Gesundbrunnen", 2)
    metro_graph.add_edge("Alexanderplatz", "Spittelmarkt", 2)

    start_vertex = "Alexanderplatz"
    shortest_distances = metro_graph.dijkstra(start_vertex)

    print("\nShortest distances from Alexanderplatz:")
    print("Station                | Distance")
    print("-----------------------|---------")
    for station, dist in sorted(shortest_distances.items()):
        d = "inf" if dist == float("infinity") else str(dist)
        print(f"{station:<23} | {d}")


if __name__ == "__main__":
    main()
