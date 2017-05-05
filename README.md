# SimpleHTTPS
    Quick and dirty HTTPS Python Server.

# Usage:
     Most Basic Usage: python simplehttps.py (default server:127.0.0.1, port:443)
     
     Options:
     python simplehttps.py --server 127.0.0.1 --port 443
     python simplehttps.py --server 127.0.0.1 --port 443 -d www.myserver.com

     
     Note: HTTPS server runs in SimpleHTTPS/var/www/


    Example:
             SimpleHTTPS v1.05052017
             Description: Quick and dirty HTTPS Python Server.
             Created by: Nick Sanzotta/@Beamr
             *******************************************************************************
             writing new private key to '../../key.pem'
             -----
             [*] SSL Certificate Created:
             [i] HTTPS Server Started: https://127.0.0.1:443
             [!] Press Enter to close
             ----------------------------------------

# Help
    optional arguments:
      -h, --help            show this help message and exit

    Server options:
      -s Default [127.0.0.1], --server Default [127.0.0.1]
      -p [Default [443]], --port [Default [443]]

    SSL Cert options:
      -cn Default [US], --country Default [US]
      -st Default [DEL], --state Default [DEL]
      -c Default [DOVER], --city Default [DOVER]
      -comp Default [Company Inc], --company Default [Company Inc]
      -ou Default [IT], --orgUnit Default [IT]
      -d Default [www.myserver.com], --fqdn Default [www.myserver.com]
      -e Default [it@support.com], --email Default [it@support.com]



 
 
