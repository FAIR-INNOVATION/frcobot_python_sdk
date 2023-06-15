import frrpc
import time
import _thread

def print_program_state(name,rb):
    while(1):
        pstate = robot.GetProgramState()    #Query program running status,1-program stopped or Nothing program running, 2-program running, 3-program suspended
        linenum = robot.GetCurrentLine()    #Query the line number of the current job program
        name = robot.GetLoadedProgram()     #Queries the name of the loaded job program
        print("the robot program state is:",pstate[1])
        print("the robot program line number is:",linenum[1])
        print("the robot program name is:",name[1])
        time.sleep(1)

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

#The robot webapp program uses the interface
robot.Mode(0)   #The robot entered automatic operation mode
robot.ProgramLoad('/fruser/testPTP.lua')   #To load the robot program to execute, the testPTP.lua program needs to be written on webapp first
robot.ProgramRun()     #Executive robot program
_thread.start_new_thread(print_program_state,("print_state",robot))
time.sleep(5)         #10s rest
robot.ProgramPause()   #Pause the robot program in progress
time.sleep(5)
robot.ProgramResume()  #Resume the suspended robot program
time.sleep(5)
robot.ProgramStop()    #Stop the robot program in progress
time.sleep(2)
