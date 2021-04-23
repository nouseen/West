import re
from unittest import TestCase

from baseOption.Dungeons import Dungeons
from baseOption.TheOption import TheOption
from baseOption.Urls import Urls
from baseOption.WayOrCut import WayOrCut

SKILL = "举火"
SKILL_SINGLE = "回马"


class TestNewDailyTask(TestCase):

    # 打新手区
    def test_xinshouqu_cailiaoguai(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        dungeons = Dungeons();
        # 打新手区
        dungeons.xinshouqu(wayOrCut)

    # 吃药
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
        dungeons = Dungeons()
        dungeons.allDungeonsAuto(wayOrCut, SKILL_SINGLE)

    def test_fuben_single(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        dungeons = Dungeons()
        dungeons.commonBySkill(wayOrCut, TheOption.huaShengShi_vip, SKILL_SINGLE)

    def test_shifangzhen(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.cutMonsterBySkill('十方', SKILL_SINGLE)

    def test_BossHome(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.cutBOSSHomeBySkill(SKILL_SINGLE)

    def test_for(self):
        for i in ("ddd", "xxx"):
            print(i)

    def test_if(self):
        if 1:
            print(1)
        if 0:
            print(2)


pass
