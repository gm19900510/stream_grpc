# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stream.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stream.proto',
  package='stream',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cstream.proto\x12\x06stream\"\x1b\n\x0bRequestData\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1c\n\x0cResponseData\x12\x0c\n\x04text\x18\x01 \x01(\t2\x99\x02\n\rStreamService\x12\x38\n\tSimpleFun\x12\x13.stream.RequestData\x1a\x14.stream.ResponseData\"\x00\x12\x44\n\x13ServerSideStreamFun\x12\x13.stream.RequestData\x1a\x14.stream.ResponseData\"\x00\x30\x01\x12\x44\n\x13\x43lientSideStreamFun\x12\x13.stream.RequestData\x1a\x14.stream.ResponseData\"\x00(\x01\x12\x42\n\x0fTwoWayStreamFun\x12\x13.stream.RequestData\x1a\x14.stream.ResponseData\"\x00(\x01\x30\x01\x62\x06proto3')
)




_REQUESTDATA = _descriptor.Descriptor(
  name='RequestData',
  full_name='stream.RequestData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='stream.RequestData.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=24,
  serialized_end=51,
)


_RESPONSEDATA = _descriptor.Descriptor(
  name='ResponseData',
  full_name='stream.ResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='stream.ResponseData.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=53,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['RequestData'] = _REQUESTDATA
DESCRIPTOR.message_types_by_name['ResponseData'] = _RESPONSEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestData = _reflection.GeneratedProtocolMessageType('RequestData', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTDATA,
  __module__ = 'stream_pb2'
  # @@protoc_insertion_point(class_scope:stream.RequestData)
  ))
_sym_db.RegisterMessage(RequestData)

ResponseData = _reflection.GeneratedProtocolMessageType('ResponseData', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEDATA,
  __module__ = 'stream_pb2'
  # @@protoc_insertion_point(class_scope:stream.ResponseData)
  ))
_sym_db.RegisterMessage(ResponseData)



_STREAMSERVICE = _descriptor.ServiceDescriptor(
  name='StreamService',
  full_name='stream.StreamService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=84,
  serialized_end=365,
  methods=[
  _descriptor.MethodDescriptor(
    name='SimpleFun',
    full_name='stream.StreamService.SimpleFun',
    index=0,
    containing_service=None,
    input_type=_REQUESTDATA,
    output_type=_RESPONSEDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ServerSideStreamFun',
    full_name='stream.StreamService.ServerSideStreamFun',
    index=1,
    containing_service=None,
    input_type=_REQUESTDATA,
    output_type=_RESPONSEDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClientSideStreamFun',
    full_name='stream.StreamService.ClientSideStreamFun',
    index=2,
    containing_service=None,
    input_type=_REQUESTDATA,
    output_type=_RESPONSEDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TwoWayStreamFun',
    full_name='stream.StreamService.TwoWayStreamFun',
    index=3,
    containing_service=None,
    input_type=_REQUESTDATA,
    output_type=_RESPONSEDATA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMSERVICE)

DESCRIPTOR.services_by_name['StreamService'] = _STREAMSERVICE

# @@protoc_insertion_point(module_scope)