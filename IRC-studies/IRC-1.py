import socket

#PASS <a password>
#NICK <a nickname>
#USER <a username> <node> <unused> <a real name>

#Encode it's a method

#Purpose of logging 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Connection
HOST = 'irc.libera.chat'
PORT = 6667
NICK = 'YourNick'

#Stabblish Connection and Authorize server (NICK / USER)
s.connect((HOST, PORT))

nick_data = ('NICK ' + NICK + '\r\n')
s.send(nick_data.encode()) #Send the nick data

unsername_date = ('USER YourNick1 YourNick2 YourNick3 :YourNick4 \r\n') #\r\n instructions
s.send(unsername_date.encode())

#Join the channel
s.send('JOIN #programming \r\n'.encode())
#I sent everything above

#Get what i sent above
while True:
  result = s.recv(1024).decode('utf-8')
  print(result)

  #Respond to the server i'm still online
  if result[0:4] == "PING":
    s.send(("PONG" + result[4:] + "\r\n").encode())
  #Connection is broken/Something is bad and you need to crash 
  if len(result) == 0:
    break
