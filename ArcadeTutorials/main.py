#file:main.py			#
#########################							
#created by				#
#Mwiningban Ibrahim		#
#axorus-game			#
########################



#imports

import arcade 



class pixel():
	def __init__(self, ms_loc):
		self.ms_loc = ms_loc
	def m_returnMouseCursorPixel():
		pass

class draw():
	class gui():
	def __init__(self, size, loc):
		self.size = size
		self.loc = loc
		self.text = text
	def m_createWindow(width, height, text, bgcolor):
		arcade.open_window(width, height, text)
		arcade.set_background_color(bgcolor)
		arcade.start_render()
		arcade.finish_render()
	

draw.gui.m_createWindow(600, 600, "Hello, world!", arcade.color.GREEN)

arcade.run()