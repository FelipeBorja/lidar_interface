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

## Included Packages
* velodyne:
* velodyne_simulator

## Roslaunch Files
The following files are located in ```lidar_interface/lidar_interface/launch```. Use these to launch experiments.
* ```octomap_quadrotor_velodyne.launch```: Quadrotor simulation with velodyne sensor. Runs Octomap mapping algorithm. Incorporates: octomap, velodyne_simulator, tum_simulator.

## Scripts
The following files are located in ```lidar_interface/lidar_interface/scripts```. Use these to launch experiments.

## Built With

* [Robot Operating System](https://www.ros.org/) - OS used for connecting nodes.
* [Python](https://www.python.org/) - Coding language used for nodes.

## Authors

* **Felipe Borja** - [FelipeBorja](https://github.com/FelipeBorja)
* **Nishanth Mankame** - [nishmankame](https://github.com/nishmankame)


## Acknowledgments

* Dr. Kevin Kochersberger
* Alfred Mayalu

