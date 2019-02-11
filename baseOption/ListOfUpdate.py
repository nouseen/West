from baseOption.PreUrl import PreUrl
from baseOption.TheWay import TheWay
from baseOption.WayOrCut import WayOrCut


url='http://f12.mxxy.paop.net/game_mxxy2/s12/c.rosyclouds?u=xxm233739&x=QmD5GtxZgeekFyQfV5kvMqROVVqiioyxxRxV'
wayOrCut = WayOrCut(url,PreUrl.preUrl4159)
way = TheWay()
wayOrCut.getHtml()
#wayorcut.gameContinue()
# wayorcut.getOperation('将军府')
# wayorcut.getHtml()
#wayorcut.gameContinue()
# wayorcut.getWay(2) 
# wayorcut.getHtml()
#wayorcut.getOperationAndGo('大宝')
# way.wayToCrab(wayorcut,way.wayToCrab)
# i=0
# while i<=10:
#     way.cutMonsterByWay(wayOrCut,way.way4Plus4,"螃")
#     i=i+1
#     print(i)
# wayOrCut.getOperationAndGo("腾云")
# wayOrCut.getOperationAndGo("地府")
#way.gobyWay(wayOrCut, way.GuiMenGuanToTurning)
#地府刷怪 
while 1==1:
    m=0
    while m<9:
        m=m+1
        for i in way.wayInHell:
            way.gobyWay(wayOrCut,i)
            wayOrCut.cutMonster("\*【", "霸王枪")
    way.gobyWay(wayOrCut, way.hellBack)
#转职
# wayOrCut.getOperationAndGo("腾云")
# wayOrCut.getOperationAndGo("长安")
# wayOrCut.getOperationAndGo("张果老")
#wayOrCut.getOperationAndGo("轮回")
# wayOrCut.getOperationAndGo("100银")
# wayOrCut.getOperationAndGo(" 确认")
