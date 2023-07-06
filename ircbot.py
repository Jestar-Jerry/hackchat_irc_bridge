import socket
import sys

class bot_irc:

    irc_socket = socket.socket()

    def __init__(self):
        self.irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_irc(self, channel, msg):
        self.irc_socket.send(bytes("PRIVMSG " + channel + " " + msg + "\n", "UTF-8"))

    def connect_irc(self, server, port, bot_nick, bot_pass, bot_nickpass):
        print("Server connection: " + server)
        self.irc_socket.connect((server, port))

        self.irc_socket.send(bytes("USER " + bot_nick + " " + bot_nick +" " + bot_nick + " :python\n", "UTF-8"))
        self.irc_socket.send(bytes("NICK " + bot_nick + "\n", "UTF-8"))
        #self.irc_socket.send(bytes("NICKSERV IDENTIFY " + bot_nickpass + " " + bot_pass + "\n", "UTF-8"))
    
    def join(self,channel):
        self.irc_socket.send(bytes("JOIN " + channel + "\n", "UTF-8"))
        print("join success")

    def response_irc(self):
        r = self.irc_socket.recv(2040).decode("UTF-8")
        if r.find('PING') != -1:
            self.irc_socket.send(bytes('PONG ' + r.split()[1] + '\r\n', "UTF-8"))
        return r
