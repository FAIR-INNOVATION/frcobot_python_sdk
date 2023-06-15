import frrpc

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')


J1=[127.888,-101.535,-94.860,17.836,96.931,-61.325]
eP1=[0.000,0.000,0.000,0.000]
dP1=[50.0,0.0,0.0,-30.0,0.0,0.0]
J2=[127.888,-101.535,-94.860,17.836,96.931,-61.325]
eP2=[0.000,0.000,0.000,0.000]
dP2=[50.0,0.0,0.0,-5.0,0.0,0.0]
Pa = [5.0,5.0,50.0,10.0,10.0,0.0]

P1 = robot.GetForwardKin(J1)       #The forward kinematic interface can be used to solve Cartesian space coordinates with only joint positions
print(P1)
P1 = [P1[1],P1[2],P1[3],P1[4],P1[5],P1[6]]
robot.MoveJ(J1,P1,0,0,100.0,180.0,100.0,eP1,0.0,2,dP1)
P2 = robot.GetForwardKin(J2)       #The forward kinematic interface can be used to solve Cartesian space coordinates with only joint positions
print(P2)
P2 = [P2[1],P2[2],P2[3],P2[4],P2[5],P2[6]]
robot.NewSpiral(J2,P2,0,0,100.0,180.0,eP2,100.0,2,dP2,Pa)   #Helical motion