#!/usr/bin/env python2
import BaseHTTPServer
import SimpleHTTPServer, multiprocessing
import os, ssl, signal
from arguments import *

def sslCert(country, state, city, company, orgUnit, fqdn, email):
	'''Create SSL Cert with Specified Values '''
	cert = """openssl \
	req \
    -nodes \
    -x509\
    -newkey rsa:2048 \
    -keyout ../../key.pem \
    -out ../../cert.pem \
    -days 365\
    -subj "/C={0}/ST={1}/L={2}/O={3}/OU={4}/CN={5}/emailAddress={6}"
	"""
	createCert = cert.format(country, state, city, company, orgUnit, fqdn, email)
	print(createCert)
	os.system(createCert)
	print(blue('*') + 'SSL Certificate Created:')

def serverHTTPS(server, port):
	'''Create SSL Cert and Start HTTPS Server '''
	directory = 'var/www/'
	if not os.path.exists(directory):
		os.makedirs(directory)
	os.chdir('var/www/')
	# Create SSL Cert
	sslCert(args.country, args.state, args.city, args.company, args.orgUnit, args.fqdn, args.email)
	# Configure HTTPS Server
	httpd = BaseHTTPServer.HTTPServer((server, port),
	        SimpleHTTPServer.SimpleHTTPRequestHandler, bind_and_activate=False)
	httpd.allow_reuse_address = True
	httpd.socket = ssl.wrap_socket (httpd.socket,
	        keyfile='../../key.pem',
	        certfile='../../cert.pem', server_side=True)
	print(blue('i') + 'HTTPS Server Started: ' + 'https://' + args.server + ':'+ str(args.port))
	# Start HTTPS Server process
	server_process = multiprocessing.Process(target=httpd.serve_forever)
	server_process.daemon = False
	server_process.start()
	# Obtain HTTPS Server Process ID
	global serverPid
	serverPid=server_process.pid
	# print(blue('i') + 'DEBUG: HTTPS Server running under PID:' + str(serverPid))

if __name__ == '__main__':
	args = parse_args()
	serverHTTPS(args.server, args.port)
	raw_input(red('!') + 'Press Enter to close\n\n')
	# Send the signal terminate HTTPS Serverprocess
	os.kill(os.getpgid(serverPid), signal.SIGTERM)