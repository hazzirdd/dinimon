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


def add_dini_to_player(dinimon, dinimon_dex, player_id):
    new_dini = Captured_Dinimon(player_id=player_id, dinimon_id=dinimon.dinimon_id, nickname=dinimon_dex.name, move1=dinimon.move1, move2=dinimon.move2, move3=dinimon.move3, move4=dinimon.move4, energy=dinimon.max_energy, max_energy=dinimon.max_energy, health=dinimon.health, max_health=dinimon.max_health, experience=1, max_experience=9999, level=1, level_to_evolve=-1, in_party=False, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/{{ dinimon_dex.name }}.png')

    db.session.add(new_dini)
    db.session.commit()

    return new_dini