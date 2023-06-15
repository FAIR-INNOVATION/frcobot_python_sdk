import frrpc
import time

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

company = 17    #Sensor manufacturer,17-Kunwei Technology,
device = 0      #Sensor equipment number
softversion = 0 #software version number
bus = 1         #End bus position
robot.FT_SetConfig(company, device, softversion, bus)   #Configured force sensor
config = robot.FT_GetConfig() #Obtain the configuration information of the force sensor. The manufacturer number is one larger than the feedback
print(config)

time.sleep(1)

robot.FT_Activate(0)  #Sensor reset
time.sleep(1)
robot.FT_Activate(1)  #Sensor activation
time.sleep(1)

robot.SetLoadWeight(0.0)    #The end load setting is zero
time.sleep(1)
robot.SetLoadCoord(0.0,0.0,0.0)  #The end of the end load is set to zero
time.sleep(1)
robot.FT_SetZero(0)   #Sensor removes zero point
time.sleep(1)
origin = robot.FT_GetForceTorqueOrigin()   #Query sensor original data
print(origin)
robot.FT_SetZero(1)   #The sensor is corrected at zero point. Note that the end can not be installed at this end, only a powerful sensor
time.sleep(1)
rcs = robot.FT_GetForceTorqueRCS()  #Query sensor coordinate system data
print(rcs)
