#!/usr/bin/env python3

import rospy
from actionlib import SimpleActionClient
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion
import actionlib
from nav_msgs.msg import Odometry
from tf.transformations import quaternion_from_euler

rospy.init_node('action_client_turtlebot3')

pose_pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=1)

while pose_pub.get_num_connections() == 0:
    rospy.loginfo("Waiting for /initialpose publisher to connect")
    rospy.sleep(1)

def odom_callback(msg):
    present_pose = msg

position = { "M1": {"x": -0.607, "y": 3.251}, 
"M2": {"x": -2.29, "y": 2.852}, 
"M3": {"x": -4.044, "y": 2.26}, 
"Raw Material Station": {"x": 0.167, "y": 0.511}, 
"Inventory": {"x": -3.26, "y": -0.55}, 
"Packaging Station": {"x": -1.68, "y": 0.0216} }

order = ["M1", "M2", "M3", "Packaging Station", "M1", "M2", "M3", "Packaging Station", "Raw Material Station", "M3", "M2", "Packaging Station", "M1", "M2", "M3", 
"Packaging Station", "Inventory", "M3", "M2", "Packaging Station", "Inventory", "Packaging Station", "Inventory", "Packaging Station", "Inventory", "Packaging Station", "Inventory"]
prev_location = "Raw Material Station"

pose = PoseWithCovarianceStamped()
pose.header.seq = 1
pose.header.stamp = rospy.Time.now()
pose.header.frame_id = "map"
pose.pose.pose.position.x = position["Raw Material Station"]["x"]
pose.pose.pose.position.y = position["Raw Material Station"]["y"]

roll = 0.0
pitch = 0.0
yaw = 0.0
quaternion = quaternion_from_euler(roll, pitch, yaw)

rospy.loginfo("Initial pose is set! (Turtlebot is currently at the raw material station.)")

odom_sub_r1 = rospy.Subscriber('/odom', Odometry, odom_callback)

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
client.wait_for_server()

rospy.loginfo("Begin the process.")

for obj_location in order:
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = position[obj_location]["x"]
    goal.target_pose.pose.position.y = position[obj_location]["y"]
    goal.target_pose.pose.orientation = Quaternion(*quaternion)

    rospy.loginfo(f"Starting navigation from {prev_location} to {obj_location}.")

    client.send_goal(goal)
    wait = client.wait_for_result()

    rospy.loginfo(f"Arrived at {obj_location}.")
    prev_location = obj_location

    next_step_checker = input('Press Enter for the next step...')

rospy.loginfo("Entire process completed.")

rospy.spin()