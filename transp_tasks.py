import pyhop


def walk(state,driver,y):
	print "Entro en walk"
	state.at_cond[driver]=y
	return state
    
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
	
pyhop.declare_operators(walk,drive,carga,descarga)

    
