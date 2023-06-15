import frrpc
import time

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')


#Test peripheral instruction
robot.SetGripperConfig(4,0,0,1)
time.sleep(1)
config = robot.GetGripperConfig()
print(config)
robot.ActGripper(1,0)
time.sleep(1)
robot.ActGripper(1,1)
time.sleep(2)
robot.MoveGripper(1,100,48,46,30000,0)
time.sleep(3)
robot.MoveGripper(1,0,50,0,30000,0)
robot.GetGripperMotionDone()