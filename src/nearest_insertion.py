import numpy as np


class NearestInsertion:
    # self.__nodes - unsorted nodes dictionary ({...node's number: Node object...})
    # self.__nodes_len - length of the nodes dictionary
    # self.__total_cost - full length of the way
    # self.__result - list of the connected nodes (already has node 1 within)
    # self.__insertion_steps - the history (steps) of the algorithm
    def __init__(self, nodes):
        self.__nodes = nodes
        self.__nodes_len = len(nodes)
        self.__total_cost = 0
        self.__result = [nodes[1]]
        self.__insertion_steps = []

    # 1. Add a node, nearest to the node 1, to a self.result.
    # 2. Call self.insertion_step until the length of the result list is smaller than self.nodes_len.
    # 3. Count the total cost, then print.
    def start(self):
        self.__result.append(self.__result[0].nearest(self.__nodes)[0])     # 1
        self.__insertion_steps.append([e.get_number() for e in self.__result])

        while len(self.__result) < self.__nodes_len:                        # 2
            self.__insertion_step()
            self.__insertion_steps.append([e.get_number() for e in self.__result])
        
        for i in list(range(1, len(self.__result))) + [0]:                  # 3
            self.__total_cost += self.__result[i].get_distance(self.__result[i-1])
        
        return self.__total_cost, self.__result

    # Firstly remove all duplicates (description below).
    
    # Then find the nearest node using tmp_dist (numpy array with following structure:
    # [...],[any_nearest_node distance_between_two_certain_nodes],[...])

    # Clear tmp_dist to use it later.

    # for cycle that iterates following list [1, 2, 3 .., self.result length, 0]
    # (It needs to have this shape due to the Nearest Insertion's working principle, element 0 and -1 is actually a pair)

    # Inside the cycle we have a formula for nodes 1, 3, and the choosen nearest_node 5 (as an example);
    # we find distances between 1-5 and 3-5, add them, then subtract distance between 1-3;
    # add result to tmp_dist: {...node_number : result...}.

    # Then determine the result's minimum, get the node's index (place for nearest_node), and insert nearest_node there.
    def __insertion_step(self):
        self.__remove_duplicates()

        tmp_dist = np.array([e.nearest(self.__nodes) for e in self.__result])
        nearest_node = tmp_dist[tmp_dist[:, 1:].argmin()][0]
        tmp_dist = {}
        
        for i in list(range(1, len(self.__result))) + [0]:
            nearest_sum = self.__result[i-1].get_distance(nearest_node) + self.__result[i].get_distance(nearest_node)
            between_sum = self.__result[i-1].get_distance(self.__result[i])

            tmp_dist[i] = nearest_sum - between_sum

        nearest_idx = min(tmp_dist, key=tmp_dist.get)

        if nearest_idx == 0: self.__result.append(nearest_node)
        else: self.__result.insert(nearest_idx, nearest_node)

    # Remove all repeated in self.result elements from the nodes dictionary
    def __remove_duplicates(self):
        for e in self.__result:
            if e.get_number() in self.__nodes:
                self.__nodes.pop(e.get_number())

    # Getting the history of the algorithm
    def get_history(self):
        return self.__insertion_steps