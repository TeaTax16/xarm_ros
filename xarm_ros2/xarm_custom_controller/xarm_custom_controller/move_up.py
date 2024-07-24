#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
import time
import signal
import threading

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub_ = self.create_publisher(TwistStamped, "/servo_server/delta_twist_cmds", 10)
        self.stop_thread = False
        self.thread = threading.Thread(target=self.send_velocity_command)
        self.thread.start()

    def send_velocity_command(self):
        while rclpy.ok() and not self.stop_thread:
            msg = TwistStamped()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = "link_base"  # Adjust the frame_id as needed
            msg.twist.linear.z = 1.0
            self.cmd_vel_pub_.publish(msg)
            time.sleep(0.1)  # Adjust the sleep time as needed to control the rate

    def shutdown(self):
        self.stop_thread = True
        self.thread.join()

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()

    def signal_handler(sig, frame):
        node.shutdown()
        rclpy.shutdown()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.shutdown()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
