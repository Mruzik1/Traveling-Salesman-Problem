import numpy as np
import matplotlib.pyplot as plt
from random import randint


class NodesGenerator:
    # self.__axis_nodes - points (nodes) with random x and y
    def __init__(self, count):
        self.__axis_nodes = np.array([(randint(0, 500), randint(0, 500)) for _ in range(count)])
    
    # generate typical txt file with distances between the nodes
    def generate_distances(self, file_name):
        with open(file_name, 'w') as f:
            for i, n1 in enumerate(self.__axis_nodes):
                for j, n2 in enumerate(self.__axis_nodes[i+1:]):
                    f.write(f'{i+1} {i+j+2} {int(np.sqrt((n1[0]-n2[0])**2 + (n1[1]-n2[1])**2))}\n')

    # makes an animation using matplotlib
    # history - saved algorithm's steps (you can check it out in the nearest_insertion.py)
    def draw_algorithm(self, history):
        for step_idx, step in enumerate(history):
            plt.scatter(self.__axis_nodes[:, 0], self.__axis_nodes[:, 1])

            for i in range(0, len(step)):
                x1, x2 = self.__axis_nodes[step[i]-1][0], self.__axis_nodes[step[i-1]-1][0]
                y1, y2 = self.__axis_nodes[step[i]-1][1], self.__axis_nodes[step[i-1]-1][1]
                plt.plot((x1, x2), (y1, y2), color='r')

            plt.draw()
            plt.pause(0.3)
            if (step_idx != len(history)-1): plt.clf()
        
        plt.show()