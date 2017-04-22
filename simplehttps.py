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
  + colors.normal + '\n Description: Quick and dirty HTTPS for Pentesters.' + '\n'\
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
	# Positional Arguments
	server_group = parser.add_argument_group(colors.green + 'Server options' + colors.normal)
	
	server_group.add_argument('-s','--server', type=str, metavar='Server [127.0.0.1]', required=True,
		help='Define HTTP Server IP ex: -s 127.0.0.1')

	server_group.add_argument('-p','--port', type=int, metavar='Port [443]', nargs='?', const=1, default = 443, required=True,
		help='Define HTTP Server Port ex: -p 443')
	# Parse/Return the Arguments
	args = parser.parse_args()
	return args

def serverHTTPS(server, port):
	os.system('openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365')
	httpd = BaseHTTPServer.HTTPServer((server, port),
	        SimpleHTTPServer.SimpleHTTPRequestHandler)	
	httpd.socket = ssl.wrap_socket (httpd.socket,
	        keyfile='key.pem',
	        certfile='cert.pem', server_side=True)	
	httpd.serve_forever()

def main():
	args = parse_args()
	server = args.server
	port = args.port
	serverHTTPS(server, port)

if __name__ == '__main__':
	main()