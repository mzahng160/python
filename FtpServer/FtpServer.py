from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import configparser

cf = configparser.ConfigParser()
cf.read("ftpCfg.ini")

Dir = cf.get("Setting", 'FtpDir')
Usr = cf.get("Setting", 'FtpUsr')
Psd = cf.get("Setting", 'FtpPsd')


authorizer = DummyAuthorizer()
authorizer.add_user(Usr, Psd, Dir, perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("192.168.1.134", 21), handler)
server.serve_forever()
