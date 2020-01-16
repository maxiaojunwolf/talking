# -*- coding: utf-8 -*-

import redis

from config import HOST_USER, PORT_USER, DB_USER
from utils.tkexception import Set_Exception, Del_Exception, User_Exception, Room_Exception



pool_user = redis.ConnectionPool(host=HOST_USER, port=PORT_USER,db=DB_USER)
Redis_User = redis.Redis(connection_pool=pool_user)





class User(object):
    """用户"""

    def __init__(self,id):
        """
        date:2020-01-16 21:11:52
        description：
        """
        self.id = id

    @property
    def status(self):
        """
        date:2020-01-16 21:18:45
        description：用户登录状态
        """
        try:
            status = Redis_User.hget('status',self.id)
            if status=='1':
                return True
        except:
            raise User_Exception
        return False

    @status.setter
    def status(self,status):
        """
        date:2020-01-16 21:34:43
        description：修改用户状态
        """
        try:
            status = 1 if status else 0
            Redis_User.hset('status',self.id,status)
        except:
            raise User_Exception

    @property
    def rooms(self):
        """
        date:2020-01-16 21:18:45
        description：用户所有房间id
        """
        try:
            rooms = Redis_User.smembers(self.id)
            return eval(rooms)
        except:
            raise Room_Exception

    def add_room(self,roomid):
        """
        date:2020-01-16 21:18:45
        description：添加房间id
        """
        try:
            Redis_User.sadd(self.id,roomid)
        except:
            raise Room_Exception

    def del_room(self,roomid):
        """
        date:2020-01-16 21:18:45
        description：删除房间id
        """
        try:
            Redis_User.srem(self.id,roomid)
        except:
            raise Room_Exception

    @classmethod
    def has_user(self):
        """
        date:2020-01-16 22:08:54
        description：判断用户对象是否存在
        """
        return Redis_User.exists(self.id)