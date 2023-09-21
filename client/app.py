from fastapi import FastAPI
# import requests
# import os
import uvicorn
import grpc
import hello_world_pb2
import hello_world_pb2_grpc
from google.protobuf.json_format import MessageToDict


# Create an instance of the FastAPI class
app = FastAPI()

# @app.get("/get_from_rest")
# async def get_from_rest():
#     ret = requests.get(f"http://localhost:10009/")
#     return {"message": ret.json()["message"]}


@app.get("/get_from_grpc")
async def get_from_grpc():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = hello_world_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_world_pb2.HelloRequest())
        ret = MessageToDict(response, including_default_value_fields=True)
    return {"message": ret["message"]}




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10010)