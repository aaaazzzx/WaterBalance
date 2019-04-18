# 用于水量平衡计算
# 基于《南县南汉垸、和康垸水资源配置报告》、算表《和康垸北河口水量平衡》编写


import numpy as np


# 1.计算需水:生态、其他（灌溉、鱼塘、牲畜）

class WaterNeed():
    """需水"""

    def __init__(self,name,dinge):
        """初始化属性名字和定额"""
        self.name = name
        self.dinge = dinge

    def Need(self):
        """需求计算"""
        return self.dinge

class GuanGai(WaterNeed):
    """灌溉用水"""
    def __init__(self,name,dinge,size):
        """初始化父类属性"""
        super().__init__(name,dinge)
        self.size = size    # 面积
    def Need(self):
        """需求计算"""
        return self.dinge*self.size

# Early_rice = GuanGai("Early_rice",np.array([13,11]),1)
# Middle_rice = GuanGai("Middle_rice",np.array([10,8]),1)
# Later_rice = GuanGai("Later_rice",12,12)
# Rape = GuanGai("Rape",12,12)    # 油菜
# Cotton = GuanGai("Cotton",12,12)   # 棉花
# Pond = GuanGai("Pond",12,12)    # 鱼塘
# livestock_L = GuanGai("livestock_L",12,12)    # 大牲畜
# livestock_S = GuanGai("livestock_S",12,12)    # 小牲畜
#
# environment = WaterNeed("shuidao",np.array([12,12]))    # 生态用水



def Final_Need(environment,Non_environment):
    """计算最终需水:比较生态需水与其他需水,取较大值"""
    # 暂时略过其他需水之和计算
    # n = len(Non_environment.Need)
    n = 2 # 暂时设置定额序列长度为1

    Final_Watter_Need = []
    for i in range(n) :
        if environment.Need()[i]>= Non_environment.Need()[i] :
            Final_Watter_Need.append(environment.Need()[i])
        else:
            Final_Watter_Need.append(Non_environment.Need()[i])
    return Final_Watter_Need

# Non_environment = WaterNeed("Non_environment_WaterNeed",Early_rice.Need()+Middle_rice.Need())
# print( Final_Need(environment,Non_environment))

class Rain():
    """降雨"""
    def __init__(self,rain,area,Production_rate):
        """初始化属性降雨量"""
        self.rain = rain
        self.area = area
        self.Production_rate = Production_rate
        self.production = []
    def Production(self):
        self.production = self.rain * self.area * self.Production_rate
        return self.production

# rain1 = Rain(np.array([13,11]),1,0.5)
# print(rain.rain)
# print(rain1.Production())

class RiverStorageCapacity():

    def __init__(self,StorageCapacity,StorageCapacity_Min):
        """初始化河道库容"""
        # StorageCapacity 初始水量
        self.StorageCapacity = StorageCapacity
        self.StorageCapacity_Min = StorageCapacity_Min  # 输入最低库容
        self.RiverWaterNeed = []  # 经河道调蓄后的缺水量
    """
        self.StorageCapacity_Min = 389.37    # 固定最低库容
    def StorageCapacityMin(self,StorageCapacity_Min):
        # 提供修改最低库容的方式
        self.StorageCapacity_Min = StorageCapacity_Min
    """
    def Waterlevel(self):
        # 此处暂时取用公式 StorageCapacity*0.0688-0.0022
        waterlevel = self.StorageCapacity *0.0688-0.0022
        return waterlevel

    def WaterAvailable(self,Rain_Production, WaterNeed):
        """计算河道可供水量，同时更新河道水量"""
        # Rain_Production:降雨产水序列 WaterNeed：需水序列
        wateravailable = np.zeros(len(Rain_Production))   # 河道供水能力
        for i in range(len(Rain_Production)):
            print(self.StorageCapacity, Rain_Production, self.StorageCapacity_Min,wateravailable)
            wateravailable[i] = self.StorageCapacity + Rain_Production[i] - self.StorageCapacity_Min
            if wateravailable[i] >= WaterNeed[i]:
                self.StorageCapacity = self.StorageCapacity + Rain_Production[i] - WaterNeed[i]
                self.RiverWaterNeed.append(0)
                # return WaterNeed
            else:
                self.StorageCapacity = self.StorageCapacity_Min
                self.RiverWaterNeed.append(WaterNeed[i] - wateravailable[i])
                # return wateravailable
        return self.RiverWaterNeed

# river = RiverStorageCapacity(401)
# print(river.Waterlevel())
# print(river.StorageCapacity_Min)
# Need = (Final_Need(environment,Non_environment))
# print(Need[0])
# print(river.WaterAvailable(rain1.production[0],Need[0]))





class Waihe():
    """外河可供水量"""
    def __init__(self,waterlevel):
        self.waterlevel = waterlevel
        self.waterlevel_Min = 26.2    # 固定地板高层
        self.Water = []
    def WaterIn(self):
        for i in range(len(self.waterlevel)):
            if self.waterlevel[i] >= self.waterlevel_Min:
                """计算可进水量，时间为10天"""
                self.Water.append(1 * 1.5 * (self.waterlevel[i] - self.waterlevel_Min) * 365 * 24 * 10 / 10000)
            else:
                self.Water.append(0)

# Waihe = Waihe(27.44)
# print(Waihe.waterlevel,Waihe.waterlevel_Min)
# print(Waihe.WaterIn())

def Final_WaterAvailable(WaterIn,RiverWaterNeed):
    """最终可供水量"""
    """修改此处输出"""
    global Final_WaterAvailable
    global Final_Watershortage
    Final_WaterAvailable = []
    Final_Watershortage = []
    for i in range(len(WaterIn)):
        print(WaterIn, RiverWaterNeed)
        if WaterIn[i] > RiverWaterNeed[i]:
            Final_WaterAvailable.append(RiverWaterNeed[i])
            Final_Watershortage.append(0)
        else:
            Final_WaterAvailable.append(WaterIn[i])
            Final_Watershortage.append(RiverWaterNeed[i] - WaterIn[i])
    return Final_WaterAvailable,Final_Watershortage
# print(Final_WaterAvailable(Waihe.WaterIn(),river.RiverWaterNeed))