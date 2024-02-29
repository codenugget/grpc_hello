import grpc
from concurrent import futures
import time
import hello_pb2_grpc as pb2_grpc
import hello_pb2 as pb2


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        print(f"Received a message: {message}")
        result = f'Hello I am up and running received "{message}" message from you'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)


def serve(port, max_workers):
    print(f"Starting chat server on port: {port}, with max workers: {max_workers}")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"Server started...")
    print(f"Waiting for termination")
    server.wait_for_termination()


if __name__ == '__main__':
    serve(port=50051, max_workers=10)
