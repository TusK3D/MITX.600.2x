class Node(object):
    def __init__(self, name):
        """Assume name is a str"""
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self) -> str:
        return self.name
    
class Edge(object):
    def __init__(self, _src, _dest):
        self.src = _src
        self.dest = _dest
    
    def getSource(self):
        return self.src
    def getDest(self):
        return self.dest
    def __str__(self) -> str:
        return self.src.get_name() + '-->'\
        + self.dest.get_name()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.get_name() + "-->" + self.dest.get_name()\
        + " (" + self.weight + ")"

    
class Digraph(object):
    """edges is a dict mapping a src node to a list of its children"""
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicate Node")
        else:
            self.edges[node] = []
    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDest()
        if not (src in self.edges or dest in self.edges):
            raise ValueError('Node not in Graph')
        self.edges[src].append(dest)
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self,node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)
        
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.get_name() + '-->'\
                    + dest.get_name() + '\n'
        return result[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDest(), edge.getSource())
        Digraph.addEdge(self, rev)

nodes = []
nodes.append(Node("ABC"))    
nodes.append(Node("ACB"))
nodes.append(Node("BAC"))
nodes.append(Node("BCA"))
nodes.append(Node("CAB"))
nodes.append(Node("CBA"))

g = Graph()

for n in nodes:
    g.addNode(n)



g.addEdge(Edge(g.getNode("ABC"),g.getNode("ACB")))
g.addEdge(Edge(g.getNode("ABC"),g.getNode("BAC")))
g.addEdge(Edge(g.getNode("ACB"),g.getNode("CAB")))
g.addEdge(Edge(g.getNode("BAC"),g.getNode("BCA")))
g.addEdge(Edge(g.getNode("BCA"),g.getNode("CAB")))
g.addEdge(Edge(g.getNode("CAB"),g.getNode("CBA")))
g.addEdge(WeightedEdge(g.getNode("CAB"),g.getNode("CBA"), 10))
Digraph.addEdge(g, Edge(g.getNode("CBA"),g.getNode("BCA")))

edges = g.childrenOf(nodes[5])
for n in g.edges[nodes[5]]:
    print(n)
print(g)
