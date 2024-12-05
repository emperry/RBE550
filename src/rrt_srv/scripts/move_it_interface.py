#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav2_msgs.action import FollowPath
from rclpy.action import ActionClient
from geometry_msgs.msg import Pose, PoseStamped
from nav_msgs.msg import Path
from rclpy.duration import Duration

class MoveItInterface(Node):
    def __init__(self):
        super().__init__('move_it_int')

        self.subscription = self.create_subscription(
                    Path,
                    '/rrt_path',
                    self.path_callback,
                    10)
        self.subscription  # prevent unused variable warning

        # Initialize the Nav2 Local Planner
        self._action_client = ActionClient(self, FollowPath, 'follow_path')
        self._action_client.wait_for_server()
        self.get_logger().info("Node started")


    def path_callback(self,msg:Path):
        waypoints = msg

        print(waypoints)

        goal_msg = FollowPath.Goal()
        goal_msg.path = waypoints

        # Send the goal to the action server
        self.get_logger().info("Sending goal to FollowPath action server")
        future = self._action_client.send_goal_async(goal_msg)
        
        # Wait for the result
        future.add_done_callback(self.result_callback)

       

    def result_callback(self, future):
        result = future.result()
        if result:
            self.get_logger().info("Successfully followed the path!")
        else:
            self.get_logger().warn("Failed to follow the path!")


def main():
    rclpy.init()

    minimal_client = MoveItInterface()
    rclpy.spin(minimal_client)
    rclpy.shutdown()




if __name__ == "__main__":
    main()



