# -*- coding: cp1252 -*-
# 25/09/2015
# Ejemplo de wxPython 
# El Viaje del Navegante 

import wx

class login(wx.Frame):
    def __init__(self):

        # Llamamos al init (código del constructor) del wx.Frame del que 
        # heredamos.
		#Subclase del Frame
        wx.Frame.__init__(self, None, -1, 'Bienvenidos al Sistema de Usuario',
        pos=wx.Point(300, 400),size=wx.Size(800,850))
        
        self.etiqueta_mensaje = wx.StaticText(id=-1,label='Ingrese  Su  Usuario  y  Contraseña ',
		name='mensaje', parent=self,pos=wx.Point(250, 90), size=wx.Size(300,1000), style=0)

        # Usuario.
        self.etiqueta_usuario = wx.StaticText(id=-1,label='Usuario: ',
        name='etiqueta_usuario', parent=self,pos=wx.Point(200, 150),
        size=wx.Size(74, 13), style=0)
		
		#crea la grilla, caja de texto
        self.texto_usuario = wx.TextCtrl(id=-1, name='usuario',
        parent=self,pos=wx.Point(300, 142), size=wx.Size(150, 30))

        # Correo electrónico.        
        self.etiqueta_pass = wx.StaticText(id=-1,label='Contraseña',
        name='etiqueta_usuario', parent=self,pos=wx.Point(200, 185),
        size=wx.Size(74, 13), style=0)

		#crea la grilla, caja de texto, correo electronico
        self.texto_contrasenha= wx.TextCtrl(id=-1, name='contrasenha',
        parent=self,pos=wx.Point(300, 180), size=wx.Size(150, 30))

        # Botón de salida de la aplicación.
        self.boton_ingresar = wx.Button(self, id=-1,label="Ingresar",
        pos=wx.Point(315,230),size=wx.Size(75,30))
        # Creamos los manejadores de eventos, ligando los eventos a
        # los métodos que tendrán el código asociado.
        self.boton_ingresar.Bind(wx.EVT_BUTTON, self.ingresar_menu)       
    # Definimos los métodos que contienen el código que se ejecutará
    # cuando sean llamados a petición de los eventos definidos anteriormente.
    def ingresar_menu(self, event):
        admin = "admin"
        cont_reg = "12345"
        
        usuar = self.texto_usuario.GetValue()
        cont = self.texto_contrasenha.GetValue()
        
        if cont_reg == cont:
            print "Bienvenido al Sistema!"
            class menu(wx.Frame):
                def __init__(self):
                # Llamamos al init (código del constructor) del wx.Frame del que # heredamos.
                #Subclase del Frame
                    wx.Frame.__init__(self, None, -1, 'Bienvenidos al Sistema', 
                    pos=wx.Point(300, 400),size=wx.Size(800,850))
                    self.mensaje_menu = wx.StaticText(id=-1,label='MENU PRINCIPAL, ELIJA UNA OPCIÓN', 
                    name='mensaje', parent=self,pos=wx.Point(250, 90), size=wx.Size(300,1000), style=0)
                   # self.mensaje_menup = wx.StaticText(id=-1,label='MENU PRINCIPAL, ELIJA UNA 
                    #OPCIÓN',name='mensaje',parent=self,pos=wx.Point(250, 90), size=wx.Size(300,1000), style=0)
                    self.boton_clientes = wx.Button(self, id=-1,label="MENU CLIENTES",
                    pos=wx.Point(200, 150),size=wx.Size(120,55))
                    self.boton_empleados = wx.Button(self, id=-1,label="MENU EMPLEADOS",
                    pos=wx.Point(350, 150),size=wx.Size(120,55))
                    # Botón de salida de la aplicación.
                    self.boton_salir = wx.Button(self, id=-1,label="SALIR",
                    pos=wx.Point(500,150),size=wx.Size(120,55))
                    self.boton_salir.Bind(wx.EVT_BUTTON, self.menu_salir)
                    self.boton_clientes.Bind(wx.EVT_BUTTON, self.menu_clientes)
                    self.boton_empleados.Bind(wx.EVT_BUTTON, self.menu_empleados)
                    # Definimos los métodos que contienen el código que se ejecutará
                    # cuando sean llamados a petición de los eventos definidos anteriormente.
                def menu_salir(self, event):
                    print('salir ')
                def menu_clientes(self, event):
                    print('clientes ')
                def menu_empleados(self, event):
                    print('empleados ')
            def main():
               print('printt')
                # Creamos una aplicación simple wx.
            #aplicacion = wx.PySimpleApp()
            # Creamos el objeto frame, fruto de la instanciación de la clase 
            # menu.
            #frame = menu()
            # Mostramos la instanciación de la clase menu.
            #frame.Show()
            # Lanzamos el MainLoop, para escuchar peticiones de eventos.
           # aplicacion.MainLoop()
            if __name__ == '__main__':
                main()
        else:
            print "Valor incorrecto"
     
    def imprmir(self):
    	print('python ')

def main():
	app = wx.App(False)
	# Creamos una aplicación simple wx.
	aplicacion = wx.PySimpleApp()

	# Creamos el objeto frame, fruto de la instanciación de la clase 
	# subclase_frame.
	frame = login()

	# Mostramos la instanciación de la clase subclase_frame.
	frame.Show()
	# Lanzamos el MainLoop, para escuchar peticiones de eventos.
	aplicacion.MainLoop()


if __name__ == '__main__':
	main()
#	main1()


