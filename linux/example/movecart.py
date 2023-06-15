import frrpc
import time

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

P1=[75.414,568.526,338.135,-178.348,-0.930,52.611]
P2=[-273.856,643.260,259.235,-177.972,-1.494,80.866]
P3=[-423.044,229.703,241.080,-173.990,-5.772,123.971]
robot.MoveCart(P1,0,0,100.0,100.0,100.0,-1.0,-1)       #Point-to-point motion in Cartesian space
robot.MoveCart(P2,0,0,100.0,100.0,100.0,-1.0,-1)
robot.MoveCart(P3,0,0,100.0,100.0,100.0,0.0,-1)
time.sleep(1)
robot.StopMotion()    #Stop moving