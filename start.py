import wx
import os
import pandas as pd
import WaterBalance
import numpy as np


# import the newly created GUI file
import WB01


class CalcFrame(WB01.WB01):
    def __init__(self, parent):
        WB01.WB01.__init__(self, parent)

    #############################################################################
    # 需水计算
    def InExcel01(self, event):
        """用于输入非生态需水"""
        global Non_environment        # 非生态需水
        wildcard = "Excel 工作簿(*.xlsx)|*.xlsx|Excel 97-2003 工作簿(*.xls)|*.xls"
        f = wx.FileDialog(self, "选择非生态需水文件", os.getcwd(), "", wildcard, wx.FD_OPEN)

        if f.ShowModal() == wx.ID_OK:
            Non_environment = pd.read_excel(f.GetPath())
            # self.m_textCtrl9.SetValue()
        f.Destroy()
        # print(Non_environment)
        # return Non_environment

    def InExcel02(self, event):
        """用于输入生态需水"""
        global environment        # 生态需水
        wildcard = "Excel 工作簿(*.xlsx)|*.xlsx|Excel 97-2003 工作簿(*.xls)|*.xls"
        f = wx.FileDialog(self, "选择生态需水文件", os.getcwd(), "", wildcard, wx.FD_OPEN)

        if f.ShowModal() == wx.ID_OK:
            environment = pd.read_excel(f.GetPath())
            # self.m_textCtrl9.SetValue()
        f.Destroy()
        # print(environment)
        # return Non_environment

    def WaterNeed( self, event ):
        """用于计算最终需水"""

        # Non_environment
        m1, n1 = Non_environment.shape[0],Non_environment.shape[1]   # m为行，n为列
        # print(m1, n1)
        # environment
        m2, n2 = environment.shape[0], environment.shape[1]   # m为行，n为列
        # print(m2, n2)
        if m2 != m1-2 :
            self.m_textCtrl9.SetValue("长度不一致")
            return

        # 开始赋值
        names = globals()
        Non_environment_WaterNeed =  np.zeros([m1-2,n1])
        a = []
        for i in range(n1):
            names['Non_environment%s' %i] = WaterBalance.GuanGai(Non_environment.columns.values.tolist()[i], Non_environment.iloc[1, i],Non_environment.iloc[2:, i].values, Non_environment.iloc[0, i])
            a.append(names['Non_environment%s' %i])
        # print(a[0].name)
        # print(a[0].Need())
            # print(a[i].Need())
            Non_environment_WaterNeed[:, i] = a[i].Need()
        # print(Non_environment_WaterNeed)
        Non_environment00 = WaterBalance.WaterNeed("Non_environment_WaterNeed", 1, Non_environment_WaterNeed.sum(axis=1))
        # print(Non_environment00.Need())
        # print(Non_environment_WaterNeed)
        # print(Non_environment1.dinge)
        # print(Non_environment1.size)
        # print(Non_environment1.Need())

        global environment0
        environment0 = WaterBalance.WaterNeed('environment', 1, environment.iloc[:, 0].values)
        # print(environment0.name)
        # print(environment0.dinge)
        # print(environment0.Need())


        global Final_Watter_Need
        # print(environment0.Need(), Non_environment00.Need())
        Final_Watter_Need = WaterBalance.Final_Need(environment0, Non_environment00)

        print('最终需水:', Final_Watter_Need)


    #############################################################################
    # 供水能力计算

    def InExcel03( self, event ):
        """用于输入降水"""
        global Rain        # 非生态需水
        wildcard = "Excel 工作簿(*.xlsx)|*.xlsx|Excel 97-2003 工作簿(*.xls)|*.xls"
        f = wx.FileDialog(self, "选择降水", os.getcwd(), "", wildcard, wx.FD_OPEN)

        if f.ShowModal() == wx.ID_OK:
            Rainf = pd.read_excel(f.GetPath())
            # self.m_textCtrl9.SetValue()
        f.Destroy()
        Rain = WaterBalance.Rain( Rainf.iloc[:, 0].values, Rainf.iloc[0, 1], Rainf.iloc[0, 2])
        print(Rain.rain, Rain.area, Rain.Production_rate, Rain.Production())
        # print(Non_environment)
        # return Non_environment

    '''
    def InStorage(self, event):
        global StorageCapacity
        StorageCapacity = self.m_textCtrl13.GetValue()
        # print(N)
    def InStorage_Min(self, event):
        global StorageCapacity_Min
        StorageCapacity_Min = self.m_textCtrl14.GetValue()
    '''


    def WaterAvailable01(self, event):
        # 计算降雨产水的可用水量
        # 需要修改
        global wateravailable
        global river
        wateravailable = []
        StorageCapacity = float(self.m_textCtrl13.GetValue())
        StorageCapacity_Min = float(self.m_textCtrl14.GetValue())
        river = WaterBalance.RiverStorageCapacity(StorageCapacity,StorageCapacity_Min)
        # print(river.)

        # print(Rain.Production())
        wateravailable = river.WaterAvailable(Rain.Production(), Final_Watter_Need)    # 经河道调蓄后的缺水量
        print('经河道调蓄后的缺水量:', wateravailable)


    def InExcel04(self, event):
        # 导入外河水位
        global waterlevel        # 外河水位
        waterlevel = []
        wildcard = "Excel 工作簿(*.xlsx)|*.xlsx|Excel 97-2003 工作簿(*.xls)|*.xls"
        f = wx.FileDialog(self, "外河水位", os.getcwd(), "", wildcard, wx.FD_OPEN)

        if f.ShowModal() == wx.ID_OK:
            waterlevel = pd.read_excel(f.GetPath())
            # self.m_textCtrl9.SetValue()
        f.Destroy()


    def FinalWaterAvailable(self, event):
        waihe01 = WaterBalance.Waihe(waterlevel.iloc[:, 0].values)    # 输入外河水位
        waihe01.WaterIn()     # 计算外河可进水量
        # 外河供水量
        Final_WaterAvailable01 = []
        Final_Watershortage01 = []
        print('外河供水能力：', waihe01.Water)
        print('经河道调蓄后的缺水量：', wateravailable)
        Final_WaterAvailable01, Final_Watershortage01 = WaterBalance.Final_WaterAvailable(waihe01.Water, wateravailable)    # 外河供水量，缺水量 WaterBalance.Final_WaterAvailable
        print('外河供水量：', Final_WaterAvailable01)
        print('缺水量：', Final_Watershortage01)





    def test( self, event ):
        """用于测试"""
        print(Non_environment)

    ############################
    # 系列长度
    # N = WB01.WB01.m_textCtrl10.GetValue()
    # print(N)
    def InNub( self, event):
        global N
        N = int(self.m_textCtrl10.GetValue())
        # print(range(N))

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()
