import commands
import SocketServer

def iptoid(ip):
    ret=commands.getoutput("nova list")
    m=ret.splitlines()
    for i in m:
        if(i.find(ip)!=-1):
            return i[2:39]


class UDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data=self.request[0].strip()
        socket=self.request[1]
        addr=self.client_address[0]
        vmid=iptoid(addr)
        #print commands.getoutput("nova delete "+vmid)
        print vmid


if __name__ == "__main__":
        HOST, PORT = "10.40.39.2", 8888
        server = SocketServer.UDPServer((HOST, PORT), UDPHandler)
        server.serve_forever()

