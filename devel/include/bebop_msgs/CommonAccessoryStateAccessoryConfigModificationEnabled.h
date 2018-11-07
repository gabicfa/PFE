// Generated by gencpp from file bebop_msgs/CommonAccessoryStateAccessoryConfigModificationEnabled.msg
// DO NOT EDIT!


#ifndef BEBOP_MSGS_MESSAGE_COMMONACCESSORYSTATEACCESSORYCONFIGMODIFICATIONENABLED_H
#define BEBOP_MSGS_MESSAGE_COMMONACCESSORYSTATEACCESSORYCONFIGMODIFICATIONENABLED_H


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
struct CommonAccessoryStateAccessoryConfigModificationEnabled_
{
  typedef CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> Type;

  CommonAccessoryStateAccessoryConfigModificationEnabled_()
    : header()
    , enabled(0)  {
    }
  CommonAccessoryStateAccessoryConfigModificationEnabled_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , enabled(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint8_t _enabled_type;
  _enabled_type enabled;





  typedef boost::shared_ptr< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> const> ConstPtr;

}; // struct CommonAccessoryStateAccessoryConfigModificationEnabled_

typedef ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<std::allocator<void> > CommonAccessoryStateAccessoryConfigModificationEnabled;

typedef boost::shared_ptr< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled > CommonAccessoryStateAccessoryConfigModificationEnabledPtr;
typedef boost::shared_ptr< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled const> CommonAccessoryStateAccessoryConfigModificationEnabledConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fce93efbb8b61357f131a1998ab02e91";
  }

  static const char* value(const ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xfce93efbb8b61357ULL;
  static const uint64_t static_value2 = 0xf131a1998ab02e91ULL;
};

template<class ContainerAllocator>
struct DataType< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bebop_msgs/CommonAccessoryStateAccessoryConfigModificationEnabled";
  }

  static const char* value(const ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# CommonAccessoryStateAccessoryConfigModificationEnabled\n\
# auto-generated from up stream XML files at\n\
#   github.com/Parrot-Developers/libARCommands/tree/master/Xml\n\
# To check upstream commit hash, refer to last_build_info file\n\
# Do not modify this file by hand. Check scripts/meta folder for generator files.\n\
#\n\
# SDK Comment: Availability to declare or not an accessory.\n\
\n\
Header header\n\
\n\
# 1 if the modification of the accessory Config is enabled, 0 otherwise\n\
uint8 enabled\n\
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

  static const char* value(const ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.enabled);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CommonAccessoryStateAccessoryConfigModificationEnabled_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::bebop_msgs::CommonAccessoryStateAccessoryConfigModificationEnabled_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "enabled: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.enabled);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEBOP_MSGS_MESSAGE_COMMONACCESSORYSTATEACCESSORYCONFIGMODIFICATIONENABLED_H
