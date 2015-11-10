#include "ros/ros.h"
#include "std_msgs/String.h"
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include "TopicReader.h"
#include <log4cxx/logger.h> //for debugging messages

//#define DEBUG //uncomment for debugging messages

void theora_callback(const sensor_msgs::ImageConstPtr&);

int main(int argc, char** argv)
{
#ifdef DEBUG
	log4cxx::Logger::getLogger(ROSCONSOLE_DEFAULT_NAME)->setLevel(ros::console::g_level_lookup[ros::console::levels::Debug]);
	ros::console::notifyLoggerLevelsChanged();
#endif
	ros::init(argc,argv,"video_stream_subscriber");
	ros::NodeHandle n;
	image_transport::ImageTransport it(n);

	std::string stereo_ns_ = ros::names::resolve(std::string("stereo"));
	std::string left_topic = ros::names::clean(stereo_ns_ + "/left/image_raw");
	image_transport::Subscriber sub=it.subscribe(left_topic,100,&theora_callback);

//	image_transport::Subscriber sub=it.subscribe("/stereo/left/image_raw",100,&theora_callback);

//	image_transport::CameraSubscriber camSub= it.subscribeCamera("/stereo/left/image_raw",100,&subCameraCallback);

//	image_transport::Subscriber sub=it.subscribe("/stereo/left/image_raw", 100, &TopicReader::theora_callback, &tr);

	ros::spin();

	return 0;
}

void theora_callback(const sensor_msgs::ImageConstPtr& msg)
{
		ROS_DEBUG("theora_callback called");
		cv::namedWindow("theora_callback",CV_WINDOW_AUTOSIZE);
//		cv_bridge::CvImagePtr cv_ptr;
		cv_bridge::CvImageConstPtr cv_ptr;
		try
		{
			cv_ptr = cv_bridge::toCvShare(msg,"bgr8");
			ROS_DEBUG("within try block");
			cv::imshow("theora_callback", cv_ptr->image);

		}
		catch (sensor_msgs::CvBridgeException& e)
		{
			ROS_ERROR("Could not open video stream: exception %s.", e.what());
		}
		ROS_DEBUG("before waitkey");
		cv::waitKey(10);
		ROS_DEBUG("after waitkey");
}



/***************************************************************************
 *
using namespace cv;
void streamingCallback(const sensor_msgs::ImageConstPtr& msg)
{
	namedWindow("video streaming",CV_WINDOW_AUTOSIZE);

//code from theora_listener.cpp's callback function
	sensor_msgs::CvBridge bridge;
	Mat frame;
	try
	{
		frame = bridge.imgMsgToCv(msg,"bgr8");
		imshow("video streaming", frame);
	}
	catch (sensor_msgs::CvBridgeException& e)
	{
		ROS_ERROR("Could not convert from '%s' to 'rgb8'.", msg->encoding.c_str());
	}


	IplImage *video;
	video = bridge.imgMsgToCv(msg,"bgr8");
	VideoWriter writer("pippo.avi",CV_FOURCC('M','J','P','G'),24,cvSize(video->width,video->height),true);
	writer << video;

}
******************************************************/
