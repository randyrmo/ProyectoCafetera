
cafedisp = 100
vasosP = 20
vasosM = 20
vasosG = 20
azucar = 100


while True:
	cafeusuario = input("\nBienvenido a la maquina de cafe.\nSeleccione el tamano del vaso de cafe que desea\n1) Vaso Pequeno (3 Oz de cafe)\n2) Vaso Mediano (5 Oz de cafe)\n3) Vaso Grande (7 Oz de cafe)\n")
	if cafeusuario == "1":
		if vasosP >= 1:
			if cafedisp >= 3:
				azucarusuario = int(input("Digite las cucharadas de azucar que desea.\n"))
				if azucarusuario <= azucar:
					print ("Gracias por su compra, su cafe de 3 Onz con "+str(azucarusuario),"cucharadas de azucar se encuentra listo, lo puede recojer\n")
					break
				else:
					print("Lo sentimos, la maquina no cuenta con la cantidad de azucar deseada.\n")
			else:
				print("Lo sentimos, la maquina no cuenta con la cantidad de cafe deseada.\n")
		else:
			print("Lo sentimos, la maquina no cuenta con la cantidad de vasos deseados.\n")
		break

	if cafeusuario == "2":
		if vasosM >= 1:
			if cafedisp >= 5:
				azucarusuario = int(input ("Digite las cucharadas de azucar que desea.\n"))
				if azucarusuario <= azucar:
					print ("Gracias por su compra, su cafe de 5 Onz con "+str(azucarusuario),"cucharadas de azucar se encuentra listo, lo puede recojer\n")
					break
				else:
					print("Lo sentimos, la maquina no cuenta con la cantidad de azucar deseada.\n")
			else:
				print("Lo sentimos, la maquina no cuenta con la cantidad de cafe deseada.\n")
		else:
			print("Lo sentimos, la maquina no cuenta con la cantidad de vasos deseados.\n")	
		break

	if cafeusuario == "3":
		if vasosG >= 1:
			if cafedisp >= 7:
				azucarusuario = int(input ("Digite las cucharadas de azucar que desea.\n"))
				if azucarusuario <= azucar:
					print ("Gracias por su compra, su cafe de 7 Onz con "+ str(azucarusuario),"cucharadas de azucar se encuentra listo, lo puede recojer\n")
					break
				else:
					print("Lo sentimos, la maquina no cuenta con la cantidad de azucar deseada.\n")
			else:
				print("Lo sentimos, la maquina no cuenta con la cantidad de cafe deseada.\n")
		else:
			print("Lo sentimos, la maquina no cuenta con la cantidad de vasos deseados.\n")	
		break


	else:
		print("Lo sentimos, la maquina no cuenta con esta opcion, seleccione una opcion valida.\n")
		break