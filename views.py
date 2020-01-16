# -*- coding:utf-8 -*-
from ig.talking.main import TalkingApp
from ig.talking.models import Rooms,Room


@TalkingApp.json(model=Rooms, request_method="GET")
def get_message(self, request):

    data = {'code':200,'method':'get','rooms':self.rooms}
    return data


@TalkingApp.json(model=Room, request_method="GET")
def post_message(self, request):

    data = {'code':200,'method':'get','messages':self.new_messages}
    return data

