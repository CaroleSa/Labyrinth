import os
from labyrinth_position import *













    
mouv_dict={0: 520}

for cle, valeur in mouv_dict.items():
    position_finale = ("({}, {})".format(cle+40, valeur))
    new_key=cle+40
    new_value=valeur
    print((cle+40, valeur))
    mouv_dict.clear()
    mouv_dict[new_key]=new_value

print(type(position_finale))
    
    
    


"""quand monte ou descend
for cle, valeur in mouv_dict.items():
    position_finale = ("({}, {})".format(cle+40, valeur))
    mouv_dict[cle]=valeur+100
    print(mouv_dict)"""
          
    

  
