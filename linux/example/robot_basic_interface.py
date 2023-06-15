import frrpc
import time

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

ret = robot.GetSDKVersion()    #Query SDK version number
if ret[0] == 0:  #0-No fault, return format:[errcode,data],errcode-Fault code,data-Data
    print("SDK version is:",ret[1])
else:
    print("some things happened, the errcode is: ", ret[0])

ret = robot.GetControllerIP()    #Obtain Controller IP
if ret[0] == 0:
    print("controller ip is:",ret[1])
else:
    print("some things happened, the errcode is: ", ret[0])

#Control the robot to enter or exit the drag teaching mode
robot.Mode(1) #The robot goes into manual mode
time.sleep(1)
robot.DragTeachSwitch(1)  #When the robot enters the drag teaching mode, it can only enter the drag teaching mode in manual mode
time.sleep(1)
ret = robot.IsInDragTeach()    #Check whether the user is in drag mode, 1-Drag mode, 0-No drag mode
if ret[0] == 0:
    print("drag state is:",ret[1])
else:
    print("the errcode is: ", ret[0])
time.sleep(3)
robot.DragTeachSwitch(0)  #When the robot enters the non-drag teaching mode, it can only enter the non-drag teaching mode in manual mode
time.sleep(1)
ret = robot.IsInDragTeach()    #Check whether the user is in drag mode, 1-Drag mode, 0-No drag mode)
if ret[0] == 0:
    print("drag state is:",ret[1])
else:
    print("some things happened, the errcode is: ", ret[0])
time.sleep(3)

#Control the robot to enable or lower enable
robot.RobotEnable(0)   #Enable the robot
time.sleep(3)
robot.RobotEnable(1)   #This function is enabled on the robot. After the robot is powered on, it is automatically enabled by default

#Control robot manual/automatic mode switch
robot.Mode(0)   #The robot goes into automatic operation mode
time.sleep(1)
robot.Mode(1)   #The robot goes into manual mode
