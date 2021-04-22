import re
from unittest import TestCase

from baseOption.Dungeons import Dungeons
from baseOption.Urls import Urls
from baseOption.WayOrCut import WayOrCut


class TestNewDailyTask(TestCase):

    # 打新手区
    def test_xinshouqu_cailiaoguai(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        # 加载页面
        wayOrCut.getHtml()
        dungeons = Dungeons();
        # 打新手区
        dungeons.xinshouqu(wayOrCut)

    # 打新手区
    def test_chiyao(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        # 加载页面
        wayOrCut.getHtml()
        for name in range(52, 53):
            dungeons = Dungeons();
            dungeons.eatDanYao(wayOrCut, str(name))

    # 强化装备
    def test_qianghua(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        # 加载页面
        wayOrCut.getHtml()
        for i in range(1, 25):
            wayOrCut.getByHrefNumberAndGo(3)

    def test_fuben(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        baiGuLingMu=[6,8,6,6,2,2,'食尸鬼',8,8,6,2,2,'剥皮鬼',8,8,6,6,'炼尸鬼',4,4,8,8,4,4,4,8,8,'白骨将',8,6,6,6,'大祭祀',2,2,4,8,6,'白骨夫人','白骨宝箱',"继续"]
        dungeons = Dungeons()
        dungeons.commonBySkill(wayOrCut, baiGuLingMu, "举火")

    def test_for(self):
        for i in ("ddd", "xxx"):
            print(i)

    def test_if(self):
        if 1:
            print(1)
        if 0:
            print(2)

pass
