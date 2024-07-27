# xarm_ros
#### This project works in conjuction with the [xarm_unity](https://github.com/TeaTax16/xarm_unity) GitHub Repo.
#### Ensure the trees in both projects match with each other

## 1. Pre-requisites

- ### 1.1 Install [ROS2 Foxy](https://docs.ros.org/en/ros2_documentation/foxy/Installation.html)

- ### 1.2 Setup ROS-TCP-Connector following instructions from [xarm_unity](https://github.com/TeaTax16/xarm_unity)

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

- ### 3.1 Start ROS 2 Side server
```bash
cd ~/xarm_ros/
source ~/xarm_ros/install/setup.bash
ros2 run ros_tcp_endpoint default_server_point --ros-args -p ROS_IP:=<hostname -I>
```
- ### 3.2 Connect Unity to Server following [Unity Hub Instructions](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/setup.md#-unity-setup)

- ### 3.3 Once connected, view the Pos and Rot data being sent
```bash
cd ~/xarm_ros/
source ~/xarm_ros/install/setup.bash
ros2 topic echo pos_rot
```