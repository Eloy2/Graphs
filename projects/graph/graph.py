"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Error vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty Queue and add starting vertex to it
        # This will keep track of all next_to_visit_vertices
        queue = []
        queue.append(starting_vertex)
        # Create an empty set to keep track of visited vertices
        visited = set()
        # While the queue is not empty
        while len(queue) > 0:
            # dequeue a vertex off the queue
            current_vertex = queue.pop(0)
            # if vertex not in visited vertices
            if current_vertex not in visited:
                # Print it 
                print(current_vertex)
                # Add the vertex to our visited set
                visited.add(current_vertex)
                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty Stack and add starting vertex to it
        # This will keep track of all next_to_visit_vertices
        stack = []
        stack.append(starting_vertex)
        # Create an empty set to keep track of visited vertices
        visited = set()
        # While the queue is not empty
        while len(stack) > 0:
            # dequeue a vertex off the stack
            current_vertex = stack.pop()
            # if vertex not in visited vertices
            if current_vertex not in visited:
                # Print it 
                print(current_vertex)
                # Add the vertex to our visited set
                visited.add(current_vertex)
                # Add all neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and Add a PATH TO starting vertex 
        # I.e add array [1] to the queue
        queue = []
        queue.append([starting_vertex])
        # Create an empty set to keep track of visited vertices
        visited = set()
        # While the queue is not empty
        while len(queue) > 0:
            # dequeue the current PATH from the queue
            path = queue.pop(0)
            # get the current vertex to analyze from the path 
            # use the vertex at the END of the path array
            current_vertex = path[-1]

            # if vertex not visited:
                # add vertex to visited list
            if current_vertex not in visited:
                visited.add(current_vertex)

                # CHECK IF CURRENT VERTEX IS THE TARGET VERTEX
                    # we found our vertex, and the path to it
                    # return the PATH
                if current_vertex == destination_vertex:
                    return path
                
                # for each neighbor of current vertex
                    # Add the path to that neighbor, to the queue
                        # COPY THE CURRENT PATH
                        # add neighbor to new path
                        # add the whole path to the Queue
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = path[:]
                    new_path.append(neighbor)
                    queue.append(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and Add a PATH TO starting vertex 
        # I.e add array [1] to the stack
        stack = []
        stack.append([starting_vertex])
        # Create an empty set to keep track of visited vertices
        visited = set()
        # While the stack is not empty
        while len(stack) > 0:
            # destack the current PATH from the stack
            path = stack.pop()
            # get the current vertex to analyze from the path 
            # use the vertex at the END of the path array
            current_vertex = path[-1]

            # if vertex not visited:
                # add vertex to visited list
            if current_vertex not in visited:
                visited.add(current_vertex)

                # CHECK IF CURRENT VERTEX IS THE TARGET VERTEX
                    # we found our vertex, and the path to it
                    # return the PATH
                if current_vertex == destination_vertex:
                    return path
                
                # for each neighbor of current vertex
                    # Add the path to that neighbor, to the stack
                        # COPY THE CURRENT PATH
                        # add neighbor to new path
                        # add the whole path to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = path[:]
                    new_path.append(neighbor)
                    stack.append(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, path, visited)
                if new_path:
                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
