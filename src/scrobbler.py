# -*- coding: UTF-8 -*-
import time
import hashlib
import urllib.request

class Scrobbler:
    def __init__(self,user,password,app_id,app_version):
        """Class constructor."""
        self.username=user
        self.password=password
        self.timestamp=int(time.time())
        hasha=hashlib.md5(password.encode())
        self.token=hashlib.md5(((hashlib.md5(self.password.encode()).hexdigest())+str(self.timestamp)).encode()).hexdigest()
        base="http://post.audioscrobbler.com/?hs=true&p=1.2.1"
        base=base+"&c="+str(app_id)+"&v="+str(app_version)+"&"
        self.req=base+"u="+str(self.username)+"&t="+str(self.timestamp)+"&a="+self.token
        response=urllib.request.urlopen(self.req)
        response_data=[s[:-1] for s in response.readlines()]
        if response_data[0]!=b'OK':
            print("error!!!!!!!!!!")
            print(response_data[0]);
            pass
        else:
            self.session_id=response_data[1]
            self.now_playing_url=response_data[2]
            self.submission_url=response_data[3]
    def submit(self,artist,tracktitle,s_time,source,rating,secs,album,tracknumber="",mb_trackid=""):
        """Submits a track on last.fm.

        Returns True on success, False on problem."""
        post_req="s="+(str(self.session_id, 'utf8'))+"&a[0]="+(artist)+"&t[0]="+(tracktitle)+"&i[0]="+str(int(s_time))+"&o[0]="+(source)+"&r[0]="+(rating)+"&l[0]="+str(secs)+"&b[0]="+(album)+"&n=[0]"+str(tracknumber)+"&m=[0]"+str(mb_trackid)
        response=urllib.request.urlopen(str(self.submission_url,"utf8"),bytes(post_req,'utf8'))
        response_data=[s[:-1] for s in response.readlines()]
        if response_data[0]!=b'OK':
            print (response_data[0])
            return False
        else:
            return True
    def now_playing(self,artist,tracktitle,album="",secs="",tracknumber="",mb_trackid=""):
        """Submits a track on last.fm now_playing system.

        Return True on success, False on problem."""
        post_req="s="+(str(self.session_id))+"&a="+(artist)+"&t="+(tracktitle)+"&b="+(album)+"&l="+(secs)+"&n="+str(tracknumber)+"&m="+str(mb_trackid)
        response=urllib.request.urlopen(str(self.now_playing_url,'utf8'),post_req)
        response_data=[s[:-1] for s in response.readlines()]
        if response_data[0]!=b'OK':
            return False
        else:
            return True

