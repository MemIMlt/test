
import wx

class App(wx.App):
    '''初始化方法'''
    def OnInit(self):
        frame = wx.Frame(parent = None,title = 'What the hell!!!')
        frame.Show()
        return True

if __name__ == '__main__':

    app = App()
    # app.MainLoop()
    app2=wx.App()
    # frame = wx.Frame(parent=None, title='What the hell!!!')
    # frame.Show()
    app2.MainLoop()