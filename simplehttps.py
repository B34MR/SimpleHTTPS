#!/usr/bin/env python2
import BaseHTTPServer, SimpleHTTPServer
import os, argparse, ssl
from argparse import RawTextHelpFormatter
# from Arguments import *
App = ' SimpleHTTPS'
Version = ' v1.05012017'
Author = 'Nick Sanzotta/@Beamr'
# Colors
class colors:
   white = "\033[1;37m"
   normal = "\033[0;00m"
   red = "\033[1;31m"
   blue = "\033[1;34m"
   green = "\033[1;32m"
   lightblue = "\033[0;34m"
# Symbols
def blue(symbol):
  blue_info = ' [' + colors.blue + symbol + colors.normal + '] ' + colors.normal
  return str(blue_info)
def green(symbol):
  green_info = ' [' + colors.green + symbol + colors.normal + '] ' + colors.normal
  return str(green_info)
def red(symbol):
  red_bang = ' [' + colors.red + symbol + colors.normal + '] ' + colors.normal
  return str(red_bang)
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
# Banner
def banner():
  banner = colors.red + '\n' + App + Version \
  + colors.normal + '\n Description: Quick and dirty HTTPS Python Server.' + '\n'\
  + colors.normal + ' Created by: ' + Author + '\n'\
  + colors.normal + ' ' + '*' * 79 +'\n' + colors.normal
  print(banner)

def parse_args():
	''' CLI Argument Options'''
	cls()
	# Custom Usage
	msg = """simplehttps.py <SERVER> <PORT>
	Example: python simplehttps.py 127.0.0.1 -p 443
         [-s, Define Server ex: -s 127.0.0.1]
         [-p, Define HTTP Server port ex: -p 443]
        """
	# Create Parser
	parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=' '+
		str(banner()), usage=msg)	
	# Server Argument Group
	server_group = parser.add_argument_group(colors.green + 'Server options' + colors.normal)
	server_group.add_argument('-s','--server', type=str, metavar='Default [127.0.0.1]', default='127.0.0.1',
		help='')
	server_group.add_argument('-p','--port', type=int, metavar='Default [443]', nargs='?', const=1, default = 443,
		help='')
	# SSL Cert Argument Group
	SSLCert_group = parser.add_argument_group(colors.green + 'SSL Cert options' + colors.normal)
	SSLCert_group.add_argument('-cn','--country', type=str, metavar='Default [US]', default='US',
		help='')
	SSLCert_group.add_argument('-st','--state', type=str, metavar='Default [DEL]', default = 'DEL',
		help='')
	SSLCert_group.add_argument('-c','--city', type=str, metavar='Default [DOVER]', default = 'DOVER',
		help='')	
	SSLCert_group.add_argument('-comp','--company', type=str, metavar='Default [Company Inc]', default = 'Company Inc',
		help='')
	SSLCert_group.add_argument('-ou','--orgUnit', type=str, metavar='Default [IT]', default = 'IT',
		help='')
	SSLCert_group.add_argument('-d', '--fqdn', type=str, metavar='Default [www.myserver.com]', default = 'www.myserver.com',
		help='')
	SSLCert_group.add_argument('-e','--email', type=str, metavar='Default [it@support.com]', default = 'it@support.com',
		help='')
	# Parse/Return the Arguments
	args = parser.parse_args()
	return args

def sslCert(country, state, city, company, orgUnit, fqdn, email):
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
	print(blue('i') + 'SSL Certificate Created:')

def serverHTTPS(server, port):
	directory = 'var/www/'
	if not os.path.exists(directory):
		os.makedirs(directory)
	os.chdir('var/www/')
	# Create SSL Cert
	sslCert(args.country, args.state, args.city, args.company, args.orgUnit, args.fqdn, args.email)
	# Start HTTPS Server
	httpd = BaseHTTPServer.HTTPServer((server, port),
	        SimpleHTTPServer.SimpleHTTPRequestHandler)	
	httpd.socket = ssl.wrap_socket (httpd.socket,
	        keyfile='../../key.pem',
	        certfile='../../cert.pem', server_side=True)
	print(blue('i') + 'HTTPS Server Started: ' + 'https://' + args.server + ':'+ str(args.port))
	httpd.serve_forever()

if __name__ == '__main__':
	args = parse_args()
	serverHTTPS(args.server, args.port)
