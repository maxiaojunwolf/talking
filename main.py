# -*- coding:utf-8 -*-

from cs.platform.web.root import V1, get_v1
from cs.platform.web import PlatformApp


class TalkingApp(PlatformApp):
    PATH = "talking"

    @classmethod
    def get_cim_database(cls, request):
        return get_v1(request).child(cls.PATH)


@V1.mount(app=TalkingApp, path=TalkingApp.PATH)
def _mount_cim_database():
    return TalkingApp()
