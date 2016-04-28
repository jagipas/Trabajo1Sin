import pyhop

def walk_to_dest_m(state,driver,dest):
	#Localizacion del conductor
	driverAt = state.at_cond[driver]

	if dest==driverAt:
		return [('already_there',)]

	elif dest in state.ruta_cond[driverAt]:	
		return [('walk',driver, dest)]
				
	#Si el driver solo tienen un posible trayecto desde su posicion actual
	elif len(state.ruta_cond[driverAt])==1:
		return [('walk',driver, state.ruta_cond[driverAt][0]),('walk_to_dest',driver,dest)]
	
	#Si el conductor tiene varios destinos desde su posicion actual y ninguno de ellos es el destino final
	else:
		minValue=100
		indexMinDest=''
		for i in state.ruta_cond[driverAt]:
			print i
			if state.distancias[i][dest]<minValue:
				minValue=state.distancias[i][dest]
				indexMinDest = i

		return [('walk',driver, i),('walk_to_dest',driver,dest)]
				

pyhop.declare_methods('walk_to_dest', walk_to_dest_m)

def drive_to_dest_m(state,transport,dest):
	#Localizacion del camion
	transpAt = state.at_camiones[transport]
	
	#Comprobamos si hay conductor en la posicion origen del camion y si hay lo guardamos
	hayDriver=False	
	for i in state.at_cond:
		if state.at_cond[i]==transpAt:
			hayDriver=True
			driver=i
	
	if dest==transpAt:
		return [('already_there',)]	
	
	#Si hay un conductor se realizan las acciones necesarias para conducirlo y poner el estado de manera correcta
	elif hayDriver:
		return[('subir_camion',transport,driver),('drive',transport,dest),('bajar_camion',transport,driver)]
	#Si no hay conductor se busca el mas cercano
	else:
		return[('find_nearest_driver',transport),('drive_to_dest',transport,dest)]

pyhop.declare_methods('drive_to_dest', drive_to_dest_m)

def pack_to_dest_m(state, paquete, dest):
	#Localizacion del camion
	packetAt = state.at_paquete[paquete]
	
	#Comprobamos si hay conductor en la posicion origen del camion y si hay lo guardamos
	hayCamion=False	
	for i in state.at_camiones:
		if state.at_camiones[i]==packetAt:
			hayCamion=True
			camion=i

	#Si el camion ya esta en el destino devuelve False
	if dest==packetAt:
		return [('already_there',)]

	#Si hay un conductor se realizan las acciones necesarias para conducirlo y poner el estado de manera correcta
	elif hayCamion :
		return[('carga',camion,paquete),('drive_to_dest',camion,dest),('descarga',camion,paquete)]
	#Si no hay conductor se busca el mas cercano
	else:
		return[('find_nearest_transport',paquete),('pack_to_dest',paquete,dest)]
		
pyhop.declare_methods('pack_to_dest', pack_to_dest_m)

def find_nearest_driver_m(state, transport):

	#Ciudad donde se encuentra el camion a conducir	
	transportAt=state.at_camiones[transport]

	#Variables auxiliares
	minValue=100
	indexMinDest=''
	
	#Buscamos en la lista de localizaciones de conductores y seleccionamos el conductor mas cercano a la posicion del camion
	for i in state.at_cond:
		if state.distancias[state.at_cond[i]][transportAt]<minValue:
			minValue=state.distancias[state.at_cond[i]][transportAt]
			indexMinDest = i
	#El conductor va andando hacia el camion
	return [('walk_to_dest',indexMinDest,transportAt)]
	

pyhop.declare_methods('find_nearest_driver', find_nearest_driver_m)

def find_nearest_transport_m(state, packet):

	#Ciudad donde se encuentra el paquete a llevar	
	packetAt=state.at_paquete[packet]

	#Variables auxiliares
	minValue=100
	indexMinDest=''
	
	#Buscamos en la lista de localizaciones de camiones y seleccionamos el camion mas cercano a la posicion del paquete
	for i in state.at_camiones:
		if state.distancias[state.at_camiones[i]][packetAt]<minValue:
			minValue=state.distancias[state.at_camiones[i]][packetAt]
			indexMinDest = i
	#El conductor va andando hacia el camion
	return [('drive_to_dest',indexMinDest,packetAt)]
	

pyhop.declare_methods('find_nearest_transport', find_nearest_transport_m)






















	
	
	






		
