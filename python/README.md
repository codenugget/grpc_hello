## 1 create environment "grpc_hello" in i.e. conda
conda env create -f environment.yml

## 2 switch
conda activate grpc_hello

## 3 build service code for both server and client
Windows: python -m grpc_tools.protoc --proto_path=..\contracts ..\contracts\hello.proto --python_out=. --grpc_python_out=.
Linux: python -m grpc_tools.protoc --proto_path=../contracts ../contracts/hello.proto --python_out=. --grpc_python_out=.

## 4 Start server in one terminal (with conda env activated)
python server.py


## 5 Test with client in another terminal (with conda env activated)
python client.py


Press Ctrl+C to kill the server when done.
