
from prueb1 import prueba1
class prueba2(object):

	def imprimir(self):
		print("prueba1")
	

def main():
	p = prueba2()
	p1 = prueba1()
	p1.imprimir()
	p.imprimir()
	prueba1nc()
	
if __name__ == '__main__':
	main()
