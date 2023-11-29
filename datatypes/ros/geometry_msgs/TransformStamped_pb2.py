# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ros/geometry_msgs/TransformStamped.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from datatypes.ros.geometry_msgs import Transform_pb2 as ros_dot_geometry__msgs_dot_Transform__pb2
from datatypes.ros.std_msgs import Header_pb2 as ros_dot_std__msgs_dot_Header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ros/geometry_msgs/TransformStamped.proto',
  package='ros.geometry_msgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n(ros/geometry_msgs/TransformStamped.proto\x12\x11ros.geometry_msgs\x1a!ros/geometry_msgs/Transform.proto\x1a\x19ros/std_msgs/Header.proto\"\x81\x01\n\x10TransformStamped\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.ros.std_msgs.Header\x12\x16\n\x0e\x63hild_frame_id\x18\x02 \x01(\t\x12/\n\ttransform\x18\x03 \x01(\x0b\x32\x1c.ros.geometry_msgs.Transformb\x06proto3'
  ,
  dependencies=[ros_dot_geometry__msgs_dot_Transform__pb2.DESCRIPTOR,ros_dot_std__msgs_dot_Header__pb2.DESCRIPTOR,])




_TRANSFORMSTAMPED = _descriptor.Descriptor(
  name='TransformStamped',
  full_name='ros.geometry_msgs.TransformStamped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='ros.geometry_msgs.TransformStamped.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child_frame_id', full_name='ros.geometry_msgs.TransformStamped.child_frame_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transform', full_name='ros.geometry_msgs.TransformStamped.transform', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=255,
)

_TRANSFORMSTAMPED.fields_by_name['header'].message_type = ros_dot_std__msgs_dot_Header__pb2._HEADER
_TRANSFORMSTAMPED.fields_by_name['transform'].message_type = ros_dot_geometry__msgs_dot_Transform__pb2._TRANSFORM
DESCRIPTOR.message_types_by_name['TransformStamped'] = _TRANSFORMSTAMPED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransformStamped = _reflection.GeneratedProtocolMessageType('TransformStamped', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMSTAMPED,
  '__module__' : 'ros.geometry_msgs.TransformStamped_pb2'
  # @@protoc_insertion_point(class_scope:ros.geometry_msgs.TransformStamped)
  })
_sym_db.RegisterMessage(TransformStamped)


# @@protoc_insertion_point(module_scope)