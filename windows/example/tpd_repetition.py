import frrpc


# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

P1=[-378.9,-340.3,107.2,179.4,-1.3,125.0]
name = 'tpd2023'   #Track name
blend = 1   #Is it smooth, 0-not smooth, 1-smooth
ovl = 100.0   #Speed scaling
robot.LoadTPD(name)  #Trajectory preloading
robot.MoveCart(P1,1,0,100.0,100.0,100.0,-1.0,-1)       #Let's go to the starting point
robot.MoveTPD(name, blend, ovl)  #Trajectory reproduction
