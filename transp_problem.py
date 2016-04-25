import pyhop
import distr_methods
import distr_tasks

state1=pyhop.State('state1')


#Informacion dinamica
state1.at_camiones={'t1':'d0','t0':'d1'}
#state1.palets={'p0':['c1','c2'],'p1':['c0','c4'],'p2':[]}
state1.palets={'p0':['c1'],'p1':['c0'],'p2':[]}
state1.grua={'h0':'','h1':'','h2':''}
state1.carga_camion={'t0':[],'t1':[]}
#state1.cont={'c0':'p1','c1':'p0','c2':'p0','c4':'p1'}
state1.cont={'c0':'p1','c1':'p0'}

#Informacion estatica
state1.dist_palets={'d0':'p0','d1':'p1','d2':'p2'}
state1.dist_gruas={'d0':'h0','d1':'h1','d2':'h2'}

#GOAL

#pyhop.pyhop(state1, [('move_to_dest','c4','d2'),('move_to_dest','c1','d2')], verbose=3)
pyhop.pyhop(state1, [('move_to_dest','c0','d2'),('move_to_dest','c1','d2')], verbose=3)
#pyhop.pyhop(state1, [('move_to_dest','c1','d2')], verbose=3)
#pyhop.pyhop(state1, [('communicate_image_data','o1','high-res')], verbose=3)
