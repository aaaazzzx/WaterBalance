# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class WB01
###########################################################################

class WB01 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"WaterBalance0.1", pos = wx.DefaultPosition, size = wx.Size( 686,388 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer2 = wx.FlexGridSizer( 0, 8, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"用水类型", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"非生态用水", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button17, 0, wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"生态用水", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"计算需水", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button19, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"降水", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button23, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button24, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button17.Bind( wx.EVT_BUTTON, self.InExcel01 )
		self.m_button22.Bind( wx.EVT_BUTTON, self.InExcel02 )
		self.m_button19.Bind( wx.EVT_BUTTON, self.WaterNeed )
		self.m_button23.Bind( wx.EVT_BUTTON, self.InExcel03 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def InExcel01( self, event ):
		event.Skip()

	def InExcel02( self, event ):
		event.Skip()

	def WaterNeed( self, event ):
		event.Skip()

	def InExcel03( self, event ):
		event.Skip()


