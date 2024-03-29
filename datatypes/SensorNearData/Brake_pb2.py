# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SensorNearData/Brake.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2
from SensorNearData import SensorStates_pb2 as SensorNearData_dot_SensorStates__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='SensorNearData/Brake.proto',
  package='pb.SensorNearData',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x1aSensorNearData/Brake.proto\x12\x11pb.SensorNearData\x1a\x0cheader.proto\x1a!SensorNearData/SensorStates.proto\"\xc4\x02\n\x05\x42rake\x12\x1a\n\x06header\x18\x01 \x01(\x0b\x32\n.pb.Header\x12+\n\x04\x65rrs\x18\x03 \x01(\x0b\x32\x1d.pb.SensorNearData.Brake.Errs\x12\x31\n\x07signals\x18\x04 \x01(\x0b\x32 .pb.SensorNearData.Brake.Signals\x1aw\n\x04\x45rrs\x12\x36\n\x0f\x64river_pressure\x18\x01 \x01(\x0e\x32\x10.pb.SensorStates:\x0bSTATE_FAULT\x12\x37\n\x10is_brake_applied\x18\x02 \x01(\x0e\x32\x10.pb.SensorStates:\x0bSTATE_FAULT\x1a\x46\n\x07Signals\x12\x1a\n\x0f\x64river_pressure\x18\x02 \x01(\x02:\x01\x30\x12\x1f\n\x10is_brake_applied\x18\x03 \x01(\x08:\x05\x66\x61lse'
  ,
  dependencies=[header__pb2.DESCRIPTOR,SensorNearData_dot_SensorStates__pb2.DESCRIPTOR,])




_BRAKE_ERRS = _descriptor.Descriptor(
  name='Errs',
  full_name='pb.SensorNearData.Brake.Errs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='driver_pressure', full_name='pb.SensorNearData.Brake.Errs.driver_pressure', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_brake_applied', full_name='pb.SensorNearData.Brake.Errs.is_brake_applied', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=351,
)

_BRAKE_SIGNALS = _descriptor.Descriptor(
  name='Signals',
  full_name='pb.SensorNearData.Brake.Signals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='driver_pressure', full_name='pb.SensorNearData.Brake.Signals.driver_pressure', index=0,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_brake_applied', full_name='pb.SensorNearData.Brake.Signals.is_brake_applied', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=423,
)

_BRAKE = _descriptor.Descriptor(
  name='Brake',
  full_name='pb.SensorNearData.Brake',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='pb.SensorNearData.Brake.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errs', full_name='pb.SensorNearData.Brake.errs', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signals', full_name='pb.SensorNearData.Brake.signals', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BRAKE_ERRS, _BRAKE_SIGNALS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=423,
)

_BRAKE_ERRS.fields_by_name['driver_pressure'].enum_type = SensorNearData_dot_SensorStates__pb2._SENSORSTATES
_BRAKE_ERRS.fields_by_name['is_brake_applied'].enum_type = SensorNearData_dot_SensorStates__pb2._SENSORSTATES
_BRAKE_ERRS.containing_type = _BRAKE
_BRAKE_SIGNALS.containing_type = _BRAKE
_BRAKE.fields_by_name['header'].message_type = header__pb2._HEADER
_BRAKE.fields_by_name['errs'].message_type = _BRAKE_ERRS
_BRAKE.fields_by_name['signals'].message_type = _BRAKE_SIGNALS
DESCRIPTOR.message_types_by_name['Brake'] = _BRAKE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Brake = _reflection.GeneratedProtocolMessageType('Brake', (_message.Message,), {

  'Errs' : _reflection.GeneratedProtocolMessageType('Errs', (_message.Message,), {
    'DESCRIPTOR' : _BRAKE_ERRS,
    '__module__' : 'SensorNearData.Brake_pb2'
    # @@protoc_insertion_point(class_scope:pb.SensorNearData.Brake.Errs)
    })
  ,

  'Signals' : _reflection.GeneratedProtocolMessageType('Signals', (_message.Message,), {
    'DESCRIPTOR' : _BRAKE_SIGNALS,
    '__module__' : 'SensorNearData.Brake_pb2'
    # @@protoc_insertion_point(class_scope:pb.SensorNearData.Brake.Signals)
    })
  ,
  'DESCRIPTOR' : _BRAKE,
  '__module__' : 'SensorNearData.Brake_pb2'
  # @@protoc_insertion_point(class_scope:pb.SensorNearData.Brake)
  })
_sym_db.RegisterMessage(Brake)
_sym_db.RegisterMessage(Brake.Errs)
_sym_db.RegisterMessage(Brake.Signals)


# @@protoc_insertion_point(module_scope)
