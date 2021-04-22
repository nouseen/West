import threading

from baseOption.Dungeons import Dungeons
from baseOption.TheOption import TheOption


class NewDailyTask(threading.Thread):
    def __init__(self,wayOrCut,mark):
        threading.Thread.__init__(self)
        self.mark=mark
        self.wayOrCut=wayOrCut
        self.dungeons=Dungeons()
        self.option=TheOption()
        self.dungeons=Dungeons()
    def run(self):
        #1 每日领奖
        self.wayOrCut.getHtml()
        self.wayOrCut.gameContinue()
        self.dungeons.common(self.wayOrCut,self.option.dailyDust)
        self.dungeons.watchMovie(self.wayOrCut)
        #2副本
        if self.mark==1:
            self.dungeons.common(self.wayOrCut, self.option.jingDouDong)

        self.dungeons.tongTianTa(self.wayOrCut, '【')
        self.dungeons.common(self.wayOrCut,self.option.tongTianFu)
        self.dungeons.common(self.wayOrCut,self.option.tongTianFu)
        self.dungeons.guojia(self.wayOrCut)
        self.dungeons.couple(self.wayOrCut)
        self.wayOrCut.gameContinue()
        self.dungeons.allDungeonsAuto(self.wayOrCut, '回马')
        #3 押镖
        i=0
        while i<3:
            i+=1
            self.dungeons.commonBySkill(self.wayOrCut, self.option.yaBiao,"举火")
        #5 赏金降妖夫国家
        self.dungeons.xiangYao(self.wayOrCut)
        self.dungeons.shangJing(self.wayOrCut)