import pyhop


def walk(state,driver,y):
	print "Entro en walk"
	state.at_cond[driver]=y
	return state
    
def drive(state,transp,x,y):
	print "Entro en lift"
	state.ciudades[ciudad][t].remove(transp)
	state.ciudades[ciudad][t].append(transp)
	state.at_camiones[camion]=y
	return state
		

def descarga(state,transp,paquete,ciudad):
	print "Entro en descarga
	state.ciudades[ciudad][p].remove(paquete)
	state.at_paquete[paquete]=ciudad
	state.carga_camiones.remove(paquete)
	return state

def carga(state,transp,paquete,ciudad):
	state.ciudades[ciudad][p].append(paquete)
	state.at_paquete[paquete]=transp
	state.carga_camion[transp].append(paquete)
	return state
	
pyhop.declare_operators(walk,drive,carga,descarga)

    
