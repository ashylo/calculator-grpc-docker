# Simple Calculator using gRPC and Python wrapped in Docker.

Simple POC of calculator that demonstrates communication between Docker containers using gRPC and Protobuf.


## Quick start

```shell
git clone https://github.com/ashylo/calculator-grpc-docker.git
cd calculator-grpc-docker
docker-compose up
```


## Project structure

```
.
├── calculator_client/
│   ├── calculator_client.py        # grpc calculator client
│   ├── calculator_pb2.py           # generated request and response classes
│   ├── calculator_pb2_grpc.py      # generated client and server classes
│   └── requirements.txt            # required dependencies for container
├── calculator_server/
│   ├── calculator.py               # calculator module
│   ├── calculator_pb2.py           # generated request and response classes
│   ├── calculator_pb2_grpc.py      # generated client and server classes
│   ├── calculator_server.py        # grpc calculator server
│   ├── requirements.txt            # required dependencies for container
│   └── test_calculator.py          # pytest tests for calculator module
├── Dockerfile.calculator_client    # conatiner configuration for client
├── Dockerfile.calculator_server    # conatiner configuration for server
├── calculator.proto                # protobuf definition
└── docker-compose.yml              # configuration for docker compose that is required to run multiple containers
```