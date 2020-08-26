#coding:utf8
"""
Les commandes sont :
					-Bonjours
					-yo
					-beug
					-cls
					-info
"""
import os
import ctypes
global paramètre1

lancer = True
lancer = bool(lancer)

def d():
	print("début")

def all():
	os.system('cls' if os.name == 'nt' else 'clear')
	while lancer == True:
		choixmenu = input(">>>")
	
		if choixmenu == "Bonjours":
			print("Bonjour a toi jeune ami(e),")
			print("tape info pour avoir plus d'info")
			print("le message d'au dessu fait trup pancer au pub, je sit : <tape caca au 7,12,12 pour avoir ta sonerie personalisée>. ")	
		elif choixmenu == "exit":
			break

		elif choixmenu == "yo":
			print("arraite ces vulgairiter tout de suite mathéo!!!")
	
		elif choixmenu == "beug":
			print("ok")
			n = input("met un gros nombre : ")
			try:
				n = int(n)
				print("c bien un nombre")
			except:
				print("Je t'ai demander un nombre.")
			else:
				p = input("met une phrase : ")
				pa = 0
				pa = int(pa)
				while pa < n:
					print( p)
				pa += 1
			finally:
				print("fin.")
	
		elif choixmenu == "cls":
			os.system('cls' if os.name == 'nt' else 'clear')
	
		elif choixmenu == "info":
			print("Ici tu peut retrouver tout (pas toute certaine ne sont que des teste (et je vien de commencer donc se ne sera peut \n être pas le cas à l'avenir)) mes travaille que je fait en python")
			print("ps : comme je l'ai dit je vie de commencer donc soyer indulgent.")	

		elif choixmenu == "caca":
			print("mdr")

		else:
			print("commande introuveble.")

	"""	elif choixmenu == "paramètre":
			os.system('cls' if os.name == 'nt' else 'clear')
			paremère1 = input("Oui pour activer le cls auto : ")
		if paremère1 == "Oui":
			clsAuto()
"""

		



def clsAuto():
		os.system('cls' if os.name == 'nt' else 'clear')
		while lancer == True:
			choixmenu = input(">>>")
	
			if choixmenu == "Bonjours":
				os.system('cls' if os.name == 'nt' else 'clear')
				print("Bonjour a toi jeune ami(e),")
				print("tape info pour avoir plus d'info")
				print("le message d'au dessu fait trup pancer au pub, je sit : <tape caca au 7,12,12 pour avoir ta sonerie personalisée>. ")	
			elif choixmenu == "exit":
				os.system('cls' if os.name == 'nt' else 'clear')
				break

			elif choixmenu == "yo":
				os.system('cls' if os.name == 'nt' else 'clear')
				print("arraite ces vulgairiter tout de suite mathéo!!!")
	
			elif choixmenu == "beug":
				os.system('cls' if os.name == 'nt' else 'clear')
				print("ok")
				n = input("met un gros nombre : ")
				try:
					n = int(n)
					print("c bien un nombre")
				except:
					print("Je t'ai demander un nombre.")
				else:
					p = input("met une phrase : ")
					pa = 0
					pa = int(pa)
					while pa < n:
						print( p)
					pa += 1
				finally:
					print("fin.")
	
			elif choixmenu == "cls":
				os.system('cls' if os.name == 'nt' else 'clear')
	
			elif choixmenu == "info":
				os.system('cls' if os.name == 'nt' else 'clear')
				print("Ici tu peut retrouver tout (pas toute certaine ne sont que des teste (et je vien de commencer donc se ne sera peut \n être pas le cas à l'avenir)) mes travaille que je fait en python")
				print("ps : comme je l'ai dit je vie de commencer donc soyer indulgent.")	

			elif choixmenu == "caca":
				os.system('cls' if os.name == 'nt' else 'clear')
				print("mdr")

			else:
				print("commande introuveble.")

		"""	elif choixmenu == "paramètre":
				os.system('cls' if os.name == 'nt' else 'clear')
				paremètre1bis = input("Oui pour désactiver le cls auto : ")
			if paramètre1bis == "Oui":
				all()
"""


d()
variable_numéro_un = input("Veut-tu le cls auto : ")
if variable_numéro_un == "oui":
	clsAuto()
elif variable_numéro_un == "Oui":
	clsAuto()
else:
	all()

