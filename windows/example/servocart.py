import frrpc
import time

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

mode = 2  #Tool coordinate system incremental exercise
n_pos = [0.0,0.0,0.5,0.0,0.0,0.0]   #Descartes space increase
gain = [0.0,0.0,1.0,0.0,0.0,0.0]
acc = 0.0
vel = 0.0
t = 0.008
lookahead_time = 0.0
P = 0.0
count = 100
while(count):
    robot.ServoCart(mode, n_pos, gain, acc, vel, t, lookahead_time, P)
    count = count - 1
    time.sleep(0.008)
    # robot.WaitMs(1)
