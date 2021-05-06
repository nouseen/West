import re
from datetime import time

from baseOption.TheOption import TheOption
from baseOption.TheWay import TheWay


class Dungeons:
    option = TheOption()
    way = TheWay()

    def allDungeonsAuto(self, wayOrCut, skill):
        # 一波刷完
        for i in self.option.optionList:
            self.commonBySkill(wayOrCut, i, skill)

    def common(self, wayOrCut, option):
        # 刷本通用
        self.commonBySkill(wayOrCut, option, '举火')

    def commonBySkill(self, wayOrCut, option, skill):
        # 刷本通用
        for i in option:
            if i == 6 or i == 4 or i == 2 or i == 8:
                wayOrCut.getWayAndGo(i)
            elif wayOrCut.getOperationAndGo(i) != 1:
                print(i + "失败")
            # 使用完技能会返回，腾云后不能点返回
            if i != '腾云':
                wayOrCut.useSkill(skill)
                wayOrCut.getOperationAndGo("继续")

    def eatDanYao(self,wayOrCut,name):
        wayOrCut.getOperationAndGo(name)
        wayOrCut.getOperationAndGo('人物吃丹')
        detail = str(wayOrCut.getHtml())
        ans = re.search(u'上限:([0-9]*)/([0-9]*)', detail)
        eated = int(ans.group(1));
        total = int(ans.group(2));
        rest = total - eated
        print('剩余可吃：' + str(rest))
        data = {'a': rest, 'submit': '提交'}
        wayOrCut.getFormAction("吃丹")
        wayOrCut.postForm(data)
        wayOrCut.getHtml()
        wayOrCut.getOperationAndGo('返回上级')
        wayOrCut.getOperationAndGo('返回列表')

    # 新手区
    def xinshouqu(self, wayOrCut):
        # 新手区
        self.commonBySkill(wayOrCut, self.option.xinshouqu, '举火')
        wayOrCut.cutMonsterBySkill('材料','举火')

        wayOrCut.getOperationAndGo("中心区")
        wayOrCut.getOperationAndGo("声望区")
        wayOrCut.cutMonsterBySkill('声望','举火')

        wayOrCut.getOperationAndGo("中心区")
        wayOrCut.getOperationAndGo("boss区")
        wayOrCut.cutMonsterBySkill('回馈boss','举火')

    def updateInHell(self, wayOrCut, skill):
        # 地府刷怪
        wayOrCut.coudeToAnyWhere('地府')
        self.way.gobyWay(wayOrCut, self.way.GuiMenGuanToTurning)
        while 1 == 1:
            m = 0
            while m < 9:
                m = m + 1
                for i in self.way.wayInHell:
                    self.way.gobyWay(wayOrCut, i)
                    wayOrCut.cutMonster("\*【")
            self.way.gobyWay(wayOrCut, self.way.hellBack)

    def updateInZhiZhuLin(self, wayOrCut):
        while 1 == 1:
            wayOrCut.coudeToAnyWhere("普陀")
            wayOrCut.getOperationAndGo('知客僧')
            wayOrCut.getOperationAndGo('紫竹林')
            option = [6, 6, 6, 6, 2, 2, 2, 2, 6, 2, 6, 6, 6, 6, 6, 2, 2, 2, 2, 6, 2, 6, 6, 6, 6, 6, 2, 2, 2, 2, 6, 2, 6]
            self.way.cutMonsterByWay(wayOrCut, option, "\*【")
            time.sleep(30)

    def cutInSquare(self, wayOrCut):
        # 恶魔广场刷怪
        self.common(wayOrCut, self.option.goTOSquare)
        while 1 == 1:
            self.way.cutMonsterByWayBySkill(wayOrCut, self.way.way4Plus4, '\*【', '举火')
            wayOrCut.getWayAndGo(4)
            self.way.cutMonsterByWayBySkill(wayOrCut, self.way.way5Plus5, '\*【', '举火')
            wayOrCut.getWayAndGo(6)
            if '恶魔广场活动结束' in str(wayOrCut.soup):
                break

    def watchMovie(self, wayOrCut):
        while 1 == 1:
            if wayOrCut.getOperationAndGo('继续') == 1:
                print('自动继续')
            elif wayOrCut.getOperationAndGo("返回") == 1:
                print('返回成功')
            elif wayOrCut.getOperationAndGo("对打") == 1:
                wayOrCut.useSkill("回马")
                print("对打!")
            else:
                break

    def qunMoZheng(self, wayOrCut):
        wayOrCut.getOperationAndGo("群魔")
        wayOrCut.getOperationAndGo("继续")
        while 1 == 1:
            for i in self.way.way2Plus3:
                wayOrCut.getWayAndGo(i)
                if wayOrCut.matchTheXinMo() == 1:
                    wayOrCut.useSkill("回马")

    def tongTianTa(self, wayOrCut, name):
        # 通天塔
        self.common(wayOrCut, self.option.tongTianTa)
        wayOrCut.cutMonster(name)
        print('砍怪中')

    def guaJi(self, wayOrCut):
        while 1 == 1:
            time.sleep(60)
            wayOrCut.getHtml()
            wayOrCut.getOperationAndGo('刷新')
            if "群魔乱舞活动" in str(wayOrCut.soup):
                self.qunMoZheng(wayOrCut)

    def guojia(self, wayOrCut):
        wayTOGuoJiaDashi = ['腾云', '长安', 2, 2, "国家大使"]
        self.common(wayOrCut, wayTOGuoJiaDashi)
        i = 0
        while i < 10:
            i += 1
            wayOrCut.getOperationAndGo('每日国家任务')
            wayOrCut.getOperationAndGo('返回上级')
            wayOrCut.getOperationAndGo('继续')
        wayOrCut.getOperationAndGo("返回")

    def couple(self, wayOrCut):
        thisWay = ['腾云', '长安', '李白', '区域传说', '姻缘', 8, 6, '女娲']
        self.common(wayOrCut, thisWay)
        i = 0
        while i < 10:
            i += 1
            wayOrCut.getOperationAndGo('夫妻每日任务')
            wayOrCut.getOperationAndGo('返回上级')
        wayOrCut.getOperationAndGo("返回")

    def xiangYao(self, wayOrCut):
        wayToXiangYao = ['腾云', '长安', 2, 2, '赏金猎人', '199级', '继续', '返回', '返回', 4, '袁天罡', '降妖任务']
        self.common(wayOrCut, wayToXiangYao)
        n = 0
        while n <= 20:
            n = n + 1
            string = str(wayOrCut.soup)
            match = re.search(u'打败(.*)x([0-9]{1,2})', string)
            print(match)
            if match == None:
                return 0
            name = match.group(1)
            option1 = []
            if name == '硬壳龟怪' or name == '鲨鱼精' or name == '巨鳌怪':
                option1 = ['继续', '返回', '返回', '任务', '下\.页', '赏金任务', '海底莽林', 8, 4, 4, 8, 4, 4, 8, 6, 6, 8, 4, 4]
            elif name == '野狼' or name == '野兔' or name == '山猪':
                option1 = ['继续', '返回', '返回', '腾云', '城南', 2, 2, 6, 6, 8, 4, 8, 6]
            elif name == '鳅鱼精' or name == '赤背虾精':
                option1 = ['继续', '返回', '返回', '任务', '下\.页', '赏金任务', '海底莽林', 2, 2, 6, 6, 8, 4, 2]
            elif name == '虾兵' or name == '蟹将':
                option1 = ['继续', '返回', '返回', '任务', '下\.页', '赏金任务', '泾水河', 2, 2, 6, 6, 8, 4, 2]
            elif name == '雪狼' or name == '雪豹':
                option1 = ['继续', '返回', '返回', '任务', '下\.页', '赏金任务', '雪山迷宫', 2, 2, 6, 6, 8, 4, 2]
            elif name == '雪妖' or name == '雪莲精':
                option1 = ['继续', '返回', '返回', '任务', '下\.页', '赏金任务', '冰风谷迷宫', 2, 2, 6, 6, 8, 4, 2]
            elif name == '黄雀精' or name == '彩碟精':
                option1 = ['继续', '返回', '返回', '任务', '下\.页', '赏金任务', '紫竹林', 2, 2, 6, 6, 8, 4, 2]
            elif name == '老狼':
                option1 = ['继续', '返回', '返回', '任务', '下\.页', '赏金任务', '松林', 2, 2, 6, 6, 8, 4, 2]
            elif name == '灯笼怪' or name == '蜡烛怪':
                option1 = ['继续', '返回', '返回', '腾云', '小雁塔', 2, 2, 6, 6, 8, 4, 8, 6]
            elif name == '灯芯怪' or name == '扫帚怪':
                option1 = ['继续', '返回', '返回', '腾云', '大雁塔', 2, 2, 6, 6, 8, 4, 8, 6]
            elif name == '宣纸怪' or name == '油墨':
                option1 = ['继续', '返回', '返回', 6, 8, 8, 6, 6, 6, 8, 8, 4, 2, 2, 2, 6, 6, 8, 4, 8, 6]
            elif name == '小虾米':
                option1 = ['继续', '返回', '返回', '任务', '下\.页', '赏金任务', '海底莽林', 2, 2, 2, 6, 6, 6, 6]
            elif name == '潮水螃蟹':
                option1 = ['继续', '返回', '返回', '腾云', '东海沙滩', 6, 6, 6, 2, 2, 2]
            elif name == "螃蟹":
                option1 = ['继续', '返回', '返回', '任务', '下\.页', '赏金任务', '沙滩', 2, 2, 6, 6, 8, 4, 8, 6]
            if option1 == []:
                return 0
            task = 0

            for i in option1:
                if task != 0:
                    break;
                if i == 6 or i == 4 or i == 2 or i == 8:
                    wayOrCut.getWayAndGo(i)
                else:
                    wayOrCut.getOperationAndGo(i)
                while task == 0 and wayOrCut.getOperationAndGo(name) == 1:
                    if wayOrCut.getOperationAndGo("攻击") == 1:
                        print("自动攻击")
                    if task == 0 and (wayOrCut.getOperationAndGo('举火') == 1 or wayOrCut.getOperationAndGo('王枪')):
                        string = str(wayOrCut.soup)
                        matches = re.findall(u'\(([0-9]{1,2})/([0-9]{1,2})\)<br/>', string)
                        if matches == []:
                            continue
                        match = matches[len(matches) - 1]
                        if match[0] == match[1]:
                            task += 1
                    wayOrCut.getOperationAndGo('返回')
            option2 = ['腾云', '长安', 2, 2, 4, '袁天罡', '降妖任务', '继续', '返回', '返回', '袁天罡', '降妖任务']
            self.common(wayOrCut, option2)

    def shangJing(self, wayOrCut):
        self.common(wayOrCut, self.option.getShangjing)
        n = 0
        while n <= 20:
            n = n + 1
            string = str(wayOrCut.soup)
            match = re.search(u'打败(.*)x([0-9]{1,2})', string)
            if match == None:
                return 0
            name = match.group(1)
            option1 = []
            if name == '硬壳龟怪' or name == '鲨鱼精' or name == '巨鳌怪':
                option1 = ['继续', '返回', '返回', '任务', '赏金任务', '下\.页', '赏金任务', '海底莽林', 8, 4, 4, 8, 4, 4, 8, 6, 6, 8, 4, 4]
            if name == '野狼' or name == '野兔' or name == '山猪':
                option1 = ['继续', '返回', '返回', '腾云', '城南', 2, 2, 6, 6, 8, 4, 8, 6]
            if name == '鳅鱼精' or name == '赤背虾精':
                option1 = ['继续', '返回', '返回', '任务', '赏金任务', '下\.页', '赏金任务', '海底莽林', 2, 2, 6, 6, 8, 4, 2]
            if name == '虾兵' or name == '蟹将':
                option1 = ['继续', '返回', '返回', '任务', '赏金任务', '下\.页', '赏金任务', '泾水河', 2, 2, 6, 6, 8, 4, 2]
            if name == '雪狼' or name == '雪豹':
                option1 = ['继续', '返回', '返回', '任务', '赏金任务', '下\.页', '赏金任务', '雪山迷宫', 2, 2, 6, 6, 8, 4, 2]
            if name == '雪妖' or name == '雪莲精':
                option1 = ['继续', '返回', '返回', '任务', '赏金任务', '下\.页', '赏金任务', '冰风谷迷宫', 2, 2, 6, 6, 8, 4, 2]
            if name == '黄雀精' or name == '彩碟精':
                option1 = ['继续', '返回', '返回', '任务', '赏金任务', '下\.页', '赏金任务', '紫竹林', 2, 2, 6, 6, 8, 4, 2]
            if name == '老狼':
                option1 = ['继续', '返回', '返回', '任务', '赏金任务', '下\.页', '赏金任务', '松林', 2, 2, 6, 6, 8, 4, 2]
            if name == '小虾米':
                option1 = ['继续', '返回', '返回', '任务', '赏金任务', '下\.页', '赏金任务', '海底莽林', 2, 2, 2, 6, 6, 6, 6]
            if name == '潮水螃蟹':
                option1 = ['继续', '返回', '返回', '腾云', '东海沙滩', 6, 6, 6, 2, 2, 2]
            if option1 == []:
                return 0
            task = 0
            for i in option1:
                if task != 0:
                    break;
                if i == 6 or i == 4 or i == 2 or i == 8:
                    wayOrCut.getWayAndGo(i)
                else:
                    wayOrCut.getOperationAndGo(i)
                while task == 0 and wayOrCut.getOperationAndGo(name) == 1:
                    if wayOrCut.getOperationAndGo("攻击") == 1:
                        print("自动攻击")
                    if task == 0 and (wayOrCut.getOperationAndGo('举火') == 1 or wayOrCut.getOperationAndGo('王枪')):
                        string = str(wayOrCut.soup)
                        matches = re.findall(u'\(([0-9]{1,2})/([0-9]{1,2})\)<br/>', string)
                        if matches == [] or matches == None:
                            wayOrCut.getOperationAndGo('返回')
                            continue;
                        match = matches[len(matches) - 1]
                        if match[0] == match[1]:
                            task += 1
                    wayOrCut.getOperationAndGo('返回')
            option2 = ['腾云', '长安', 2, 2, '赏金猎人', '199级', '继续', '返回', '返回', '赏金猎人', '199级']
            self.common(wayOrCut, option2)
        option3 = ['继续', '返回', '返回']
        self.common(wayOrCut, option3)
