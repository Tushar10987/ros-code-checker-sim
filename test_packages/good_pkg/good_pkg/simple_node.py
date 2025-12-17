import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleNode(Node):

    def __init__(self):
        super().__init__('simple_node')
        self.pub = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.timer_cb)

    def timer_cb(self):
        msg = String()
        msg.data = "Hello from good_pkg"
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = SimpleNode()
    rclpy.spin(node)
    rclpy.shutdown()

