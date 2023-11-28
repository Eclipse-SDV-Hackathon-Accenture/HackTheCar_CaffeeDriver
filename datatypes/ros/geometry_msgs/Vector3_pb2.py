# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ros/geometry_msgs/Vector3.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ros/geometry_msgs/Vector3.proto',
  package='ros.geometry_msgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1fros/geometry_msgs/Vector3.proto\x12\x11ros.geometry_msgs\"*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x62\x06proto3'
)




_VECTOR3 = _descriptor.Descriptor(
  name='Vector3',
  full_name='ros.geometry_msgs.Vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='ros.geometry_msgs.Vector3.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='ros.geometry_msgs.Vector3.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='ros.geometry_msgs.Vector3.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=54,
  serialized_end=96,
)

DESCRIPTOR.message_types_by_name['Vector3'] = _VECTOR3
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR3,
  '__module__' : 'ros.geometry_msgs.Vector3_pb2'
  # @@protoc_insertion_point(class_scope:ros.geometry_msgs.Vector3)
  })
_sym_db.RegisterMessage(Vector3)


# @@protoc_insertion_point(module_scope)
