# lidar_interface

This Robot Operating System (ROS) package is my work at interfacing with the Velodyne VLP-16 LIDAR for my master's thesis on LiDAR-based SLAM.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The things you need to recreate my setup.

* Linux Operating System (preferrably Ubuntu 16.04)
* Robot Operating System (preferrably [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu))
* [Velodyne VLP-16](https://velodynelidar.com/products/puck/) - The LIDAR in question.

### Installing

1. Once you have ROS Kinetic installed on Ubuntu, create your [catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace).
2. Clone this repository inside: 'catkin ws/src'.

## Deployment

1. Connect the VLP-16 LIDAR to your computer via ethernet. Connect the power supply to the LIDAR. GPS is optional.
2. Follow Step 1.1 of [this guide](http://wiki.ros.org/velodyne/Tutorials/Getting%20Started%20with%20the%20Velodyne%20VLP16) to set up your networks.
3. Run the following three lines in the command line:
```
sudo ifconfig enxa0cec80e9f5c 192.168.1.100
sudo route add 192.168.1.201 enxa0cec80e9f5c
roslaunch velodyne_pointcloud VLP16_points.launch
```
You can access VLP-16 settings by typing the ip '192.168.1.100' into your browser.
4. Open up another terminal (Ctrl+Shift+T) and type the following into the command line to initialize RViz:
```
rosrun rviz rviz -f velodyne
```
In RViz go to 'File -> Open Config (Ctrl+O)'. Select the config file 'velodyne_live.rviz' from the repository. This is the configuration file for viewing the Velodyne data in RViz.
To list rosnodes and rostopics use:
```
rosnode list
rostopic list
```
5. To run one of the nodes in 'scripts', open another terminal (Ctrl+Shift+T). 'cd' into the 'catkin_ws' directory and type the following into the command line to "source" the terminal:
```
source ./devel/setup.bash
```
Then run your selected node with 'rosrun':
```
rosrun lidar_interface [node name]
```
For example, enter the following into the command line to run 'lidar_xyz.py':
```
rosrun lidar_interface lidar_xyz.py
```

## Built With

* [Robot Operating System](https://www.ros.org/) - OS used for connecting nodes.
* [Python](https://www.python.org/) - Coding language used for nodes.

## Authors

* **Felipe Borja** - [FelipeBorja](https://github.com/FelipeBorja)


## Acknowledgments

* Dr. Kevin Kochersberger
* Alfred Mayalu

