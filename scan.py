#!/usr/bin/env python3

import getopt
from multiprocessing import Process
from socket import *

class Args():
    def __init__(self):
        #host '220.181.57.216' // port ['80','85'] 
        self._host, self._port = self._get_args()
    
    def _get_args(self)
        opts,_  = getopt.getopt(sys.argv[1:],'',['host=','port='])
        
        for opt_name,opt_value in opts:
            if opt_name in ['--host']:
                host = opt_value
            if opt_name in ['--port']
                port = opt_value.split('-')
        return host,port
    
    @property
    def host_path(self):
        return self._host
        
    @property
    def port_path(self):
        return self._port

args = Args()

class Scanf(Process):
    
    def __init__(self):
        super().__init__()
        
    def run(self):
        #arg.port_path[0] arg.port_path[1]端口起始截止
        for port in range(arg.port_path[0],arg.port_path[1])：
            address_tuple = (arg.host_path,port)
            tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                tcpSock.connect(address_tuple)
            except socket.error:
                print('{} closed'.format(port))
            
            tcpSock.close()
            print('{} open'.format(port)

def main():

    scanf = Scanf()
    scanf.start()
    scanf.join()

if __name__ == '__main__':
    main()
