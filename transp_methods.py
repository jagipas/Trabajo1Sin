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
pyhop.declare_methods('move_to_dest', move_to_dest_m)

def drive_to_dest_m(state,transport,dest):
	#Palet en el que esta el contenedor a mover
	palet = state.cont[cont]
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
		return [('cargar_cont', cont, pos, camion), ('drive', camion, dest),('descargar_cont',cont, dest, camion)]

	else:
		return False
pyhop.declare_methods('move_to_dest', move_to_dest_m)

def cargar_cont_m(state, cont, dist, camion):
	for i in state.dist_gruas:	
		if i == dist:
			grua = state.dist_gruas[i]
			break
	palet=state.dist_palets[dist]
	#Si el contenedor que esta en el tope de la pila del camion no es el que queremos, desapilamos y cargamos el que haya
	#condiciones para el if: len(state.carga_camion[camion])==0 
	if len(state.palets[palet])>1 and state.palets[palet][-1]!=cont:
		cont1=state.palets[palet].pop()
		return [('lift',grua,cont1),('load',grua,camion),('cargar_cont',cont,dist,camion)]
	else :
		cont1=state.palets[palet].pop()
		return [('lift',grua,cont1),('load',grua,camion)]
pyhop.declare_methods('cargar_cont', cargar_cont_m)

def descargar_cont_m(state, cont, dist, camion):
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
pyhop.declare_methods('descargar_cont', descargar_cont_m)























	
	
	






		
