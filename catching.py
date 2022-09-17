import random

from server_folder import db
from server_folder.model import Event, Area, Dinimon, Type, Captured_Dinimon, Move, Enemy_Dinimon, Dinidex


def catch_dinimon(item, dinimon):
    print(f'Catching: {dinimon.name} with {item.catch_rate}')
    
    catch_rate = ((1000/item.catch_rate) + (dinimon.catchability))
    chance = random.randint(1, int(catch_rate))
    print(f'Chance: {chance} / {catch_rate} (needs a 1-10)')

    # WRITE CODE FOR DINIMON HEALTH CALCULATIONS

    if chance <= 10:
        catch = True
    else:
        catch = False

    print('Catch Is:', catch)
    return catch


def add_dini_to_player(dinimon, dinimon_dex, player_id):
    new_dini = Captured_Dinimon(player_id=player_id, dinimon_id=dinimon.dinimon_id, nickname=dinimon_dex.name, move1=dinimon.move1, move2=dinimon.move2, move3=dinimon.move3, move4=dinimon.move4, energy=dinimon.max_energy, max_energy=dinimon.max_energy, health=dinimon.health, max_health=dinimon.max_health, experience=0, max_experience=50, level=1, level_to_evolve=dinimon_dex.level_to_evolve, evo_ready=False, in_party=False, image=f'https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/{dinimon_dex.name}.png')

    entry = Dinidex(player_id=player_id, dinimon_id=dinimon.dinimon_id)

    db.session.add(entry)
    db.session.add(new_dini)
    db.session.commit()

    return new_dini