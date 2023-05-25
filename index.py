import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='URL Search')
        panel = wx.Panel(self)
        
        # Create UI elements
        url_label = wx.StaticText(panel, label='Enter URL:')
        self.url_input = wx.TextCtrl(panel)
        search_button = wx.Button(panel, label='Search')
        self.result_display = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY)
        accept_button = wx.Button(panel, id=wx.ID_OK)
        cancel_button = wx.Button(panel, id=wx.ID_CANCEL)
        
        # Add UI elements to a sizer
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(url_label, flag=wx.RIGHT, border=8)
        hbox1.Add(self.url_input, proportion=1)
        hbox1.Add(search_button)
        hbox2.Add(self.result_display, proportion=1, flag=wx.EXPAND)
        hbox3.Add(accept_button)
        hbox3.Add(cancel_button, flag=wx.LEFT, border=5)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox2, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, border=10)
        vbox.Add(hbox3, flag=wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM, border=10)
        panel.SetSizer(vbox)
        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()