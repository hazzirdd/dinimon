from audioop import add
import random

from server_folder import db
from server_folder.model import Event, Area, Dinimon, Type, Captured_Dinimon, Move, Enemy_Dinimon

def move_sprite(direction, left, top, sprite_xy):
    if direction == 'up':
        move = move_boundry(left, top - 70)
        if move == 'success':
            top -= 70
            sprite_xy += 100
    elif direction == 'down':
        move = move_boundry(left, top + 70)
        if move == 'success':
            top += 70
            sprite_xy -= 100
    elif direction == 'left':
        move = move_boundry(left - 70, top)
        if move == 'success':
            left -= 70
            sprite_xy -= 1
    elif direction == 'right':
        move = move_boundry(left + 70, top)
        if move == 'success':
            left += 70
            sprite_xy += 1

    return left, top, sprite_xy


def move_boundry(left, top):
    if left > 840 or left < 0 or top > 490 or top < 0:
        return 'error'
    else:
        return 'success'


def event_check(area_id, sprite_xy):
    area = Area.query.get(area_id)
    events = Event.query.filter(Event.area_id == area.area_id).all()
    area_x, area_y = split_area_coords(area.coordinates)
    print('PLAYER:',sprite_xy)
    for event in events:
        if event.xy == sprite_xy:
            if event.event == 'bottom_exit':
                area_x -= 1
                result = find_new_area(event, area_x, area_y)
                return result
            elif event.event == 'top_exit':
                area_x += 1
                result = find_new_area(event, area_x, area_y)
                return result
            elif event.event == 'left_exit':
                area_y -= 1
                result = find_new_area(event, area_x, area_y)
                return result
            elif event.event == 'right_exit':
                area_y += 1
                result = find_new_area(event, area_x, area_y)
                return result
            elif event.event == 'dinimon':
                dinimon = Dinimon.query.filter(Dinimon.image == event.image).first()
                print(f'You found a {dinimon.name}!')
                db.session.delete(event)
                db.session.commit()
                return ['wild_battle', dinimon]

    return 'no event'

                
def find_new_area(event, area_x, area_y):
    area_coords = str(area_x) + '/' + str(area_y)
    area = Area.query.filter(Area.coordinates == area_coords).one()
    return [event.event, area.area_id]


def split_area_coords(coords):
    area_x, area_y = coords.split('/')
    return int(area_x), int(area_y)


def spawn_events(area):
    events = Event.query.filter(Event.area_id == area.area_id).all()
    return events


def spawn_dinimon(area):
    biome = area.biome
    all_dinimon = Dinimon.query.all()
    area_spawners = Event.query.filter(Event.event == 'dinimon_spawn').all()
    possible_dinimon = []

    for spawner in area_spawners:
        possible_dinimon.clear()
        spawn_chance = random.randint(1,100)
        if spawn_chance >= 10:
            for dini in all_dinimon:
                if spawner.biome in dini.biomes:
                    for x in range(dini.rarity):
                        possible_dinimon.append(dini)

        if possible_dinimon:
            dinimon = random.choice(possible_dinimon)
            spawn_dinimon = Event(event='dinimon', area_id=spawner.area_id, left_coord=spawner.left_coord, top_coord=spawner.top_coord, xy=spawner.xy, image=dinimon.image, width=dinimon.width)
            db.session.add(spawn_dinimon)

    db.session.commit()


def get_party(player_id):
    players_dinimon = Captured_Dinimon.query.filter(Captured_Dinimon.player_id == player_id).all()
    party = []
    for dinimon in players_dinimon:
        if dinimon.in_party == True:
            party.append(dinimon)
    return party


def setup_dini_moves(main_dini):
    moves = []
    if main_dini.move1 != 14:
        move1 = Move.query.get(main_dini.move1)
        moves.append(move1)
    if main_dini.move2 != 14:
        move2 = Move.query.get(main_dini.move2)
        moves.append(move2)
    if main_dini.move3 != 14:
        move3 = Move.query.get(main_dini.move3)
        moves.append(move3)
    if main_dini.move4 != 14:
        move4 = Move.query.get(main_dini.move4)
        moves.append(move4)
    return moves
 

def create_enemy_dinimon(dinimon_id):
    dinimon = Dinimon.query.get(dinimon_id)
    all_moves = dinimon.possible_moves.split('/')

    for move in all_moves:
        if not move:
            all_moves.remove(move)

    move1 = random.choice(all_moves)
    move1_full = Move.query.filter(Move.move == move1).first()
    move1_id = move1_full.move_id
    all_moves.remove(move1)

    if all_moves:
        move2 = random.choice(all_moves)
        move2_full = Move.query.filter(Move.move == move2).first()
        move2_id = move2_full.move_id
        all_moves.remove(move2)
    else:
        move2_id = 14
    if all_moves:
        move3 = random.choice(all_moves)
        move3_full = Move.query.filter(Move.move == move3).first()
        move3_id = move3_full.move_id
        all_moves.remove(move3)
    else:
        move3_id = 14
    if all_moves:
        move4 = random.choice(all_moves)
        move4_full = Move.query.filter(Move.move == move4).first()
        move4_id = move4_full.move_id
        all_moves.remove(move4)
    else:
        move4_id = 14

    health = random_from_range(dinimon.health_range)
    energy = random_from_range(dinimon.energy_range)

    enemy_dinimon = Enemy_Dinimon(dinimon_id=dinimon_id, move1=move1_id, move2=move2_id, move3=move3_id, move4=move4_id, type1=dinimon.type1, type2=dinimon.type2, energy=0, max_energy=energy, health=health, max_health=health, level=1)
    db.session.add(enemy_dinimon)
    db.session.commit()

    return enemy_dinimon.enemy_dinimon_id


def random_from_range(range):
    low, high = range.split('-')
    result = random.randint(int(low), int(high))
    return result


def get_dini_health(dinimon):
    health = dinimon.health
    max_health = dinimon.max_health
    decimal = health/max_health
    dini_health = decimal*100
    return dini_health


def get_dini_energy(dinimon):
    energy = dinimon.energy
    max_energy = dinimon.max_energy
    decimal = energy/max_energy
    dini_energy = decimal*100
    return dini_energy


def get_dini_xp(dinimon):
    xp = dinimon.experience
    max_experience = dinimon.max_experience
    decimal = xp/max_experience
    dini_xp = decimal*100
    return dini_xp


def run_attack_on_enemy(move_id, enemy_dinimon_id, dinimon):
    print('ATTACK ON ENEMY::::________________________________________________________________')
    move = Move.query.get(move_id)
    enemy = Enemy_Dinimon.query.get(enemy_dinimon_id)
    damage = int(move.damage)
    health = int(enemy.health)

    move_type = Type.query.get(move.type_id)
    move_super_effectives = move_type.super_effective.split('/')
    move_not_effectives = move_type.not_effective.split('/')
    enemy_types = [Type.query.get(enemy.type1), Type.query.get(enemy.type2)]

    dinimon.energy -= int(move.energy_cost)

    for enemy_type in enemy_types:
        enemy_vulnerabilities = enemy_type.vulnerable_to.split('/')
        enemy_resistances = enemy_type.resistant_to.split('/')
        for vulnerablility in enemy_vulnerabilities:
            if str(move_type.type_id) == vulnerablility:
                damage *= 2
                print(f'{vulnerablility} is vulnerable to your {move_type.type} attack!')
        for resistance in enemy_resistances:
            if str(move_type.type_id) == resistance:
                damage //= 2
                print(f'{vulnerablility} is resistant against your {move_type.type} attack...')

    # print(f'Enemy is at {enemy.health} / {enemy.max_health} health points!')
    health -= damage
    enemy.health = health
    # print(f'You used {move.move} for {damage} damage!')
    # print(f'The enemy is NOW at {enemy.health} / {enemy.max_health} health points!')
    db.session.commit()


def run_enemy_attack(main_dini_id, enemy_dini):
    main_dini = Captured_Dinimon.query.get(main_dini_id)
    enemy_moves = []
    if enemy_dini.move1 != 14:
        enemy_moves.append(enemy_dini.move1)
    if enemy_dini.move2 != 14:
        enemy_moves.append(enemy_dini.move2)
    if enemy_dini.move3 != 14:
        enemy_moves.append(enemy_dini.move3)
    if enemy_dini.move4 != 14:
        enemy_moves.append(enemy_dini.move4)

    move_id = random.choice(enemy_moves)
    move = Move.query.get(move_id)
    damage = int(move.damage)
    health = int(main_dini.health)
    move_type = Type.query.get(move.type_id)
    dini_in_dex = Dinimon.query.get(main_dini.dinimon_id)
    main_dini_types = [Type.query.get(dini_in_dex.type1), Type.query.get(dini_in_dex.type2)]

    for main_dini_type in main_dini_types:
        dini_vulnerabilities = main_dini_type.vulnerable_to.split('/')
        dini_resistances = main_dini_type.resistant_to.split('/')
        for vulnerablility in dini_vulnerabilities:
            if str(move_type.type_id) == vulnerablility:
                damage *= 2
        for resistance in dini_resistances:
            if str(move_type.type_id) == resistance:
                damage //= 2

    health -= damage
    main_dini.health = health
    db.session.commit()
    return move


def health_check(main_dini, enemy_dini):
    if main_dini.health <= 0:
        return 'main_dini_dead'
    if enemy_dini.health <= 0:
        return 'enemy_dini_dead'
    
    return 'none'


def nickname_dinimon(nickname, captured_dini_id):
    new_dini = Captured_Dinimon.query.get(captured_dini_id)
    new_dini.nickname = nickname
    db.session.commit()


def manage_party(dinimon, add_remove, player_id):
    party_data = Captured_Dinimon.query.filter(
        Captured_Dinimon.in_party == True,
        Captured_Dinimon.player_id == player_id
        )
    party = []
    for dini in party_data:
        party.append(dini)

    if add_remove == 'add':
        if len(party) < 6:
            dinimon.in_party = True

    elif add_remove == 'remove':
        if len(party) > 1:
            dinimon.in_party = False

    db.session.commit()


def collect_wild_battle_xp(player_id, enemy_dini, main_dini):
    main_xp = enemy_dini.catchability * 10
    party_xp = enemy_dini.catchability * 5
    main_dini.experience += main_xp
    level_up_check(main_dini)

    party = Captured_Dinimon.query.filter(
        Captured_Dinimon.in_party == True,
        Captured_Dinimon.player_id == player_id,
        Captured_Dinimon.captured_dinimon_id != main_dini.captured_dinimon_id
    )
    for dinimon in party:
        dinimon.experience += party_xp
        level_up_check(dinimon)

    print(f"{main_xp} earned!")
    db.session.commit()


def catch_xp(player_id, enemy_dini, main_dini, is_discovered):
    if is_discovered == True:
        main_xp = enemy_dini.catchability * 15
        party_xp = enemy_dini.catchability * 6
    else:
        main_xp = enemy_dini.catchability * 8
        party_xp = enemy_dini.catchability * 4
    main_dini.experience += main_xp
    level_up_check(main_dini)
    party = Captured_Dinimon.query.filter(
        Captured_Dinimon.in_party == True,
        Captured_Dinimon.player_id == player_id,
        Captured_Dinimon.captured_dinimon_id != main_dini.captured_dinimon_id
    )
    print(f"{main_xp} earned!")
    for dinimon in party:
        dinimon.experience += party_xp
        level_up_check(dinimon)
    db.session.commit()


def level_up_check(dinimon):
    if dinimon.experience >= dinimon.max_experience:
        new_max_experience = dinimon.max_experience
        new_max_experience *= 1.15

        remainder = dinimon.experience - dinimon.max_experience

        dinimon.level += 1
        dinimon.experience = remainder
        dinimon.max_experience = new_max_experience

        dinimon.max_health += 10
        dinimon.health = dinimon.max_health

        # evolution_check(dinimon)

        db.session.commit()


def evolution_check(player_id):

    all_dinimon = Captured_Dinimon.query.filter(
        Captured_Dinimon.player_id == player_id,
        Captured_Dinimon.in_party == True
        )
    
    for dinimon in all_dinimon:
        dini_dex = Dinimon.query.get(dinimon.dinimon_id)
        if dinimon.level >= dini_dex.level_to_evolve and dini_dex.can_evolve == True:
            dinimon.evo_ready = True
            db.session.commit()
            new_dini_id = dini_dex.number + 1
            new_dini = Dinimon.query.get(new_dini_id)
            return dini_dex, dinimon, new_dini, True

    # AS THE EVOLUTION CALCULATES BY NEXT DINI NUMBER, I"LL NEED TO ADD SPECIFIC CONDITIONALS FOR BRANCHED EVOLUTIONS OR SPECIFIC EVO REQUIRMENTS LATER
    return None, None, None, False