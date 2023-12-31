from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:
    # We Rock Crazy Smart Asians
    # Kinda confused ngl
    # Monday Tuesday Wednesday Thursday Friday Saturday Sunday

    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info

    def output_paths(self):
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """

        # print("isp id", self.isp)
        # for i in self.graph:
            # print("graph", i)
        # for i in self.info["bandwidths"]:
            # print(i)
        # print(self.info["bandwidths"])

        result = bfs_path(self.graph, self.isp, self.info["list_clients"])



        paths, bandwidths, priorities = result, {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
