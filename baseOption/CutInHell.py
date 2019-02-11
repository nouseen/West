#地府刷怪
from baseOption import WayOrCut
from baseOption.TheWay import TheWay
class CutInHell:
    way=TheWay.wayInHell
    #刷一趟回来
    def __init__(self,url,preUrl):
        self.wayOrCat=WayOrCut(url,preUrl)
        self.wayOrCat.getHtml()
    def cutInHell(self):
        j=0
        while j<9:
            for i in self.way[0]:
                if self.wayOrCat.getWay(i)==1:
                    self.wayOrCat.getHtml()
            self.wayOrCat.cutMonster("\*【")
            for i in self.way[1]:
                self.wayOrCat.getWay(i)
                self.wayOrCat.getHtml()
            for i in self.way[2]:
                self.wayOrCat.getWay(i)
                self.wayOrCat.getHtml()
            self.wayOrCat.cutMonster("\*【")
            for i in self.way[3]:
                self.wayOrCat.getWay(i)
                self.wayOrCat.getHtml()
        for i in self.way[4]:
                self.wayOrCat.getWay(i)
                self.wayOrCat.getHtml()