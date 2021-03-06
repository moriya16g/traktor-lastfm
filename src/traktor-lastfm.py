# -*- coding: utf-8 -*-
import tkinter
import config
import icecast
import lastfm

"""
traktor-lastfm main module
"""
__author__ = "Shigeru Moriya <moriya@sarotti.net>"

class Frame(tkinter.Frame):
    """
    Main Window
    """

    def __init__(self, master=None):
        """
        constructor
        """
        tkinter.Frame.__init__(self, master)
        self.master.title('traktor-lastfm')
        self.master.wm_iconbitmap('icon.ico')

        #status label
        self.label_status = tkinter.Label(self)
        self.label_status.grid(row=0, column=0, columnspan=2, 
                               padx=5, pady=5)
        self.set_label_status_not_running()

        #music label
        self.label_status = tkinter.Label(self)
        self.label_status.grid(row=1, column=0, columnspan=2, 
                               padx=5, pady=5)
        self.set_label_music_not_running()

        #port title label
        self.label_port_title = tkinter.Label(self, text='port')
        self.label_port_title.grid(row=2, column=0, padx=5, pady=5)

        #port label
        self.label_port = tkinter.Label(self, text='9999', 
                                              bg='LightGray',
                                              relief=tkinter.RIDGE, bd=2)
        self.label_port.grid(row=2, column=1, padx=5, pady=5)
        
        #last.fm username title label
        self.label_lastfm_username_title = tkinter.Label(self, 
                                                         text='Last.fm username')
        self.label_lastfm_username_title.grid(row=3, column=0, padx=5, pady=5)

        #last.fm username label
        self.label_lastfm_username = tkinter.Label(self, text='username', 
                                              bg='LightGray',
                                              relief=tkinter.RIDGE, bd=2)
        self.label_lastfm_username.grid(row=3, column=1, padx=5, pady=5)

        #last.fm checkbutton frame
        self.frame_lastfm_checkbutton_frame = tkinter.Frame(self)
        self.frame_lastfm_checkbutton_frame.grid(row=3, column=2, padx=5, pady=5)

        #last.fm checkbutton
        self.var_checkbutton_lastfm = tkinter.BooleanVar()
        self.var_checkbutton_lastfm.set(True)
        self.checkbutton_lastfm = tkinter.Checkbutton(self.frame_lastfm_checkbutton_frame,
                                                      variable=self.var_checkbutton_lastfm).pack()
        
        
####################################################################
        self.lastfm = lastfm.Scrobbler("username", "password", 60)
####################################################################

    def set_label_status_not_running(self):
        """
        set 'not running' to status label
        """
        self.label_status.configure(text=' not running ', bg='yellow',
                                    relief=tkinter.RIDGE, bd=2)

    def set_label_status_running(self):
        """
        set 'running' to status label
        """
        self.label_status.configure(text='   running   ',
                                    bg='LightSkyBlue', bd=2)

    def set_label_music_not_running(self):
        """
        set 'not running' to music label
        """
        self.label_status.configure(text=
                            '------------------- / ---------------------')

    def set_label_music_running(self, artist, title):
        """
        set 'running' to music label
        """
        self.lastfm.stop()
        self.artist = artist
        self.title = title
        self.label_status.configure(text=self.title + " / " + self.artist)
        self.lastfm.set_music(self.artist, self.title)
        self.lastfm.run()

    def set_label_port(self, port):
        """
        set port label
        """
        self.label_port.configure(text=str(port))

if __name__ == '__main__':
    conf = config.Config("setting.ini")
    app = Frame()
    app.pack()
    app.set_label_port(conf.get_port())
    server = icecast.Server(conf.get_port(), app.set_label_music_running)
    server.start()
    app.mainloop()
