# graph dictionary
'''
graph = {'a': ['d'],
         'b': ['d', 'f'],
         'c': [],
         'd': ['a', 'b', 'e', 'f'],
         'e': ['d'],
         'f': ['b', 'd']}
'''


class Graph:

    # We can initialize an object with an existing graph. If we don't,
    # an empty graph is created, which is represented by an empty 
    # dictionary.
    def __init__(self, graph = {}):
        self.__graph = graph
    
    # Here's our edges function turned into a method. It returns 
    # the list of all the edges.
    def edges(self):
        return [(node, neighbor) 
                 for node in self.__graph 
                 for neighbor in self.__graph[node]]
    
    # Now that we have a method that returns all the edges, let's
    # create a method that returns all the nodes. 

    # We must convert the keys view that is returned by the keys()
    # method to a list.

    # If you want to learn more about dictionary views, I have a video 
    # about it, so feel free to watch. -> link

    def nodes(self):
        return list(self.__graph.keys())

    # And here's the isolated_nodes method, which returns all the isolated 
    # nodes.
    def isolated_nodes(self):
        return [node for node in self.__graph if not self.__graph[node]]
    
    # We'll define two more methods. One for adding new nodes and the
    # other for adding new edges. 

    # Let's start with the nodes:
    def add_node(self, node):
        # If we try to add a node that already exists in the graph,
        # nothing will happen. If the node doesn't exist, it will
        # be created as an isolated node.
        if node not in self.__graph:
            self.__graph[node] = []

    # And now the edges.
    def add_edge(self, node1, node2):
        # We assume that by calling this method, 2 edges are
        # created: one from node1 to node2 and one from node to node1.

        # There are 4 possible scenarios here:
        # 1. The two nodes may both exist in the graph or
        # 2. node1 exists in the graph but not node2 or
        # 3. node2 exists in the graph but not node1 or
        # 4. neither node1 nor node2 exists in the graph

        # The method has to take care of each of these cases. To 
        # make it easier, let's first check if the two nodes exist 
        # in the graph and if they don't, let's add them:
        if node1 not in self.__graph:
            self.add_node(node1)
        if node2 not in self.__graph:
            self.add_node(node2)

        # Now we know for sure that the two nodes exist in the graph.
        # Let's add the edges between them.
        self.__graph[node1].append(node2)
        self.__graph[node2].append(node1)


# example code
'''
g = Graph(graph)

print("The nodes:")
for node in g.nodes():
    print(node)

print("\nThe isolated nodes:")
for isolated_node in g.isolated_nodes():
    print(isolated_node)

print("\nThe edges:")
for edge in g.edges():
    print(edge)

# Now the transportation company is doing better. You can now travel
# to Miami. Let's create a new node, m.
g.add_node('m')

# Now m is an isolated node. Let's print all the nodes and all the
# isolated nodes again.
print("\nThe nodes after adding 'm':")
for node in g.nodes():
    print(node)

print("\nThe isolated nodes after adding 'm':")
for isolated_node in g.isolated_nodes():
    print(isolated_node)

# We can go from Kansas City and from Washington to Miami, so we'll need
# two connections, or edges.
g.add_edge('k', 'm')
g.add_edge('w', 'm')

# Now two things have changed: First, we should be able to see the new
# edges. Second, k and m are no longer isolated nodes becaise they are
# connected, do there should be no isolated nodes at all.
# Let's check it out:
print("\nThe edges after connecting 'k' with 'm' and 'w' with 'm':")
for edge in g.edges():
    print(edge)

print("\nThe isolated nodes after connecting 'k' with 'm' and 'w' with 'm':")
if not g.isolated_nodes():
    print("There are no isolated nodes.")
else:
    for isolated_node in g.isolated_nodes():
        print(isolated_node)

# Finally, let's add a totally new edge between two totally new
# nodes. Let's say there's a second line open between Sacramento ('s')
# and Vegas ('v'):
g.add_edge('s', 'v')

# Let's see if the new edge was successfully created. Let's print all
# the nodes and edges one more time.
print("The nodes after adding an edge between 's' and 'v':")
for node in g.nodes():
    print(node)

print("\nThe edges after adding an edge between 's' and 'v':")
for edge in g.edges():
    print(edge)

'''