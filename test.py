import wx    #1 导入必备的wxPython包
import Demo


class App(wx.App):    #2 子类化wxPython应用程序类

    def OnInit(self):    #3 定义一个应用的初始化方法
        frame = Calculation(None)
        frame.Show()
        return True

class Calculation(Demo.First):
    def __init__(self, parent):
        Demo.First.__init__(self, parent)

    def FindSquare(self, event):
        num = int(self.m_textCtrl1.GetValue())
        self.m_textCtrl2.SetValue(str(num * num))


app=App()    #4 创建一个应用程序类的实例
app.MainLoop()    #5 进入这个应用程序的主事件循环


# 已完成： https://blog.csdn.net/qq_35203425/article/details/78568141

#  1.建立xxx.py程序   test.py
#  2.cmd     pyinstaller xxx.py    pyinstaller test.py