import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class PostCPU(Node):
    def __init__(self):
        super().__init__('post_cpu')
        self.topicName = '/cpu_temp'
        self.pub = self.create_publisher(Float32, self.topicName, 10)
        self.cpuTemp_msg = Float32()
        timer_rate = 10/1000
        self.rate = self.create_timer(timer_rate, self.timerCB)

    def timerCB(self):
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as thermal:
            thermal = float(thermal.read())/1000
            self.cpuTemp_msg.data = thermal
            self.pub.publish(self.cpuTemp_msg)
            self.get_logger().info('CPU Temp: {}'.format(thermal))

def main(args=None):
    rclpy.init(args=args)
    post_cpu = PostCPU()
    try:
        rclpy.spin(post_cpu)
    except KeyboardInterrupt:
        print('killing process...')
    post_cpu.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
