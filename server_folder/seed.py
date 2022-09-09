from turtle import right
from model import connect_to_db, db, Area, Event, Type, Dinimon

jungle = 'http://www.clker.com/cliparts/a/r/C/L/q/z/green-box-hi.png'

top_exit = "https://storage.cloud.google.com/property-runner/Dinimon/top_exit.png"
left_exit = "https://storage.cloud.google.com/property-runner/Dinimon/left_exit.png"
right_exit = "https://storage.cloud.google.com/property-runner/Dinimon/right_exit.png"
bottom_exit = "https://storage.cloud.google.com/property-runner/Dinimon/bottom_exit.png"


def create_area():
    print('Areas')
    Area.query.delete()

    area1 = Area(biome='Grasslands', coordinates='1/1', image="https://i.pinimg.com/originals/23/5d/2d/235d2d090029b4ff9031f67b0e5f4767.jpg")
    area2 = Area(biome='Grasslands', coordinates='2/1', image="https://i.pinimg.com/originals/e4/9d/11/e49d1124a69f97fa7d8600604e6fc881.jpg")
    area3 = Area(biome='Grasslands', coordinates='3/1', image="https://i.pinimg.com/originals/41/bc/2b/41bc2bbc9a6429cf8f8f69a44b5153c4.jpg")
    area4 = Area(biome='Grasslands', coordinates='4/1', image="https://i.pinimg.com/originals/5c/13/10/5c1310b40372ca3a25b3fb56446d5d6e.jpg")
    area5 = Area(biome='Grasslands', coordinates='2/0', image="https://i.pinimg.com/originals/27/fe/c5/27fec5def92dcdbf9bcd0d55360605e9.jpg")
    area6 = Area(biome='Grasslands', coordinates='3/0', image="https://i.pinimg.com/originals/ae/20/3a/ae203ae7a1e39685d5bce3ac7c681821.jpg")
    area7 = Area(biome='Grasslands', coordinates='4/0', image="https://i.pinimg.com/originals/86/76/4c/86764c46415446e4568c44145f08d4a5.jpg")
    area8 = Area(biome='Jungle', coordinates='3/-1', image=jungle)
    area9 = Area(biome='Grasslands', coordinates='2/2', image="https://i.pinimg.com/originals/22/c1/89/22c18905c82e907b1548c7d89194e3a0.jpg")
    area10 = Area(biome='Desert', coordinates='5/2', image="https://i.pinimg.com/originals/58/b5/3e/58b53e2ecbbd774cb0688d7993b21df2.jpg")
    area11 = Area(biome='Grasslands', coordinates='3/2', image="https://i.pinimg.com/originals/3d/06/cb/3d06cb30e1186db39f925dcb397406e2.jpg")
    area12 = Area(biome='Grasslands', coordinates='4/2', image="https://i.pinimg.com/originals/16/3a/20/163a208303fdba022a850fc611a15073.jpg")

    db.session.add(area1)
    db.session.add(area2)
    db.session.add(area3)
    db.session.add(area4)
    db.session.add(area5)
    db.session.add(area6)
    db.session.add(area7)
    db.session.add(area8)
    db.session.add(area9)
    db.session.add(area10)
    db.session.add(area11)
    db.session.add(area12)

def create_event():
    print('Events')
    Event.query.delete()

    # 1/1
    event1 = Event(event='top_exit', area_id=1, left_coord=346, top_coord=0, xy=806, image=top_exit)
    # 2/1
    event2 = Event(event='top_exit', area_id=2, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event3 = Event(event='left_exit', area_id=2, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event4 = Event(event='right_exit', area_id=2, left_coord=618, top_coord=210, xy=512, image=right_exit)
    event5 = Event(event='bottom_exit', area_id=2, left_coord=124, top_coord=490, xy=106, image=bottom_exit)

    spawner1 = Event(event='dinimon_spawn', area_id=2, left_coord=630, top_coord=280, xy=409, image='none')
    spawner2 = Event(event='dinimon_spawn', area_id=2, left_coord=140, top_coord=210, xy=502, image='none')
    # 2/2
    event6 = Event(event='top_exit', area_id=9, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event7 = Event(event='left_exit', area_id=9, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event8 = Event(event='right_exit', area_id=9, left_coord=618, top_coord=210, xy=512, image=right_exit)
    # 2/0
    event10 = Event(event='top_exit', area_id=5, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event11 = Event(event='right_exit', area_id=5, left_coord=618, top_coord=210, xy=512, image=right_exit)
    # 3/0
    event12 = Event(event='bottom_exit', area_id=6, left_coord=124, top_coord=490, xy=106, image=bottom_exit)
    event13 = Event(event='right_exit', area_id=6, left_coord=618, top_coord=210, xy=512, image=right_exit)
    # 3/1
    event14 = Event(event='top_exit', area_id=3, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event15 = Event(event='left_exit', area_id=3, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event16 = Event(event='right_exit', area_id=3, left_coord=618, top_coord=210, xy=512, image=right_exit)
    event17 = Event(event='bottom_exit', area_id=3, left_coord=124, top_coord=490, xy=106, image=bottom_exit)
    # 3/2
    event18 = Event(event='top_exit', area_id=11, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event19 = Event(event='left_exit', area_id=11, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event20 = Event(event='bottom_exit', area_id=11, left_coord=124, top_coord=490, xy=106, image=bottom_exit)    
    # 4/0
    event21 = Event(event='right_exit', area_id=7, left_coord=618, top_coord=210, xy=512, image=right_exit)    
    # 4/1
    event22 = Event(event='left_exit', area_id=4, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event23 = Event(event='right_exit', area_id=4, left_coord=618, top_coord=210, xy=512, image=right_exit)
    event24 = Event(event='bottom_exit', area_id=4, left_coord=124, top_coord=490, xy=106, image=bottom_exit)    
    # 4/2
    event25 = Event(event='top_exit', area_id=12, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event26 = Event(event='left_exit', area_id=12, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event27 = Event(event='bottom_exit', area_id=12, left_coord=124, top_coord=490, xy=106, image=bottom_exit)    
    # 5/2
    event28 = Event(event='bottom_exit', area_id=10, left_coord=124, top_coord=490, xy=106, image=bottom_exit)

    db.session.add(event1)
    db.session.add(event2)
    db.session.add(event3)
    db.session.add(event4)
    db.session.add(event5)
    db.session.add(event6)
    db.session.add(event7)
    db.session.add(event8)
    db.session.add(spawner1)
    db.session.add(event10)
    db.session.add(event11)
    db.session.add(event12)
    db.session.add(event13)
    db.session.add(event14)
    db.session.add(event15)
    db.session.add(event16)
    db.session.add(event17)
    db.session.add(event18)
    db.session.add(event19)
    db.session.add(event20)
    db.session.add(event21)
    db.session.add(event22)
    db.session.add(event23)
    db.session.add(event24)
    db.session.add(event25)
    db.session.add(event26)
    db.session.add(event27)
    db.session.add(event28)
    db.session.add(spawner2)


def create_types():
    print("Types")
    Type.query.delete()

    type_1 = Type(type='bright', super_effective='3/7/11', not_effective='1/6/10', vulnerable_to='5/8/10', resistant_to='1/2/3/11')
    type_2 = Type(type='cold', super_effective='5/8', not_effective='1/3/11', vulnerable_to='6/7/9', resistant_to='4/10/13')
    type_3 = Type(type='shadow', super_effective='5/7/8', not_effective='1/4/9/11', vulnerable_to='1/11', resistant_to='2/8/9')
    type_4 = Type(type='air', super_effective='6/7/9', not_effective='2/5/8/11', vulnerable_to='8/11/13', resistant_to='3/6')
    type_5 = Type(type='water', super_effective='1/9/10/13', not_effective='6/7/8/11', vulnerable_to='2/3/6/8/11', resistant_to='4/7/9/13')
    type_6 = Type(type='electric', super_effective='2/5/10', not_effective='4/7/9/11', vulnerable_to='4/7', resistant_to='1/5/10')
    type_7 = Type(type='earth', super_effective='2/6/9/13', not_effective='5/7/10/11', vulnerable_to='1/3/4/10/11', resistant_to='5/6/7/13')
    type_8 = Type(type='growth', super_effective='1/4/5', not_effective='3/9/10/11', vulnerable_to='2/3/9', resistant_to='4/5')
    type_9 = Type(type='burning', super_effective='2/8/10', not_effective='3/5/9/11', vulnerable_to='4/5/7/11', resistant_to='3/6/8/9')
    type_10 = Type(type='metal', super_effective='1/7', not_effective='2/6/13', vulnerable_to='5/6/9/13', resistant_to='1/7/8')
    type_11 = Type(type='titan', super_effective='3/4/5/7/9/11/12', not_effective='1/13', vulnerable_to='1/11/13', resistant_to='2/3/4/5/6/7/8/9/12')
    type_12 = Type(type='familiar', super_effective='', not_effective='11', vulnerable_to='11', resistant_to='')
    type_13 = Type(type='toxic', super_effective='', not_effective='', vulnerable_to='', resistant_to='')
    type_14 = Type(type='none', super_effective='', not_effective='', vulnerable_to='', resistant_to='')

    db.session.add(type_1)
    db.session.add(type_2)
    db.session.add(type_3)
    db.session.add(type_4)
    db.session.add(type_5)
    db.session.add(type_6)
    db.session.add(type_7)
    db.session.add(type_8)
    db.session.add(type_9)
    db.session.add(type_10)
    db.session.add(type_11)
    db.session.add(type_12)
    db.session.add(type_13)
    db.session.add(type_14)


def create_dinimon():
    print('Dinimon')
    Dinimon.query.delete()

    dinimon_1 = Dinimon(number=1, name='Sunbun', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Sunbun.png', type1=1, type2=14, line='Sunbun', can_evolve=True, rarity=10, biomes='Grasslands', health_range='45-60', energy_range='10-15', possible_moves='Bright Attack')

    dinimon_2 = Dinimon(number=2, name='Shinebun', width=55, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Shinebun.png', type1=1, type2=14, line='Sunbun', can_evolve=True, rarity=5, biomes='Grasslands', health_range='50-85', energy_range='10-15', possible_moves='Bright Attack')

    db.session.add(dinimon_1)
    db.session.add(dinimon_2)


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)

    db.create_all()

    create_area()
    create_event()
    create_types()
    create_dinimon()

    db.session.commit()