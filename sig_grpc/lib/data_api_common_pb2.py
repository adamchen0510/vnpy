# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_api_common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
import data_types_pb2 as data__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='data_api_common.proto',
  package='io.lightcone.data.api.common',
  syntax='proto3',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\x15\x64\x61ta_api_common.proto\x12\x1cio.lightcone.data.api.common\x1a\x19google/protobuf/any.proto\x1a\x10\x64\x61ta_types.proto\"\xb5\x01\n\x08OHLCData\x12\x11\n\topen_time\x18\x01 \x01(\x03\x12-\n\x04size\x18\x02 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12/\n\x06volume\x18\x03 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\x0c\n\x04open\x18\x04 \x01(\t\x12\r\n\x05\x63lose\x18\x05 \x01(\t\x12\x0c\n\x04high\x18\x06 \x01(\t\x12\x0b\n\x03low\x18\x07 \x01(\t\"\xaa\x01\n\x06Ticker\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12-\n\x04size\x18\x02 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\x0c\n\x04open\x18\x03 \x01(\t\x12\x0c\n\x04high\x18\x04 \x01(\t\x12\x0b\n\x03low\x18\x05 \x01(\t\x12\x0c\n\x04last\x18\x06 \x01(\t\x12\r\n\x05\x63ount\x18\x07 \x01(\x04\x12\x0b\n\x03\x62id\x18\x08 \x01(\t\x12\x0b\n\x03\x61sk\x18\t \x01(\t\"y\n\x07\x42\x61lance\x12\r\n\x05token\x18\x01 \x01(\t\x12\x30\n\x07\x62\x61lance\x18\x02 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12-\n\x04lock\x18\x03 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\"\x89\x01\n\tDepthItem\x12\r\n\x05price\x18\x01 \x01(\t\x12-\n\x04size\x18\x02 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12/\n\x06volume\x18\x03 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\"w\n\x05Trade\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x0f\n\x07tradeId\x18\x02 \x01(\x04\x12\x0c\n\x04side\x18\x03 \x01(\t\x12-\n\x04size\x18\x04 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\r\n\x05price\x18\x05 \x01(\t\"\xbe\x03\n\x05Order\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x15\n\rclientOrderId\x18\x02 \x01(\t\x12-\n\x04size\x18\x03 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12/\n\x06volume\x18\x04 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\r\n\x05price\x18\x05 \x01(\t\x12\x34\n\x0b\x66illed_size\x18\x06 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\x36\n\rfilled_volume\x18\x07 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\x33\n\nfilled_fee\x18\x08 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\x0e\n\x06status\x18\t \x01(\t\x12\x13\n\x0bvalid_since\x18\n \x01(\x04\x12\x13\n\x0bvalid_until\x18\x0b \x01(\x04\x12\x12\n\ncreated_at\x18\x0c \x01(\x04\x12\x12\n\nupdated_at\x18\r \x01(\x04\x12\x0c\n\x04side\x18\x0e \x01(\t\x12\x0e\n\x06market\x18\x0f \x01(\tB\x02P\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,data__types__pb2.DESCRIPTOR,])




_OHLCDATA = _descriptor.Descriptor(
  name='OHLCData',
  full_name='io.lightcone.data.api.common.OHLCData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='open_time', full_name='io.lightcone.data.api.common.OHLCData.open_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='io.lightcone.data.api.common.OHLCData.size', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='io.lightcone.data.api.common.OHLCData.volume', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open', full_name='io.lightcone.data.api.common.OHLCData.open', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close', full_name='io.lightcone.data.api.common.OHLCData.close', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='io.lightcone.data.api.common.OHLCData.high', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='io.lightcone.data.api.common.OHLCData.low', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=101,
  serialized_end=282,
)


_TICKER = _descriptor.Descriptor(
  name='Ticker',
  full_name='io.lightcone.data.api.common.Ticker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='io.lightcone.data.api.common.Ticker.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='io.lightcone.data.api.common.Ticker.size', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open', full_name='io.lightcone.data.api.common.Ticker.open', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='io.lightcone.data.api.common.Ticker.high', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='io.lightcone.data.api.common.Ticker.low', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last', full_name='io.lightcone.data.api.common.Ticker.last', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='io.lightcone.data.api.common.Ticker.count', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bid', full_name='io.lightcone.data.api.common.Ticker.bid', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ask', full_name='io.lightcone.data.api.common.Ticker.ask', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=285,
  serialized_end=455,
)


_BALANCE = _descriptor.Descriptor(
  name='Balance',
  full_name='io.lightcone.data.api.common.Balance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='io.lightcone.data.api.common.Balance.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='io.lightcone.data.api.common.Balance.balance', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lock', full_name='io.lightcone.data.api.common.Balance.lock', index=2,
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
  serialized_start=457,
  serialized_end=578,
)


_DEPTHITEM = _descriptor.Descriptor(
  name='DepthItem',
  full_name='io.lightcone.data.api.common.DepthItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='io.lightcone.data.api.common.DepthItem.price', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='io.lightcone.data.api.common.DepthItem.size', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='io.lightcone.data.api.common.DepthItem.volume', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='io.lightcone.data.api.common.DepthItem.count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=581,
  serialized_end=718,
)


_TRADE = _descriptor.Descriptor(
  name='Trade',
  full_name='io.lightcone.data.api.common.Trade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='io.lightcone.data.api.common.Trade.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tradeId', full_name='io.lightcone.data.api.common.Trade.tradeId', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='side', full_name='io.lightcone.data.api.common.Trade.side', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='io.lightcone.data.api.common.Trade.size', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='io.lightcone.data.api.common.Trade.price', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=720,
  serialized_end=839,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='io.lightcone.data.api.common.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='io.lightcone.data.api.common.Order.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientOrderId', full_name='io.lightcone.data.api.common.Order.clientOrderId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='io.lightcone.data.api.common.Order.size', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='io.lightcone.data.api.common.Order.volume', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='io.lightcone.data.api.common.Order.price', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filled_size', full_name='io.lightcone.data.api.common.Order.filled_size', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filled_volume', full_name='io.lightcone.data.api.common.Order.filled_volume', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filled_fee', full_name='io.lightcone.data.api.common.Order.filled_fee', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='io.lightcone.data.api.common.Order.status', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_since', full_name='io.lightcone.data.api.common.Order.valid_since', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_until', full_name='io.lightcone.data.api.common.Order.valid_until', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='io.lightcone.data.api.common.Order.created_at', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='io.lightcone.data.api.common.Order.updated_at', index=12,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='side', full_name='io.lightcone.data.api.common.Order.side', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market', full_name='io.lightcone.data.api.common.Order.market', index=14,
      number=15, type=9, cpp_type=9, label=1,
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
  serialized_start=842,
  serialized_end=1288,
)

_OHLCDATA.fields_by_name['size'].message_type = data__types__pb2._AMOUNT
_OHLCDATA.fields_by_name['volume'].message_type = data__types__pb2._AMOUNT
_TICKER.fields_by_name['size'].message_type = data__types__pb2._AMOUNT
_BALANCE.fields_by_name['balance'].message_type = data__types__pb2._AMOUNT
_BALANCE.fields_by_name['lock'].message_type = data__types__pb2._AMOUNT
_DEPTHITEM.fields_by_name['size'].message_type = data__types__pb2._AMOUNT
_DEPTHITEM.fields_by_name['volume'].message_type = data__types__pb2._AMOUNT
_TRADE.fields_by_name['size'].message_type = data__types__pb2._AMOUNT
_ORDER.fields_by_name['size'].message_type = data__types__pb2._AMOUNT
_ORDER.fields_by_name['volume'].message_type = data__types__pb2._AMOUNT
_ORDER.fields_by_name['filled_size'].message_type = data__types__pb2._AMOUNT
_ORDER.fields_by_name['filled_volume'].message_type = data__types__pb2._AMOUNT
_ORDER.fields_by_name['filled_fee'].message_type = data__types__pb2._AMOUNT
DESCRIPTOR.message_types_by_name['OHLCData'] = _OHLCDATA
DESCRIPTOR.message_types_by_name['Ticker'] = _TICKER
DESCRIPTOR.message_types_by_name['Balance'] = _BALANCE
DESCRIPTOR.message_types_by_name['DepthItem'] = _DEPTHITEM
DESCRIPTOR.message_types_by_name['Trade'] = _TRADE
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OHLCData = _reflection.GeneratedProtocolMessageType('OHLCData', (_message.Message,), {
  'DESCRIPTOR' : _OHLCDATA,
  '__module__' : 'data_api_common_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.data.api.common.OHLCData)
  })
_sym_db.RegisterMessage(OHLCData)

Ticker = _reflection.GeneratedProtocolMessageType('Ticker', (_message.Message,), {
  'DESCRIPTOR' : _TICKER,
  '__module__' : 'data_api_common_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.data.api.common.Ticker)
  })
_sym_db.RegisterMessage(Ticker)

Balance = _reflection.GeneratedProtocolMessageType('Balance', (_message.Message,), {
  'DESCRIPTOR' : _BALANCE,
  '__module__' : 'data_api_common_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.data.api.common.Balance)
  })
_sym_db.RegisterMessage(Balance)

DepthItem = _reflection.GeneratedProtocolMessageType('DepthItem', (_message.Message,), {
  'DESCRIPTOR' : _DEPTHITEM,
  '__module__' : 'data_api_common_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.data.api.common.DepthItem)
  })
_sym_db.RegisterMessage(DepthItem)

Trade = _reflection.GeneratedProtocolMessageType('Trade', (_message.Message,), {
  'DESCRIPTOR' : _TRADE,
  '__module__' : 'data_api_common_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.data.api.common.Trade)
  })
_sym_db.RegisterMessage(Trade)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'data_api_common_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.data.api.common.Order)
  })
_sym_db.RegisterMessage(Order)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)