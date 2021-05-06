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

    def test_full(self):
        self.test_tong_tian_ta()
        self.test_tong_tian_ta_vip()
        self.test_fuben()
        # self.test_xinshouqu_cailiaoguai()
        self.test_shijuezhen()
        self.test_shifangzhen()
        self.test_BossHome()
        self.test_she_ji_tu()
        self.test_ge_ren_Boss()

    def test_tong_tian_ta(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','通天','通天'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '查看地图传送(1)')

    def test_ba_shi_yi_nan(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','八十一'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '孟婆')

    def test_da_nao_tian_gong(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','天宫'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '孟婆')

    def test_da_nao_di_fu(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','地府'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '孟婆')

    def test_tong_tian_ta_vip(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','可点','副本','通 天 塔'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '进入【通天塔37层】')

    # 打新手区
    def test_xinshouqu_cailiaoguai(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        dungeons = Dungeons();
        # 打新手区
        dungeons.xinshouqu(wayOrCut)

    def test_fuben(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        dungeons = Dungeons()
        dungeons.allDungeonsAuto(wayOrCut, SKILL_SINGLE)

    def test_fuben_single(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        dungeons = Dungeons()
        # WU_DI_DONG = ['继续', '返回', '返回', '腾云', '无底洞', '激活【无底洞困难副本】', '继续',2,6,'【白鼠精】',4,2,2,6,6,2,4,'【黑鼠精】',6,6,8,8,6,8,8,4,'【田鼠精】',4,2,2,2,2,6,6,'【地涌夫人】']
        # dungeons.commonBySkill(wayOrCut, WU_DI_DONG, SKILL_SINGLE)
        dungeons.commonBySkill(wayOrCut, TheOption.SI_TUO_DONG_VIP, SKILL_SINGLE)

    def test_shifangzhen(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['腾云','十方','十方','十方','继续'])
        wayOrCut.cutMonsterBySkill('十方', SKILL_SINGLE)
        wayOrCut.getByHrefNumberAndGo(1,"")
        wayOrCut.getByHrefNumberAndGo(0,"")


    def test_shijuezhen(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','十绝','十绝','继续'])
        wayOrCut.cutMonsterBySkill('十绝', SKILL_SINGLE)

    def test_BossHome(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.cutBOSSHomeBySkill(SKILL_SINGLE)

    def test_ge_ren_Boss(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','挑战'])
        for i in range(1, 7):
            wayOrCut.getOperationsAndGo(['挑战'])
            wayOrCut.cutMonsterBySkill('击杀', SKILL_SINGLE)

    def test_she_ji_tu(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','社稷图使者','【社稷图】','继续'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '孟婆')
        self.test_shan_he_tu();
        self.test_shan_he_tu_vip();

    def test_shan_he_tu(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['状态','十年','挑战','社稷图使者','【山河图】','继续'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '孟婆')

    def test_shan_he_tu_vip(self):
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        wayOrCut.getOperationsAndGo(['继续', '返回', '返回', '状态', '可点', '副本', '继续','山 河 图','继续'])
        wayOrCut.cutFixSiteMonsterBySkill(1, SKILL_SINGLE, '孟婆')

    # 吃药
    def test_chiyao(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        # 加载页面
        wayOrCut.getHtml()
        for name in range(52, 53):
            dungeons = Dungeons();
            dungeons.eatDanYao(wayOrCut, str(name))

    # 群
    def test_qunMoZheng(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        # 加载页面
        wayOrCut.getHtml()
        dungeons = Dungeons();
        dungeons.qunMoZheng(wayOrCut)

    # 加神通
    def test_shentong(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        # 加载页面
        for name in range(0, 44):
            wayOrCut.getByHrefNumberAndGo(19,"返回游戏")
            # wayOrCut.getByHrefNumberAndGo(0,"返回游戏")

    # 加神通
    def test_shengji(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        # 加载页面
        for name in range(0, 219):
            wayOrCut.getOperationsAndGo(['升级','返回上级'])

    # 强化
    def test_jingjie(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        # 加载页面
        for name in range(0, 1500):
            wayOrCut.getOperationsAndGo(['进阶'])

    # 强化装备 13最后一个 吃药等
    def test_qianghua(self):
        # 初始化
        wayOrCut = WayOrCut(Urls.fullUrl828, Urls.preUrl8128)
        # 加载页面
        while wayOrCut.getByHrefNumberAndGo(4,"返回游戏"):
            continue;

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
