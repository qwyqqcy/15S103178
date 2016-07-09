#! /usr/bin/env python
#  Wroten by CY QIN

import socket
import thread
import string


def receive_data (conn, address, file_dict):
  port = conn.recv (1024)
  data = "Default"
  while data:
    data = conn.recv (1024)
    file_list = list (eval(data)) 
    for i in file_list:
      file_dict[i] = (address[0], int (port))
    print file_dict
    data = conn.recv (1024)
    if cmp (data, "exit") is 0:
      break
    if data in file_dict:
      addr = str (file_dict[data]) 
      conn.send (addr)
    else:
      conn.send ("No such file!")
  conn.close ()
  print "Close connection from ", address




if __name__ == '__main__':
  # The list of files
  file_dict = {} 

  # Create a socket    
  server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

  # Set option reused
  server.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  # Bind socket to port
  server_address = ('127.0.0.1', 20000)
  server.bind (server_address)
  server.listen (10)

  # Waiting for connection
  while True:
    connection, addr = server.accept ()
    print "Connection from ", addr

    # Create a thread for connection
    thread.start_new_thread (receive_data, (connection, addr, file_dict)) 
  
  # Close socket
  server.close ()
