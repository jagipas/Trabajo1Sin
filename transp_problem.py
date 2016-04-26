import pyhop
import distr_methods
import distr_tasks

state1=pyhop.State('state1')


#Informacion dinamica
state1.at_camiones={'t1':'c1','t2':'c0'}
state1.ciudades={'c0':{t:["t2"],p:["p1","p2"],co:[""]},'c1':{t:["t1"],p:[""],co:["d2"]},'c1':{t:[""],p:[""],co:[""]}}
state1.carga_camion={'t1':[],'t2':[]}
state1.at_cond={'d1':'pi01','d2':'c1'}
#Informacion estatica
state1.ruta_cam={'c0':['c1','c2'],'c1':['c0','c2'],'c2':['c0','c1']}
state1.ruta_cond={'c0':['pi01'],'pi01':['c0','c1'],'c1':['pi01','pi12'],'pi12':['c1','c2'],'c2':['pi12']}

#GOAL

#pyhop.pyhop(state1, [('move_to_dest','c4','d2'),('move_to_dest','c1','d2')], verbose=3)
pyhop.pyhop(state1, [('move_to_dest','c0','d2'),('move_to_dest','c1','d2')], verbose=3)
#pyhop.pyhop(state1, [('move_to_dest','c1','d2')], verbose=3)
#pyhop.pyhop(state1, [('communicate_image_data','o1','high-res')], verbose=3)