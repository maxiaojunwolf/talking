# -*- coding: utf-8 -*-

"""异常"""

class Set_Exception(Exception):

    Message = '属性不允许修改'
    def __init__(self):
        super().__init__(self.Message)

class Del_Exception(Exception):

    Message = '属性不允许删除'
    def __init__(self):
        super().__init__(self.Message)

class User_Exception(Exception):

    Message = '用户信息错误'
    def __init__(self):
        super().__init__(self.Message)

class Room_Exception(Exception):

    Message = '房间信息错误'
    def __init__(self):
        super().__init__(self.Message)

class Message_Exception(Exception):

    Message = '消息错误'
    def __init__(self):
        super().__init__(self.Message)

if __name__ == '__main__':
    raise User_Exception()
    raise Room_Exception()
    raise Message_Exception()