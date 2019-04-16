import wx
import os


class Mywin(wx.Frame):

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title)

        self.InitUI()

    def InitUI(self):
        self.count = 0
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        # 顶层帧显示按钮和一个多行TextCtrl
        self.text = wx.TextCtrl(pnl, size=(-1, 200), style=wx.TE_MULTILINE)
        self.btn1 = wx.Button(pnl, label="Open a File")

        # EVT_BUTTON事件绑定注册 OnClick() 函数到按钮。
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn1)

        hbox1.Add(self.text, proportion=1, flag=wx.ALIGN_CENTRE)
        hbox2.Add(self.btn1, proportion=1, flag=wx.RIGHT, border=10)

        vbox.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTRE)

        vbox.Add(hbox1, proportion=1, flag=wx.EXPAND | wx.ALIGN_CENTRE)

        pnl.SetSizer(vbox)
        self.Centre()
        self.Show(True)

    def OnClick(self, e):
        """OnClick()函数显示一个FileDialog的打开模式。其选择返回为dlg。通过GetPath()函数获得的选定文件和它的内容显示在父窗口的TextCtrl框"""
        wildcard = "Text Files (*.txt)|*.txt"
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            f = open(dlg.GetPath(), encoding='gbk')

            with f:
                data = f.read()
                self.text.SetValue(data)
        dlg.Destroy()


ex = wx.App()
Mywin(None, 'FileDialog Demo - www.yiibai.com')
ex.MainLoop()

