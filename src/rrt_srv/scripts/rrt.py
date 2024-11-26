#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rrt_srv.srv import Rrt
import numpy as np
import sys
from collections import deque
import queue
import math
import random
import matplotlib.pyplot as plt
from scipy.spatial import KDTree
from rrt_classes import Pt, RRT_Star
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped


class MinimalService(Node):

    def __init__(self):
        super().__init__('rrt_service')
        self.srv = self.create_service(Rrt, 'rrt_srv_node', self.rrt_callback)
        print("started")

    def rrt_callback(self, request, response):

        start_node = Pt(request.start.pose.position.x, request.start.pose.position.y) 
        goal_node = Pt(request.goal.pose.position.x, request.goal.pose.position.y) 
        occupancy_grid = request.map.data
        width = request.map.info.width
        height = request.map.info.height
        np_array = np.array(occupancy_grid).reshape((height, width))
        step_size = 1
        radius = 0.5
        cell_size = request.map.info.resolution
        print(cell_size)

        #print(np.shape(np_array))

    
        planner = RRT_Star(start_node, goal_node, np_array, step_size, radius, cell_size)

        response.path = self.array_to_path(planner.get_path())

        return response

    def array_to_path(self,path_arry):
        path = []
        return path


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()



if __name__ == "__main__":
    main()
    
