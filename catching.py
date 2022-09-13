import random

from server_folder import db
from server_folder.model import Event, Area, Dinimon, Type, Captured_Dinimon, Move, Enemy_Dinimon

def catch_dinimon(item):

    if item.item_id == 1:
        chance = random.randint(1,4)
    elif item.item_id == 2:
        chance = random.randint(1,3)
    elif item.item_id == 3:
        chance = random.randint(1,2)
    elif item.item_id == 4:
        chance = 1
    
    if chance == 1:
        catch = True
        print(f'{catch}, common baby!!')
    else:
        catch = False
        print(f'{catch}, It broke free!')

    return catch