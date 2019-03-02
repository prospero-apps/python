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

    # Let's begin with the method that returns all the paths 
    # between two nodes.    
    # The optional path parameter is set to an empty list, so that
    # we start with an empty path by default. 
    def all_paths(self, node1, node2, path = []):
        # We add node1 to the path.
        path = path + [node1]
        
        # If node1 is not in the graph, the function returns an empty list.
        if node1 not in self.__graph:
            return []

        # If node1 and node2 are one and the same node, we can return 
        # the path now.
        if node1 == node2:
            return [path]

        # Let's create an empty list that will store the paths.
        paths = []

        # Now we'll take each node adjacent to node1 and recursively 
        # call the all_paths method for them to find all the paths
        # from the adjacent node to node2.
        # The adjacent nodes are the ones in the value lists in 
        # the graph dictionary.        
        for node in self.__graph[node1]:
            if node not in path:

                subpaths = self.all_paths(node, node2, path)

                for subpath in subpaths:
                    paths.append(subpath)

        return paths

    # And now the other method that returns the shortest path.
    # We'll just use the method that finds all the paths and then
    # select the one with the minimum number of nodes.
    # If there are more than one paths with the minimum number of nodes,
    # the first one will be returned.
    def shortest_path(self, node1, node2):
        return sorted(self.all_paths(node1, node2), key = len)[0]



# example code
'''
g = Graph(graph)

print("The paths from 'a' to 'b':")
print(g.all_paths('a', 'b'))
print("The shortest path: ", g.shortest_path('a', 'b'))

print("\nThe paths from 'e' to 'a':")
print(g.all_paths('e', 'a'))
print("The shortest path: ", g.shortest_path('e', 'a'))

print("\nThe paths from 'f' to 'e':")
print(g.all_paths('f', 'e'))
print("The shortest path: ", g.shortest_path('f', 'e'))


complex_graph = {'a': ['b', 'e', 'i'],
                 'b': ['a', 'f'],
                 'c': ['d', 'f'],
                 'd': ['c', 'l'],
                 'e': ['a', 'g'],
                 'f': ['b', 'c', 'g'],
                 'g': ['e', 'f', 'i', 'j'],
                 'h': ['j', 'l'],
                 'i': ['a', 'g'],
                 'j': ['g', 'h', 'k'],
                 'k': ['j'],
                 'l': ['d', 'h']}

g = Graph(complex_graph)

print("The paths from 'a' to 'i':")
print(g.all_paths('a', 'i'))
print("The shortest path: ", g.shortest_path('a', 'i'))

print("\nThe paths from 'b' to 'g':")
print(g.all_paths('b', 'g'))
print("The shortest path: ", g.shortest_path('b', 'g'))

'''