import zmq
import time

# ZeroMQ Context
context = zmq.Context()

def get_reply_socket(context, srv_addr="127.0.0.1", srv_port = 5678):
	sock = context.socket(zmq.REP)
	sock.bind("tcp://" + srv_addr + ":" + str(srv_port))
	return sock

def get_publish_socket(context, srv_addr="127.0.0.1", srv_port = 5680):
	sock = context.socket(zmq.PUB)
	sock.bind("tcp://" + srv_addr + ":" + str(srv_port))
	return sock

# listens
rep_sock = get_reply_socket(context)
# publishes
pub_sock = get_publish_socket(context)

print "Listening for messages..."
while True:
	# listen for message
    message = rep_sock.recv()
    print "Publishing message \"" + message + "\""
    # forward to subscribers
    pub_sock.send(message)

    # Echo back to message client
    time.sleep(1)
    rep_sock.send("Sent \"" + message + "\"")