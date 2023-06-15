import frrpc
import time

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

#Load identification. At this time, the tool to be identified is installed at the end. The tool is installed under the force sensor, and the end is vertical down
robot.FT_SetRCS(0)    #Set reference coordinate system to tool coordinate system, 0- tool coordinate system, 1- base coordinate system
time.sleep(1)
tool_id = 10  #Sensor coordinate number
tool_coord = [0.0,0.0,35.0,0.0,0.0,0.0]   # Position of sensor relative to end flange
tool_type = 1  # 0-Tool, 1-Sensor
tool_install = 0 # 0-Mount end, 1-Outside of robot
robot.SetToolCoord(tool_id,tool_coord,tool_type,tool_install)     #Set sensor coordinate system, sensor relative end flange position
time.sleep(1)
robot.FT_PdIdenRecord(tool_id)   #Record identification data
time.sleep(1)
weight = robot.FT_PdIdenCompute()  #Calculated load weight,unit[kg]
print(weight)

#For load centroid identification, the robot needs to teach three different poses, then record the identification data, and finally calculate the load centroid
P1=[-160.619,-586.138,384.988,-170.166,-44.782,169.295]
robot.MoveCart(P1,9,0,100.0,100.0,100.0,-1.0,-1)         #Point to point motion in joint space
time.sleep(1)
robot.FT_PdCogIdenRecord(tool_id,1)                               #Record identification data
time.sleep(1)
P2=[-87.615,-606.209,556.119,-102.495,10.118,178.985]
robot.MoveCart(P2,9,0,100.0,100.0,100.0,-1.0,-1)
time.sleep(1)
robot.FT_PdCogIdenRecord(tool_id,2)
time.sleep(1)
P3=[41.479,-557.243,484.407,-125.174,46.995,-132.165]
robot.MoveCart(P3,9,0,100.0,100.0,100.0,-1.0,-1)
time.sleep(1)
robot.FT_PdCogIdenRecord(tool_id,3)
time.sleep(1)
cog = robot.FT_PdCogIdenCompute()   # Calculated and identified load centroid
print(cog)
