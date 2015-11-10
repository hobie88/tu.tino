/*
 * TopicReader.cpp
 *
 *  Created on: Nov 9, 2015
 *      Author: qbobot
 */

#include "TopicReader.h"

TopicReader::TopicReader() {
	// TODO Auto-generated constructor stub

}

TopicReader::~TopicReader() {
	// TODO Auto-generated destructor stub
}

//
void TopicReader::camera_info_callback(const sensor_msgs::CameraInfo& msg)
{
	ROS_INFO("camera_info_callback called \n msg header: %s", msg.header.frame_id);
}

void TopicReader::compressed_callback(const sensor_msgs::ImageConstPtr& msg)
{
	ROS_INFO("compressed_callback called");
	cv::namedWindow("compressed_callback",CV_WINDOW_AUTOSIZE);
	sensor_msgs::CvBridge bridge;
	cv::Mat frame;
	try
	{
		frame = bridge.imgMsgToCv(msg,"bgr8");
		imshow("compressed_callback", frame);
	}
	catch (sensor_msgs::CvBridgeException& e)
	{
		ROS_ERROR("Could not convert from '%s' to 'rgb8'.", msg->encoding.c_str());
	}
}

/*
void topic_reader::compressed_param_description_callback(const dynamic_reconfigure::ConfigDescription& msg)
{
	ROS_INFO("compressed_param_description_callback called");
}

void topic_reader::compressed_param_updates_callback(const dynamic_reconfigure::Config& msg)
{
	ROS_INFO("compressed_param_updates_callback called");
}
*/

void TopicReader::image_raw_callback(const sensor_msgs::ImageConstPtr& msg)
{
	ROS_INFO("image_raw_callback called");
	cv::namedWindow("image_raw_callback",CV_WINDOW_AUTOSIZE);
	sensor_msgs::CvBridge bridge;
	cv::Mat frame;
	try
	{
		frame = bridge.imgMsgToCv(msg,"bgr8");
		imshow("image_raw_callback", frame);
	}
	catch (sensor_msgs::CvBridgeException& e)
	{
		ROS_ERROR("Could not convert from '%s' to 'rgb8'.", msg->encoding.c_str());
	}
}

void TopicReader::theora_callback(const sensor_msgs::ImageConstPtr& msg)
{
	ROS_INFO("theora_callback called");
	cv::namedWindow("theora_callback",CV_WINDOW_AUTOSIZE);
	sensor_msgs::CvBridge bridge;
	cv::Mat frame;
	try
	{
		frame = bridge.imgMsgToCv(msg,"bgr8");
			imshow("theora_callback", frame);
		}
		catch (sensor_msgs::CvBridgeException& e)
		{
			ROS_ERROR("Could not convert from '%s' to 'rgb8'.", msg->encoding.c_str());
		}
}

/*
void topic_reader::theora_param_description_callback(const dynamic_reconfigure::ConfigDescription& msg)
{
	ROS_INFO("theora_param_description_callback called");
}

void topic_reader::theora_param_updates_callback(const dynamic_reconfigure::Config& msg)
{
	ROS_INFO("theora_param_updates_callback called");
}
*/

void TopicReader::foo()
{
	ROS_INFO("FOO: I DO NOTHING");
}
