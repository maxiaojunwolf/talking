# -*- coding:utf-8 -*-
from config import HOST_ROOM, PORT_ROOM, DB_ROOM
from message.model import Message
from user.model import User
from utils import generate_id


import redis

pool_room = redis.ConnectionPool(host=HOST_ROOM, port=PORT_ROOM,db=DB_ROOM)
Redis_Room = redis.Redis(connection_pool=pool_room)


__author__ = 'mxj'
__date__ = '2019/8/27 18:26'

class Room(object):

    def __init__(self,id,**kwargs):
        """
        @author: mxj
        @date: 2019-08-27 18:32:10
        @description: 聊天室
        """
        self.id = id

    @classmethod
    def create_room(self):
        """
        @author: mxj
        @date: 2020-01-16 18:51:24
        @description: 新建房间
        """
        return Room(generate_id())

    def add_user(self,userid):
        """
        @author: mxj
        @date: 2019-08-27 18:32:10
        @description: 添加聊天室内的用户
        """
        user = User(userid)
        user.add_room(self.id)

    def del_user(self,userid):
        """
        @author: mxj
        @date: 2019-08-27 18:32:10
        @description: 删除聊天室内的用户
        """
        user = User(userid)
        user.del_room(self.id)


    @property
    def message(self):
        """
        @author: mxj
        @date: 2019-08-27 18:32:10
        @description: 聊天室消息对象
        """
        return Message(self.id).get_messages()
    @staticmethod
    def has_room(self):
        """
        date:2020-01-16 22:08:54
        description：判断房间对象是否存在
        """
        return Redis_Room.exists(self.id)

if __name__ == '__main__':
    room = Room()
    print(room.message.room_id)
