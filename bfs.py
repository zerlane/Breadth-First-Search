class Vertex:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {}

    def add_edge(self, start = None, end = None):


        if start in self.adj_list:
            self.adj_list[start].append(end)
        else:
            self.adj_list[start] = [end]

        if end not in self.adj_list:
            self.adj_list[end] = [start]

    def print_graph(self):
        for key in range (self.V):
            print(key, ":", end = " ")
            if (self.adj_list[key] is not None):
                print(*self.adj_list[key], sep = ", ")

    def bfs

if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    graph.add_edge(2, None)
    graph.add_edge(3, 4)


    graph.print_graph()
