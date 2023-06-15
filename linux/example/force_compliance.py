import frrpc

# 与机器人控制器建立连接，连接成功返回一个机器人对象
robot = frrpc.RPC('192.168.58.2')

J1=[-105.3,-68.0,-127.9,-75.5,90.8,77.8]
P1=[-208.9,-274.5,334.6,178.8,-1.3,86.7]
eP1=[0.000,0.000,0.000,0.000]
dP1=[0.000,0.000,0.000,0.000,0.000,0.000]
J2=[-105.3,-97.9,-101.5,-70.3,90.8,77.8]
P2=[-264.8,-480.5,341.8,179.2,0.3,86.7]
eP2=[0.000,0.000,0.000,0.000]
dP2=[0.000,0.000,0.000,0.000,0.000,0.000]

#Constant force parameter
status = 1  #Constant force control open flag, 0-off, 1-on
sensor_num = 1 #Force sensor number
is_select = [1,0,0,0,0,0]  #Six degrees of freedom choice[fx,fy,fz,mx,my,mz],0-ineffective, 1-effective
force_torque = [-2.0,0.0,0.0,0.0,0.0,0.0]  #Collision detection force and torque, detection range（force_torque-min_threshold,force_torque+max_threshold）
gain = [0.0002,0.0,0.0,0.0,0.0,0.0]  #Maximum threshold
adj_sign = 0  #Adaptive start stop status, 0-off, 1-on
ILC_sign = 0  #ILC control start stop status, 0-stop, 1-training, 2-practical operation
max_dis = 100.0  #Maximum adjustment distance
max_ang = 5.0  #Maximum adjustment angle
#Compliance control
robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)
p = 0.00005  #Coefficient of position adjustment or compliance
force = 30.0 #Compliant opening force threshold,unit[N]
robot.FT_ComplianceStart(p,force)
count = 15  #Number of cycles
while(count):
    robot.MoveL(J1,P1,9,0,100.0,180.0,100.0,-1.0,eP1,0,1,dP1)   #Rectilinear motion in Cartesian space
    robot.MoveL(J2,P2,9,0,100.0,180.0,100.0,-1.0,eP2,0,0,dP2)
    count = count - 1
robot.FT_ComplianceStop()
status = 0
robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)