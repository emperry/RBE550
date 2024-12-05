#!/usr/bin/env python3
import sys
from rrt_srv.srv import Rrt
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Pose
from nav_msgs.msg import Path, OccupancyGrid
from tf2_ros import Buffer, TransformListener, LookupException, ConnectivityException, ExtrapolationException


class TestRRTStar(Node):

    def __init__(self):
        super().__init__('rrt_tester')
        self.cli = self.create_client(Rrt, 'rrt_srv_node')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.get_logger().info('connected to service')        
        self.req = Rrt.Request()

        self.publisher_ = self.create_publisher(Path, '/rrt_path', 10)

        self.subscription = self.create_subscription(
            PoseStamped,
            '/rrt_goal',
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

        self.planner_timer = self.create_timer(2.0, self.get_path) 

        # self.start = PoseStamped()
        # self.start.pose.position.x = 0.0
        # self.start.pose.position.y = 0.0

        # self.goal = PoseStamped()
        # self.goal.pose.position.x = 10.0
        # self.goal.pose.position.y = 10.0

        # self.map = OccupancyGrid()
        # self.map.info.resolution = 0.5
        # self.map.info.width = 10
        # self.map.info.height = 10
        # orig = Pose()
        # orig.position.x = 0.0
        # orig.position.y = 0.0
        # self.map.info.origin = orig
        # self.map.data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        #    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        #    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        #    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        #    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        #    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        #    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        #    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        #    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        #    0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.start = None
        self.goal = None
        self.map = None


    def send_request(self):
        self.req.start = self.start
        self.req.goal = self.goal
        self.req.map = self.map
        print("sending")     
        self.goal = None  
       
        self.future = self.cli.call_async(self.req)
        self.future.add_done_callback(self.response_callback)
        
        #rclpy.spin_until_future_complete(self, self.future)


    def response_callback(self, future):
        try:
            response = future.result()
            self.publisher_.publish(response.path)
            self.get_logger().info(f"Service response received: {response}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")



    def listener_callback(self, msg):
        self.goal = msg
                

    def map_calback(self, msg):
        self.map = msg


    def get_path(self):
        if self.start is not None:
            if self.map is not None and self.goal is not None:
                self.send_request()

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
