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
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import PoseStamped


class MinimalService(Node):

    def __init__(self):
        super().__init__('rrt_service')
        self.srv = self.create_service(Rrt, 'rrt_srv_node', self.rrt_callback)
        print("started")

    def rrt_callback(self, request, response):
        start_pos_x = request.start.pose.position.x + request.map.info.origin.position.x
        start_pos_y = request.start.pose.position.y + request.map.info.origin.position.y

        goal_pos_x = request.goal.pose.position.x + request.map.info.origin.position.x
        goal_pos_y = request.goal.pose.position.y + request.map.info.origin.position.y

        start_node = Pt(start_pos_x, start_pos_y) 
        goal_node = Pt(goal_pos_x, goal_pos_y) 
        
        occupancy_grid = request.map.data
        width = request.map.info.width
        height = request.map.info.height
        np_array = np.array(occupancy_grid).reshape((height, width))
        step_size = 1
        radius = 0.5
        cell_size = request.map.info.resolution
        print(cell_size)
    
        planner = RRT_Star(start_node, goal_node, np_array, step_size, radius, cell_size)
        #print(planner.get_path())
        response.path = self.array_to_path(planner.get_path())
        
        print("Done!")
        try:
        # Your logic here
            print("here!")
            return response
        except Exception as e:
            print("here")
            self.get_logger().error(f"Service callback error: {e}")
            return None  # Avoid returning incomplete responses
        

    def array_to_path(self,path_arry):
        path = Path()
    
        # Set the header
        path.header.frame_id = "path"
        path.header.stamp = rclpy.time.Time().to_msg()
        
        # Convert points to PoseStamped
        for point in path_arry:
            pose = PoseStamped()
            pose.header = path.header  # Reuse the path header
            pose.pose.position.x = point[0]
            pose.pose.position.y = point[1]
            pose.pose.position.z = 0.0
            
            # Neutral orientation (facing forward, no rotation)
            pose.pose.orientation.x = 0.0
            pose.pose.orientation.y = 0.0
            pose.pose.orientation.z = 0.0
            pose.pose.orientation.w = 1.0
            
            path.poses.append(pose)
        return path


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()



if __name__ == "__main__":
    main()
    
