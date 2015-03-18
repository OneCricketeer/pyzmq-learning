import zmq

# ZeroMQ Context
context = zmq.Context()

def get_subscription_socket(context, channels="", srv_addr="127.0.0.1", srv_port=5680):
	# Define the socket using the "Context"
	sock = context.socket(zmq.SUB)

	def set_channels(channels):
		# A single string is given
		if isinstance(channels, basestring):
			sock.setsockopt(zmq.SUBSCRIBE, channels)
		else:
			# A list is given
			for c in channels:
				sock.setsockopt(zmq.SUBSCRIBE, str(c))

	# Define subscription and messages with prefix to accept.
	set_channels(channels)
	sock.connect("tcp://" + srv_addr + ":" + str(srv_port))
	return sock

# Define the socket using the "Context"
sock = get_subscription_socket(context, channels=["1", "3"])

while True:
    message= sock.recv()
    print message