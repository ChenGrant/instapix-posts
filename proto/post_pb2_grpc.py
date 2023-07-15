# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import post_pb2 as post__pb2


class PostServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GeneratePosts = channel.unary_stream(
                '/PostService/GeneratePosts',
                request_serializer=post__pb2.GeneratePostsRequest.SerializeToString,
                response_deserializer=post__pb2.GeneratePostResponse.FromString,
                )


class PostServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GeneratePosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GeneratePosts': grpc.unary_stream_rpc_method_handler(
                    servicer.GeneratePosts,
                    request_deserializer=post__pb2.GeneratePostsRequest.FromString,
                    response_serializer=post__pb2.GeneratePostResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PostService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GeneratePosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/PostService/GeneratePosts',
            post__pb2.GeneratePostsRequest.SerializeToString,
            post__pb2.GeneratePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
