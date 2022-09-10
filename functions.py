import random

from server_folder import db
from server_folder.model import Event, Area, Dinimon, Type

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
                
            # This loop is printing spawning multiple dinimon in one spot

        if possible_dinimon:
            print(possible_dinimon)
            dinimon = random.choice(possible_dinimon)

            spawn_dinimon = Event(event='dinimon', area_id=spawner.area_id, left_coord=spawner.left_coord, top_coord=spawner.top_coord, xy=spawner.xy, image=dinimon.image, width=dinimon.width)

            db.session.add(spawn_dinimon)

    db.session.commit()








