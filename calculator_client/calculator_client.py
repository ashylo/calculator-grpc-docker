from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    channel = grpc.insecure_channel('calculator_server:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # asks server to calculate 10 + 5
    response = stub.Calc(
        calculator_pb2.CalcRequest(number_1=10, number_2=5, operation='+'))
    print("Result: ", response.res)

    # asks server to calculate wrong operation
    response1 = stub.Calc(
        calculator_pb2.CalcRequest(number_1=10, number_2=5, operation='[+]'))
    print("Result: ", response1.res)

    # asks server to calculate 10 - 5
    response2 = stub.Calc(
        calculator_pb2.CalcRequest(number_1=10, number_2=5, operation='-'))
    print("Result: ", response2.res)
    channel.close()


if __name__ == '__main__':
    run()
