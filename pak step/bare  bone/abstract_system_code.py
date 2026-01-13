from abstract_system_constants import *
from abstract_system_encoder import *

FIB_MAX=84
def load_code(ramState):
    AND_prog=[
    [ADD,R3,R1,R2]            
    ]
        
    DIV_iws=encodeProgram(DIV_prog)

    pc=0
    for iw in DIV_iws:
        ramState[CODE+pc] = iw  
        pc+=1
        
    return ramState

