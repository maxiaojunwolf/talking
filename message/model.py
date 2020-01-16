# -*- coding:utf-8 -*-
import redis

from config import HOST_MESSAGE, PORT_MESSAGE, DB_MESSAGE
from utils.tkexception import Room_Exception

__author__ = 'mxj'
__date__ = '2020/1/16 19:11'


pool_message = redis.ConnectionPool(host=HOST_MESSAGE, port=PORT_MESSAGE,db=DB_MESSAGE)
Redis_Msg = redis.Redis(connection_pool=pool_message)

class Message(object):

    def __init__(self,id):
        """
        @author: mxj
        @date: 2020-01-16 19:13:03
        @description: 消息对象message_id 就是房间id
        """
        self.id = id
        self.messages = {}

    def get_messages(self):
        """
        date:2020-01-16 22:44:27
        description：
        """
        try:
            return Redis_Msg.hgetall(self.id)
        except:
            return self.messages


    def new_messages(self,messageid=None,counts=10):
        self._new_messages(self.id,messageid,counts)
        return self.messages

    def oldmessages(self,messageid=None,counts=10):
        self._old_messages(self.id, messageid, counts)
        return self.messages

    def _new_messages(self, roomid,messageid=None,counts=None):
        """获取新消息：默认10条"""
        if messageid:
                for i in range(1,counts+1):
                    if Redis_Msg.exists(roomid,messageid+i):
                        self.messages[messageid+i] =  Redis_Msg.hget(roomid,messageid+i)
                    else:
                        break
        else:
            max_messageid = max(Redis_Msg.hkeys(roomid))
            self.oldmessages(max_messageid)
        return self.messages

    def _old_messages(self, roomid,messageid,counts):
        """获取旧消息：根据当前消息id取值，默认10条"""
        if messageid:
                for i in range(1,counts+1):
                    if Redis_Msg.exists(roomid,messageid-i):
                        self.messages[messageid+i] =  Redis_Msg.hget(roomid,messageid-i)
                    else:
                        break
        else:
            max_messageid = max(Redis_Msg.hkeys(roomid))
            self.oldmessages(max_messageid)
        return self.messages

    def add_message(self,msg):
        """
        date:2020-01-16 23:54:11
        description：添加消息
        """
        try:
            cur_messageid = max(Redis_Msg.hkeys(self.id))+1
        except:
            cur_messageid = 1
        Redis_Msg.hset(self.id,cur_messageid,msg)

    def del_message(self,messageid):
        """
        date:2020-01-16 23:54:11
        description：删除消息
        """
        try:
            Redis_Msg.hdel(self.id,messageid)
        except:
            pass