import pygame
import sys
import random
import wx
import time


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='菜的抠脚~弟弟', pos=(120, 600), size=(300, 100))
        panel = wx.Panel(self)

        self.bt_confirm = wx.Button(panel, label='干就完事了')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnClickSubmit)
        self.bt_cancel = wx.Button(panel, label='耻辱退游')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnClickCancel)

        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=0, flag=wx.ALIGN_CENTER, border=5)

        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)
        panel.SetSizer(vsizer_all)

    def OnClickSubmit(self, event):
        self.Close()
        global click
        click = 1

    def OnClickCancel(self, event):
        self.Close()
        global click
        click = 2


def Choose():
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


class Bird:
    '''定义鸟类'''

    def __init__(self):
        self.InitBird()
        # self.bird = pygame.Rect(65, 50, 40, 40)  # bird[1]是鸟的高度
        self.birdstatus = [pygame.image.load('assets/1.png'),
                           pygame.image.load('assets/2.png'),
                           pygame.image.load('assets/dead.png'), ]
        # self.status = 0  # 此时鸟的状态展示
        # self.birdx = 100  # X轴坐标
        # self.birdy = 354  # Y轴坐标
        # self.jump = False
        # self.jumpSpeed = 15
        # self.gravity = 5
        # self.dead = False

    def InitBird(self):
        self.bird = pygame.Rect(65, 50, 40, 40)
        self.status = 0  # 此时鸟的状态展示
        self.birdx = 100  # X轴坐标
        self.birdy = 354  # Y轴坐标
        self.jump = False
        self.jumpSpeed = 15
        self.gravity = 5
        self.dead = False

    def InitSpeed(self):
        self.jumpSpeed = 15
        self.gravity = 5

    def UpdataBird(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdy -= self.jumpSpeed
        else:
            self.gravity += 0.5
            self.birdy += self.gravity
        self.bird[1] = self.birdy

    def IsSpeedZero(self):
        if self.jumpSpeed == 0:
            self.jump = False


class Pipeline:
    '''定义管道类'''

    def __init__(self):
        self.InitPie()
        # self.axisX = 400
        # self.axisYup = -300
        # self.axisYdown = 500
        # self.move = 2
        # self.space = 0  # 上下管道间距的缩小值，慢慢变大
        # self.vis = False  # 标志分数的变动与否
        self.pineup = pygame.image.load("assets/top.png")
        self.pinedown = pygame.image.load("assets/bottom.png")

    def InitPie(self):
        self.axisX = 400
        self.axisYup = -300
        self.axisYdown = 500
        self.move = 2
        self.space = 0
        self.vis = False

    def UpdataLine(self):
        '''管道移动'''
        self.axisX -= self.move
        # 计算分数
        if self.axisX < 50 and not self.vis:
            global score
            score += 1
            self.vis = True
        # 刷新管道
        if self.axisX < -100 and self.vis:
            self.axisX = 400
            # 赋予一个随机变量，让管道空隙位置不固定
            temp = random.randint(-200, 200)
            self.axisYup = -300 + temp + self.space
            self.axisYdown = 500 + temp - self.space
            self.vis = False


def Mapcreate():
    '''初始化地图'''
    screen.fill((255, 255, 255))  # 填充颜色-白
    screen.blit(background, (0, 0))  # 加入背景图片

    # 显示管道
    screen.blit(Pipeline.pineup, (Pipeline.axisX, Pipeline.axisYup))
    screen.blit(Pipeline.pinedown, (Pipeline.axisX, Pipeline.axisYdown))
    Pipeline.UpdataLine()

    # 显示鸟
    if Bird.dead:
        Bird.status = 2
    elif Bird.jump:
        Bird.status = 1
    else:
        Bird.status = 0
    screen.blit(Bird.birdstatus[Bird.status], (Bird.birdx, Bird.birdy))
    Bird.UpdataBird()

    # 显示分数
    screen.blit(font.render(str(score), -1, (255, 255, 255)), (50, 50))

    pygame.display.update()  # 刷新


def CheckDead():
    uprect = pygame.Rect(Pipeline.axisX, Pipeline.axisYup,
                         Pipeline.pineup.get_width() - 10,
                         Pipeline.pineup.get_height())
    downrect = pygame.Rect(Pipeline.axisX, Pipeline.axisYdown,
                           Pipeline.pinedown.get_width() - 10,
                           Pipeline.pinedown.get_height())
    # 碰撞管道之后并不返回值，会继续刷新地图，将出现小鸟以死亡状态抛物线落下的动画
    if uprect.colliderect(Bird.bird) or downrect.colliderect(Bird.bird) or Bird.bird[1] <= 0:
        Bird.dead = True

    if Bird.bird[1] >= height:
        Bird.dead = True
        return True
    else:
        return False


def SpeedUp():
    temp = score / 2
    Pipeline.move = 2 + temp
    Pipeline.space = score / 5 * 10


def getresult():
    final_text1 = "Game Over"
    final_text2 = "Your final score is:  " + str(score)
    # ft1_font = pygame.font.SysFont("Arial", 70)  # 设置第一行文字字体
    ft1_surf = font.render(final_text1, 1, (242, 3, 36))  # 设置第一行文字颜色
    # ft2_font = pygame.font.SysFont("Arial", 50)  # 设置第二行文字字体
    ft2_surf = font.render(final_text2, 1, (253, 177, 6))  # 设置第二行文字颜色
    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])  # 设置第一行文字显示位置
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])  # 设置第二行文字显示位置
    pygame.display.flip()  # 更新整个待显示的Surface对象到屏幕上


# def Countdown():
#     final_text1 = "Game Over"
#     ft1_surf = font.render(final_text1, 1, (242, 3, 36))  # 设置第一行文字颜色
#     screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])  # 设置第一行文字显示位置
#     pygame.display.flip()  # 更新整个待显示的Surface对象到屏幕上

def Initall():
    Bird.InitBird()
    Pipeline.InitPie()
    global score, click
    score = 0
    click = 0


if __name__ == '__main__':
    '''主函数'''
    pygame.init()

    # 字体设置
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)

    size = width, height = 400, 708
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()  # 设置时钟
    Pipeline = Pipeline()
    Bird = Bird()
    score = 0  # 初始化分数
    click = 0
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True
                Bird.InitSpeed()  # 当点击响应后将鸟的速度重置
        background = pygame.image.load("assets/background.png")
        Bird.IsSpeedZero()  # 检测鸟的上升速度是否为0
        SpeedUp()  # 加快游戏速度
        if CheckDead():
            getresult()
            Choose()
            if click == 2:
                break
            elif click == 1:
                Initall()
                Mapcreate()
                time.sleep(3)
        else:
            Mapcreate()
    pygame.quit()
