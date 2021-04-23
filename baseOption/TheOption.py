class TheOption:
    optionList = []
    getShangjing = ['继续', '返回', '返回', '腾云', '长安', 2, 2, '赏金猎人', '199级', '继续', '返回', '返回', '赏金猎人', '199级']
    dailyDust = ['继续', '返回', '返回', '腾云', '长安', '状态', '毫毛', '领取', '返回', '返回', '福利', '每日签到', '每日签到', '继续', '返回', '重阳节', '重阳领', '继续', '返回', '返回', 4, '幸运大使', '运气', '继续', '返回', '返回', 6, 6, 6, '神算子', '算', '继续', '返回', '返回', 4, 4, 2, 4, '剧场负责人', '每天一次', '继续', '观看']

    tongTianTa = ['继续', '返回', '返回', '腾云', '通天塔', '通天仙官', '挑战通天塔', '继续']
    SHI_FANG_ZHEN = ['继续', '返回', '返回', '十方',]
    xinshouqu = ['继续', '返回', '返回', '腾云', '新手专区', '材料区']
    goTOSquare = ['继续', '返回', '返回', '腾云', '长安', '李白', '返回李白', '开封广场', 6, 8, '传送员', '200', '返回上级', '159', 6, 6, 6, 6, 2, 2, 2, 2, 6]

    # 4/22 1次
    jingDouDong = ['继续', '返回', '返回', '腾云', '金兜', '金兜山土地神', '激活', '继续', 8, 8, 4, 8, '花豹将军', 2, 6, 8, 8, '鹿头军师', 2, 2, 2, 2, 6, 6, 8, 8, '山妖头目', 2, 2, 6, '金兜大王', '金兜宝箱', '继续']

    # 4/22 3次
    yaBiao = ['继续', '返回', '返回', '状态', '十年', '出门', '十字', 6, 6, 6, 8, 4, '林镖头', '接取镖车', '返回上级', '返回游戏', 6, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 4, '月老', '完成押镖任务', '继续', '返回游戏']
    # 白骨陵墓 4/22
    baiGuLingMu = ['继续', '返回', '返回', '腾云', '白骨陵墓', '梦魇', '继续', 6, 8, 6, 8, 6, 6, 2, 2, '食尸鬼', 8, 8, 6, 2, 2, '剥皮鬼', 8, 8, 6, 6, '炼尸鬼', 4, 4, 8, 8, 4, 4, 4, 8, 8, '白骨将', 8, 6, 6, 6, '大祭祀', 2, 2, 4, 8, 6, '白骨夫人', '白骨宝箱', "继续"]
    # 天宫瑶池   4/22确认ok 2次
    tianGongYaoChi = ['继续', '返回', '返回', '腾云', '天宫瑶池', u'激活', u'继续', '瑶池巡卫', 8, 8, u'瑶池守将', 4, 4, u'仙子', 6, 6, 6, 6, u'仙女', 4, 4, 8, 8, u'王母', u'宝箱', u'继续']
    # 水帘洞 确认OK 2次
    shuiLianDong = ['继续', '返回', '返回', '腾云', '水帘洞', '梦魇', '继续', 6, 6, '通天教头', 6, 8, u'独角', 2, 6, 2, u'混世', 2, 4, 4, 8, u'魔王', u'宝箱', u'继续']
    # 水帘洞  1次
    shuiLianDong_vip = ['继续', '返回', '返回', '腾云', '水帘洞', '水帘洞',  6, 6, '通天教头', 6, 8, u'独角', 2, 6, 2, u'混世', 2, 4, 4, 8, u'魔王', u'宝箱', u'继续']
    # 变异竹林 确认OK 1次 大于3转不能进
    bianYiZhuLin = ['继续', '返回', '返回', '腾云', '变异', '梦魇', '继续', 6, 6, 6, u'蓝', 6, 8, 6, 8, u'无影', 2, 4, 2, 2, 6, 2, 2, u'黄雀', 8, 8, 6, 8, u"妖王", 6, 6, u'鬼门', u"宝箱", "继续"]
    # 化生寺  确认OK 1次 Ok
    huaShengShi = ['继续', '返回', '返回', '腾云', '化生寺', '法明长老', '化生寺副本', '返回', '返回', '任务', '下\.页', '化生寺副本', '化生寺戒律院', '戒律院主持', 8, '护寺棍僧', 8, '护寺棍僧', 8, '护寺棍僧', 8, '护寺棍僧', 8, '护寺棍僧', 8, '罗汉堂主持', 2, '护寺棍僧', 2, 2, '护寺棍僧', 6, 6, 6, '化生寺老主持','化生寺主持', '进入藏经阁', '藏经阁书架', '继续', '法明长老', '化生寺副本', '继续', '返回上级', '返回游戏']
    huaShengShi_vip = ['继续', '返回', '返回', '状态','可点','副本', '化生寺',  '返回', '任务', '下\.页', '化生寺副本', '化生寺戒律院', '戒律院主持', 8, '护寺棍僧', 8, '护寺棍僧', 8, '护寺棍僧', 8, '护寺棍僧', 8, '护寺棍僧', 8, '罗汉堂主持', 2, '护寺棍僧', 2, 2, '护寺棍僧', 6, 6, 6, '化生寺老主持','化生寺主持', '进入藏经阁', '藏经阁书架', '继续', '法明长老', '化生寺副本', '继续',
                       '返回上级',
                    '返回游戏']

    # 冰晶塔 确认OK 有问题
    bingJingTa = ['继续', '返回', '返回', '腾云', '晶', '冰晶塔守卫', '西阁', '宝帐怙主', 8, '迷途小沙弥', 8, '迷途小沙弥', 6, '迷途小沙弥', 6, '迷途小沙弥', 6, '迷途小沙弥', 6, '迷途小沙弥', 2, 2, '措达怙主', 2, '迷途小沙弥', 2, '迷途小沙弥', 4, '迷途小沙弥', 4, '轮回使者', 8, '迷途小沙弥', 4, 8, 6, '堕落神将', '任务', '下\.页', '冰晶塔副本', '冰风谷迷宫', '冰晶塔守卫', '返回游戏']
    bingJingTa_vip = ['继续', '返回', '返回', '任务', '冰晶塔', '西阁', '宝帐怙主', 8, '迷途小沙弥', 8, '迷途小沙弥', 6, '迷途小沙弥', 6, '迷途小沙弥', 6, '迷途小沙弥', 6, '迷途小沙弥', 2, 2, '措达怙主', 2, '迷途小沙弥', 2, '迷途小沙弥', 4, '迷途小沙弥', 4, '轮回使者', 8, '迷途小沙弥', 4, 8, 6, '堕落神将', '任务', '下\.页', '冰晶塔副本', '冰风谷迷宫', '冰晶塔守卫', '返回游戏']
    # 枉死城 确认OK 2次 大于3转不能进
    wangSiCheng = ['继续', '返回', '返回', '腾云', '枉死城', '夜游鬼', '梦', '继续', 4, 8, 4, 4, '索命无常', 2, 4, '鬼面判官', 6, 6, 2, 2, 4, 4, 8, '夜叉王', '鬼面宝箱', '返回游戏', '枉死城入口']
    # 压龙洞 确认OK 2次
    yaLongDong = ['继续', '返回', '返回', '腾云', '压', '激活', '继续', 6, 8, 6, 6, 2, 2, 6, '百花娘子', 2, 6, 6, 6, 2, 6, '狐女', 4, 8, 4, 4, 4, 8, 4, 8, 8, 8, 8, 8, 8, '狐将军', 2, 2, 2, 6, 2, '狐长老', 6, 6, 6, 6, 2, 4, '拨地鼠精', 6, 6, 6, 6, 6, '天香夫人', '黑龙敖厉', '黑龙宝箱', '继续']
    # 老君炉  确认OK 2次
    laoJunLu = ['继续', '返回', '返回', '腾云', '天宫', '接引仙子', '返回接引仙子', '老君炉', '太上老君', '太上老君', '梦魇', '继续', 2, 6, 2, 2, 4, '九趾蟠龙', 6, 6, 6, 8, 8, 8, 4, '九天应龙', 2, 6, 2, 2, 6, 2, 6, '赤足青鸟', 4, 2, 6, 6, 2, 2, 2, 2, '昊冥玄鸟', 6, 6, '金眼狻猊', '老君宝箱', '继续']
    # 通天府  大号手动打!!
    tongTianFu = ['继续', '返回', '返回', '腾云', '通天水府', '困难', '继续', 6, 2, '黑鳞鲛人', 8, 6, 6, 6, '倚海龙王', 8, 8, 8, '银鳞大王', 2, 2, 2, 6, 6, 6, '金鳞大王', '金鳞宝箱', '继续']
    # 波月洞 确认OK 两次 大于5转不能进
    boyueDong = ['继续', '返回', '返回', '腾云', '波月洞', '梦魇', '继续', 6, 2, 2, 2, 2, '巡逻妖将', 8, 8, 8, 8, 8, 8, 6, 6, 6, '黑熊厨子', 4, 4, 4, 2, 2, 6, 6, 6, 6, 6, 8, 6, 6, 2, '山妖将军', 8, 4, 4, 2, 4, 2, 2, 6, 2, 2, '野鹿大王', 8, 8, 6, 6, 2, '野熊大王', 8, 6, '黄袍老妖', '波月宝箱', '继续']
    # 平顶山莲花洞 确认OK 两次
    lianHuanDong = ['继续', '返回', '返回', '腾云', '莲花洞', '激活', '继续', 2, 6, 8, 6, 6, 8, '传令妖将', 2, 2, 2, 4, 2, 6, 2, '监察妖将', 8, 4, 8, 6, 8, 8, 6, 6, 2, 6, '训练妖将', 4, 8, 4, 8, 8, 6, 6, 6, '守备妖将', 8, '银角大王', 2, 2, '金角大王', '莲花宝箱', '继续']

    # 火焰山
    huoYanShan = ['继续', '返回', '返回', '腾云','火焰山洞',6, '进入火焰山洞', '火云恶龙', 6, '火焰君王', '完成副本', '继续']

    #五色琉璃塔 待测试
    LIU_LI_TA = ['继续', '返回', '返回', '腾云','五色琉璃塔', '迎客僧', '住持佛牌一', '副本', 2, 6, '百花羞', 6,6,2,2,6,6,6,'四翼蛇精',6,2,2,2,2,2,2,'烛阴',2,6,6,6,6,2,2,6,'狡兔妖后',6,6,2,2,2,2,6,6,6,'蓝彩毒后','完成']

    #芭蕉洞 待测试
    BA_JIAO_DONG = ['继续', '返回', '返回', '腾云','芭蕉洞', '激活', '发现',8,6,2,'云里雾',4, '雾里云',6,8,6,8,'千年芭蕉精',8,8,'牛魔王',]
    BA_JIAO_DONG = ['继续', '返回', '返回', '腾云','小雷音寺', '激活【小雷音寺副本】', '守门僧','进入',8,6,6,2,'守门金刚',8,8, '灵山接引僧',2,6,6,6,'迦叶',6,'青莲妖女',8,6,'黄眉老佛','黄眉宝']

    def __init__(self):
        self.optionList = [self.tianGongYaoChi, self.tianGongYaoChi, self.shuiLianDong, self.shuiLianDong, self.baiGuLingMu, self.baiGuLingMu, self.bingJingTa, self.huaShengShi, self.lianHuanDong,
                           self.lianHuanDong, self.yaLongDong, self.yaLongDong, self.laoJunLu, self.laoJunLu, self.tongTianFu, self.jingDouDong, self.huoYanShan, self.huoYanShan]
