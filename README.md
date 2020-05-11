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
3. Run the following in the command line:
```
sudo ifconfig enxa0cec80e9f5c 192.168.1.100
sudo route add 192.168.1.201 enxa0cec80e9f5c
roslaunch velodyne_pointcloud VLP16_points.launch
```
4. Open up another terminal (ctrl+shift+t) and type the following into the command line to initialize RViz:
```
rosrun rviz rviz -f velodyne
```

## Built With

* [Robot Operating System](https://www.ros.org/) - OS used for connecting nodes.
* [Python](https://www.python.org/) - Coding language used for nodes.

## Authors

* **Felipe Borja** - [FelipeBorja](https://github.com/FelipeBorja)


## Acknowledgments

* Dr. Kevin Kochersberger
* Alfred Mayalu

