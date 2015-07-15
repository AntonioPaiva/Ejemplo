
import wx
from login import login

class app(object):

	def impre(self):
		print("python 22") 
	
	def imp(self):
		lg = login()
		

def main1():	
	p = app()	
	p.impre()
	p.imp()

def main():
	print("py")
	

#if __name__ == '__main__':
#	main()
#	main1()
		
	# Creamos una aplicación simple wx.
aplicacion = wx.PySimpleApp()

	# Creamos el objeto frame, fruto de la instanciación de la clase 
	# subclase_frame.
frame = login()

	# Mostramos la instanciación de la clase subclase_frame.
frame.Show()
	# Lanzamos el MainLoop, para escuchar peticiones de eventos.
aplicacion.MainLoop()
	
	
	
	
	
