# -*- coding: utf-8 -*-
import Tkinter
import config
import icecast

"""
traktor-lastfm main module
"""
__author__ = "Shigeru Moriya <moriya@sarotti.net>"

class Frame(Tkinter.Frame):
    """
    Main Window
    """

    def __init__(self, master=None):
        """
        constructor
        """
        Tkinter.Frame.__init__(self, master)
        self.master.title('traktor-lastfm')
        self.master.wm_iconbitmap('icon.ico')

        #status label
        self.label_status = Tkinter.Label(self)
        self.label_status.grid(row=0, column=0, columnspan=2, 
                               padx=5, pady=5)
        self.set_label_status_not_running()

        #music label
        self.label_status = Tkinter.Label(self)
        self.label_status.grid(row=1, column=0, columnspan=2, 
                               padx=5, pady=5)
        self.set_label_music_not_running()

        #port title label
        self.label_port_title = Tkinter.Label(self, text='port')
        self.label_port_title.grid(row=2, column=0, padx=5, pady=5)

        #port label
        self.label_port = Tkinter.Label(self, text='9999', 
                                              bg='LightGray',
                                              relief=Tkinter.RIDGE, bd=2)
        self.label_port.grid(row=2, column=1, padx=5, pady=5)
        
        #last.fm username title label
        self.label_lastfm_username_title = Tkinter.Label(self, 
                                                         text='Last.fm username')
        self.label_lastfm_username_title.grid(row=3, column=0, padx=5, pady=5)

        #last.fm username label
        self.label_lastfm_username = Tkinter.Label(self, text='username', 
                                              bg='LightGray',
                                              relief=Tkinter.RIDGE, bd=2)
        self.label_lastfm_username.grid(row=3, column=1, padx=5, pady=5)

        #last.fm checkbutton frame
        self.frame_lastfm_checkbutton_frame = Tkinter.Frame(self)
        self.frame_lastfm_checkbutton_frame.grid(row=3, column=2, padx=5, pady=5)

        #last.fm checkbutton
        self.var_checkbutton_lastfm = Tkinter.BooleanVar()
        self.var_checkbutton_lastfm.set(True)
        self.checkbutton_lastfm = Tkinter.Checkbutton(self.frame_lastfm_checkbutton_frame,
                                                      variable=self.var_checkbutton_lastfm).pack()      


    def set_label_status_not_running(self):
        """
        set 'not running' to status label
        """
        self.label_status.configure(text=' not running ', bg='yellow',
                                    relief=Tkinter.RIDGE, bd=2)

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

    def set_label_music_running(self, music):
        """
        set 'running' to music label
        """
        self.label_status.configure(text=music)

    def set_label_port(self, port):
        """
        set port label
        """
        self.label_port.configure(text=str(port))


if __name__ == '__main__':
    conf = config.Config("setting.ini")
    server = icecast.Server(conf.get_port())
    server.start()
    app = Frame()
    app.pack()
    app.set_label_port(conf.get_port())
    app.mainloop()
