# -*- coding: utf-8 -*-
import ConfigParser
import os

"""
configuration file manager
"""
__author__ = "Shigeru Moriya <moriya@sarotti.net>"

class Config(object):
    """
    configuration file manager
    """

    def __init__(self, filename):
        """
        constructor

        filename -- configuration file name
        """
        self.file = os.path.join(os.path.dirname(__file__), filename)
        # check for the existence of the configiration file
        if not os.path.exists(self.file):
            self.create()
        

    def create(self):
        """
        create the configuration file
        """
        ini = ConfigParser.SafeConfigParser()
        
        ini.add_section('server')
        ini.set('server', 'port', '')
        ini.add_section('lastfm')
        ini.set('lastfm', 'username', '')
        ini.set('lastfm', 'password', '')

        f = open(self.file, 'w')
        ini.write(f)
        f.close()

    def set_port(self, port):
        """
        set port to the configuration file
        
        port -- number of port
        """
        ini = ConfigParser.SafeConfigParser()
        ini.read(self.file)

        if not port.isdigit():
            return 0

        ini.set('server', 'port', port)

        f = open(self.file, 'w')
        ini.write(f)
        f.close()
        return int(port)

    def get_port(self):
        """
        return port from the configparser file
        """
        ini = ConfigParser.SafeConfigParser()
        ini.read(self.file)

        port = ini.get('server', 'port')
        if not port.isdigit():
            self.set_port('0')
            return 0

        return int(port)

    def set_lastfm_username(self, username):
        """
        set username of last.fm to the configuration file
        
        username -- username
        """
        ini = ConfigParser.SafeConfigParser()
        ini.read(self.file)

        ini.set('lastfm', 'username', username)

        f = open(self.file, 'w')
        ini.write(f)
        f.close()

    def get_lastfm_username(self):
        """
        return username of last.fm from the configparser file
        """
        ini = ConfigParser.SafeConfigParser()
        ini.read(self.file)

        username = ini.get('lastfm', 'username')

        return username

    def set_lastfm_password(self, password):
        """
        set password of last.fm to the configuration file
        
        username -- username
        """
        ini = ConfigParser.SafeConfigParser()
        ini.read(self.file)

        ini.set('lastfm', 'password', password)

        f = open(self.file, 'w')
        ini.write(f)
        f.close()

    def get_lastfm_password(self):
        """
        return password of last.fm from the configparser file
        """
        ini = ConfigParser.SafeConfigParser()
        ini.read(self.file)

        password = ini.get('lastfm', 'password')

        return password
