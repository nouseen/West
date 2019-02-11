from baseOption.TheOption import TheOption


class Dungeons:
    option = TheOption()
    def bingJingTa(self,wayOrCut):
        wayOrCut.gameContinue()
        wayOrCut.CoudeToAnyWhere('晶')
        for i in self.option.BingJingTa:
            wayOrCut.getOperationAndGo(i)
            wayOrCut.useSkill("举火")
            wayOrCut.cutMonster("沙", '举火')
    def huaShengShi(self,wayOrCut):
#         wayOrCut.gameContinue()
#         wayOrCut.CoudeToAnyWhere('化生')
        for i in self.option.ShengHuaShi:
            print(i)
            wayOrCut.getOperationAndGo(i)
            wayOrCut.useSkill("举火")
    def bianYiZhuLin(self,wayOrCut):
        for i in self.option.BianYiZhuLin:
            print(i)
            if i==6 or i==4 or i==2 or i==8:
                wayOrCut.getWayAndGo(i)
            else:
                wayOrCut.getOperationAndGo(i)
            wayOrCut.useSkill("举火")
            