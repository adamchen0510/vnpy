# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import data_requests_pb2 as data__requests__pb2
import db_service_offchain_withdrawals_pb2 as db__service__offchain__withdrawals__pb2
import db_service_request_common_pb2 as db__service__request__common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


class OffchainWithdrawalsDBServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.receiveRequest = channel.unary_unary(
        '/io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService/receiveRequest',
        request_serializer=data__requests__pb2.OffchainWithdrawalRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.getRequestsToProcess = channel.unary_unary(
        '/io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService/getRequestsToProcess',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.getRequestNonce = channel.unary_unary(
        '/io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService/getRequestNonce',
        request_serializer=db__service__request__common__pb2.GetRequestNonceReq.SerializeToString,
        response_deserializer=db__service__request__common__pb2.GetRequestNonceRes.FromString,
        )
    self.getUserRequests = channel.unary_unary(
        '/io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService/getUserRequests',
        request_serializer=db__service__request__common__pb2.GetUserRequestsReq.SerializeToString,
        response_deserializer=db__service__offchain__withdrawals__pb2.GetUserRequestsRes.FromString,
        )
    self.getStats = channel.unary_unary(
        '/io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService/getStats',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=db__service__request__common__pb2.RequestStats.FromString,
        )
    self.cancelAccountPendingOffchainRequests = channel.unary_unary(
        '/io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService/cancelAccountPendingOffchainRequests',
        request_serializer=db__service__request__common__pb2.CancelAccountPendingOffchainRequestsReq.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.releaseFreezeRepeatJob = channel.unary_unary(
        '/io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService/releaseFreezeRepeatJob',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.getByBlockId = channel.unary_unary(
        '/io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService/getByBlockId',
        request_serializer=db__service__request__common__pb2.GetByBlockIdReq.SerializeToString,
        response_deserializer=db__service__request__common__pb2.GetByBlockIdRes.FromString,
        )
    self.updateTxHashes = channel.unary_unary(
        '/io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService/updateTxHashes',
        request_serializer=db__service__request__common__pb2.UpdateTxHashesReq.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString,
        )
    self.finishDistributed = channel.unary_unary(
        '/io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService/finishDistributed',
        request_serializer=db__service__request__common__pb2.FinishDistributedReq.SerializeToString,
        response_deserializer=db__service__request__common__pb2.FinishDistributedRes.FromString,
        )


class OffchainWithdrawalsDBServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def receiveRequest(self, request, context):
    """save the offchain withdraw request when just received but ignore the enclosed receipt object.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRequestsToProcess(self, request, context):
    """schedule job, find requests to process
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRequestNonce(self, request, context):
    """return account's next effective nonce in request
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUserRequests(self, request, context):
    """-- For frontends --
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getStats(self, request, context):
    """-- For Internal --
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def cancelAccountPendingOffchainRequests(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def releaseFreezeRepeatJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getByBlockId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateTxHashes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def finishDistributed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OffchainWithdrawalsDBServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'receiveRequest': grpc.unary_unary_rpc_method_handler(
          servicer.receiveRequest,
          request_deserializer=data__requests__pb2.OffchainWithdrawalRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'getRequestsToProcess': grpc.unary_unary_rpc_method_handler(
          servicer.getRequestsToProcess,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'getRequestNonce': grpc.unary_unary_rpc_method_handler(
          servicer.getRequestNonce,
          request_deserializer=db__service__request__common__pb2.GetRequestNonceReq.FromString,
          response_serializer=db__service__request__common__pb2.GetRequestNonceRes.SerializeToString,
      ),
      'getUserRequests': grpc.unary_unary_rpc_method_handler(
          servicer.getUserRequests,
          request_deserializer=db__service__request__common__pb2.GetUserRequestsReq.FromString,
          response_serializer=db__service__offchain__withdrawals__pb2.GetUserRequestsRes.SerializeToString,
      ),
      'getStats': grpc.unary_unary_rpc_method_handler(
          servicer.getStats,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=db__service__request__common__pb2.RequestStats.SerializeToString,
      ),
      'cancelAccountPendingOffchainRequests': grpc.unary_unary_rpc_method_handler(
          servicer.cancelAccountPendingOffchainRequests,
          request_deserializer=db__service__request__common__pb2.CancelAccountPendingOffchainRequestsReq.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'releaseFreezeRepeatJob': grpc.unary_unary_rpc_method_handler(
          servicer.releaseFreezeRepeatJob,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'getByBlockId': grpc.unary_unary_rpc_method_handler(
          servicer.getByBlockId,
          request_deserializer=db__service__request__common__pb2.GetByBlockIdReq.FromString,
          response_serializer=db__service__request__common__pb2.GetByBlockIdRes.SerializeToString,
      ),
      'updateTxHashes': grpc.unary_unary_rpc_method_handler(
          servicer.updateTxHashes,
          request_deserializer=db__service__request__common__pb2.UpdateTxHashesReq.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString,
      ),
      'finishDistributed': grpc.unary_unary_rpc_method_handler(
          servicer.finishDistributed,
          request_deserializer=db__service__request__common__pb2.FinishDistributedReq.FromString,
          response_serializer=db__service__request__common__pb2.FinishDistributedRes.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'io.lightcone.services.offchain_withdrawals_db_service.OffchainWithdrawalsDBService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))