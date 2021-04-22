import re
import time

from bs4 import BeautifulSoup
import requests


class WayOrCut:
    def __init__(self, url, preUrl):
        self.url = url
        self.preUrl = preUrl
        self.act = "连接成功"
        self.isEnableHtmlOut = 0
        self.getHtml()

    def connect(self):
        try:
            self.wb_data = requests.get(self.url)
            return 1;
        except:
            return 0;

    # 打开当前URL
    def getHtml(self):
        # 打开当前URL
        time.sleep(0.25)
        statue = 1
        while self.connect() == 0:
            statue = 0
            print("重连中。。")
        content = (self.wb_data.text).replace("&nbsp;", '')
        self.soup = BeautifulSoup(content, 'html.parser')
        if "手机太棒了" in str(self.soup) or "点击频度" in str(self.soup) or "源站返回未知错误" in str(self.soup):
            print("手机太棒")
            time.sleep(1)
            self.getHtml()
            statue = 0
        if self.getOperation('领奖') == 1:
            self.getHtml()
            self.getOperationAndGo('返回')
            self.getOperationAndGo('继续')
        print(self.act)
        if self.isEnableHtmlOut:
            print(self.soup)
        return statue

    def postForm(self, data):
        time.sleep(0.4)
        wb_data = requests.post(self.url, data)
        self.soup = BeautifulSoup(wb_data.text, 'html')
        print(self.act)
        if self.isEnableHtmlOut:
            print(self.soup)
        return self.soup

    # 获取上下左右
    def getWay(self, way):
        # 获取上下左右的URL
        fresh = self.soup.find('a', {'accesskey': way})
        if fresh == None:
            return 0
        h_fresh = fresh['href']
        p = h_fresh.split('x=')
        self.url = self.preUrl + p[1]
        self.act = way;
        return 1

    def getWayAndGo(self, way):
        # 获取数字方向并打开URL
        if self.getWay(way) == 0:
            return 0
        while self.getHtml() == 0:
            self.getWay(way)
        return 1

    # 获取操作URL
    def getOperation(self, op):
        refresh = self.soup.find('a', text=re.compile(op))
        return self.anaUrlFromAMark(op, refresh)

    def getOperationByHrefNumber(self, hrefNumber):
        refresh = self.soup.findAll('a')[hrefNumber]
        return self.anaUrlFromAMark(refresh.string, refresh)

    def anaUrlFromAMark(self, op, refresh):
        if refresh == None:
            self.act = "查找" + op + "失败"
            return 0
        hr = refresh['href']
        p = hr.split('x=')
        self.url = self.preUrl + p[1]
        self.act = op
        return 1;

    # 获取操作URL
    def getOperationByNextSiblingByName(self, op):
        refresh = self.soup.find('font', text=re.compile(op)).nextSibling
        return self.anaUrlFromAMark(op, refresh)

    def getFormAction(self, op):
        action = self.soup.form.attrs['action']
        if action == None:
            return 0
        p = action.split('x=')
        self.url = self.preUrl + p[1]
        self.act = op
        return 1;

    def getOperationAndGo(self, op):
        # 获取匹配值并打开URL
        if self.getOperation(op) == 0:
            return 0
        while self.getHtml() == 0:
            self.getOperation(op)
        return 1;

    def getByHrefNumberAndGo(self, hrefNumber):
        result = self.getOperationByHrefNumber(hrefNumber)
        if result == 1:
            self.getHtml()
        return result;

    def getOperationByNextSiblingByNameAndGo(self, op):
        result = self.getOperationByNextSiblingByName(op)
        if result == 1:
            self.getHtml()
        return result;

    def cutMonster(self, name):
        # 砍完怪
        while self.getOperation(name) == 1:
            self.getHtml()
            if self.getOperation("攻击") == 1:
                self.getHtml()
            while self.getOperation('回马') == 1 or self.getOperation('举火') == 1 or self.getOperation('排山') == 1 or self.getOperation('王枪'):
                self.getHtml()
            if self.getOperation("返回") == 1:
                self.getHtml()

    def cutMonsterBySkill(self, name, skill):
        # 砍完怪,仅用于刷材料
        while self.getOperation(name) == 1:
            self.getHtml()
            if self.getOperation("攻击") == 1:
                self.getHtml()
            while self.getOperation(skill) == 1 or self.getOperation('举火') == 1 or self.getOperation('排山') == 1 or self.getOperation('王枪') or self.getOperation('回马') == 1:
                self.getHtml()
            if self.getOperation("返回") == 1:
                self.getHtml()

            # 连续砍怪

    def useSkill(self, skill):
        # 连续砍怪
        while self.getOperation(skill) or self.getOperation('举火') == 1 or self.getOperation('回马') == 1 or self.getOperation('排山') == 1 or self.getOperation('王枪'):
            while self.getHtml() == 0:
                if self.getOperation(skill) or self.getOperation('举火') == 1 or self.getOperation('回马') == 1 or self.getOperation('排山') == 1 or self.getOperation('王枪'):
                    print("重连成功")
            if self.getOperation("返回游戏") == 1:
                self.getHtml()

    # 连续继续
    def gameContinue(self):
        # 连续继续或返回
        while self.getOperation("继续") == 1 or self.getOperation('返回'):
            self.getHtml()

    def coudeToAnyWhere(self, way):
        # 腾云符去一个地方
        self.gameContinue()
        self.getOperationAndGo("腾云")
        self.getOperationAndGo(way)

    def matchByhand(self, name):
        # <a href="c.rosyclouds?u=xxm233381&amp;x=Q1UiVJnV8iLKR3On0oPw86_k1FD644m0nnnr_"><img alt="感叹号" src="img.rosyclouds?uid=233381&amp;src=O__xd8u76KKdSKFldBShg2Vk6hw7b5k7D4TdXaeL5GBcJXbHx6O7dlRx8k1vIQDW"/>激活变异竹林副本(梦魇)</a><br/>
        string = str(self.soup)
        word = re.findall(u'href.{100,300}' + name, string)
        word1 = re.findall('x=.{0,50}_\"', word[0])
        ans = word1[0].replace('x=', '')
        ans = ans.replace('\"', '')
        self.url = self.preUrl + ans
        return self.url

    def matchTheXinMo(self):
        string = str(self.soup)
        string = string.replace("\n", "")
        word = re.findall(u'刷新.*?请选择出口', string)
        print(word)
        if len(word) == 1:
            if '系统' in word[0] or '喇叭' in word[0] or '【' in word[0]:
                return 0
            word1 = re.findall('x=.{0,50}\">', word[0])
            if len(word1) != 1:
                return 0
            ans = word1[0].replace('x=', '')
            ans = ans.replace('\">', '')
            self.url = self.preUrl + ans
            self.getHtml()
            return 1
        else:
            return 0

    # 使用药品
    def userMedicine(self, name):
        # <a href="c.rosyclouds?u=xxm233381&amp;x=Q1UiVJnV8iLKR3On0oPw86_k1FD644m0nnnr_"><img alt="感叹号" src="img.rosyclouds?uid=233381&amp;src=O__xd8u76KKdSKFldBShg2Vk6hw7b5k7D4TdXaeL5GBcJXbHx6O7dlRx8k1vIQDW"/>激活变异竹林副本(梦魇)</a><br/>
        string = str(self.soup)
        ans = re.search(u'' + name + '.*?href=\"([^\"]*)\">使用', string)
        ans = ans.group(1).split('x=')[1]
        self.url = self.preUrl + ans
        self.getHtml()
        return self.url
