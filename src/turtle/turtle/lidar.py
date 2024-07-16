import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import tf_transformations
import math
from rclpy.qos import QoSProfile, QoSReliabilityPolicy

class LidarNode(Node):
    def __init__(self):
        super().__init__('lidar')

        qos_profile = QoSProfile(depth=10, reliability=QoSReliabilityPolicy.BEST_EFFORT)
        self.subscription = self.create_subscription(LaserScan,'scan',self.lidar_callback,qos_profile)
        self.odom_subscription = self.create_subscription( Odometry,'odom',self.odom_callback,10)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        self.initial_yaw = None
        self.current_yaw = None
        self.rotating = True
        self.moving_forward = True

    def lidar_callback(self, msg):
        array_length = len(msg.ranges)
        ranges = msg.ranges

        self.get_logger().info(f"Range at 0°: {ranges[0]:.6f} meters")
        self.get_logger().info(f"Range at 90°: {ranges[array_length//4]:.6f} meters")
        self.get_logger().info(f"Range at 180°: {ranges[array_length//2]:.6f} meters")
        self.get_logger().info(f"Range at 270°: {ranges[(3*array_length)//4]:.6f} meters")

        if ranges[0] < 0.3:
            self.stop_movement()
            self.get_logger().info("Obstacle Detected!")

    def odom_callback(self, msg):
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = tf_transformations.euler_from_quaternion(orientation_list)
        
        if self.initial_yaw is None:
            self.initial_yaw = yaw
            self.get_logger().info(f"Initial yaw: {self.initial_yaw}")
        
        self.current_yaw = yaw
        self.check_rotation()

    def check_rotation(self):
        if self.initial_yaw is not None and self.current_yaw is not None and self.rotating:
            angle_turned = self.current_yaw - self.initial_yaw
            if angle_turned < -math.pi:
                angle_turned += 2 * math.pi
            elif angle_turned > math.pi:
                angle_turned -= 2 * math.pi

            if abs(angle_turned) >= math.radians(90):
                self.get_logger().info("90° rotation achieved!")
                self.stop_rotation()
            else:
                self.continue_rotation()

    def continue_rotation(self):
        msg = Twist()
        msg.angular.z = 0.3 
        self.publisher_.publish(msg)

    def stop_rotation(self):
        msg = Twist()
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.rotating = False

    def stop_movement(self):
        msg = Twist()
        msg.linear.x = 0.0
        self.publisher_.publish(msg)
        self.moving_forward = False

    def start_movement(self):
        msg = Twist()
        msg.linear.x = 0.2
        self.publisher_.publish(msg)
        self.moving_forward = True

def main():
    rclpy.init()
    lidar_node = LidarNode()
    rclpy.spin(lidar_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

