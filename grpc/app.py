import grpc
import os
import hello_world_pb2
import hello_world_pb2_grpc
from dotenv import load_dotenv
from google.protobuf.json_format import MessageToDict
from concurrent import futures

load_dotenv()

class Greeter(hello_world_pb2_grpc.GreeterServicer):
    def SayHello(
            self, request: hello_world_pb2.HelloRequest,
            context: grpc.ServicerContext) -> hello_world_pb2.HelloReply:
        return hello_world_pb2.HelloReply(message="Hello, World!")


    # def GetPreHello(
    #         self, 
    #         request: hello_world_pb2.HelloRequest,
    #         context: grpc.ServicerContext) -> hello_world_pb2.HelloReply:

    #     with grpc.insecure_channel(f"hello-world-grpc{int(os.getenv('pod_num')) - 1}:50051") as channel:
    #         stub = hello_world_pb2_grpc.GreeterStub(channel)
    #         response = stub.SayHello()
    #         ret = MessageToDict(response, including_default_value_fields=True)

    #     return hello_world_pb2.HelloReply(message=ret["message"])


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_world_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
