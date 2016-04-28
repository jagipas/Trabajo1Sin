import pyhop

def walk_to_dest_m(state,driver,dest):
	#Localizacion del conductor
	driverAt = state.at_cond[driver]
	#Buscar localizacion
	pos = -1
	
	if len(state.ruta_cond[driverAt])==1:
			pos = state.ruta_cond[0]
			
	else:
		for i in state.ruta_cond:
			if state.ruta_cond[i]==dest:
				pos = i
				break

	if pos == -1:
	#Camion que se encuentra el distribuidor donde esta el contenedor
	for i in state.at_camiones:
		if state.at_camiones[i]==pos:
			camion = i
			break
	#Si el contenedor no esta en su distribuidor destino
	if dest!=pos:
		return [('cargar_cont', cont, pos, camion), ('drive', camion, dest),('descargar_cont',cont, dest, camion)]

	else:
		return False
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

def pack_to_dest_m(state, transp, paquete, dest):
	for i in state.at_paquetes:	
		if i == paquete:
			ciudad = state.at_paquetes[i]
			break
	#Si el contenedor que esta en el tope de la pila del camion no es el que queremos, desapilamos y cargamos el que haya
	#condiciones para el if: len(state.carga_camion[camion])==0 
	if state.at_camiones[transp]==ciudad and state.driver_atCamion[transp]!='':
		return [('carga',transp,paquete,ciudad),('drive_to_dest',transp,dest),('descarga',transp,paquete,dest)]
	elif state.at_camiones[transp]==ciudad and state.driver_atCamion[transp]=='':
		return [('walk_to_dest',grua,cont1),('load',grua,camion)]
pyhop.declare_methods('pack_to_dest', pack_to_dest_m)

def driver_to_transp_m(state, cont, dist, camion):
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
pyhop.declare_methods('driver_to_transp', driver_to_transp_m)























	
	
	






		
