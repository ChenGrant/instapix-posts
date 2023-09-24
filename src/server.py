import os
import sys
from concurrent import futures
import grpc
from post_service import Post


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../protos")))
import post_pb2_grpc


# start grpc server
def start():
    server = grpc.server(futures.ThreadPoolExecutor())
    post_pb2_grpc.add_PostServiceServicer_to_server(Post(), server)
    address = f"{os.environ['DOMAIN']}:{os.environ['PORT']}"
    server.add_insecure_port(address)
    print(f"starting posts server on {address}")
    server.start()
    server.wait_for_termination()
