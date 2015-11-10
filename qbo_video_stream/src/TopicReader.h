/*
 * TopicReader.h
 *
 *  Created on: Nov 9, 2015
 *      Author: qbobot
 */

#ifndef SRC_TOPICREADER_H_
#define SRC_TOPICREADER_H_

#include "sensor_msgs/CompressedImage.h"
#include "image_transport/image_transport.h"
#include <opencv/highgui.h>
#include <cv_bridge/CvBridge.h>


class TopicReader {
	public:
		TopicReader();
		virtual ~TopicReader();
		void foo();
		void image_raw_callback(const sensor_msgs::ImageConstPtr&);
		void compressed_callback(const sensor_msgs::ImageConstPtr&);
	//	void compressed_param_description_callback(const dynamic_reconfigure::ConfigDescription&);
	//	void compressed_param_updates_callback(const dynamic_reconfigure::Config&);
		void theora_callback(const sensor_msgs::ImageConstPtr&);
	//	void theora_param_description_callback(const dynamic_reconfigure::ConfigDescription&);
	//	void theora_param_updates_callback(const dynamic_reconfigure::Config&);
		void camera_info_callback(const sensor_msgs::CameraInfo&);

};

#endif /* SRC_TOPICREADER_H_ */
