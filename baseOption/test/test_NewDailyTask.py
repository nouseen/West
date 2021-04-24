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

    # 强化装备 13最后一个 吃药等
    def test_qianghua(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        # 加载页面
        while wayOrCut.getByHrefNumberAndGo(4,"返回游戏"):
            continue;

    def test_fuben(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        dungeons = Dungeons()
        dungeons.allDungeonsAuto(wayOrCut, SKILL_SINGLE)

    def test_fuben_single(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        dungeons = Dungeons()
        # BA_JIAO_DONG_VIP = ['发现', 8, 6, 2, '云里雾', 4, '雾里云', 6, 8, 6, '千年芭蕉精', 8, 8, 8, '牛魔王']
        # LIU_LI_TA_VIP = [ 2, 6, '百花羞', 6, 6, 2, 2, 6, 6, 6, '四翼蛇精', 6, 2, 2, 2, 2, 2, 2, '烛阴', 2, 6, 6, 6, 6, 2, 2, 6, '狡兔妖后', 6, 6, 2, 2, 2, 6, 6, 6, '蓝彩毒后', '完成']
        # dungeons.commonBySkill(wayOrCut, LIU_LI_TA_VIP, SKILL_SINGLE)
        dungeons.commonBySkill(wayOrCut, TheOption.XIAO_LEI_YIN_SHI, SKILL_SINGLE)

    def test_shifangzhen(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.cutMonsterBySkill('十方', SKILL_SINGLE)

    def test_shijuezhen(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.cutMonsterBySkill('十绝', SKILL_SINGLE)

    def test_BossHome(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.cutBOSSHomeBySkill(SKILL_SINGLE)

    def test_ge_ren_Boss(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)

        for i in range(1, 5):
            wayOrCut.getOperationsAndGo(['挑战'])
            wayOrCut.cutMonsterBySkill('击杀', SKILL_SINGLE)

    def test_she_ji_tu(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','社稷图使者','【社稷图】','继续'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '孟婆')

    def test_shan_he_tu(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','社稷图使者','【山河图】','继续'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '孟婆')

    def test_tong_tian_ta(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','通天','通天'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '孟婆')

    def test_for(self):
        for i in ("ddd", "xxx"):
            print(i)

    def test_if(self):
        if 1:
            print(1)
        if 0:
            print(2)

    def test_array(self):
        a = [1, 2, 3]
        b = [3, 5, 7]

        a.extend(b)
        for i in a:
            print(i)

    def test_get_vip1(self):
        result = OptionHelper.get_vip('123', [1, 3, 5])
        for i in result:
            print(i)

    def test_get_vip23(self):
        result = get_vip('123', [1, 3, 5])
        for i in result:
            print(i)

    def test_get_vip3(self):
        for i in TheOption.huaShengShi_vip:
            print(i)


pass
