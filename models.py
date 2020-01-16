# -*- coding:utf-8 -*-

import redis

pool = redis.ConnectionPool(host='localhost', port=6379,db=10)
RedisCon = redis.Redis(connection_pool=pool)


class Rooms(object):

    def __init__(self,userid):
        self.userid = userid

    @property
    def rooms(self):
        return self.get_rooms(self.userid)

    def get_rooms(self,userid):
        try:
            return list(RedisCon.smembers(userid))
        except:
            return []

    @property
    def new_messages(self):
        return {r:Room(r).new_messages for r in self.rooms}

    @property
    def old_messages(self):
        return {r: Room(r).oldmessages for r in self.rooms}

class Room(object):

    def __init__(self,userid,roomid,messageid=None,counts=10):
        self.userid = userid
        self.roomid = roomid
        self.counts = counts
        self.messageid = messageid
        self.messages = {}


    @property
    def new_messages(self):
        if self.has_room:
            self._new_messages(self.roomid,self.messageid,self.counts)
        return self.messages

    @property
    def oldmessages(self):
        if self.has_room:
            self._old_messages(self.roomid, self.messageid, self.counts)
        return self.messages

    @property
    def has_room(self):
        return self._has_room(self.userid,self.roomid)

    def _new_messages(self, roomid,messageid,counts):
        """获取新消息：默认10条"""
        try:
            messages = RedisCon.hgetall(roomid)
            if messages:
                messages = sorted(messages.items())
                if messageid:
                    for k in messages:
                        if k[0] > messageid:
                            self.messages[k[0]] = k[1]
                            if len(self.messages) == counts:
                                break
                else:
                    self.messages = {m[0]: m[1] for m in messages[-counts:]}
        except:
            pass
        return self.messages

    def _old_messages(self, roomid,messageid,counts):
        """获取旧消息：根据当前消息id取值，默认10条"""
        try:
            messages =  RedisCon.hgetall(roomid)
            if messages:
                messages = sorted(messages.items())
                if  messageid:
                    for k in messages:
                        if k[0]<messageid:
                            self.messages[k[0]] = k[1]
                            if len(self.messages)==counts:
                                break
                else:
                    self.messages = {m[0]:m[1] for m in messages[-counts:]}
        except:
            pass
        return self.messages

    def _has_room(self,userid,roomid):
        """判断某个用户是否有某个房间id"""
        if roomid in Rooms(userid).rooms:
            return True
        return False