import zmq
import sys

# ZeroMQ Context
context = zmq.Context()

def get_request_socket(context, srv_addr="127.0.0.1", srv_port=5678):
	# Define the socket using the "Context"
    sock = context.socket(zmq.REQ)
    sock.connect("tcp://" + srv_addr + ":" + str(srv_port))
    return sock

sock = get_request_socket(context)

# Send a "message" using the socket
while True:
	message = raw_input('=> ')
	sock.send(message)
	print sock.recv()