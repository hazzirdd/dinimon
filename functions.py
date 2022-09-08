from cgitb import reset
from server_folder import db
from server_folder.model import Event, Area

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

# def exit_arrow_check(left, top):
#     if left == 350 and top == 0:
#         # return True
#         return False
#     else:
#         return False



def event_check(area_id, sprite_xy):
    area = Area.query.get(area_id)
    events = Event.query.filter(Event.area_id == area.area_id).all()
    area_x, area_y = split_area_coords(area.coordinates)
    print('PLAYER:',sprite_xy)
    for event in events:
        print(event.xy)
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
            elif event.event == 'right_exit':
                area_y += 1
                result = find_new_area(event, area_x, area_y)

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


# def area_check(area):
#     if area == 'https://i.ytimg.com/vi/9TlmBmMonIc/maxresdefault.jpg':
#         left = 350
#         top = 420
#         arrow_up_left = 420
#         arrow_up_top = 0

#         return left, top, arrow_up_left, arrow_up_top

