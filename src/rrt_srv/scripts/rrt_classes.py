#!/usr/bin/env python3
import rclpy
import numpy as np
import sys
from collections import deque
import queue
import math
import random
import matplotlib.pyplot as plt
from scipy.spatial import KDTree

class Pt:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.parent = None
        self.cost = 0.0

class RRT_Star:
    def __init__(self, start, finish, grid, step, radius, cell_size):
        self.start = Pt(start.x*cell_size,start.y*cell_size)
        self.finish = Pt(finish.x*cell_size,finish.y*cell_size)
        print(start.x,start.y,finish.x,finish.y)
        self.occupancy_grid = grid
        self.step_size = step
        self.cell_size = cell_size
        self.radius = radius
        self.nodes = [self.start]
        self.grid_size = np.shape(grid)
        self.iterations = 500000  #TODO probably increase
        #plot_obs(grid)
        self.rrtstar()


    def calc_dist(self, n1:Pt, n2:Pt): 
        # Euclidean distance calculation
        # Specify node type in constructor so .x and .y work  
        return math.sqrt((n2.x-n1.x)**2 + (n2.y-n1.y)**2)
    
    def is_valid(self, x, y):
        #check:
        #  in bounds
        #  not an obstacle
        #take into account cell size and world location are not the same
        #print(self.grid_size[0]-1, self.cell_size, (self.grid_size[0]-1)*self.cell_size)
        in_bounds = 0 <= x and x <= (self.grid_size[0]-1)*self.cell_size and 0 <= y and y <= (self.grid_size[1]-1)*self.cell_size
        x_new = math.floor(x/self.cell_size)
        y_new = math.floor(y/self.cell_size)

        return in_bounds and self.occupancy_grid[x_new,y_new] < 30

    def get_random_point(self):
        #get a random x and y and make a new node out of it
        x = random.uniform(0,(self.grid_size[0]-1)*self.cell_size)
        y = random.uniform(0,(self.grid_size[1]-1)*self.cell_size)
        n = Pt(x,y)
        return n
    
    def get_nearest_node(self, n:Pt):
        #make sure theyre formatted right 
        #TODO not need this line and put it right into kdtree
        nodes = [[node.x, node.y] for node in self.nodes]
        tree = KDTree(nodes)

        _,idx = tree.query([n.x,n.y])
        return self.nodes[idx]
    
    def step(self, first, last):
        if self.step_size > self.calc_dist(first, last):
            return last
        
        theta = math.atan2(last.y - first.y, last.x - first.x)
        new_x = first.x + self.step_size*math.cos(theta)
        new_y = first.y + self.step_size*math.sin(theta)

        n = Pt(new_x,new_y)

        return n
    

    def check_clear_of_obstacles(self, n1:Pt, n2:Pt):
        num_pts = int(self.calc_dist(n1,n2))
        for i in range(num_pts):
            #interpolate pts throughout the line
            t = i / num_pts
            x = n1.x * (1-t) + n2.x*t
            y = n1.y * (1-t) + n2.y*t

            if not self.is_valid(x,y):
                return False
        return True
    

    def neighbors(self, n:Pt):
        nodes = [[node.x, node.y] for node in self.nodes]
        tree = KDTree(nodes)
        idxs = tree.query_ball_point([n.x,n.y], self.radius)
        return [self.nodes[i] for i in idxs]
    
    def rewire(self, n:Pt, nearby_ns):
        #restructure the nodes to optimize the current paths
        for neighbor in nearby_ns:
            if self.check_clear_of_obstacles(n, neighbor):
                new_cost = n.cost + self.calc_dist(n, neighbor)
                if new_cost < neighbor.cost:
                    neighbor.parent = n
                    neighbor.cost = new_cost

    def get_path(self):
        #backtrack through all the nodes to produce the calculated path
        path = []
        node = self.finish
        while node.parent is not None:
            path.append([node.x,node.y])
            node=node.parent
        path.append([self.start.x, self.start.y])
        #plot_path(path,self.occupancy_grid, self.cell_size)
        return path

    def rrtstar(self):
        print("planning")
        for i in range(self.iterations):
            #get a point
            node = self.get_random_point()

            #get closest neighbor
            nearby = self.get_nearest_node(node)

            #take a step
            new_node = self.step(nearby, node)

            #make sure new node is valid
            if not self.is_valid(new_node.x, new_node.y):
                continue
            if not self.check_clear_of_obstacles(nearby, new_node):
                continue

            #put it in the tree
            new_node.parent = nearby
            new_node.cost = nearby.cost + self.calc_dist(nearby, new_node)
            self.nodes.append(new_node)

            #check to see if theres anything closeby
            neighbors = self.neighbors(new_node)
            self.rewire(new_node, neighbors)

            # see if youve made it to the goal yet 
            if self.calc_dist(new_node, self.finish) <= self.step_size:
                print("close!")
                if self.check_clear_of_obstacles(new_node, self.finish):
                    self.finish.parent = new_node
                    self.finish.cost = new_node.cost + self.calc_dist(new_node, self.finish)
                    print("lets goooo path found")
                    return
                    
                
        print("ran out of iterations.... try again?")
                    
            
def plot_path(vertices, obs, cell_size):
    # Plot vertices
    fix,ax = plt.subplots()
    x=[]
    y=[]
    for i in range(np.shape(obs)[0]):
        for j in range(np.shape(obs)[1]):
            if obs[i,j] >=30:
                x.append(i)
                y.append(j)
    plt.scatter(x,y,color='red',label='Obstacles',s=1)
    
    x_vals = [v[0]/cell_size for v in vertices]
    y_vals = [v[1]/cell_size for v in vertices]
    ax.plot(x_vals, y_vals, color='blue', label='Vertices')
            
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Path')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')  # Keep aspect ratio equal for clarity
    plt.show(block=True)
    plt.pause(0.5)

def plot_obs( obs):
    # Plot vertices
    fix,ax = plt.subplots()
    x=[]
    y=[]
    for i in range(np.shape(obs)[0]):
        for j in range(np.shape(obs)[1]):
            if obs[i,j] >=30:
                x.append(i)
                y.append(j)
    plt.scatter(x,y,color='red',label='Obstacles',s=1)

            
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Path')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')  # Keep aspect ratio equal for clarity
    plt.show(block=True)
    plt.pause(0.5)