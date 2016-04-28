import pyhop
import transp_methods
import transp_tasks

state1=pyhop.State('state1')

#Informacion dinamica
state1.at_camiones={'t1':'c1','t2':'c0'}
state1.carga_camion={'t1':[],'t2':[]}
state1.at_cond={'d1':'pi_01','d2':'c1'}
state1.at_paquete={'p1':'c0','p2':'c0'}

#Informacion estatica
state1.ruta_cam={'c0':['c1','c2'],'c1':['c0','c2'],'c2':['c0','c1']}
state1.ruta_cond={'c0':['pi_01'],'pi_01':['c0','c1'],'c1':['pi_01','pi_12'],'pi_12':['c1','c2'],'c2':['pi_12']}
state1.distancias={'c0':{'pi_01':1,'c1':2,'pi_12':3,'c2':4}, 
                   'pi_01':{'c0':1,'c1':1,'pi_12':2,'c2':3},
                   'c1':{'c0':2,'pi_01':1,'pi_12':1,'c2':2},
                   'pi_12':{'c0':3,'p_01':2,'c1':1,'c2':1},
                   'c2':{'c0':4,'pi_01':3,'c1':2,'pi_12':1}} 

#GOAL
pyhop.pyhop(state1, [('pack_to_dest','p1','c1'),('pack_to_dest','p2','c2'),('drive_to_dest','t1','c1'),('walk_to_dest','d1','c1')],verbose=3)

