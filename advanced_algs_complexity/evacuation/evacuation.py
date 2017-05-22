# python3

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def max_flow(graph, from_, to):
    flow = 0
    # your code goes here
    return flow

def find_shortest_path():
    #go through all paths until we have the (first) of shortest length
    search_path = [0]
    short_path = search_path
    while (search_path[0]!=-1):
        #the first element of search_path will be set to -1 when there are no more paths
        #look for the next path until then
        #once a path is found, compare to the current short_path and save if shorter
        search_path=find_next_path(search_path)
        if(search_path[0]!=-1): #path found
            if (short_path[0]==0 or len(search_path)<len(short_path)): #first path or shorter path then save
                short_path=search_path

def find_next_path(last_path):
    #starting with the last path, look for the next path starting with the last vertex
    #if its the last edge for the vertex, pop the vertex from the path and look at the next edge from the previous vertex
    #repeat this until the last vertex is reached size(graph) or until there are no more edges from the first vertex
    #set the only remaining element to -1 when the end is found
    #return the path if a path is found
    #do not chose reverse edges of edges that are in the path

    #figure out how to start the loop to find the path.  can i start with the next path or go back one??
    #while (graph.get_edge(path[-1] 

    
if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
