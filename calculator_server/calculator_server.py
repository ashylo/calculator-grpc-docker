from concurrent import futures

import grpc

import calculator_pb2
import calculator_pb2_grpc

import calculator as c


class Calculator(calculator_pb2_grpc.CalculatorServicer):

    def Calc(self, request, context):
        result = c.calc(
                    request.number_1, 
                    request.number_2, 
                    request.operation)
        if result is None:
            return calculator_pb2.CalcReply(res='None')
        else:
            return calculator_pb2.CalcReply(res=str(result))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
