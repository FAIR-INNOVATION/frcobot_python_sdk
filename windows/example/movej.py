import frrpc
import time

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

J1=[-168.847,-93.977,-93.118,-80.262,88.985,11.831]
P1=[-558.082,27.343,208.135,-177.205,-0.450,89.288]
eP1=[0.000,0.000,0.000,0.000]
dP1=[1.000,1.000,1.000,1.000,1.000,1.000]
J2=[168.968,-93.977,-93.118,-80.262,88.986,11.831]
P2=[-506.436,236.053,208.133,-177.206,-0.450,67.102]
eP2=[0.000,0.000,0.000,0.000]
dP2=[1.000,1.000,1.000,1.000,1.000,1.000]

robot.MoveJ(J1,P1,1,0,100.0,180.0,100.0,eP1,-1.0,0,dP1)    #Joint space motionPTP,Tool number1,the actual test is based on field data and Tool number
robot.MoveJ(J2,P2,1,0,100.0,180.0,100.0,eP2,-1.0,0,dP2)
time.sleep(2)
j1 = robot.GetInverseKin(0,P1,-1)       #In the case of Cartesian space coordinates only, the inverse kinematic interface can be used to solve the joint position
print(j1)
j1 = [j1[1],j1[2],j1[3],j1[4],j1[5],j1[6]]
robot.MoveJ(j1,P1,1,0,100.0,180.0,100.0,eP1,-1.0,0,dP1) 
j2 = robot.GetInverseKin(0,P2,-1)
print(j2)
j2 = [j2[1],j2[2],j2[3],j2[4],j2[5],j2[6]]
robot.MoveJ(j2,P2,1,0,100.0,180.0,100.0,eP2,-1.0,0,dP2)

time.sleep(2)
p1 = robot.GetForwardKin(J1)       #The forward kinematic interface can be used to solve Cartesian space coordinates with only joint positions
print(p1)
p1 = [p1[1],p1[2],p1[3],p1[4],p1[5],p1[6]]
robot.MoveJ(J1,p1,1,0,100.0,180.0,100.0,eP1,-1.0,0,dP1) 
p2 = robot.GetForwardKin(J2)
print(p2)
p2 = [p2[1],p2[2],p2[3],p2[4],p2[5],p2[6]]
robot.MoveJ(J2,p2,1,0,100.0,180.0,100.0,eP2,-1.0,0,dP2)