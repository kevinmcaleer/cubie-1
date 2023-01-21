import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):

    def __init__(self):
        super().__init__("node_test")
        self.counter_ = 0
        # create_subscriber needs 3 parameters: Msg Type, topic name, the callback, and queue size buffer
        self.subscriber = self.create_subscription(String, "Hello", self.callback_hello, 10)
        self.get_logger().info("Subscribed to Hello topic")

    def callback_hello(self, message):
        self.get_logger().info(message.data)
     
def main(args=None):
    rclpy.init(args=args)
    node = Listener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()