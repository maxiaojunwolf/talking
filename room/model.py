# -*- coding:utf-8 -*-
from ig.talking.utils import generate_id
from ig.talking.message.model import Message

__author__ = 'mxj'
__date__ = '2019/8/27 18:26'

class Room(object):

    def __init__(self,id=None,users=[],**kwargs):
        """
        @author: mxj
        @date: 2019-08-27 18:32:10
        @description: 聊天室
        """
        self.room_id = id
        if id is None:
            self.autoset_id()
        self.users_ = users
        self.messages_ = {}

    @property
    def id(self):
        """
        @author: mxj
        @date: 2019-08-27 18:32:10
        @description: 查看聊天室id
        """
        return self.room_id

    @id.setter
    def id(self,newid):
        """
        @author: mxj
        @date: 2019-08-27 18:38:48
        @description: 设置房间id
        """
        if not self.id:
            self.room_id = newid

    @id.deleter
    def id(self,ctx=None):
        """
        @author: mxj
        @date: 2020-01-16 18:53:57
        @description: 不允许删除房间id
        """
        raise Exception('房间id无法删除')

    def autoset_id(self):
        """
        @author: mxj
        @date: 2020-01-16 18:51:24
        @description: 自动生成房间id
        """
        if not self.room_id:
            newid = generate_id()
            self.room_id = newid


    @property
    def users(self):
        """
        @author: mxj
        @date: 2019-08-27 18:32:10
        @description: 聊天室内所有用户id
        """
        return self.users_


    def add_user(self,userid):
        """
        @author: mxj
        @date: 2019-08-27 18:32:10
        @description: 添加聊天室内的用户
        """
        if userid not in self.users_:
            self.users_.append(userid)

    def del_user(self,userid):
        """
        @author: mxj
        @date: 2019-08-27 18:32:10
        @description: 删除聊天室内的用户
        """
        if userid  in self.users_:
            self.users_.remove(userid)


    @property
    def message(self):
        """
        @author: mxj
        @date: 2019-08-27 18:32:10
        @description: 聊天室消息对象
        """
        return Message(self.id)



if __name__ == '__main__':
    room = Room()
    room.id = 23
    print room.message.id_
