import frrpc
import time

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

#Overall shift of robot point position
J1=[-168.847,-93.977,-93.118,-80.262,88.985,11.831]
P1=[-558.082,27.343,208.135,-177.205,-0.450,89.288]
eP1=[0.000,0.000,0.000,0.000]
dP1=[10.000,10.000,10.000,0.000,0.000,0.000]
J2=[168.968,-93.977,-93.118,-80.262,88.986,11.831]
P2=[-506.436,236.053,208.133,-177.206,-0.450,67.102]
eP2=[0.000,0.000,0.000,0.000]
dP2=[0.000,0.000,0.000,0.000,0.000,0.000]
robot.MoveJ(J1,P1,1,0,100.0,180.0,100.0,eP1,-1.0,0,dP1)
robot.MoveJ(J2,P2,1,0,100.0,180.0,100.0,eP2,-1.0,0,dP2)
time.sleep(2)
flag = 1
offset = [100.0,5.0,6.0,0.0,0.0,0.0]   #Pose offset
robot.PointsOffsetEnable(flag, offset)   #Global offset start
robot.MoveJ(J1,P1,1,0,100.0,180.0,100.0,eP1,-1.0,0,dP1)
robot.MoveJ(J2,P2,1,0,100.0,180.0,100.0,eP2,-1.0,0,dP2)
robot.PointsOffsetDisable()  #End of global shift