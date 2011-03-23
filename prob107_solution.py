class Edge(tuple):
    def source(self):
        return self[0]
    def dest(self):
        return self[1]
    def weight(self):
        return self[2]

class Graph(dict):
    def add_vertex(self,vertex):
        self[vertex] = []
    def add_edge(self,source,dest,weight):
        self[source].append(Edge((source,dest,weight)))
    def edges_from(self,source):
        return self[source]
    def vertices(self):
        return self.keys()
    def edges(self):
        return reduce(lambda list1,list2:list1 + list2,map(lambda vertex:self.edges_from(vertex),self.vertices()))

def minimum_spanning_tree(undirected_graph):
    edges = sorted(undirected_graph.edges(),key = lambda edge: edge.weight())
    parents = {}
    ranks = {}
    def union(vertex1,vertex2):
        r1 = find(vertex1)
        r2 = find(vertex2)
        if r1 == r2:
            return
        if ranks[r1] > ranks[r2]:
            parents[r2] = r1
            ranks.pop(r2)
        else:
            parents[r1] = r2
            if ranks[r1] == ranks[r2]:
                ranks[r2] = ranks[r2] + 1
                ranks.pop(r1)
    def find(vertex):
        if vertex != parents[vertex]:
            parents[vertex] = find(parents[vertex])
            return parents[vertex]
    mst = []
    vertices = undirected_graph.vertices()
    for vertex in vertices:
        parents[vertex] = vertex
        ranks[vertex] = 0
    for edge in edges:
        vertex1, vertex2 = edge.source(),edge.dest()
        if find(vertex1) != find(vertex2):
            union(vertex1,vertex2)
            mst.append(edge)
            if len(mst) == len(vertices) - 1:
                break
    return mst

def smallest_connected_network():
    network_file = open('network.txt','r')
    network_graph = Graph({})
    for source, line in enumerate(network_file):
        network_graph.add_vertex(source)
        dests = line[:-2].split(',')
        for dest in range(source,len(dests)):
            weight = dests[dest]
            if weight != '-':
                weight = int(weight)
                network_graph.add_edge(source,dest,weight)
    return sum(map(lambda edge:edge.weight(),network_graph.edges())) - sum(map(lambda edge: edge.weight(),minimum_spanning_tree(network_graph)))

print smallest_connected_network()
