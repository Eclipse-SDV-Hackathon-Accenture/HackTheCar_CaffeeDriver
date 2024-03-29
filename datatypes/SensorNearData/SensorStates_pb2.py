# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SensorNearData/SensorStates.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SensorNearData/SensorStates.proto',
  package='pb',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n!SensorNearData/SensorStates.proto\x12\x02pb*U\n\x0cSensorStates\x12\x0f\n\x0bSTATE_FAULT\x10\x00\x12\x0c\n\x08STATE_OK\x10\x01\x12\x11\n\rSTATE_TIMEOUT\x10\x02\x12\x13\n\x0fSTATE_NOT_EXIST\x10\x03'
)

_SENSORSTATES = _descriptor.EnumDescriptor(
  name='SensorStates',
  full_name='pb.SensorStates',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_FAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_TIMEOUT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_NOT_EXIST', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=41,
  serialized_end=126,
)
_sym_db.RegisterEnumDescriptor(_SENSORSTATES)

SensorStates = enum_type_wrapper.EnumTypeWrapper(_SENSORSTATES)
STATE_FAULT = 0
STATE_OK = 1
STATE_TIMEOUT = 2
STATE_NOT_EXIST = 3


DESCRIPTOR.enum_types_by_name['SensorStates'] = _SENSORSTATES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
