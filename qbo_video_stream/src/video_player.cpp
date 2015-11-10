/*
 * video_player.cpp
 *
 *  Created on: Nov 10, 2015
 *      Author: qbobot
 */
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <cv_bridge/cv_bridge.h>

void video_player_callback(const sensor_msgs::ImageConstPtr&);
int flag=0;
cv::VideoCapture cap("/home/qbobot/Videos/1447144000.ogv");

int main(int argc, char** argv)
{
	ros::init(argc,argv,"video_player");
	ros::NodeHandle n;
	image_transport::ImageTransport it(n);
	if (cap.isOpened()) ROS_INFO("CAP IS OPENED");
	image_transport::Subscriber sub=it.subscribe("/stereo/left/image_raw",100,video_player_callback);
	ros::spin();
	return 0;
}

void video_player_callback(const sensor_msgs::ImageConstPtr& msg)
{
	ROS_INFO("CALLBACK CALLED");
	if (flag==0)
	{
		cv::namedWindow("video_player",CV_WINDOW_AUTOSIZE);

	}
	flag++;
	try
	{	ROS_INFO("IMSHOW %d",flag);
		cv::imshow("video_player",cap.grab());
	}
	catch(std::exception e)
	{
		ROS_ERROR("Could not open imshow");
	}
}
