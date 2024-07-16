import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class Line(Node):
 	# TODO: Initialize our subscriber and publisher

	def __init__(self):
		super().__init__('subscriber')
		super().__init__('publisher')
		self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
		self.subscription = self.create_subscription(Odometry, '/turtle1/odom', self.sub_cb, 10)

		self.initial_position_x = 0
		self.initial_position_y = 0
		self.cur_x = 0
		self.cur_y = 0

		self.twist = Twist()
		self.twist.linear.x = 0.1

	def sub_cb(self, msg):
		# TODO: save our message data as a class variable
		self.cur_x = msg.pose.pose.position.x
		self.cur_y = msg.pose.pose.position.y
		if (self.initial_position_x == 0 and self.initial_position_y == 0):
			self.initial_position_x = msg.pose.pose.position.x
			self.initial_position_y = msg.pose.pose.position.y

		self.get_logger().info("help")
		#self.get_logger().info(abs(cur_y))

		#self.publisher_.publish(twist)


	def pub_cb(self):
		# TODO: declare our twist variable, and populate its data accordingly
		# We want the turtlebot to move a distance of 0.2 and then stop
		# Use the data from our subscriber to determine how far the turtle has moved

		if (sqrt(pow(self.cur_x - self.initial_position.x, 2) + pow(self.cur_y - self.initial_position.y, 2)) > 0.2):
			self.twist.linear.x = 0.0
		self.publisher_.publish(self.twist)

def main():

	rclpy.init()

	# TODO: create an instance of our node and spin it
	line_node = Line()
	rclpy.spin(line_node)

	rclpy.shutdown()

if __name__ == '__main__':
	main()
