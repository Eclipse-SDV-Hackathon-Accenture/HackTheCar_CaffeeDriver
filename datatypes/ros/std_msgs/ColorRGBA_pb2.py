# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ros/std_msgs/ColorRGBA.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ros/std_msgs/ColorRGBA.proto',
  package='ros.std_msgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1cros/std_msgs/ColorRGBA.proto\x12\x0cros.std_msgs\"7\n\tColorRGBA\x12\t\n\x01r\x18\x01 \x01(\x02\x12\t\n\x01g\x18\x02 \x01(\x02\x12\t\n\x01\x62\x18\x03 \x01(\x02\x12\t\n\x01\x61\x18\x04 \x01(\x02\x62\x06proto3'
)




_COLORRGBA = _descriptor.Descriptor(
  name='ColorRGBA',
  full_name='ros.std_msgs.ColorRGBA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='r', full_name='ros.std_msgs.ColorRGBA.r', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='g', full_name='ros.std_msgs.ColorRGBA.g', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='ros.std_msgs.ColorRGBA.b', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='a', full_name='ros.std_msgs.ColorRGBA.a', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=46,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['ColorRGBA'] = _COLORRGBA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ColorRGBA = _reflection.GeneratedProtocolMessageType('ColorRGBA', (_message.Message,), {
  'DESCRIPTOR' : _COLORRGBA,
  '__module__' : 'ros.std_msgs.ColorRGBA_pb2'
  # @@protoc_insertion_point(class_scope:ros.std_msgs.ColorRGBA)
  })
_sym_db.RegisterMessage(ColorRGBA)


# @@protoc_insertion_point(module_scope)
