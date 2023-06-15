import frrpc

# A connection is established with the robot controller. A successful connection returns a robot object
robot = frrpc.RPC('192.168.58.2')

#Constant force parameter
status = 1  #Constant force control open flag, 0-off, 1-on
sensor_num = 1 #Force sensor number
is_select = [0,0,1,0,0,0]  #Six degrees of freedom choice[fx,fy,fz,mx,my,mz],0-ineffective, 1-effective
force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0]  #Collision detection force and torque, detection range（force_torque-min_threshold,force_torque+max_threshold）
gain = [0.0001,0.0,0.0,0.0,0.0,0.0]  #Maximum threshold
adj_sign = 0  #Adaptive start stop status, 0-off, 1-on
ILC_sign = 0  #ILC control start stop status, 0-stop, 1-training, 2-practical operation
max_dis = 100.0  #Maximum adjustment distance
max_ang = 5.0  #Maximum adjustment angle

#Helix explore parameters
rcs = 0  #Reference frame, 0-Tool frame, 1-Base frame
dr = 0.7  #Feed per circle radius,unit[mm]
fFinish = 1.0 #Force or moment threshold（0~100）,unit[N or Nm]
t = 60000.0 #Maximum exploration time,unit[ms]
vmax = 3.0 #The maximum linear velocity, unit[mm/s]

#Linear insertion parameter
rcs = 0  #Reference frame, 0-Tool frame, 1-Base frame
force_goal = 20.0  #Force or moment threshold（0~100）,unit[N or Nm]
lin_v = 0.0 #Linear velocity,unit[mm/s]
lin_a = 0.0 #Linear acceleration, unit[mm/s^2],not used temporarily
disMax = 100.0 #Maximum insertion distance,unit[mm]
linorn = 1 #Insertion direction, 1-positive direction, 2-negative direction

#Rotational insertion parameter
rcs = 0  #Reference frame, 0-Tool frame, 1-Base frame
angVelRot = 2.0  #Rotational angular velocity,unit[°/s]
forceInsertion = 1.0 #Force or moment threshold（0~100）,unit[N or Nm]
angleMax= 45 #Maximum rotation Angle,unit[°]
orn = 1 #Direction of force,1-fz,2-mz
angAccmax = 0.0 #Maximum rotational acceleration, unit[°/s^2],not used temporarily
rotorn = 1 #Rotation direction, 1-clockwise, 2-counterclockwise

is_select = [0,0,1,1,1,0]   #Six degrees of freedom choice[fx,fy,fz,mx,my,mz],0-ineffective, 1-effective
robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)
robot.FT_SpiralSearch(rcs,dr,fFinish,t,vmax)
status = 0
robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)

is_select = [1,1,1,0,0,0]   #Six degrees of freedom choice[fx,fy,fz,mx,my,mz],0-ineffective, 1-effective
gain = [0.00005,0.0,0.0,0.0,0.0,0.0]  #Maximum threshold
force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0]  #Collision detection force and torque, detection range（force_torque-min_threshold,force_torque+max_threshold）
status = 1
robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)
robot.FT_LinInsertion(rcs,force_goal,lin_v,lin_a,disMax,linorn)
status = 0
robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)

s_select = [0,0,1,1,1,0]   #Six degrees of freedom choice[fx,fy,fz,mx,my,mz],0-ineffective, 1-effective
force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0]  #Collision detection force and torque, detection range（force_torque-min_threshold,force_torque+max_threshold）
gain = [0.0001,0.0,0.0,0.0,0.0,0.0]  #Maximum threshold
status = 1
robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)
robot.FT_RotInsertion(rcs,angVelRot,forceInsertion,angleMax,orn,angAccmax,rotorn)
status = 0
robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)

is_select = [1,1,1,0,0,0]   #Six degrees of freedom choice[fx,fy,fz,mx,my,mz],0-ineffective, 1-effective
force_torque = [0.0,0.0,-30.0,0.0,0.0,0.0]  #Collision detection force and torque, detection range（force_torque-min_threshold,force_torque+max_threshold）
status = 1
robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)
robot.FT_LinInsertion(rcs,force_goal,lin_v,lin_a,disMax,linorn)
status = 0
robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)