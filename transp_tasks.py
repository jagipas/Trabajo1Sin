import pyhop


def walk(state,driver,y):
	print "Entro en walk"
	if y in state.ruta_cond[state.at_cond[driver]]:
		state.at_cond[driver]=y
		return state
	else: 
		return False
    
def drive(state,transp,x,y):
	print "Entro en lift"
	state.at_camiones[camion]=y
	state.at_cond[state.at_cond[transp]]==y
	return state
		

def descarga(state,transp,paquete,ciudad):
	print "Entro en descarga
	state.at_paquete[paquete]=ciudad
	state.carga_camiones.remove(paquete)
	return state

def carga(state,transp,paquete,ciudad):
	state.at_paquete[paquete]=transp
	state.carga_camion[transp].append(paquete)
	return state

def subir_camion(state,transp,driver):
	state.at_cond[driver]=transp
	return state

def bajar_camion(state,transp,driver):
	ciudad = state.at_camion[transp]
	state.at_cond[driver]=ciudad
	return state
	
pyhop.declare_operators(walk,drive,carga,descarga)

    
