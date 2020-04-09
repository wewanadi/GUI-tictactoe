import wx
import game as f

class menu(wx.Frame):
    def __init__(self ,title,size,style):
        super(menu, self).__init__(None, title=title, size=size, style=style)
         
        panel = wx.Panel(self)
        
        menubox = wx.GridBagSizer(0,0)

        tmp =  wx.Button(panel , -1 ,label = 'Welcome to TICTACTOE',size = (230,60))
        menubox.Add(tmp,pos=(0,0), flag =  wx.RIGHT|wx.LEFT | wx.TOP, border =10)
                     
        button = wx.Button(panel,-1, label = 'Player  V.S.  Player',size = (230,60))
        button.Bind(wx.EVT_BUTTON, self.ptop)
        menubox.Add(button,pos=(1,0), flag =  wx.RIGHT|wx.LEFT | wx.TOP, border = 10)
                   
        button = wx.Button(panel, label = 'Player  V.S.  Computer',size = (230,60))
        button.Bind(wx.EVT_BUTTON, self.ptoc)
        menubox.Add(button,pos=(2,0), flag =  wx.RIGHT|wx.LEFT | wx.TOP, border = 10)

        button = wx.Button(panel, label = 'EXIT',size = (230,60))
        button.Bind(wx.EVT_BUTTON, self.EXIT)
        menubox.Add(button,pos=(3,0), flag =  wx.RIGHT|wx.LEFT | wx.TOP, border = 10)
        
        panel.SetSizerAndFit(menubox)
        
        self.Show()

    def ptop(self, event):
        self.Show(False)
        gaming_ptop('TIC TAC TOE', (270, 330), style=wx.CLOSE_BOX | wx.CAPTION)
        self.Close()

    def ptoc(self, event):
        self.Show(False)
        gaming_ptoc('TIC TAC TOE', (270, 330), style=wx.CLOSE_BOX | wx.CAPTION)
        self.Close()

    def EXIT(self, event):
        self.Close()

class gaming_ptop(wx.Frame):
    def __init__(self ,title,size,style):
        super(gaming_ptop, self).__init__(None,title=title, size = size, style = style )

        self.panel = wx.Panel(self)
        self.game = f.tictactoe()
        self.game.set_up_ptop()

        gamebox = wx.GridBagSizer(0, 0)
        
        for row in range (0,3):
            for column in range(0, 3):
                button = wx.ToggleButton(self.panel, label = '{}'.format(row*3+column),size = (70,70))
                button.Bind(wx.EVT_TOGGLEBUTTON, self.select)
                gamebox.Add(button,pos=(row+1,column), flag =  wx.RIGHT|wx.LEFT | wx.TOP|wx.RIGHT|wx.LEFT | wx.TOP, border = 7)
 
        button = wx.Button(self.panel, label = 'Restart!',pos = (10,10),size = (70,40))
        button.Bind(wx.EVT_BUTTON, self.RESTART)
        gamebox.Add(button,pos=(0,0), flag =  wx.RIGHT|wx.LEFT | wx.TOP|wx.RIGHT|wx.LEFT | wx.TOP, border = 7)

        self.tern = wx.Button(self.panel, label = '{} tern.'.format(self.game.now_player()),pos = (90,10),size = (70,40))
        gamebox.Add(self.tern,pos=(0,1), flag =  wx.RIGHT|wx.LEFT | wx.TOP|wx.RIGHT|wx.LEFT | wx.TOP, border = 7)

        button = wx.Button(self.panel, label = 'Menu',pos = (170,10),size = (70,40))
        button.Bind(wx.EVT_BUTTON, self.go_menu)
        gamebox.Add(button,pos=(0,2), flag =  wx.RIGHT|wx.LEFT | wx.TOP|wx.RIGHT|wx.LEFT | wx.TOP, border = 7)

        self.panel.SetSizerAndFit(gamebox)
        self.Show()

    def select(self, event):
        state = event.GetEventObject().GetValue() 
        select = event.GetEventObject().GetLabel() 

        if state == True:
            event.GetEventObject().SetLabel('{}'.format(self.game.now_player()))
            judge = self.game.judge(select)
            if judge != None:                
                dlg = wx.MessageDialog(None, "Winner {}!!    Play again?".format(judge), "Judge", wx.YES_NO | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_YES:
                    self.Show(False)
                    gaming_ptop('TIC TAC TOE', (270, 330), style=wx.CLOSE_BOX | wx.CAPTION)
                self.Close()
            self.game.set_state()
            self.tern.SetLabel('{} tern.'.format(self.game.now_player()))

        else:
            event.GetEventObject().SetValue(True)

    def RESTART(self, event):
        self.Show(False)
        gaming_ptop('TIC TAC TOE', (270, 330), style=wx.CLOSE_BOX | wx.CAPTION)
        self.Close()

    def go_menu(self, event):
        self.Show(False)
        menu('TIC TAC TOE', (270, 330), style=wx.CLOSE_BOX | wx.CAPTION)  
        self.Close()

class gaming_ptoc(wx.Frame):
    def __init__(self ,title,size,style):
        super(gaming_ptoc, self).__init__(None,title=title, size = size, style = style )
        self.panel = wx.Panel(self)
        self.game = f.tictactoe()
        self.game.set_up_ptoc()

        gamebox = wx.GridBagSizer(0, 0)
        self.buttons = list()

        for row in range (0,3):
            for column in range(0, 3):
                button = wx.ToggleButton(self.panel, label = '{}'.format(row*3+column),size = (70,70))
                button.Bind(wx.EVT_TOGGLEBUTTON, self.select)
                gamebox.Add(button,pos=(row+1,column), flag =  wx.RIGHT|wx.LEFT | wx.TOP|wx.RIGHT|wx.LEFT | wx.TOP, border = 7)
                self.buttons.append(button)

        button = wx.Button(self.panel, label = 'Restart!',pos = (10,10),size = (70,40))
        button.Bind(wx.EVT_BUTTON, self.RESTART)
        gamebox.Add(button,pos=(0,0), flag =  wx.RIGHT|wx.LEFT | wx.TOP|wx.RIGHT|wx.LEFT | wx.TOP, border = 7)

        self.tern = wx.Button(self.panel, label = '{} tern.'.format(self.game.now_player()),pos = (90,10),size = (70,40))
        gamebox.Add(self.tern,pos=(0,1), flag =  wx.RIGHT|wx.LEFT | wx.TOP|wx.RIGHT|wx.LEFT | wx.TOP, border = 7)

        button = wx.Button(self.panel, label = 'Menu',pos = (170,10),size = (70,40))
        button.Bind(wx.EVT_BUTTON, self.go_menu)
        gamebox.Add(button,pos=(0,2), flag =  wx.RIGHT|wx.LEFT | wx.TOP|wx.RIGHT|wx.LEFT | wx.TOP, border = 7)

        self.panel.SetSizerAndFit(gamebox)
        self.Show()
        
    def select(self, event):
        state = event.GetEventObject().GetValue() 
        select = event.GetEventObject().GetLabel() 

        if state == True:
            event.GetEventObject().SetLabel('{}'.format(self.game.now_player()))
            self.umpire(select)

            if self.game.full():
                return
            com = self.game.com_place()
            self.buttons[com].SetLabel('{}'.format(self.game.now_player()))
            self.buttons[com].SetValue(True)
            self.umpire(com)                      
        else:
            event.GetEventObject().SetValue(True)

    def RESTART(self, event):
        self.Show(False)
        gaming_ptoc('TIC TAC TOE', (270, 330), style=wx.CLOSE_BOX | wx.CAPTION)
        self.Close()

    def NOTHING(self, event):
        return 

    def go_menu(self, event):
        self.Show(False)
        menu('TIC TAC TOE', (270, 330), style=wx.CLOSE_BOX | wx.CAPTION)  
        self.Close()

    def umpire(self, select):
        judge = self.game.judge(select)
        if judge != None:
            if judge == 'TIE':
                dlg = wx.MessageDialog(None, 'TIE!!    Play again?', "Judge", wx.YES_NO | wx.ICON_QUESTION)
            else:               
                dlg = wx.MessageDialog(None, "{} win!!    Play again?".format(self.game.now_player()), "Judge", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Show(False)
                gaming_ptoc('TIC TAC TOE', (270, 330), style=wx.CLOSE_BOX | wx.CAPTION)
            self.Close()
        self.game.set_state()
        self.tern.SetLabel('{} tern.'.format(self.game.now_player()))
           

app = wx.App()
menu('TIC TAC TOE', (270, 330), style=wx.CLOSE_BOX | wx.CAPTION)
app.MainLoop()