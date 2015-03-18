import zmq
import sys, os, time
import logging

def get_subscription_socket(context, message_filter="", srv_addr="127.0.0.1", srv_port=5680):
	# Define the socket using the "Context"
	sock = context.socket(zmq.SUB)

	# Define subscription and messages with prefix to accept.
	sock.setsockopt(zmq.SUBSCRIBE, message_filter)
	sock.connect("tcp://" + srv_addr + ":" + str(srv_port))
	
	log_message("Listening on " + srv_addr + " at port " + str(srv_port), "messages.log")
	return sock

def log_message(msg, file_name="messages.log", timestamp=True, closefile=False):
	# global filename
	# if file_name != filename:
	# 	filename = file_name
	
	now = get_timestamp()
	with open("messages.log", 'a+') as f:
		if timestamp:
			msg = now + "\t" + msg
		f.write(msg + "\n")
		f.flush()
		os.fsync(f)
		if closefile:
			f.close()
		    

def get_timestamp():
	return time.strftime("[%Y-%m-%d %H:%M:%S]")

def main():	
	# ZeroMQ Context
	context = zmq.Context()

	sock = get_subscription_socket(context, "")
	
	while True:
		message = sock.recv()

		time.sleep(1)
		log_message(message, "messages.log")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        log_message('Closing', "messages.log", True, True)
        try:
        	sys.exit(0)
        except SystemExit:
        	os._exit(0)
