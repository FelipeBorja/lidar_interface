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
1. ardrone_joystick: Allows for joystick teleop for the quadrotor Gazebo tum_simulator
2. hdl_graph_slam: Graph based SLAM package for 3D LIDARs (Buggy)
3. hector_slam: SLAM package to create 2D maps from laserscan data
4. octomap_mapping: SLAM package to create 3D maps from pointcloud2 data
5. pointcloud_to_laserscan: Node that converts pointcloud2 data into laserscan
6. rosbot_description: Rosbot Gazebo sim package
7. slam_gmapping: 2D SLAM package that uses laserscan data
8. tum_simulator: Parrot ARDrone Gazebo sim
9. velodyne: Package that contains the VLP-16 drivers and allows it to interface with ROS
10. velodyne_simulator: VLP-16 Gazebo simulator

## Roslaunch Files
All launch files are stored in the ```lidar_interface``` package under ```lidar_interface/lidar_interface/launch```

* ```octomap_quadrotor_velodyne.launch``` : Launches quadrotor gazebo simulation with the Velodyne mounted on top. Also launches octomap_mapping to start mapping the environment
  * Includes the following packages: ```tum_simulator, octomap_mapping, velodyne_simulator```
* ```octomap_rosbot_velodyne.launch``` : Launches the rosbot UGV Gazebo simulation with the Velodyne mounted on top. Also launches octomap_mapping to start mapping the environment
  * Includes the following packages: ```rosbot_description, octomap_mapping, velodyne_simulator```
* ```hdl_quadrotor_velodyne.launch``` : (Buggy) Launches hdl_graph_slam with the quadrotor velodyne Gazebo simulation.
  * Includes the following packages: ```tum_simulator, hdl_graph_slam, velodyne_simulator```
* ```hdl_rosbot_velodyne.launch``` : (Buggy) Launches hdl_graph_slam with the rosbot velodyne Gazebo simulation
  * Includes the following packages: ```rosbot_descripion, hdl_graph_slam, velodyne_simulator```
* ```hector_slam_velodyne.launch``` : Launches hector_slam for the physical VLP-16 LiDAR
  * Includes the following packages: ```hector_slam, velodyne```
* ```voxelize_velodyne.launch``` : Creates a voxelized (down sampled) pointcloud2 by subscribing to ```/velodyne_points``` and utilizing the pcl library
  * Includes the following packages: ```pcl```
* ```rosbot_velodyne.launch``` : Launches the rosbot world and spawns in the rosbot with the velodyne
  * Includes the following packages: ```rosbot_descripion, velodyne_simulator```
* ```rosbot_gazebo_velodyne.launch``` : Spawns in the rosbot with the velodyne
  * Includes the following packages: ```rosbot_descripion, velodyne_simulator```
* ```rosbot_rviz_velodyne.launch``` : Launches the rosbot world and spawns in the rosbot with the velodyne. Also launches an rviz window.
  * Includes the following packages: ```rosbot_descripion, velodyne_simulator```
* ```rosbot_rviz_gmapping_velodyne.launch``` : Launches the rosbot world and spawns in the rosbot with the velodyne. Also starts gmapping with an rviz window.
  * Includes the following packages: ```gmapping, rosbot_descripion, velodyne_simulator```
* ```hector_mapping_no_odom.launch``` : Launches hector_mapping without odometry
  * Includes the following packages: ```hector_slam```
* ```hector_mapping_no_odom_sim.launch``` : Launches hector_mapping without odometry for simulation use
  * Includes the following packages: ```hector_slam```
* ```hector_mapping_sim.launch``` : Launches hector_mapping with odometry for simulation use
  * Includes the following packages: ```hector_slam```




## Scripts
The following files are located in ```lidar_interface/lidar_interface/scripts```. Use these to launch experiments.
* ```lidar_xyz.py``` : Writes the points from ```/velodyne_points``` to a .xyz file
* ```lidar_xyz.py``` : Writes the points from ```/velodyne_points``` to a .txt file

## Built With

* [Robot Operating System](https://www.ros.org/) - OS used for connecting nodes.
* [Python](https://www.python.org/) - Coding language used for nodes.

## Authors

* **Felipe Borja** - [FelipeBorja](https://github.com/FelipeBorja)
* **Nishanth Mankame** - [nishmankame](https://github.com/nishmankame)


## Acknowledgments

* Dr. Kevin Kochersberger
* Alfred Mayalu
