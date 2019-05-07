import socketserver, syslog

class MyTCPHandler(socketserver.BaseRequestHandler):

    working_flag = True

    def handle(self):
        while self.working_flag:
            self.data = self.request.recv(1024)
            if self.data == '':
                break
            self.data = self.data.strip()
            syslog.syslog(syslog.LOG_CRIT, 'chainvu_test data: {0}'.format(self.data))
            # self.request.send(self.data.upper())

            if (self.data == 'led'):
                self.request.send(u'done')
                self.server._BaseServer__shutdown_request = True

if __name__ == "__main__":
    HOST, PORT = "192.168.3.252", 6666
    server = socketserver.c((HOST, PORT), MyTCPHandler)
    server.serve_forever()