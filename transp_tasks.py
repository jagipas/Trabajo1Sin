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
	if y in state.ruta_camion[state.at_camion[transp]]:
		state.at_camiones[transp]=y
		state.at_cond[state.at_cond[transp]]=y
		return state
	else:
		return False
		

def descarga(state,transp,paquete,ciudad):
	print "Entro en descarga"
	if state.at_camiones[transp]==ciudad:
		state.at_paquete[paquete]=ciudad
		state.carga_camiones.remove(paquete)
		return state
	else:
		return False

def carga(state,transp,paquete,ciudad):
	print "Entro en carga"
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
	print "Entro en descarga"
	ciudad = state.at_camiones[transp]
	if state.at_camiones[transp]==state.at_cond[driver]:
		state.at_cond[driver]=ciudad
		return state
	else:
		return False
	
pyhop.declare_operators(walk,drive,carga,descarga,subier_camion,bajar_camion)

    
