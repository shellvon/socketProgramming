#!/usr/bin/env python

import socket
import sys,time

ip,port = 'localhost',9511
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def rev_file(filename):
	f = open('%s.bak'%filename,'wb')
	
	while True:
		data = s.recv(4096)
		if not data:
			print 'ok'
			break
		f.write(data)
	f.close()
	time.sleep(1)
	
	print 'ok....'
def send_file(filename):
	pass
try:
	s.connect((ip,port))
	while True:
		command = raw_input('shellvon:>>')
		if not command:
			continue
		action,filename = command.split()
		if action=='get':
			print 'try to get file'
			s.sendall(command)
			rev_file(filename)
		elif action="put":
			print 'try to put file'
			s.sendall(command)
			send_file(filename)

except socket.error,e:
	print "get error as",e
finally:
	s.close()