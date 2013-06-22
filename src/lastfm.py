# -*- coding: utf-8 -*-
import threading
import time
import datetime
import urllib
import scrobbler

"""
last.fm scrobbler
"""
__author__ = "Shigeru Moriya <moriya@sarotti.net>"

class Scrobbler(threading.Thread):
    """
    last.fm scrobbler
    """
    
    def __init__(self, username, password, interval):
        """
        constructor
        """
        threading.Thread.__init__(self)
        self.username = username
        self.password = password
        self.interval = interval
        self.s = scrobbler.Scrobbler(self.username, self.password,
                                     "tst", "1.0")

    def run(self):
        """
        thread runner
        """
        start = time.time()
        self.running = True
        while time.time() - start < self.interval:
            if self.running == False:
                break
            time.sleep(1)
        if self.running == True:
            self.scrobble()
        
    def stop(self):
        self.running = False

    def set_music(self, artist, title):
        self.artist = urllib.parse.quote(artist)
        self.title = urllib.parse.quote(title)
        self.stop()
        
    def scrobble(self):
        self.s.submit(self.artist,self.title, 
                      time.mktime(datetime.datetime.now().timetuple()),
                      "P","","60","")
        

