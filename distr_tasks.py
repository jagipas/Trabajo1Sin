import pyhop


def drive(state,camion,y):
	print "Entro en drive"
	state.at_camiones[camion]=y
	return state
    
def lift(state,grua,cont):
	print "Entro en lift"
	print "Estos son los valores que tengo de grua, contenedor y palet:"+grua+' '+cont
	state.grua[grua]=cont
	state.cont[cont]=grua
	return state
		

def drop(state,palet,grua):
	cont=state.grua[grua]
	print "Entro en drop"
	print "Estos son los valores que tengo de grua, contenedor y camion:"+grua+' '+cont
	print "Este es el contenedor que recibo" +cont	
	state.palets[palet].append(cont)
	state.cont[cont]=palet
	return state

def load(state,grua,camion):
	cont=state.grua[grua]
	print "Entro en load"
	print "Estos son los valores que tengo de grua, contenedor y camion:"+grua+' '+cont+' '+camion
	print "Este es el contenedor que recibo" +cont
	state.carga_camion[camion].append(cont)
	state.cont[cont]=camion
	state.grua[grua]=''
	return state
	
	
def unload(state,grua,cont):
	print "Entro en unload"
	state.grua[grua]=cont
	state.cont[cont]=grua
	return state
	
pyhop.declare_operators(drive,lift,drop,load,unload)

    
