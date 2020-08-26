#coding:utf8
"""
Les commandes sont :
					-Bonjours
					-yo
					-beug
					-cls
					-info
					-exit
"""
import os
import ctypes

def d():
	print("début")



"""
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
"""
d()
lancer = True
lancer = bool(lancer)
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
