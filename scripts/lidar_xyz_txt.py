#!/usr/bin/env python

import rospy
import ros_numpy
from std_msgs.msg import String
import sensor_msgs.point_cloud2
from sensor_msgs.msg import PointCloud2

def xyz_callback(data):
    file1 = open("xyz_data.xyz", "a+")
    # Create xyz_array from a PointCloud2 data input
    xyz_array = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(data)
    sample_size = xyz_array.shape[0]
    # Loop through every point in the xyz_array
    for index in range(0,sample_size-1):
        print_point = xyz_array[index]
        # Turn point into string for printing/writing. Also remove brackets.
        print_string = ('%s' % print_point)[1:-1]
        print(print_string)
        # Publish to topic /xyz_points
        pub.publish(print_string)
        # Write to file
        file1.write(print_string + "\n")
    
    file1.close()


def lidar_xyz():
    global pub
    pub = rospy.Publisher('xyz_points', String, queue_size=10)
    rospy.init_node('lidar_xyz', anonymous=True)
    rospy.Subscriber('velodyne_points', PointCloud2, xyz_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        lidar_xyz()
    except rospy.ROSInterruptException:
        pass