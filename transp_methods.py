import pyhop

def walk_to_dest_m(state,driver,dest):
	#Localizacion del conductor
	driverAt = state.at_cond[driver]

	#Si el destino es accesible desde la posicion acutal de driver

	if dest==driverAt:
		return False

	elif dest in state.ruta_cond[driverAt]:	
		return [('walk',driver, dest)]
				
	#Si el driver solo tienen un posible trayecto desde su posicion actual
	elif len(state.ruta_cond[driverAt])==1:
		return [('walk',driver, state.ruta_cond[driverAt][0]),('walk_to_dest',driver,dest]
	
	#Si el conductor tiene varios destinos desde su posicion actual y ninguno de ellos es el destino final
	else :
		minValue=100
		indexMinDest=-1
		for i in state.ruta_cond[driverAt]:
			if state.distancias[i][dest]<minValue:
				minValue=state.distancias[i][dest]
				indexMinDest = i

		return [('walk',state, state.ruta_cond[driverAt][indexMinDest),('walk_to_dest',driver,dest)]
				

pyhop.declare_methods('walk_to_dest', walk_to_dest_m)

def drive_to_dest_m(state,transport,dest):
	#Palet en el que esta el contenedor a mover
	transpAt = state.at_camiones[transport]
	#Distribuidor donde esta el palet que tiene el contenedor
	for i in state.dist_palets:
		if state.dist_palets[i]==palet:
			pos = i
			break
	#Camion que se encuentra el distribuidor donde esta el contenedor
	for i in state.at_camiones:
		if state.at_camiones[i]==pos:
			camion = i
			break
	#Si el contenedor no esta en su distribuidor destino
	if dest!=pos:
		return [('drive', camion, dest)]

	else:
		return False
pyhop.declare_methods('drive_to_dest', drive_to_dest_m)

def pack_to_dest_m(state, paquete, dest):
	transp=-1
	for i in state.at_paquetes:	
		if i == paquete:
			ciudad = state.at_paquetes[i]
			break
	for j in state.at_camiones:
		if state.at_camiones[j] == ciudad:
			transp = j
	#Si el contenedor que esta en el tope de la pila del camion no es el que queremos, desapilamos y cargamos el que haya
	#condiciones para el if: len(state.carga_camion[camion])==0 
	if transp==-1:
		return [('driver_to_transp_to_dest', ciudad),('pack_to_dest',paquete,dest)]
	elif state.at_camiones[transp]==ciudad and state.driver_atCamion[transp]=='':
		return [('find_driver',grua,cont1),('pack_to_dest',grua,camion)]		
	elif state.at_camiones[transp]==ciudad and state.driver_atCamion[transp]!='':
		return [('carga',transp,paquete,ciudad),('drive_to_dest',transp,dest),('descarga',transp,paquete,dest)]
		
pyhop.declare_methods('pack_to_dest', pack_to_dest_m)

def driver_to_transp_to_dest_m(state, cont, dist, camion):
	for i in state.dist_gruas:	
		if i == dist:
			grua = state.dist_gruas[i]
	palet=state.dist_palets[dist]
	#Si el contenedor que esta en el tope de la pila del camion no es el que queremos, desapilamos y cargamos el que haya
	if len(state.carga_camion[camion])>1 and state.carga_camion[camion][-1]!=cont:
		cont1=state.carga_camion[camion].pop()
		return [('unload',grua,cont1),('drop',palet,grua),('descargar_cont',cont,dist,camion)]
	else:
		cont1=state.carga_camion[camion].pop()
		return [('unload',grua,cont1),('drop',palet,grua)]

pyhop.declare_methods('driver_to_transp_to_dest', driver_to_transp_to_dest_m)

def find_driver_m(state, ciudad):
	sitios_analizados=[]
	for i in state.ruta_cond:
		for j in state.at_cond:
			if state.at_cond[j]==state.ruta_cond[i] and not i in sitios_analizados:
				cond=j
				break
			else:
				sitios_analizados.append(i)
	return [('walk_to_dest',cond,ciudad)]
	

pyhop.declare_methods('find_driver', find_driver_m)

def find_transport_m(state, ciudad):
	sitios_analizados=[]
	for i in state.ruta_camion:
		for j in state.at_camion:
			if state.at_camion[j]==state.ruta_camion[i] and not i in sitios_analizados:
				camion=j
				break
			else:
				sitios_analizados.append(i)
	ciudad=state.at_camiones[camion]
	return [('walk_to_dest',cond,ciudad)]
	

pyhop.declare_methods('find_driver', find_driver_m)






















	
	
	






		
