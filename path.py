# -*- coding:utf-8 -*-
from ig.talking.main import TalkingApp
from ig.talking.models import Rooms,Room


@TalkingApp.path(model=Rooms, path='{userid}')
def get_workflow(request, userid):
    return Rooms(userid)

@TalkingApp.path(model=Room, path='{userid}/{roomid}')
def get_workflow(request, userid,roomid):
    return Room(userid,roomid)