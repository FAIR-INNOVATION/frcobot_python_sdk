import frrpc

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')


# Test control box DO
for i in range(0,16):
    robot.SetDO(i,1,0,0)      #Open the control box DO
robot.WaitMs(1000)
for i in range(0,16):
    robot.SetDO(i,0,0,0)      #Close the control box DO
robot.WaitMs(1000)

# Test end DO
for i in range(0,2):
    robot.SetToolDO(i,1,0,0)    #Open the tool DO
robot.WaitMs(1000)
for i in range(0,2):
    robot.SetToolDO(i,0,0,0)    #Close the tool DO
    

# Test control box AO
robot.SetAO(0,0.0,0)
robot.SetAO(1,100.0,0)
robot.WaitMs(1000)
robot.SetAO(0,0.0,0)
robot.SetAO(1,0.0,0)

# Test end AO
robot.SetToolAO(0,100.0,0)
robot.WaitMs(1000)
robot.SetToolAO(0,0.0,0)

# Test DI
di = robot.GetDI(0,0)
print(di)
robot.WaitDI(0,1,0,2)       # Always waiting
robot.WaitMultiDI(1,3,3,10000,2)   #Always waiting
tool_di = robot.GetToolDI(1,0)
print(tool_di)
robot.WaitToolDI(1,1,0,2)      #Always waiting

# Test AI
ai = robot.GetAI(0,1)
print(ai)
robot.WaitAI(0,0,50,0,2)         #Always waiting
robot.WaitToolAI(0,0,50,0,2)     #Always waiting
tool_ai = robot.GetToolAI(0,1)
print(tool_ai)


