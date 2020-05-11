#!/usr/bin/env python

import rospy
import ros_numpy
import math
import os
import time
from std_msgs.msg import String
import sensor_msgs.point_cloud2
from sensor_msgs.msg import PointCloud2

file_num = 0
file_name = ""
start_time = time.time()
end_time = 0

# Make a directory to hold your .xyz files
current_path = os.getcwd()
new_path = str(current_path) + "/xyz_timed_files"
os.mkdir(new_path)

def callback(data_point):
    global file_num, file_name
    if(start_time == 0):
        create_new_file(file_num, file_name)
    
    total_time = start_time - end_time
    if(total_time > 10):
        file_name.close()

    # file_name = open("xyz_data.xyz", "a+")
    # file_name.write(print_string + "\n")
    # 

def create_new_file(file_num, file_name):
    file_num += 1
    print("Printing to file " + str(file_num))

    # Make file name
    file_name = "file_" + str(file_num) + ".xyz"
    print(file_name)




def lidar_xyz_timed():
    rospy.init_node('lidar_xyz_timed', anonymous=True)
    rospy.Subscriber('xyz_points', String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        lidar_xyz_timed()
    except rospy.ROSInterruptException:
        pass