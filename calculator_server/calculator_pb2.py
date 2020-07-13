# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x63\x61lculator.proto\"D\n\x0b\x43\x61lcRequest\x12\x10\n\x08number_1\x18\x01 \x01(\x11\x12\x10\n\x08number_2\x18\x02 \x01(\x11\x12\x11\n\toperation\x18\x03 \x01(\t\"\x18\n\tCalcReply\x12\x0b\n\x03res\x18\x01 \x01(\t20\n\nCalculator\x12\"\n\x04\x43\x61lc\x12\x0c.CalcRequest\x1a\n.CalcReply\"\x00\x62\x06proto3')
)




_CALCREQUEST = _descriptor.Descriptor(
  name='CalcRequest',
  full_name='CalcRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number_1', full_name='CalcRequest.number_1', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_2', full_name='CalcRequest.number_2', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='CalcRequest.operation', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=20,
  serialized_end=88,
)


_CALCREPLY = _descriptor.Descriptor(
  name='CalcReply',
  full_name='CalcReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='CalcReply.res', index=0,
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
  serialized_start=90,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['CalcRequest'] = _CALCREQUEST
DESCRIPTOR.message_types_by_name['CalcReply'] = _CALCREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CalcRequest = _reflection.GeneratedProtocolMessageType('CalcRequest', (_message.Message,), {
  'DESCRIPTOR' : _CALCREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:CalcRequest)
  })
_sym_db.RegisterMessage(CalcRequest)

CalcReply = _reflection.GeneratedProtocolMessageType('CalcReply', (_message.Message,), {
  'DESCRIPTOR' : _CALCREPLY,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:CalcReply)
  })
_sym_db.RegisterMessage(CalcReply)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=116,
  serialized_end=164,
  methods=[
  _descriptor.MethodDescriptor(
    name='Calc',
    full_name='Calculator.Calc',
    index=0,
    containing_service=None,
    input_type=_CALCREQUEST,
    output_type=_CALCREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
