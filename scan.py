#!/usr/bin/env python3

import sys
import getopt
from multiprocessing import Process
import socket

class Args():
    def __init__(self):
        #host '220.181.57.216' // port ['80','85'] 
        self._host, self._port = self._get_args()
        #print(self._host)
        #print(self._port)
    
    def _get_args(self):
        opts,_  = getopt.getopt(sys.argv[1:],'',['host=','port='])
        
        for opt_name,opt_value in opts:
            if opt_name in ['--host']:
            
                host = opt_value
            if opt_name in ['--port']:
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
        start_port = int(args.port_path[0])
        end_port =int(args.port_path[1])

        for port in range(start_port,end_port):
            address_tuple = (args.host_path,port)
            tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpSock.settimeout(0.1)
            try:
                tcpSock.connect(address_tuple)
                print('{} open'.format(port))
            except socket.error:
                print('{} closed'.format(port))
            
            tcpSock.close()
           
def main():

    scanf = Scanf()
    scanf.start()
    scanf.join()

if __name__ == '__main__':
    main()
