# -*- coding: utf-8 -*-
import threading
import socket
import re
from struct import *

"""
Icecast server for receiving the song information from Traktor
"""
__author__ = "Shigeru Moriya <moriya@sarotti.net>"

class Server(threading.Thread):
    """
    Icecast server
    """

    def __init__(self, port):
        """
        constructor

        port -- number of port
        """
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.host = ''
        self.port = port
        # start server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(5)
        
    def run(self):
        """
        thread runner
        """
        self.conn, self.addr = self.s.accept()
        self.running = True
        while 1:
            data = self.conn.recv(65535)
            if data.find('ice') != -1:
                self.conn.sendall("HTTP/1.0 200 OK\r\n\r\n")
            if re.search(b'(....)ARTIST=(.*)', data):
                self.artist = re.search(b'(....)ARTIST=(.*)', data)
                length = unpack('l', self.artist.group(1))[0] - 7
                self.artist = (self.artist.group(2))[0:length]
                print "ARTIST:" + self.artist
            if re.search(b'(....)TITLE=(.*)', data):
                self.title = re.search(b'(....)TITLE=(.*)', data)
                length = unpack('l', self.title.group(1))[0] - 6
                self.title = (self.title.group(2))[0:length]
                print "TITLE:" + self.title
            if self.running == False:
                break

    def stop(self):
        self.running = False
        self.conn.close()

    def get_artist(self):
        """
        return artist
        """
        return self.artist

    def get_title(self):
        """
        return title
        """
        return self.titile

if __name__ == "__main__":
    server = Server(9999)
    server.start()
    while 1:
        a = ''
