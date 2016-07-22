import getpass
import os
password = getpass.getpass("Your internet password: ")
string = 'http://%s:%s@proxy.det.nsw.edu.au:8080' % (getpass.getuser(), password)
os.system('git config --global http.proxy ' + string)
os.system('git config --global https.proxy ' + string)
