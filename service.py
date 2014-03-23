#!/usr/bin/env python
import SocketServer
import  time
		
class TCP_server(SocketServer.BaseRequestHandler):
	"""docstring for TCP_server"""

	def rev_file(self,filename):
		f = open(filename, 'wb')
		self.request.send('ready...')
		while True:
			data = self.request.recv(4096)
			if not data:
				print "recv file success!"
				break
			f.write(data)
		f.close()
	def send_file(self, filename):
		print "starting send file!"
		#self.request.send('ready....')
		time.sleep(1)
		f = open(filename, 'rb')
		while True:
			data = f.read(4096)
			if not data:
				break
			print 'send....'
			self.request.send(data)
		print 'send ok'
		f.close()
		time.sleep(1)
		#self.request.send('EOF')
		print "send file success!"
	def handle(self):
		print "get connection from :",self.client_address
		while True:
			try:
				data = self.request.recv(4096)
				print "get data:", data  
				if not data:
					print "break the connection!"
					break;
				else:
					action, filename = data.split()
					if action == "put":
						self.rev_file(filename)
					elif action == 'get':
						self.send_file(filename)
					else:
						print "get error!"
						continue
			except Exception,e:
				print "get error at:",e
if __name__ == "__main__":
	host,port = 'localhost',9511
	s = SocketServer.ThreadingTCPServer((host,port), TCP_server)
	s.serve_forever()
