import re
from unittest import TestCase

from baseOption.Dungeons import Dungeons
from baseOption.OptionHelper import OptionHelper
from baseOption.TheOption import TheOption, get_vip
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
        dungeons.commonBySkill(wayOrCut, TheOption.bingJingTa_vip, SKILL_SINGLE)

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

    def test_array(self):
        a = [1,2,3]
        b = [3,5,7]

        a.extend(b)
        for i in a:
            print(i)

    def test_get_vip1(self):
        result = OptionHelper.get_vip('123',[1,3,5])
        for i in result:
            print(i)

    def test_get_vip23(self):
        result = get_vip('123',[1,3,5])
        for i in result:
            print(i)

    def test_get_vip3(self):
        for i in TheOption.huaShengShi_vip:
            print(i)


pass
