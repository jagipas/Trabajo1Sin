import pyhop

def already_there(state):
	print "Entro en already_there"
	return state

def walk(state,driver,y):
	print "Entro en walk"
	print driver
	print state.at_cond[driver]
	if y in state.ruta_cond[state.at_cond[driver]]:
		state.at_cond[driver]=y
		return state
	else: 
		return False
    
def drive(state,transp,y):
	print "Entro en drive"
	if y in state.ruta_cam[state.at_camiones[transp]]:
		state.at_camiones[transp]=y
		return state
	else:
		return False
		

def descarga(state,transp,paquete):
	print "Entro en descarga"
	ciudad=state.at_camiones[transp]
	if state.at_paquete[paquete]==transp:
		state.at_paquete[paquete]=ciudad
		state.carga_camion[transp].remove(paquete)
		return state
	else:
		return False

def carga(state,transp,paquete):
	print "Entro en carga"
	ciudad=state.at_paquete[paquete]
	if state.at_camiones[transp]==ciudad:
		state.at_paquete[paquete]=transp
		state.carga_camion[transp].append(paquete)
		return state
	else:
		return False

def subir_camion(state,transp,driver):
	print "Entro en subir_camion"
	if state.at_camiones[transp]==state.at_cond[driver]:
		state.at_cond[driver]=transp
		return state
	else:
		return False

def bajar_camion(state,transp,driver):
	print "Entro en bajar_camion"
	ciudad = state.at_camiones[transp]
	if state.at_cond[driver]==transp:
		state.at_cond[driver]=ciudad
		return state
	else:
		return False
	
pyhop.declare_operators(walk,drive,carga,descarga,subir_camion,bajar_camion,already_there)

    
