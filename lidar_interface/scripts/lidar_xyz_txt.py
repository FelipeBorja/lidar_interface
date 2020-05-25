#!/usr/bin/env python

import rospy
import ros_numpy
from std_msgs.msg import String
import sensor_msgs.point_cloud2
from sensor_msgs.msg import PointCloud2

def xyz_callback(data):
    file_txt = open("xyz_data.txt", "a+")
    # Create xyz_array from a PointCloud2 data input
    xyz_array = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(data)
    sample_size = xyz_array.shape[0]
    # Loop through every point in the xyz_array
    for index in range(0,sample_size-1):
        print_point = xyz_array[index]
        # Get coordinates
        x = print_point[0]
        y = print_point[1]
        z = print_point[2]      

        # Turn point into string for printing/writing
        print_string = (str(x) + " " + str(y) + " " + str(z))
        print(print_string)
        # Publish to topic /xyz_points
        pub.publish(print_string)
        # Write to file
        file_txt.write(print_string + "\n")
    
    file_xyz.close()
    file_txt.close()


def lidar_xyz_txt():
    global pub
    pub = rospy.Publisher('xyz_points', String, queue_size=10)
    rospy.init_node('lidar_xyz_txt', anonymous=True)
    rospy.Subscriber('velodyne_points', PointCloud2, xyz_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        lidar_xyz_txt()
    except rospy.ROSInterruptException:
        pass