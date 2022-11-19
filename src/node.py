import numpy as np


class Node:
    def __init__(self, number, nodes_list):
        self.__number = number
        self.__distances = self.__init_node(nodes_list[np.where(nodes_list[:, :2] == number)[0]])
    
    # returns a dictionary with following structure:
    # {...number_of_node: distance...}
    def __init_node(self, nodes_list):
        nodes_list = [[e[1], e[2]] if e[0] == self.__number else [e[0], e[2]] for e in nodes_list]

        return {e[0]: e[1] for e in nodes_list}

    # returns distance between this node and another (that is got as an argument, could be also a number)
    def get_distance(self, node):
        if isinstance(node, Node):
            return self.__distances[node.get_number()]
        return self.__distances[node]

    # returns a number of the node
    def get_number(self):
        return self.__number

    # find nearest node, return the node itself and its distance
    def nearest(self, nodes):
        dist = {self.get_distance(nodes[e]): e for e in nodes if nodes[e].get_number() != self.__number}

        return nodes[dist[min(dist)]], min(dist)

    # string representation
    def __str__(self):
        return str(self.__number)