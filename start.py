import wx
import os
# import the newly created GUI file
import WB01


class CalcFrame(WB01.WB01):
    def __init__(self, parent):
        WB01.WB01.__init__(self, parent)

    def InitUI(self, event):
        """用于测试的输入框"""
        wildcard = "Text Files (*.txt)|*.txt"
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            f = open(dlg.GetPath(), encoding='gbk')
            with f:
                data = f.read()
                self.m_textCtrl9.SetValue(data)
        dlg.Destroy()

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()
