# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import calculator_pb2 as calculator__pb2


class CalculatorStub(object):
  """Calculator service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Calc = channel.unary_unary(
        '/Calculator/Calc',
        request_serializer=calculator__pb2.CalcRequest.SerializeToString,
        response_deserializer=calculator__pb2.CalcReply.FromString,
        )


class CalculatorServicer(object):
  """Calculator service definition
  """

  def Calc(self, request, context):
    """Makes calculation on given numbers
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Calc': grpc.unary_unary_rpc_method_handler(
          servicer.Calc,
          request_deserializer=calculator__pb2.CalcRequest.FromString,
          response_serializer=calculator__pb2.CalcReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Calculator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
