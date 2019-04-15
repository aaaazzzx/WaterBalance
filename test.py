import wx    #1 导入必备的wxPython包

class App(wx.App):    #2 子类化wxPython应用程序类

    def OnInit(self):    #3 定义一个应用的初始化方法
        frame = wx.Frame(parent=None,title="Bare")
        frame.Show()
        return True

app=App()    #4 创建一个应用程序类的实例
app.MainLoop()    #5 进入这个应用程序的主事件循环


# 已完成： https://blog.csdn.net/qq_35203425/article/details/78568141

#  1.建立xxx.py程序   test.py
#  2.cmd     pyinstaller xxx.py    pyinstaller test.py