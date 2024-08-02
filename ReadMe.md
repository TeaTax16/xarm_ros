# xarm_ros

## 1. Pre-Requisites

- ### 1.1 Install [ROS 2 Humble](https://docs.ros.org/en/ros2_documentation/humble/Installation.html)
- ### 1.2 Install [MoveIt2](https://moveit.ros.org/install-moveit2/binary/)
- ### 1.3 Install [Gazebo](https://classic.gazebosim.org/tutorials?tut=install_ubuntu)
- ### 1.4 Install [gazebo_ros_pkgs](https://classic.gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros)

## 2. Installation Instructions
- ### 2.1 Create a Workspace
```bash
$ cd
$ mkdir -p xarm_ros/src
```
- ### 2.2 Clone Source Code of this Repository
```bash
$ cd ~/xarm_ros/src
$ git clone https://github.com/TeaTax16/xarm_ros.git
```
- ### 2.3 Install Dependencies
```bash
$ cd ~/xarm_ros/src
$ rosdep update
$ rosdep install --from-paths --ignore-src -r -y
```
- ### 2.4 Build xarm_ros
```bash
$ cd ~/xarm_ros
$ colcon build
```

## 3. Use Instructions

- ### 3.1 Enter Workspace and Source Environment in every terminal
```bash
$ cd ~/xarm_ros/
$ source install/setup.bash
```

- ### 3.2 Start ROS-TCP Connection Server
```bash
$ ros2 run ros_tcp_endpoint default_server_endpoint --ros-args -p ROS_IP:=<IP Address>
```
#### Replace <IP Address> with ROS Machine IP found by running:
```bash
$ hostname -I
```

- ### 3.3 Open Robot Control in MoveIt
```bash
$ ros2 launch xarm_moveit_config xarm6_moveit_fake.launch.py 
```

## ROS 2 Setup complete, continue setup from [Unity Repo](https://github.com/TeaTax16/xarm_unity)



