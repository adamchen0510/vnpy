# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_committer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import data_types_pb2 as data__types__pb2
import ethereum_pb2 as ethereum__pb2
import service_blockchain_delegate_pb2 as service__blockchain__delegate__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service_committer.proto',
  package='io.lightcone.services.comitter_service',
  syntax='proto3',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\x17service_committer.proto\x12&io.lightcone.services.comitter_service\x1a\x10\x64\x61ta_types.proto\x1a\x0e\x65thereum.proto\x1a!service_blockchain_delegate.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xc4\x02\n\x07\x42lockTx\x12\x0f\n\x07tx_hash\x18\x01 \x01(\t\x12\x0c\n\x04\x66rom\x18\x02 \x01(\t\x12\n\n\x02to\x18\x03 \x01(\t\x12\x14\n\x0c\x62lock_number\x18\x04 \x01(\x03\x12\x0b\n\x03gas\x18\x05 \x01(\t\x12\x10\n\x08gasPrice\x18\x06 \x01(\t\x12\r\n\x05value\x18\x07 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x08 \x01(\t\x12\r\n\x05nonce\x18\t \x01(\x03\x12/\n\x06status\x18\n \x01(\x0e\x32\x1f.io.lightcone.ethereum.TxStatus\x12\x11\n\tcreate_at\x18\x0b \x01(\x03\x12\x12\n\nupdated_at\x18\x0c \x01(\x03\x12\x30\n\x07tx_type\x18\r \x01(\x0e\x32\x1f.io.lightcone.data.types.TxType\x12\x12\n\nrequest_id\x18\x0e \x01(\x04\x12\x0f\n\x07version\x18\x0f \x01(\r\"\xdf\x01\n\tSendTxReq\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\x31\n\x08gasLimit\x18\x03 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12\n\n\x02to\x18\x04 \x01(\t\x12\x30\n\x07tx_type\x18\x05 \x01(\x0e\x32\x1f.io.lightcone.data.types.TxType\x12\x12\n\nrequest_id\x18\x06 \x01(\x04\x12\x0f\n\x07version\x18\x07 \x01(\r\"\x82\x01\n\x16GetRecommendedGasPrice\x1ah\n\x03Res\x12\x32\n\tgas_price\x18\x01 \x01(\x0b\x32\x1f.io.lightcone.data.types.Amount\x12-\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1e.io.lightcone.data.types.Error2\x88\x02\n\x10\x43ommitterService\x12~\n\x06sendTx\x12\x31.io.lightcone.services.comitter_service.SendTxReq\x1a\x41.io.lightcone.services.blockchain_delegate.SendRawTransaction.Res\x12t\n\x16getRecommendedGasPrice\x12\x16.google.protobuf.Empty\x1a\x42.io.lightcone.services.comitter_service.GetRecommendedGasPrice.ResB\x02P\x01\x62\x06proto3')
  ,
  dependencies=[data__types__pb2.DESCRIPTOR,ethereum__pb2.DESCRIPTOR,service__blockchain__delegate__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_BLOCKTX = _descriptor.Descriptor(
  name='BlockTx',
  full_name='io.lightcone.services.comitter_service.BlockTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_hash', full_name='io.lightcone.services.comitter_service.BlockTx.tx_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from', full_name='io.lightcone.services.comitter_service.BlockTx.from', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='io.lightcone.services.comitter_service.BlockTx.to', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_number', full_name='io.lightcone.services.comitter_service.BlockTx.block_number', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas', full_name='io.lightcone.services.comitter_service.BlockTx.gas', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gasPrice', full_name='io.lightcone.services.comitter_service.BlockTx.gasPrice', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='io.lightcone.services.comitter_service.BlockTx.value', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='io.lightcone.services.comitter_service.BlockTx.data', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='io.lightcone.services.comitter_service.BlockTx.nonce', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='io.lightcone.services.comitter_service.BlockTx.status', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_at', full_name='io.lightcone.services.comitter_service.BlockTx.create_at', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='io.lightcone.services.comitter_service.BlockTx.updated_at', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_type', full_name='io.lightcone.services.comitter_service.BlockTx.tx_type', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='io.lightcone.services.comitter_service.BlockTx.request_id', index=13,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='io.lightcone.services.comitter_service.BlockTx.version', index=14,
      number=15, type=13, cpp_type=3, label=1,
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
  serialized_start=166,
  serialized_end=490,
)


_SENDTXREQ = _descriptor.Descriptor(
  name='SendTxReq',
  full_name='io.lightcone.services.comitter_service.SendTxReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='io.lightcone.services.comitter_service.SendTxReq.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='io.lightcone.services.comitter_service.SendTxReq.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gasLimit', full_name='io.lightcone.services.comitter_service.SendTxReq.gasLimit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='io.lightcone.services.comitter_service.SendTxReq.to', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_type', full_name='io.lightcone.services.comitter_service.SendTxReq.tx_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='io.lightcone.services.comitter_service.SendTxReq.request_id', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='io.lightcone.services.comitter_service.SendTxReq.version', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=493,
  serialized_end=716,
)


_GETRECOMMENDEDGASPRICE_RES = _descriptor.Descriptor(
  name='Res',
  full_name='io.lightcone.services.comitter_service.GetRecommendedGasPrice.Res',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gas_price', full_name='io.lightcone.services.comitter_service.GetRecommendedGasPrice.Res.gas_price', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='io.lightcone.services.comitter_service.GetRecommendedGasPrice.Res.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=745,
  serialized_end=849,
)

_GETRECOMMENDEDGASPRICE = _descriptor.Descriptor(
  name='GetRecommendedGasPrice',
  full_name='io.lightcone.services.comitter_service.GetRecommendedGasPrice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_GETRECOMMENDEDGASPRICE_RES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=719,
  serialized_end=849,
)

_BLOCKTX.fields_by_name['status'].enum_type = ethereum__pb2._TXSTATUS
_BLOCKTX.fields_by_name['tx_type'].enum_type = data__types__pb2._TXTYPE
_SENDTXREQ.fields_by_name['value'].message_type = data__types__pb2._AMOUNT
_SENDTXREQ.fields_by_name['gasLimit'].message_type = data__types__pb2._AMOUNT
_SENDTXREQ.fields_by_name['tx_type'].enum_type = data__types__pb2._TXTYPE
_GETRECOMMENDEDGASPRICE_RES.fields_by_name['gas_price'].message_type = data__types__pb2._AMOUNT
_GETRECOMMENDEDGASPRICE_RES.fields_by_name['error'].message_type = data__types__pb2._ERROR
_GETRECOMMENDEDGASPRICE_RES.containing_type = _GETRECOMMENDEDGASPRICE
DESCRIPTOR.message_types_by_name['BlockTx'] = _BLOCKTX
DESCRIPTOR.message_types_by_name['SendTxReq'] = _SENDTXREQ
DESCRIPTOR.message_types_by_name['GetRecommendedGasPrice'] = _GETRECOMMENDEDGASPRICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockTx = _reflection.GeneratedProtocolMessageType('BlockTx', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKTX,
  '__module__' : 'service_committer_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.services.comitter_service.BlockTx)
  })
_sym_db.RegisterMessage(BlockTx)

SendTxReq = _reflection.GeneratedProtocolMessageType('SendTxReq', (_message.Message,), {
  'DESCRIPTOR' : _SENDTXREQ,
  '__module__' : 'service_committer_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.services.comitter_service.SendTxReq)
  })
_sym_db.RegisterMessage(SendTxReq)

GetRecommendedGasPrice = _reflection.GeneratedProtocolMessageType('GetRecommendedGasPrice', (_message.Message,), {

  'Res' : _reflection.GeneratedProtocolMessageType('Res', (_message.Message,), {
    'DESCRIPTOR' : _GETRECOMMENDEDGASPRICE_RES,
    '__module__' : 'service_committer_pb2'
    # @@protoc_insertion_point(class_scope:io.lightcone.services.comitter_service.GetRecommendedGasPrice.Res)
    })
  ,
  'DESCRIPTOR' : _GETRECOMMENDEDGASPRICE,
  '__module__' : 'service_committer_pb2'
  # @@protoc_insertion_point(class_scope:io.lightcone.services.comitter_service.GetRecommendedGasPrice)
  })
_sym_db.RegisterMessage(GetRecommendedGasPrice)
_sym_db.RegisterMessage(GetRecommendedGasPrice.Res)


DESCRIPTOR._options = None

_COMMITTERSERVICE = _descriptor.ServiceDescriptor(
  name='CommitterService',
  full_name='io.lightcone.services.comitter_service.CommitterService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=852,
  serialized_end=1116,
  methods=[
  _descriptor.MethodDescriptor(
    name='sendTx',
    full_name='io.lightcone.services.comitter_service.CommitterService.sendTx',
    index=0,
    containing_service=None,
    input_type=_SENDTXREQ,
    output_type=service__blockchain__delegate__pb2._SENDRAWTRANSACTION_RES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getRecommendedGasPrice',
    full_name='io.lightcone.services.comitter_service.CommitterService.getRecommendedGasPrice',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_GETRECOMMENDEDGASPRICE_RES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMITTERSERVICE)

DESCRIPTOR.services_by_name['CommitterService'] = _COMMITTERSERVICE

# @@protoc_insertion_point(module_scope)