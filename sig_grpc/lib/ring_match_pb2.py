# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ring_match.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import data_types_pb2 as data__types__pb2
import data_requests_pb2 as data__requests__pb2
import db_service_request_common_pb2 as db__service__request__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ring_match.proto',
  package='io.lightcone.service.ring_match',
  syntax='proto3',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\x10ring_match.proto\x12\x1fio.lightcone.service.ring_match\x1a\x10\x64\x61ta_types.proto\x1a\x13\x64\x61ta_requests.proto\x1a\x1f\x64\x62_service_request_common.proto\"\x85\x01\n\x0b\x44\x65pthUpdate\x12\x10\n\x08is_buyer\x18\x01 \x01(\x08\x12\x31\n\x08\x61mount_s\x18\x02 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\x31\n\x08\x61mount_b\x18\x03 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\"\x86\n\n\x10RingMatcherEvent\x12N\n\x05match\x18\x01 \x01(\x0b\x32=.io.lightcone.service.ring_match.RingMatcherEvent.MatchResultH\x00\x12_\n\x0eorder_canceled\x18\x02 \x01(\x0b\x32\x45.io.lightcone.service.ring_match.RingMatcherEvent.OrderCanceledResultH\x00\x12]\n\rorder_expired\x18\x03 \x01(\x0b\x32\x44.io.lightcone.service.ring_match.RingMatcherEvent.OrderExpiredResultH\x00\x12\x45\n\x05order\x18\x04 \x01(\x0b\x32\x34.io.lightcone.services.request.common.MatchableOrderH\x00\x12L\n\x07restart\x18\x05 \x01(\x0b\x32\x39.io.lightcone.service.ring_match.RingMatcherEvent.RestartH\x00\x12\x0e\n\x06market\x18\x06 \x01(\t\x1a\xcc\x01\n\x0bMatchResult\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\tglobal_id\x18\x02 \x01(\x04\x12J\n\tprocessed\x18\x03 \x01(\x0b\x32\x37.io.lightcone.data.requests.RingSettlementProcessedData\x12\x0e\n\x06market\x18\x04 \x01(\t\x12\x42\n\x0c\x64\x65pth_update\x18\x05 \x01(\x0b\x32,.io.lightcone.service.ring_match.DepthUpdate\x1a\xab\x02\n\x13OrderCanceledResult\x12\x36\n\naccount_id\x18\x01 \x01(\x0b\x32\".io.lightcone.data.types.AccountID\x12\x34\n\ntoken_s_id\x18\x02 \x01(\x0b\x32 .io.lightcone.data.types.TokenID\x12\x32\n\x08order_id\x18\x03 \x01(\x0b\x32 .io.lightcone.data.types.OrderID\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12\x31\n\x08\x61mount_s\x18\x05 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\x31\n\x08\x61mount_b\x18\x06 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x1a\xaa\x02\n\x12OrderExpiredResult\x12\x36\n\naccount_id\x18\x01 \x01(\x0b\x32\".io.lightcone.data.types.AccountID\x12\x34\n\ntoken_s_id\x18\x02 \x01(\x0b\x32 .io.lightcone.data.types.TokenID\x12\x32\n\x08order_id\x18\x03 \x01(\x0b\x32 .io.lightcone.data.types.OrderID\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12\x31\n\x08\x61mount_s\x18\x05 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\x31\n\x08\x61mount_b\x18\x06 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x1a\t\n\x07RestartB\x08\n\x06Result*?\n\tEventType\x12\r\n\tNEW_ORDER\x10\x00\x12\x10\n\x0c\x43\x41NCEL_ORDER\x10\x01\x12\x11\n\rEXPIRED_ORDER\x10\x02\x42\x02P\x01\x62\x06proto3')
  ,
  dependencies=[data__types__pb2.DESCRIPTOR,data__requests__pb2.DESCRIPTOR,db__service__request__common__pb2.DESCRIPTOR,])

_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='io.lightcone.service.ring_match.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEW_ORDER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_ORDER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED_ORDER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1550,
  serialized_end=1613,
)
_sym_db.RegisterEnumDescriptor(_EVENTTYPE)

EventType = enum_type_wrapper.EnumTypeWrapper(_EVENTTYPE)
NEW_ORDER = 0
CANCEL_ORDER = 1
EXPIRED_ORDER = 2



_DEPTHUPDATE = _descriptor.Descriptor(
  name='DepthUpdate',
  full_name='io.lightcone.service.ring_match.DepthUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_buyer', full_name='io.lightcone.service.ring_match.DepthUpdate.is_buyer', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_s', full_name='io.lightcone.service.ring_match.DepthUpdate.amount_s', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_b', full_name='io.lightcone.service.ring_match.DepthUpdate.amount_b', index=2,
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
  serialized_end=259,
)


_RINGMATCHEREVENT_MATCHRESULT = _descriptor.Descriptor(
  name='MatchResult',
  full_name='io.lightcone.service.ring_match.RingMatcherEvent.MatchResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='io.lightcone.service.ring_match.RingMatcherEvent.MatchResult.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_id', full_name='io.lightcone.service.ring_match.RingMatcherEvent.MatchResult.global_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processed', full_name='io.lightcone.service.ring_match.RingMatcherEvent.MatchResult.processed', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market', full_name='io.lightcone.service.ring_match.RingMatcherEvent.MatchResult.market', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth_update', full_name='io.lightcone.service.ring_match.RingMatcherEvent.MatchResult.depth_update', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=720,
  serialized_end=924,
)

_RINGMATCHEREVENT_ORDERCANCELEDRESULT = _descriptor.Descriptor(
  name='OrderCanceledResult',
  full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderCanceledResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderCanceledResult.account_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_s_id', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderCanceledResult.token_s_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderCanceledResult.order_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderCanceledResult.hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_s', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderCanceledResult.amount_s', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_b', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderCanceledResult.amount_b', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=927,
  serialized_end=1226,
)

_RINGMATCHEREVENT_ORDEREXPIREDRESULT = _descriptor.Descriptor(
  name='OrderExpiredResult',
  full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderExpiredResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderExpiredResult.account_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_s_id', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderExpiredResult.token_s_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderExpiredResult.order_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderExpiredResult.hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_s', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderExpiredResult.amount_s', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_b', full_name='io.lightcone.service.ring_match.RingMatcherEvent.OrderExpiredResult.amount_b', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=1229,
  serialized_end=1527,
)

_RINGMATCHEREVENT_RESTART = _descriptor.Descriptor(
  name='Restart',
  full_name='io.lightcone.service.ring_match.RingMatcherEvent.Restart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1529,
  serialized_end=1538,
)

_RINGMATCHEREVENT = _descriptor.Descriptor(
  name='RingMatcherEvent',
  full_name='io.lightcone.service.ring_match.RingMatcherEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match', full_name='io.lightcone.service.ring_match.RingMatcherEvent.match', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_canceled', full_name='io.lightcone.service.ring_match.RingMatcherEvent.order_canceled', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_expired', full_name='io.lightcone.service.ring_match.RingMatcherEvent.order_expired', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='io.lightcone.service.ring_match.RingMatcherEvent.order', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restart', full_name='io.lightcone.service.ring_match.RingMatcherEvent.restart', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market', full_name='io.lightcone.service.ring_match.RingMatcherEvent.market', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RINGMATCHEREVENT_MATCHRESULT, _RINGMATCHEREVENT_ORDERCANCELEDRESULT, _RINGMATCHEREVENT_ORDEREXPIREDRESULT, _RINGMATCHEREVENT_RESTART, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Result', full_name='io.lightcone.service.ring_match.RingMatcherEvent.Result',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=262,
  serialized_end=1548,
)

_DEPTHUPDATE.fields_by_name['amount_s'].message_type = data__types__pb2._AMOUNT
_DEPTHUPDATE.fields_by_name['amount_b'].message_type = data__types__pb2._AMOUNT
_RINGMATCHEREVENT_MATCHRESULT.fields_by_name['processed'].message_type = data__requests__pb2._RINGSETTLEMENTPROCESSEDDATA
_RINGMATCHEREVENT_MATCHRESULT.fields_by_name['depth_update'].message_type = _DEPTHUPDATE
_RINGMATCHEREVENT_MATCHRESULT.containing_type = _RINGMATCHEREVENT
_RINGMATCHEREVENT_ORDERCANCELEDRESULT.fields_by_name['account_id'].message_type = data__types__pb2._ACCOUNTID
_RINGMATCHEREVENT_ORDERCANCELEDRESULT.fields_by_name['token_s_id'].message_type = data__types__pb2._TOKENID
_RINGMATCHEREVENT_ORDERCANCELEDRESULT.fields_by_name['order_id'].message_type = data__types__pb2._ORDERID
_RINGMATCHEREVENT_ORDERCANCELEDRESULT.fields_by_name['amount_s'].message_type = data__types__pb2._AMOUNT
_RINGMATCHEREVENT_ORDERCANCELEDRESULT.fields_by_name['amount_b'].message_type = data__types__pb2._AMOUNT
_RINGMATCHEREVENT_ORDERCANCELEDRESULT.containing_type = _RINGMATCHEREVENT
_RINGMATCHEREVENT_ORDEREXPIREDRESULT.fields_by_name['account_id'].message_type = data__types__pb2._ACCOUNTID
_RINGMATCHEREVENT_ORDEREXPIREDRESULT.fields_by_name['token_s_id'].message_type = data__types__pb2._TOKENID
_RINGMATCHEREVENT_ORDEREXPIREDRESULT.fields_by_name['order_id'].message_type = data__types__pb2._ORDERID
_RINGMATCHEREVENT_ORDEREXPIREDRESULT.fields_by_name['amount_s'].message_type = data__types__pb2._AMOUNT
_RINGMATCHEREVENT_ORDEREXPIREDRESULT.fields_by_name['amount_b'].message_type = data__types__pb2._AMOUNT
_RINGMATCHEREVENT_ORDEREXPIREDRESULT.containing_type = _RINGMATCHEREVENT
_RINGMATCHEREVENT_RESTART.containing_type = _RINGMATCHEREVENT
_RINGMATCHEREVENT.fields_by_name['match'].message_type = _RINGMATCHEREVENT_MATCHRESULT
_RINGMATCHEREVENT.fields_by_name['order_canceled'].message_type = _RINGMATCHEREVENT_ORDERCANCELEDRESULT
_RINGMATCHEREVENT.fields_by_name['order_expired'].message_type = _RINGMATCHEREVENT_ORDEREXPIREDRESULT
_RINGMATCHEREVENT.fields_by_name['order'].message_type = db__service__request__common__pb2._MATCHABLEORDER
_RINGMATCHEREVENT.fields_by_name['restart'].message_type = _RINGMATCHEREVENT_RESTART
_RINGMATCHEREVENT.oneofs_by_name['Result'].fields.append(
  _RINGMATCHEREVENT.fields_by_name['match'])
_RINGMATCHEREVENT.fields_by_name['match'].containing_oneof = _RINGMATCHEREVENT.oneofs_by_name['Result']
_RINGMATCHEREVENT.oneofs_by_name['Result'].fields.append(
  _RINGMATCHEREVENT.fields_by_name['order_canceled'])
_RINGMATCHEREVENT.fields_by_name['order_canceled'].containing_oneof = _RINGMATCHEREVENT.oneofs_by_name['Result']
_RINGMATCHEREVENT.oneofs_by_name['Result'].fields.append(
  _RINGMATCHEREVENT.fields_by_name['order_expired'])
_RINGMATCHEREVENT.fields_by_name['order_expired'].containing_oneof = _RINGMATCHEREVENT.oneofs_by_name['Result']
_RINGMATCHEREVENT.oneofs_by_name['Result'].fields.append(
  _RINGMATCHEREVENT.fields_by_name['order'])
_RINGMATCHEREVENT.fields_by_name['order'].containing_oneof = _RINGMATCHEREVENT.oneofs_by_name['Result']
_RINGMATCHEREVENT.oneofs_by_name['Result'].fields.append(
  _RINGMATCHEREVENT.fields_by_name['restart'])
_RINGMATCHEREVENT.fields_by_name['restart'].containing_oneof = _RINGMATCHEREVENT.oneofs_by_name['Result']
DESCRIPTOR.message_types_by_name['DepthUpdate'] = _DEPTHUPDATE
DESCRIPTOR.message_types_by_name['RingMatcherEvent'] = _RINGMATCHEREVENT
DESCRIPTOR.enum_types_by_name['EventType'] = _EVENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DepthUpdate = _reflection.GeneratedProtocolMessageType('DepthUpdate', (_message.Message,), {
  'DESCRIPTOR' : _DEPTHUPDATE,
  '__module__' : 'ring_match_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.service.ring_match.DepthUpdate)
  })
_sym_db.RegisterMessage(DepthUpdate)

RingMatcherEvent = _reflection.GeneratedProtocolMessageType('RingMatcherEvent', (_message.Message,), {

  'MatchResult' : _reflection.GeneratedProtocolMessageType('MatchResult', (_message.Message,), {
    'DESCRIPTOR' : _RINGMATCHEREVENT_MATCHRESULT,
    '__module__' : 'ring_match_pb2'
    # @@protoc_insertion_point(class_scope:io.lightcone.service.ring_match.RingMatcherEvent.MatchResult)
    })
  ,

  'OrderCanceledResult' : _reflection.GeneratedProtocolMessageType('OrderCanceledResult', (_message.Message,), {
    'DESCRIPTOR' : _RINGMATCHEREVENT_ORDERCANCELEDRESULT,
    '__module__' : 'ring_match_pb2'
    # @@protoc_insertion_point(class_scope:io.lightcone.service.ring_match.RingMatcherEvent.OrderCanceledResult)
    })
  ,

  'OrderExpiredResult' : _reflection.GeneratedProtocolMessageType('OrderExpiredResult', (_message.Message,), {
    'DESCRIPTOR' : _RINGMATCHEREVENT_ORDEREXPIREDRESULT,
    '__module__' : 'ring_match_pb2'
    # @@protoc_insertion_point(class_scope:io.lightcone.service.ring_match.RingMatcherEvent.OrderExpiredResult)
    })
  ,

  'Restart' : _reflection.GeneratedProtocolMessageType('Restart', (_message.Message,), {
    'DESCRIPTOR' : _RINGMATCHEREVENT_RESTART,
    '__module__' : 'ring_match_pb2'
    # @@protoc_insertion_point(class_scope:io.lightcone.service.ring_match.RingMatcherEvent.Restart)
    })
  ,
  'DESCRIPTOR' : _RINGMATCHEREVENT,
  '__module__' : 'ring_match_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.service.ring_match.RingMatcherEvent)
  })
_sym_db.RegisterMessage(RingMatcherEvent)
_sym_db.RegisterMessage(RingMatcherEvent.MatchResult)
_sym_db.RegisterMessage(RingMatcherEvent.OrderCanceledResult)
_sym_db.RegisterMessage(RingMatcherEvent.OrderExpiredResult)
_sym_db.RegisterMessage(RingMatcherEvent.Restart)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)