# xarm_ros2

## 1. Pre-requisites

- ### 1.1 Install [ROS2 Foxy](https://docs.ros.org/en/ros2_documentation/foxy/Installation.html)

- ### 1.2 Install [Moveit2](https://moveit.ros.org/install-moveit2/binary/)  

- ### 1.3 Install [Gazebo](https://classic.gazebosim.org/tutorials?tut=install_ubuntu)  

- ### 1.4 Install [gazebo_ros_pkgs](http://gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros)  

## 2. Installation Instructions

- ### 2.1 Create a workspace
    ```bash
    $ cd ~
    $ mkdir -p xarm_ros/src
    ```

- ### 2.2 Obtain source code of "xarm_ros2" repository
    ```bash
    $ cd ~/xarm_ros/src
    $ git clone https://github.com/TeaTax16/xarm_ros.git --recurse-submodules 
    ```

- ### 2.3 Update "xarm_ros" repository 
    ```bash
    $ cd ~/xarm_ros/src/xarm_ros2
    $ git pull
    $ git submodule sync
    $ git submodule update --init --remote
    ```

- ### 2.4 Install dependencies
    ```bash
    $ cd ~/xarm_ros/src/
    $ rosdep update --include-eol-distros
    $ rosdep install --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
    ```

- ### 2.5 Build xarm_ros
    ```bash
    $ cd ~/xarm_ros/
    $ colcon build
    ```

## 3.  Use Instructions

- ### 3.1 Source Environment in every terminal
```bash
source ~/xarm_ros/install/setup.bash
```

- ### 3.2 Run robot in RViz
```bash
ros2 launch xarm_moveit_servo xarm_moveit_servo_fake.launch.py dof:=6
```

- ### 3.3 Run keyboard interface
```bash
# Might have to move individual joints first
ros2 run xarm_moveit_servo xarm_keyboard_input
```

- ### 3.4 Echo Twist Controls (for sanity check)
```bash
ros2 topic echo /servo_server/delta_twist_cmds
```

- ### 3.5 Run Custom Controller Scripts
```bash
ros2 run xarm_custom_controller move_(up/down/fw/bw/left/right)
```