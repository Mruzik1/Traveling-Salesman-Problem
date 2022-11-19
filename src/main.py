import numpy as np
from node import Node
from nearest_insertion import NearestInsertion
from points_generator import NodesGenerator


# generate random points, then create a file with the distances
ng = NodesGenerator(30)
ng.generate_distances('my_example.txt')

# read data from a file, preprocess data
with open('./my_example.txt') as f:
    nodes_raw = np.array([e.split() for e in f.read().split('\n') if len(e) != 0]).astype(object)
    nodes_raw = nodes_raw.astype(np.int32)

# nodes dictionary (consists of the Node objects)
# {...number_of_node: node...}
nodes = {i: Node(i, nodes_raw) for i in range(1, nodes_raw.T[:2].max()+1)}


# Nearest Insertion's instance
ni = NearestInsertion(nodes)

# nodes sequence formed by certain algorithm (result) and its total cost/distance (total_cost)
total_cost, result = ni.start()

# start the animation
ng.draw_algorithm(ni.get_history())

# write the result to a file
with open('./result.txt', 'w') as f:
    f.write(f"{total_cost}\n{','.join([str(e) for e in result])}")