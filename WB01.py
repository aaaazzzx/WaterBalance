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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"WaterBalance0.1", pos = wx.DefaultPosition, size = wx.Size( 728,388 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer2 = wx.FlexGridSizer( 0, 8, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"系列长度", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

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

		self.m_staticText311 = wx.StaticText( self, wx.ID_ANY, u"初始库容", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText311.Wrap( -1 )

		fgSizer2.Add( self.m_staticText311, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl13.SetMinSize( wx.Size( 50,-1 ) )

		fgSizer2.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_staticText3111 = wx.StaticText( self, wx.ID_ANY, u"死库容", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText3111.Wrap( -1 )

		fgSizer2.Add( self.m_staticText3111, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl14.SetMinSize( wx.Size( 50,-1 ) )

		fgSizer2.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"计算河道供水", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button29, 0, wx.ALL, 5 )

		self.m_button30 = wx.Button( self, wx.ID_ANY, u"外河水位", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button30, 0, wx.ALL, 5 )

		self.m_button31 = wx.Button( self, wx.ID_ANY, u"最终可供水量", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button31, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl10.Bind( wx.EVT_TEXT_ENTER, self.InNub )
		self.m_button17.Bind( wx.EVT_BUTTON, self.InExcel01 )
		self.m_button22.Bind( wx.EVT_BUTTON, self.InExcel02 )
		self.m_button19.Bind( wx.EVT_BUTTON, self.WaterNeed )
		self.m_button23.Bind( wx.EVT_BUTTON, self.InExcel03 )
		self.m_textCtrl13.Bind( wx.EVT_TEXT_ENTER, self.InStorage )
		self.m_textCtrl14.Bind( wx.EVT_TEXT_ENTER, self.InStorage_Min )
		self.m_button29.Bind( wx.EVT_BUTTON, self.WaterAvailable01 )
		self.m_button30.Bind( wx.EVT_BUTTON, self.InExcel04 )
		self.m_button31.Bind( wx.EVT_BUTTON, self.FinalWaterAvailable )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def InNub( self, event ):
		event.Skip()

	def InExcel01( self, event ):
		event.Skip()

	def InExcel02( self, event ):
		event.Skip()

	def WaterNeed( self, event ):
		event.Skip()

	def InExcel03( self, event ):
		event.Skip()

	def InStorage( self, event ):
		event.Skip()

	def InStorage_Min( self, event ):
		event.Skip()

	def WaterAvailable01( self, event ):
		event.Skip()

	def InExcel04( self, event ):
		event.Skip()

	def FinalWaterAvailable( self, event ):
		event.Skip()


