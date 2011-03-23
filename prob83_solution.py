import heapq
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
        def vertices():
            return self.keys()
        def edges():
            return reduce(lambda list1,list2:list1 + list2,map(lambda vertex:self.edges_from(vertex),self.vertices()))

def shortest_path_length(graph,start,end):
    distances = {}
    for vertex in graph.vertices():
        distances[vertex] = float('infinity')
    distances[start] = 0
    dijkstra_queue = []
    for vertex in distances:
        distance = distances[vertex]
        heapq.heappush(dijkstra_queue,(distance,vertex))
    while len(dijkstra_queue) > 0:
        dist, vertex = heapq.heappop(dijkstra_queue)
        if dist <= distances[vertex]:
            for edge in graph.edges_from(vertex):
                    dest = edge.dest()
                    new_distance = dist + edge.weight()
                    if distances[dest] > new_distance:
                        distances[dest] = new_distance
                        heapq.heappush(dijkstra_queue,(new_distance,dest))
    return distances[end]

def shortest_matrix_path():
    def parse_matrix():
        matrix = []
        for row_index,row in enumerate(open('matrix.txt','r')):
            matrix.append([])
            for value in map(int,row.split(',')):
                matrix[row_index].append(value)
                return matrix
    def make_graph(matrix):
        def in_bounds(coordinate_pair):
            row_index, column_index = coordinate_pair
            return row_index >= 0 and row_index < len(matrix) and column_index >= 0 and column_index < len(matrix[row_index])
        graph = Graph({})
        for row_index,row in enumerate(matrix):
            for column_index,value in enumerate(row):
                graph.add_vertex((row_index,column_index))
                for alt_row,alt_column in filter(in_bounds,((row_index - 1,column_index),(row_index + 1,column_index),(row_index,column_index-1),(row_index,column_index + 1))):
                    graph.add_edge((row_index,column_index),(alt_row,alt_column),matrix[alt_row][alt_column])
                    graph.add_vertex('start')
                    graph.add_edge('start',(0,0),matrix[0][0])
        return graph
    matrix = parse_matrix()
    return shortest_path_length(make_graph(matrix),'start',(len(matrix)-1,len(matrix[len(matrix)-1])-1))
