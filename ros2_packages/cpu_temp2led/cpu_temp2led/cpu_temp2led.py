from os import system
from time import sleep #used due to ros2 not having wait() method
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class CPU_TempChecker(Node):
    def __init__(self, min_temp: float = 40, max_temp: float = 60):
        super().__init__('cpu_temp2led')
        #initializing max and min temperature for cpu
        self.min_temp = min_temp
        self.max_temp = max_temp

        self.topicName = '/cpu_temp'
        self.cpuTemp = Float32()
        self.sub = self.create_subscription(Float32, 
                                            self.topicName, 
                                            self.cpu_temp2ledCB, 
                                            10)
        self.sub # to prevent unused variable warning

    def led_pin(self, switch: int, pin_id: int):
        if switch == 0 or switch == 1:
            system('echo {} > /dev/myled{}'.format(switch, pin_id))

    def cpu_temp2ledCB(self, msg):
        self.cpuTemp = msg
        self.get_logger().info('CPU Temperature: {}'.format(msg.data))
        if self.cpuTemp.data < self.min_temp:
            self.led_pin(1, 17)
            self.led_pin(0, 23)
            self.led_pin(0, 25)
        elif self.cpuTemp.data < self.max_temp:
            self.led_pin(0, 17)
            self.led_pin(1, 23)
            self.led_pin(0, 25)
        else:
            self.led_pin(0, 17)
            self.led_pin(0, 23)
            self.led_pin(1, 25)

    def startup(self): #function for initial run
        for i in range(3):
            if i%3 == 0:
                self.led_pin(1, 17)
            elif i%3 == 1:
                self.led_pin(1, 23)
            else:
                self.led_pin(1, 25)
            self.led_pin(0, 17)
            self.led_pin(0, 23)
            self.led_pin(0, 25)
            sleep(1)
        self.led_pin(1, 17)
        self.led_pin(1, 23)
        self.led_pin(1, 25)
        sleep(1)

def main(args=None):
    rclpy.init(args=args) #initialization
    min_temp = float(input('input the minimal temperature[C]: '))
    max_temp = float(input('input the maximum temperature[C]: '))
    cpu_temp2led = CPU_TempChecker(min_temp=min_temp, max_temp=max_temp)
    cpu_temp2led.startup()
    rclpy.spin(cpu_temp2led)
    cpu_temp2led.destroy_node() #destroying node after exit (garbage collector)
    rclpy.shutdown()            #shutting down ROS2

if __name__ == '__main__':
    main()
