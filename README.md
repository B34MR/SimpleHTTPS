# SimpleHTTPS
Quick and dirty HTTPS Server for Pentesters.

# Usage:
python simplehttps.py --server 127.0.0.1 --port 443
   
Go through OpenSSL Wizard to generate cert.pem and key.pem files.
Set up a new PEM password, enter Country Name, State, etc ..


   SimpleHTTPS v1.05012017
   Description: Quick and dirty HTTPS for Pentesters.
   Created by: Nick Sanzotta/@Beamr
   *******************************************************************************

  Generating a 2048 bit RSA private key
  ........+++
  ...............+++
  writing new private key to '../../key.pem'
  Enter PEM pass phrase:
  Verifying - Enter PEM pass phrase:
  -----
  You are about to be asked to enter information that will be incorporated
  into your certificate request.
  What you are about to enter is what is called a Distinguished Name or a DN.
  There are quite a few fields but you can leave some blank
  For some fields there will be a default value,
  If you enter '.', the field will be left blank.
  -----
  Country Name (2 letter code) [AU]:US
  State or Province Name (full name) [Some-State]:
  
  ...
  Email Address []:
  Enter PEM pass phrase:

Enter your previous PEM password to start HTTPS server.


 
 
