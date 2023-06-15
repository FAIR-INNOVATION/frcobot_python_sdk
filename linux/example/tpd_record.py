import frrpc
import time


# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

type = 1  # Data type, 1-joint position
name = 'tpd2023'  # Track name
period = 4  #Sampling period, fixed value, 2ms or 4ms or 8ms
di_choose = 0 # di input configuration
do_choose = 0 # do output configuration
robot.SetTPDParam(type, name, period, di_choose, do_choose)    #Configure TPD Parameter

robot.Mode(1)  # The robot goes into manual mode
time.sleep(1)
robot.DragTeachSwitch(1)  #The robot goes into drag teaching mode
robot.SetTPDStart(type, name, period, di_choose, do_choose)   # Start recording the teaching track
time.sleep(30)
robot.SetWebTPDStop()  # Stop recording instructional tracks
robot.DragTeachSwitch(0)  #The robot enters the non-drag teaching mode

# robot.SetTPDDelete('tpd2023')   # Delete the TPD trace
