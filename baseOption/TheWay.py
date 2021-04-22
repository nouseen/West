

class TheWay:
    way4Plus4 =["2","2","2","6","6","6","8","8","8","4","2","2","4","8","8","4"]
    way4Plus5=[2,2,2,6,6,6,6,8,4,4,4,8,6,6,6,8,4,4,4,4]
    way5Plus5=[8,8,8,8,4,2,2,4,4,8,6,8,8,4,2,4,8,2,2,2,2,6,6,6,6]
    wayInHell=[["4","2","2","2","2","2","2","6","6","6","6","6"],["4","4","4","4","4","4","8","8","8","8","8","8"],["8","6","6","6","6","6"],["4","4","4","4","4","2"]]
    hellBack=[6,6,6,6,6,6,6,6,6]
    GuiMenGuanToTurning=[2,4]
    wayToCrab=[6,8,8,8,8]
    #一路走不砍怪
    def gobyWay(self,wayOrCut,theWay):
        for i in theWay:
            wayOrCut.getWayAndGo(i)
    #走一步砍个怪
    def cutMonsterByWay(self,wayOrCut,theWay,monster):
        for i in theWay:
            print(i)
            if wayOrCut.getWay(i)==1:
                wayOrCut.getHtml()
            wayOrCut.cutMonster(monster)
    def cutMonsterByWayBySkill(self,wayOrCut,theWay,monster,skill):
        #恶魔广场专用
        for i in theWay:
            print(i)
            if wayOrCut.getWay(i)==1:
                wayOrCut.getHtml()
            wayOrCut.cutMonsterBySkill(monster,skill)
    def forThings(self,wayOrCut,theWay,monster,skill):
        #刷材料专用
        while 1==1:
            for i in theWay:
                if wayOrCut.getWay(i)==1:
                    wayOrCut.getHtml()
                    wayOrCut.cutMonsterBySkill(monster,skill)