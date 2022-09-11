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


def setup_main_dini_moves(main_dini):
    moves = []
    print(main_dini, ", I CHOOSE YOU!!!")
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

    print('ALL POSSIBLE MOVES:', all_moves)
    # BUG: when i split all_moves it creates a none type variable

    move1 = random.choice(all_moves)
    move1_id = Move.query.filter(Move.move == move1).first()
    all_moves.remove(move1)

    if all_moves:
        move2 = random.choice(all_moves)
        move2_id = Move.query.filter(Move.move == move2).first()
        all_moves.remove(move2)
    else:
        move2_id = 14
    if all_moves:
        move3 = random.choice(all_moves)
        move3_id = Move.query.filter(Move.move == move3).first()
        all_moves.remove(move3)
    else:
        move3_id = 14
    if all_moves:
        move4 = random.choice(all_moves)
        move4_id = Move.query.filter(Move.move == move4).first()
        all_moves.remove(move4)
    else:
        move4_id = 14

    print('MOVES:',move1_id, move2_id, move3_id, move4_id)

    enemy_dinimon = Enemy_Dinimon(dinimon_id=dinimon_id, move1=move1_id, move2=move2_id, move3=move3_id, move4=move4_id)