from baseOption.Dungeons import Dungeons
from baseOption.PreUrl import PreUrl
from baseOption.TheWay import TheWay
from baseOption.WayOrCut import WayOrCut


url='http://f12.mxxy.paop.net/game_mxxy2/s12/c.rosyclouds?u=xxm233381&x=Q1UiVJnV8iLKR3On0oPw86_CXBD644m0nnnr_'
wayOrCut = WayOrCut(url,PreUrl.preUrl8128)
way = TheWay()
dungeons=Dungeons()
wayOrCut.getHtml()

# wayOrCut.getOperationAndGo("")
# while 1==1:
#     way.cutMonsterByWay(wayOrCut, way.way4Plus4, "\*【")
#     wayOrCut.getWayAndGo(4)
#     way.cutMonsterByWay(wayOrCut,way.way5Plus5,"\*【")
#     wayOrCut.getWayAndGo(6)

#dungeons.bingJingTa(wayOrCut)
#dungeons.huaShengShi(wayOrCut)
# dungeons.bianYiZhuLin(wayOrCut) 

# print(wayOrCut.getOperation("刷新"))
# wayOrCut.getHtml() 
print(wayOrCut.matchByhand(u'金豆'))