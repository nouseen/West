import re
import time

from bs4 import BeautifulSoup
import requests

class WayOrCut:
        def __init__(self,url,preUrl):
            self.url = url
            self.preUrl=preUrl
            self.act="连接成功"
        #打开当前URL
        def getHtml(self):
            time.sleep(0.4)
            wb_data = requests.get(self.url)
            self.soup=BeautifulSoup(wb_data.text,'html')
            print(self.act)
            print(self.soup)
            return self.soup
        #获取上下左右
        def getWay(self,way):
            fresh=self.soup.find('a', {'accesskey':way})
            if fresh==None: 
                return 0
            h_fresh=fresh['href']
            p=h_fresh.split('x=')
            self.url=self.preUrl+p[1]
            self.act=way;
            return 1
        def getWayAndGo(self,way):
            fresh=self.soup.find('a', {'accesskey':way})
            if fresh==None: 
                return 0
            h_fresh=fresh['href']
            p=h_fresh.split('x=')
            self.url=self.preUrl+p[1]
            self.act=way
            self.getHtml()
            return 1
        #获取操作URL
        def getOperation(self,op):
            refresh=self.soup.find('a',text=re.compile(op))
            if refresh==None:
                return 0 
            hr = refresh['href']
            p=hr.split('x=')
            self.url=self.preUrl+p[1]
            self.act=op
            return 1;
        def getOperationAndGo(self,op):
            refresh=self.soup.find('a',text=re.compile(op))
            if refresh==None:
                return 0 
            hr = refresh['href']
            p=hr.split('x=')
            self.url=self.preUrl+p[1]
            self.act=op
            self.getHtml()
            return 1;
        
        def cutMonster(self,name,skill):
        #砍完怪
            while self.getOperation(name)==1:
                self.getHtml()
                if self.getOperation("攻击")==1:
                    self.getHtml()
                while self.getOperation(skill)==1:
                    self.getHtml()
                if self.getOperation("返回")==1:
                    self.getHtml()
            print("砍完1个怪")
        #连续砍怪
        def useSkill(self,skill):
            while self.getOperation(skill)==1:
                self.getHtml()
                if self.getOperation("返回游戏")==1:
                    self.getHtml()
               
        #连续继续
        def  gameContinue(self):
            while self.getOperation("继续")==1 or self.getOperation('返回'):
                    self.getHtml()
        def CoudeToAnyWhere(self,way):  
            self.getOperationAndGo("腾云")
            self.getOperationAndGo(way)    
        def matchByhand(self,name):  
            #<a href="c.rosyclouds?u=xxm233381&amp;x=Q1UiVJnV8iLKR3On0oPw86_k1FD644m0nnnr_"><img alt="感叹号" src="img.rosyclouds?uid=233381&amp;src=O__xd8u76KKdSKFldBShg2Vk6hw7b5k7D4TdXaeL5GBcJXbHx6O7dlRx8k1vIQDW"/>激活变异竹林副本(梦魇)</a><br/>
            string=str(self.soup)
            word = re.findall(u'href.{100,300}'+name,string) 
            word1 = re.findall('x=.{0,50}_\"',word[0]) 
            ans= word1[0].replace('x=','')
            ans=ans.replace('\"','')
            self.url=self.preUrl+ans
            return self.url