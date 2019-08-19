import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='我也不知道我创了个啥', pos=(100, 100), size=(600, 800))
        panel = wx.Panel(self)  # 画板
        title = wx.StaticText(panel, label='Python之禅--Tim Peters', pos=(100, 20))
        font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font)
        wx.StaticText(panel, label='优美胜于丑陋', pos=(50, 50))
        wx.StaticText(panel, label='明了胜于晦涩', pos=(50, 70))
        wx.StaticText(panel, label='简洁胜于复杂', pos=(50, 90))
        wx.StaticText(panel, label='复杂胜于凌乱', pos=(50, 110))
        wx.StaticText(panel, label='扁平胜于嵌套', pos=(50, 130))
        wx.StaticText(panel, label='间隔胜于紧凑', pos=(50, 150))
        wx.StaticText(panel, label='可读性很重要', pos=(50, 170))
        wx.StaticText(panel, label='即便假借特例的实用性之名，也不可违背这些规则', pos=(50, 190))
        wx.StaticText(panel, label='不要包容所有错误，除非你确定需要这样做', pos=(50, 210))
        wx.StaticText(panel, label='当存在多种可能，不要尝试去猜测', pos=(50, 230))
        wx.StaticText(panel, label='而是尽量找一种，最好是唯一一种明显的解决方案', pos=(50, 250))
        wx.StaticText(panel, label='虽然这并不容易，因为你不是 Python 之父', pos=(50, 270))
        wx.StaticText(panel, label='做也许好过不做，但不假思索就动手还不如不做', pos=(50, 290))
        wx.StaticText(panel, label='如果你无法向人描述你的方案，那肯定不是一个好方案;反之亦然', pos=(50, 310))
        wx.StaticText(panel, label='命名空间是一种绝妙的理念，我们应当多加利用', pos=(50, 330))

        wx.StaticText(panel, label='**********************************', pos=(50, 350))

        wx.StaticText(panel, label='即便假借特例的实用性之名，也不可违背这些规则', pos=(50, 370))
        wx.StaticText(panel, label='不要包容所有错误，除非你确定需要这样做', pos=(50, 390))
        wx.StaticText(panel, label='当存在多种可能，不要尝试去猜测', pos=(50, 410))
        wx.StaticText(panel, label='而是尽量找一种，最好是唯一一种明显的解决方案', pos=(50, 430))
        wx.StaticText(panel, label='虽然这并不容易，因为你不是 Python 之父', pos=(50, 450))
        wx.StaticText(panel, label='做也许好过不做，但不假思索就动手还不如不做', pos=(50, 470))
        wx.StaticText(panel, label='如果你无法向人描述你的方案，那肯定不是一个好方案;反之亦然', pos=(50, 490))
        wx.StaticText(panel, label='命名空间是一种绝妙的理念，我们应当多加利用', pos=(50, 510))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
