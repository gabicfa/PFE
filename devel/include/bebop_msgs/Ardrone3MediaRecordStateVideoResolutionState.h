// Generated by gencpp from file bebop_msgs/Ardrone3MediaRecordStateVideoResolutionState.msg
// DO NOT EDIT!


#ifndef BEBOP_MSGS_MESSAGE_ARDRONE3MEDIARECORDSTATEVIDEORESOLUTIONSTATE_H
#define BEBOP_MSGS_MESSAGE_ARDRONE3MEDIARECORDSTATEVIDEORESOLUTIONSTATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace bebop_msgs
{
template <class ContainerAllocator>
struct Ardrone3MediaRecordStateVideoResolutionState_
{
  typedef Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> Type;

  Ardrone3MediaRecordStateVideoResolutionState_()
    : header()
    , streaming(0)
    , recording(0)  {
    }
  Ardrone3MediaRecordStateVideoResolutionState_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , streaming(0)
    , recording(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint8_t _streaming_type;
  _streaming_type streaming;

   typedef uint8_t _recording_type;
  _recording_type recording;



  enum {
    streaming_res360p = 0u,
    streaming_res480p = 1u,
    streaming_res720p = 2u,
    streaming_res1080p = 3u,
    recording_res360p = 0u,
    recording_res480p = 1u,
    recording_res720p = 2u,
    recording_res1080p = 3u,
  };


  typedef boost::shared_ptr< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> const> ConstPtr;

}; // struct Ardrone3MediaRecordStateVideoResolutionState_

typedef ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<std::allocator<void> > Ardrone3MediaRecordStateVideoResolutionState;

typedef boost::shared_ptr< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState > Ardrone3MediaRecordStateVideoResolutionStatePtr;
typedef boost::shared_ptr< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState const> Ardrone3MediaRecordStateVideoResolutionStateConstPtr;

// constants requiring out of line definition

   

   

   

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace bebop_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/home/gabicfa/catkin_ws/src/std_msgs/msg'], 'bebop_msgs': ['/home/gabicfa/catkin_ws/src/bebop_autonomy/bebop_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "478002c2ec614a227f494865922fd580";
  }

  static const char* value(const ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x478002c2ec614a22ULL;
  static const uint64_t static_value2 = 0x7f494865922fd580ULL;
};

template<class ContainerAllocator>
struct DataType< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bebop_msgs/Ardrone3MediaRecordStateVideoResolutionState";
  }

  static const char* value(const ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Ardrone3MediaRecordStateVideoResolutionState\n\
# auto-generated from up stream XML files at\n\
#   github.com/Parrot-Developers/libARCommands/tree/master/Xml\n\
# To check upstream commit hash, refer to last_build_info file\n\
# Do not modify this file by hand. Check scripts/meta folder for generator files.\n\
#\n\
# SDK Comment: Video resolution.\\n Informs about streaming and recording video resolutions.\\n Note that this is only an indication about what the resolution should be. To know the real resolution, you should get it from the frame.\n\
\n\
Header header\n\
\n\
# Streaming resolution\n\
uint8 streaming_res360p=0  # 360p resolution.\n\
uint8 streaming_res480p=1  # 480p resolution.\n\
uint8 streaming_res720p=2  # 720p resolution.\n\
uint8 streaming_res1080p=3  # 1080p resolution.\n\
uint8 streaming\n\
# Recording resolution\n\
uint8 recording_res360p=0  # 360p resolution.\n\
uint8 recording_res480p=1  # 480p resolution.\n\
uint8 recording_res720p=2  # 720p resolution.\n\
uint8 recording_res1080p=3  # 1080p resolution.\n\
uint8 recording\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.streaming);
      stream.next(m.recording);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Ardrone3MediaRecordStateVideoResolutionState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::bebop_msgs::Ardrone3MediaRecordStateVideoResolutionState_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "streaming: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.streaming);
    s << indent << "recording: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.recording);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEBOP_MSGS_MESSAGE_ARDRONE3MEDIARECORDSTATEVIDEORESOLUTIONSTATE_H
