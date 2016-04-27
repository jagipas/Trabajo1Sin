import pyhop
import distr_methods
import distr_tasks

state1=pyhop.State('state1')


#Informacion dinamica
state1.at_camiones={'t1':'c1','t2':'c0'}
state1.ciudades={'c0':{t:["t2"],p:["p1","p2"]},'c1':{t:["t1"],p:[""]},'c1':{t:[""],p:[""]}}
state1.carga_camion={'t1':[],'t2':[]}
state1.at_cond={'d1':'pi_01','d2':'c1'}
state1.at_paquete={'p1':'c0','p2':'c0'}
#Informacion estatica
state1.ruta_cam={'c0':['c1','c2'],'c1':['c0','c2'],'c2':['c0','c1']}
state1.ruta_cond={'c0':['pi_01'],'pi_01':['c0','c1'],'c1':['pi_01','pi_12'],'pi_12':['c1','c2'],'c2':['pi_12']}

#GOAL

#pyhop.pyhop(state1, [('move_to_dest','c4','d2'),('move_to_dest','c1','d2')], verbose=3)
pyhop.pyhop(state1, [('move_to_dest','c0','d2'),('move_to_dest','c1','d2')], verbose=3)
#pyhop.pyhop(state1, [('move_to_dest','c1','d2')], verbose=3)
#pyhop.pyhop(state1, [('communicate_image_data','o1','high-res')], verbose=3)
