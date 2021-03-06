"""autogenerated by genmsg_py from FacePosAndDist.msg. Do not edit."""
import roslib.message
import struct

import std_msgs.msg

class FacePosAndDist(roslib.message.Message):
  _md5sum = "25b96c14697425c4e9c9aa5538bcad7c"
  _type = "qbo_face_msgs/FacePosAndDist"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Software License Agreement (LGPL v2.1 License)
#
# Copyright (c) 2012 Thecorpora, S.L.
#
# This library is free software; you can redistribute it and/or modify 
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation; either version 2.1 of the License, 
# or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public 
# License for more details.
#  
# You should have received a copy of the GNU General Public License 
# along with this program; if not, write to the Free Software 
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# MA 02110-1301, USA.

Header header
float32 u
float32 v
float32 distance_to_head
int32 image_width
int32 image_height
bool face_detected
string type_of_tracking

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['header','u','v','distance_to_head','image_width','image_height','face_detected','type_of_tracking']
  _slot_types = ['Header','float32','float32','float32','int32','int32','bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       header,u,v,distance_to_head,image_width,image_height,face_detected,type_of_tracking
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(FacePosAndDist, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      if self.u is None:
        self.u = 0.
      if self.v is None:
        self.v = 0.
      if self.distance_to_head is None:
        self.distance_to_head = 0.
      if self.image_width is None:
        self.image_width = 0
      if self.image_height is None:
        self.image_height = 0
      if self.face_detected is None:
        self.face_detected = False
      if self.type_of_tracking is None:
        self.type_of_tracking = ''
    else:
      self.header = std_msgs.msg._Header.Header()
      self.u = 0.
      self.v = 0.
      self.distance_to_head = 0.
      self.image_width = 0
      self.image_height = 0
      self.face_detected = False
      self.type_of_tracking = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3f2iB.pack(_x.u, _x.v, _x.distance_to_head, _x.image_width, _x.image_height, _x.face_detected))
      _x = self.type_of_tracking
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 21
      (_x.u, _x.v, _x.distance_to_head, _x.image_width, _x.image_height, _x.face_detected,) = _struct_3f2iB.unpack(str[start:end])
      self.face_detected = bool(self.face_detected)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.type_of_tracking = str[start:end]
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3f2iB.pack(_x.u, _x.v, _x.distance_to_head, _x.image_width, _x.image_height, _x.face_detected))
      _x = self.type_of_tracking
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 21
      (_x.u, _x.v, _x.distance_to_head, _x.image_width, _x.image_height, _x.face_detected,) = _struct_3f2iB.unpack(str[start:end])
      self.face_detected = bool(self.face_detected)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.type_of_tracking = str[start:end]
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_3I = struct.Struct("<3I")
_struct_3f2iB = struct.Struct("<3f2iB")
