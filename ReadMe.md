# xarm_ros

## 1. Pre-Requisites

- ### 1.1 Install ROS 2 Humble
- ### 1.2 Install MoveIt2
- ### 1.3 Install Gazebo

## 2. Installation Instructions

## 3. Use Instructions

- ### 3.1 Enter Workspace and Source Environment in every terminal
```bash
cd ~/xarm_ros/
source install/setup.bash
```

- ### 3.2 Start ROS-TCP Connection Server
```bash
ros2 run ros_tcp_endpoint default_server_endpoint --ros-args -p ROS_IP:=< IP Address >
```
#### Replace < IP Address > with ROS Machine IP found by running:
```bash
hostname -I
```

- ### 3.3 Open Robot Control in MoveIt
```bash
ros2 launch xarm_moveit_config xarm6_moveit_fake.launch.py 
```



