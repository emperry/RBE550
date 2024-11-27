#!/usr/bin/env python3
import sys
from rrt_srv.srv import Rrt
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path, OccupancyGrid
from tf2_ros import Buffer, TransformListener, LookupException, ConnectivityException, ExtrapolationException


class TestRRTStar(Node):

    def __init__(self):
        super().__init__('rrt_tester')
        self.cli = self.create_client(Rrt, 'rrt_srv_node')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Rrt.Request()

        self.publisher_ = self.create_publisher(Path, '/path', 10)

        self.subscription = self.create_subscription(
            PoseStamped,
            '/goal_pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.map_subscription = self.create_subscription(
            OccupancyGrid,
            '/global_costmap/costmap',
            self.map_calback,
            10)
        self.map_subscription  # prevent unused variable warning
        
        
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # Define source and target frames
        self.source_frame = 'map'       
        self.target_frame = 'base_link'        # TODO is it this or base link 
        self.timer = self.create_timer(1.0, self.get_pose_stamped)  # Call every 1 second
        #TODO maybe use amcl pose since this sucks? 

        self.start = PoseStamped()
        self.start.pose.position.x = 250.0
        self.start.pose.position.y = 410.0


    def send_request(self, goal):
        #print(self.map)
        self.req.start = self.start
        self.req.goal = goal
        self.req.map = self.map
        print("sending")
        
       
        self.response = self.cli.call(self.req)
        return self.response


    def listener_callback(self, msg):
        self.goal = msg
        response = self.send_request(self.goal)
        print("here?")
        #rclpy.spin_until_future_complete(self, self.future)

        # while not self.future.done():
        #     rclpy.spin_once(self, timeout_sec=0.1)
        #     print("Waiting for response...")
        
        #response = self.future.result()
        print(f"Received response: {response}")

        if self.future.result() is not None:
            response = self.future.result()
            self.get_logger().info(f'Received response: {response}')
        else:
            self.get_logger().error('Failed to call service')

        print(response)


    def map_calback(self, msg):
        print("map_received")
        self.map = msg

    def get_pose_stamped(self):
        try:
            # Lookup the latest transform between the frames
            transform = self.tf_buffer.lookup_transform(
                self.source_frame,
                self.target_frame,
                rclpy.time.Time(),  # Use the latest transform
                timeout=rclpy.duration.Duration(seconds=2.0)  # Wait for 1 second if necessary
            )

            # Convert transform to PoseStamped
            self.start = self.transform_to_pose_stamped(transform)

         # Log the PoseStamped
            #self.get_logger().info(f"PoseStamped:\n{self.start}")

        except (LookupException, ConnectivityException, ExtrapolationException) as e:
            self.get_logger().error(f"Failed to get transform: {str(e)}")

    def transform_to_pose_stamped(self, transform):
        # Create a PoseStamped message
        pose_stamped = PoseStamped()

        # Set the header
        pose_stamped.header.stamp = transform.header.stamp
        pose_stamped.header.frame_id = transform.header.frame_id

        # Set the position (translation)
        pose_stamped.pose.position.x = transform.transform.translation.x
        pose_stamped.pose.position.y = transform.transform.translation.y
        pose_stamped.pose.position.z = transform.transform.translation.z

        # Set the orientation (rotation)
        pose_stamped.pose.orientation.x = transform.transform.rotation.x
        pose_stamped.pose.orientation.y = transform.transform.rotation.y
        pose_stamped.pose.orientation.z = transform.transform.rotation.z
        pose_stamped.pose.orientation.w = transform.transform.rotation.w

        return pose_stamped

def main(args=None):
    rclpy.init(args=args)

    minimal_client = TestRRTStar()
    #response = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin(minimal_client)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
