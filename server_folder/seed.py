from turtle import right
from model import connect_to_db, db, Area, Event, Type, Dinimon, Player, Captured_Dinimon, Move, Enemy_Dinimon, Item, Inventory

top_exit = "https://storage.cloud.google.com/property-runner/Dinimon/top_exit.png"
left_exit = "https://storage.cloud.google.com/property-runner/Dinimon/left_exit.png"
right_exit = "https://storage.cloud.google.com/property-runner/Dinimon/right_exit.png"
bottom_exit = "https://storage.cloud.google.com/property-runner/Dinimon/bottom_exit.png"

def create_player():
    print('Players')
    Player.query.delete()

    player1 = Player(username='Haz', password='123')

    db.session.add(player1)


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
    area8 = Area(biome='Jungle', coordinates='3/-1', image='https://www.komar.de/en/media/catalog/product/cache/5/image/9df78eab33525d08d6e5fb8d27136e95/l/j/ljx8-060.jpg')
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
    spawner3 = Event(event='dinimon_spawn', area_id=1, left_coord=770, top_coord=140, xy=611, image='none')
    spawner4 = Event(event='dinimon_spawn', area_id=2, left_coord=210, top_coord=420, xy=203, image='none')
    spawner5 = Event(event='dinimon_spawn', area_id=2, left_coord=770, top_coord=140, xy=611, image='none')
    spawner6 = Event(event='dinimon_spawn', area_id=2, left_coord=280, top_coord=70, xy=704, image='none')
    # 2/2
    event6 = Event(event='top_exit', area_id=9, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event7 = Event(event='left_exit', area_id=9, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event8 = Event(event='right_exit', area_id=9, left_coord=618, top_coord=210, xy=512, image=right_exit)

    spawner7 = Event(event='dinimon_spawn', area_id=9, left_coord=70, top_coord=420, xy=201, image='none')
    spawner8 = Event(event='dinimon_spawn', area_id=9, left_coord=420, top_coord=420, xy=206, image='none')
    spawner9 = Event(event='dinimon_spawn', area_id=9, left_coord=420, top_coord=210, xy=506, image='none')
    spawner10 = Event(event='dinimon_spawn', area_id=9, left_coord=70, top_coord=0, xy=801, image='none')
    spawner11 = Event(event='dinimon_spawn', area_id=9, left_coord=630, top_coord=70, xy=709, image='none')
    spawner12 = Event(event='dinimon_spawn', area_id=9, left_coord=700, top_coord=350, xy=310, image='none')
    # 2/0
    event10 = Event(event='top_exit', area_id=5, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event11 = Event(event='right_exit', area_id=5, left_coord=618, top_coord=210, xy=512, image=right_exit)

    spawner13 = Event(event='dinimon_spawn', area_id=5, left_coord=770, top_coord=420, xy=211, image='none')
    spawner14 = Event(event='dinimon_spawn', area_id=5, left_coord=420, top_coord=210, xy=506, image='none')
    spawner15 = Event(event='dinimon_spawn', area_id=5, left_coord=700, top_coord=70, xy=710, image='none')
    # 3/0
    event12 = Event(event='bottom_exit', area_id=6, left_coord=124, top_coord=490, xy=106, image=bottom_exit)
    event13 = Event(event='right_exit', area_id=6, left_coord=618, top_coord=210, xy=512, image=right_exit)

    spawner16 = Event(event='dinimon_spawn', area_id=6, left_coord=630, top_coord=420, xy=209, image='none')
    spawner17 = Event(event='dinimon_spawn', area_id=6, left_coord=560, top_coord=70, xy=708, image='none')
    spawner41 = Event(event='dinimon_spawn', area_id=6, left_coord=70, top_coord=140, xy=601, image='none', biome="Jungle")
    # 3/1
    event14 = Event(event='top_exit', area_id=3, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event15 = Event(event='left_exit', area_id=3, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event16 = Event(event='right_exit', area_id=3, left_coord=618, top_coord=210, xy=512, image=right_exit)
    event17 = Event(event='bottom_exit', area_id=3, left_coord=124, top_coord=490, xy=106, image=bottom_exit)

    spawner18 = Event(event='dinimon_spawn', area_id=3, left_coord=140, top_coord=420, xy=202, image='none')
    spawner19 = Event(event='dinimon_spawn', area_id=3, left_coord=770, top_coord=420, xy=211, image='none')
    spawner20 = Event(event='dinimon_spawn', area_id=3, left_coord=700, top_coord=70, xy=710, image='none')
    spawner21 = Event(event='dinimon_spawn', area_id=3, left_coord=70, top_coord=0, xy=801, image='none')
    # 3/2
    event18 = Event(event='top_exit', area_id=11, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event19 = Event(event='left_exit', area_id=11, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event20 = Event(event='bottom_exit', area_id=11, left_coord=124, top_coord=490, xy=106, image=bottom_exit)

    spawner22 = Event(event='dinimon_spawn', area_id=11, left_coord=280, top_coord=70, xy=704, image='none')
    spawner23 = Event(event='dinimon_spawn', area_id=11, left_coord=70, top_coord=350, xy=301, image='none')
    spawner24 = Event(event='dinimon_spawn', area_id=11, left_coord=770, top_coord=420, xy=211, image='none')
    spawner25 = Event(event='dinimon_spawn', area_id=11, left_coord=630, top_coord=70, xy=709, image='none')    
    # 4/0
    event21 = Event(event='right_exit', area_id=7, left_coord=618, top_coord=210, xy=512, image=right_exit)

    spawner26 = Event(event='dinimon_spawn', area_id=7, left_coord=700, top_coord=420, xy=210, image='none')
    spawner27 = Event(event='dinimon_spawn', area_id=7, left_coord=70, top_coord=450, xy=301, image='none')
    spawner28 = Event(event='dinimon_spawn', area_id=7, left_coord=210, top_coord=70, xy=703, image='none')
    spawner29 = Event(event='dinimon_spawn', area_id=7, left_coord=420, top_coord=140, xy=606, image='none')
    # 4/1
    event22 = Event(event='left_exit', area_id=4, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event23 = Event(event='right_exit', area_id=4, left_coord=618, top_coord=210, xy=512, image=right_exit)
    event24 = Event(event='bottom_exit', area_id=4, left_coord=124, top_coord=490, xy=106, image=bottom_exit) 

    spawner30 = Event(event='dinimon_spawn', area_id=4, left_coord=140, top_coord=350, xy=302, image='none')
    spawner31 = Event(event='dinimon_spawn', area_id=4, left_coord=770, top_coord=420, xy=211, image='none')
    spawner32 = Event(event='dinimon_spawn', area_id=4, left_coord=700, top_coord=70, xy=710, image='none')   
    # 4/2
    event25 = Event(event='top_exit', area_id=12, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event26 = Event(event='left_exit', area_id=12, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event27 = Event(event='bottom_exit', area_id=12, left_coord=124, top_coord=490, xy=106, image=bottom_exit)

    spawner33 = Event(event='dinimon_spawn', area_id=12, left_coord=210, top_coord=350, xy=303, image='none')
    spawner34 = Event(event='dinimon_spawn', area_id=12, left_coord=210, top_coord=70, xy=703, image='none')
    spawner35 = Event(event='dinimon_spawn', area_id=12, left_coord=560, top_coord=210, xy=508, image='none')
    spawner36 = Event(event='dinimon_spawn', area_id=12, left_coord=770, top_coord=420, xy=211, image='none')
    
    # 5/2
    event28 = Event(event='bottom_exit', area_id=10, left_coord=124, top_coord=490, xy=106, image=bottom_exit)

    spawner37 = Event(event='dinimon_spawn', area_id=10, left_coord=770, top_coord=280, xy=411, image='none', biome="Desert")
    spawner38 = Event(event='dinimon_spawn', area_id=10, left_coord=700, top_coord=70, xy=710, image='none', biome="Desert")
    spawner39 = Event(event='dinimon_spawn', area_id=10, left_coord=210, top_coord=140, xy=603, image='none', biome="Desert")
    spawner40 = Event(event='dinimon_spawn', area_id=10, left_coord=70, top_coord=350, xy=301, image='none', biome="Desert")

    db.session.add(event1)
    db.session.add(event2)
    db.session.add(event3)
    db.session.add(event4)
    db.session.add(event5)
    db.session.add(event6)
    db.session.add(event7)
    db.session.add(event8)
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

    db.session.add(spawner1)
    db.session.add(spawner2)
    db.session.add(spawner3)
    db.session.add(spawner4)
    db.session.add(spawner5)
    db.session.add(spawner6)
    db.session.add(spawner7)
    db.session.add(spawner8)
    db.session.add(spawner9)
    db.session.add(spawner10)
    db.session.add(spawner11)
    db.session.add(spawner12)
    db.session.add(spawner13)
    db.session.add(spawner14)
    db.session.add(spawner15)
    db.session.add(spawner16)
    db.session.add(spawner17)
    db.session.add(spawner18)
    db.session.add(spawner19)
    db.session.add(spawner20)
    db.session.add(spawner21)
    db.session.add(spawner22)
    db.session.add(spawner23)
    db.session.add(spawner24)
    db.session.add(spawner25)
    db.session.add(spawner26)
    db.session.add(spawner27)
    db.session.add(spawner28)
    db.session.add(spawner29)
    db.session.add(spawner30)
    db.session.add(spawner31)
    db.session.add(spawner32)
    db.session.add(spawner33)
    db.session.add(spawner34)
    db.session.add(spawner35)
    db.session.add(spawner36)
    db.session.add(spawner37)
    db.session.add(spawner38)
    db.session.add(spawner39)
    db.session.add(spawner40)
    db.session.add(spawner41)


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
    type_12 = Type(type='familiar', super_effective='/', not_effective='11/', vulnerable_to='11/', resistant_to='/')
    type_13 = Type(type='toxic', super_effective='4/10/11', not_effective='2/5/7', vulnerable_to='5/7', resistant_to='10/11')
    type_14 = Type(type='none', super_effective='/', not_effective='/', vulnerable_to='/', resistant_to='/')

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


def create_move():
    print('Move')
    Move.query.delete()

    move1 = Move(move='Bright Attack', type_id=1, energy_cost=1, damage=3)
    move2 = Move(move='Cold Attack', type_id=2, energy_cost=1, damage=3)
    move3 = Move(move='Shadow Attack', type_id=3, energy_cost=1, damage=3)
    move4 = Move(move='Air Attack', type_id=4, energy_cost=1, damage=3)
    move5 = Move(move='Water Attack', type_id=5, energy_cost=1, damage=3)
    move6 = Move(move='Electric Attack', type_id=6, energy_cost=1, damage=3)
    move7 = Move(move='Earth Attack', type_id=7, energy_cost=1, damage=3)
    move8 = Move(move='Growth Attack', type_id=8, energy_cost=1, damage=3)
    move9 = Move(move='Burning Attack', type_id=9, energy_cost=1, damage=3)
    move10 = Move(move='Metal Attack', type_id=10, energy_cost=1, damage=3)
    move11 = Move(move='Titan Attack', type_id=11, energy_cost=1, damage=3)
    move12 = Move(move='Familiar Attack', type_id=12, energy_cost=1, damage=3)
    move13 = Move(move='Toxic Attack', type_id=13, energy_cost=1, damage=3)
    move_none_14 = Move(move='none', type_id=14, energy_cost=0, damage=0)
    
    db.session.add(move1)
    db.session.add(move2)
    db.session.add(move3)
    db.session.add(move4)
    db.session.add(move5)
    db.session.add(move6)
    db.session.add(move7)
    db.session.add(move8)
    db.session.add(move9)
    db.session.add(move10)
    db.session.add(move11)
    db.session.add(move12)
    db.session.add(move13)
    db.session.add(move_none_14)


def create_dinimon():
    print('Dinimon')
    Dinimon.query.delete()

    dinimon_1 = Dinimon(number=1, name='Sunbun', width=30, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Sunbun.png', type1=1, type2=14, line='Sunbun', can_evolve=True, rarity=20, biomes='Grasslands/Desert', health_range='45-60', energy_range='10-15', possible_moves='Bright Attack/Familiar Attack')

    dinimon_2 = Dinimon(number=2, name='Shinebun', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Shinebun.png', type1=1, type2=14, line='Sunbun', can_evolve=True, rarity=6, biomes='Grasslands/Desert', health_range='50-85', energy_range='10-15', possible_moves='Bright Attack/')

    dinimon_3 = Dinimon(number=3, name='Brightbun', width=69, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Brightbun.png', type1=1, type2=14, line='Sunbun', can_evolve=False, rarity=3, biomes='Grasslands/Desert', health_range='85-95', energy_range='10-15', possible_moves='Bright Attack/')

    dinimon_4 = Dinimon(number=4, name='Cubbit', width=15, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Cubbit.png', type1=2, type2=14, line='Cubbit', can_evolve=True, rarity=14, biomes='Snow', health_range='50', energy_range='10-15', possible_moves='Cold Attack/')

    dinimon_5 = Dinimon(number=5, name='Froggo', width=30, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Froggo.png', type1=2, type2=14, line='Cubbit', can_evolve=True, rarity=10, biomes='Snow', health_range='50', energy_range='10-15', possible_moves='Cold Attack/')

    dinimon_6 = Dinimon(number=6, name='Froaking', width=50, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Froaking.png', type1=2, type2=14, line='Cubbit', can_evolve=False, rarity=3, biomes='Snow', health_range='50', energy_range='10-15', possible_moves='Cold Attack/')

    dinimon_7 = Dinimon(number=7, name='Rockball', width=45, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Rockball.png', type1=7, type2=14, line='Rockball', can_evolve=True, rarity=16, biomes='Grasslands/Desert/Mountain', health_range='50', energy_range='10-15', possible_moves='Earth Attack/')

    dinimon_8 = Dinimon(number=8, name='Ballrock', width=60, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Ballrock.png', type1=7, type2=14, line='Rockball', can_evolve=True, rarity=6, biomes='Grasslands/Desert/Mountain', health_range='50', energy_range='10-15', possible_moves='Earth Attack/')
    
    dinimon_9 = Dinimon(number=9, name='Riprock', width=65, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Ruprock.png', type1=7, type2=14, line='Rockball', can_evolve=False, rarity=3, biomes='Mountain', health_range='50', energy_range='10-15', possible_moves='Earth Attack/')

    dinimon_10 = Dinimon(number=10, name='Spitlick', width=55, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Spitlick.png', type1=5, type2=14, line='Spitlick', can_evolve=True, rarity=15, biomes='Grasslands/Swamp/Beach/Jungle', health_range='50', energy_range='10-15', possible_moves='Water Attack/')

    dinimon_11 = Dinimon(number=11, name='Spitbo', width=85, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Spitbo.png', type1=5, type2=14, line='Spitlick', can_evolve=True, rarity=7, biomes='Grasslands/Swamp/Beach/Jungle', health_range='50', energy_range='10-15', possible_moves='Water Attack/')

    dinimon_12 = Dinimon(number=12, name='Salivamus', width=115, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Salivamus.png', type1=5, type2=14, line='Spitlick', can_evolve=False, rarity=3, biomes='Grasslands/Beach/Swamp/Jungle', health_range='50', energy_range='10-15', possible_moves='Water Attack/')

    dinimon_13 = Dinimon(number=13, name='Noose', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Noose.png', type1=3, type2=4, line='Noose', can_evolve=True, rarity=13, biomes='Desert', health_range='50', energy_range='10-15', possible_moves='Shadow Attack/')

    dinimon_14 = Dinimon(number=14, name='Wrapparition', width=50, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Wrapparition.png', type1=3, type2=4, line='Noose', can_evolve=True, rarity=3, biomes='Desert', health_range='50', energy_range='10-15', possible_moves='Shadow Attack/')

    dinimon_15 = Dinimon(number=15, name='Knotaliss', width=60, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Knotaliss.png', type1=3, type2=4, line='Noose', can_evolve=False, rarity=1, biomes='Desert', health_range='50', energy_range='10-15', possible_moves='Shadow Attack/')

    dinimon_16 = Dinimon(number=16, name='Shaydlet', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Shaydlet.png', type1=3, type2=14, line='Shaydlet', can_evolve=True, rarity=15, biomes='Grasslands/Mountain/Desert/Cave', health_range='50', energy_range='10-15', possible_moves='Shadow Attack/')

    dinimon_17 = Dinimon(number=17, name='Shaydark', width=65, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Shaydark.png', type1=3, type2=14, line='Shaydlet', can_evolve=True, rarity=7, biomes='Grasslands/Mountain/Desert/Cave', health_range='50', energy_range='10-15', possible_moves='Shadow Attack/')

    dinimon_18 = Dinimon(number=18, name='Shayddler', width=70, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Shayddler.png', type1=3, type2=14, line='Shadlet', can_evolve=False, rarity=3, biomes='Mountain/Desert/Cave', health_range='50', energy_range='10-15', possible_moves='Shadow Attack/')

    dinimon_19 = Dinimon(number=19, name='Beak Beak', width=30, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Beak Beak.png', type1=4, type2=14, line='Beak Beak', can_evolve=True, rarity=18, biomes='Grasslands/Mountain/Beach/Jungle', health_range='50', energy_range='10-15', possible_moves='Air Attack/')

    dinimon_20 = Dinimon(number=20, name='Beakwing', width=80, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Beakwing.png', type1=4, type2=14, line='Beak Beak', can_evolve=True, rarity=7, biomes='Grasslands/Mountain/Beach/Jungle', health_range='50', energy_range='10-15', possible_moves='Air Attack/')

    dinimon_21 = Dinimon(number=21, name='Quetzabeak', width=150, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Quetzabeak.png', type1=4, type2=14, line='Beak Beak', can_evolve=False, rarity=3, biomes='Jungle/Mountain/Peaks', health_range='50', energy_range='10-15', possible_moves='Air Attack/')

    dinimon_22 = Dinimon(number=22, name='Buzzmouse', width=22, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Buzzmouse.png', type1=6, type2=14, line='Buzzmouse', can_evolve=True, rarity=16, biomes='Grasslands/Desert', health_range='50', energy_range='10-15', possible_moves='Electric Attack/')

    dinimon_23 = Dinimon(number=23, name='Stratic', width=35, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Stratic.png', type1=6, type2=14, line='Buzzmouse', can_evolve=True, rarity=7, biomes='Grasslands/Desert', health_range='50', energy_range='10-15', possible_moves='Electric Attack/')

    dinimon_24 = Dinimon(number=24, name='Statratic', width=60, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Statratic.png', type1=6, type2=14, line='Buzzmouse', can_evolve=False, rarity=3, biomes='Grasslands/Desert', health_range='50', energy_range='10-15', possible_moves='Electric Attack/')

    dinimon_25 = Dinimon(number=25, name='Enchantling', width=35, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Enchantling.png', type1=12, type2=14, line='Enchantling', can_evolve=True, rarity=6, biomes='Grasslands/Jungle', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_26 = Dinimon(number=26, name='Magic Shell', width=60, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Magic Shell.png', type1=12, type2=14, line='Enchantling', can_evolve=True, rarity=2, biomes='Jungle', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_27 = Dinimon(number=27, name='Tortanic', width=115, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Tortanic.png', type1=12, type2=11, line='Enchantling', can_evolve=False, rarity=1, biomes='Jungle', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_28 = Dinimon(number=28, name='BimBim', width=34, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/BimBim.png', type1=12, type2=14, line='BimBim', can_evolve=True, rarity=17, biomes='Grasslands/Mountain', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_29 = Dinimon(number=29, name='BimBam', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Bimbam.png', type1=12, type2=14, line='BimBim', can_evolve=True, rarity=6, biomes='Grasslands/Mountain', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_30 = Dinimon(number=30, name='BlamSlam', width=55, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Blamslam.png', type1=12, type2=14, line='BimBim', can_evolve=False, rarity=3, biomes='Grasslands/Mountain', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_31 = Dinimon(number=31, name='Tulil', width=35, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Tulil.png', type1=8, type2=14, line='Tulil', can_evolve=True, rarity=15, biomes='Grasslands/Jungle', health_range='50', energy_range='10-15', possible_moves='Growth Attack/')

    dinimon_32 = Dinimon(number=32, name='Tuking', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Tuking.png', type1=8, type2=14, line='Tulil', can_evolve=True, rarity=6, biomes='Grasslands/Jungle', health_range='50', energy_range='10-15', possible_moves='Growth Attack/')

    dinimon_33 = Dinimon(number=33, name='Tutwine', width=75, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Tutwine.png', type1=8, type2=14, line='Tulil', can_evolve=False, rarity=3, biomes='Jungle', health_range='50', energy_range='10-15', possible_moves='Growth Attack/')

    dinimon_34 = Dinimon(number=34, name='Stickmatch', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Stickmatch.png', type1=12, type2=14, line='Stickmatch', can_evolve=True, rarity=15, biomes='Mountain/Cave', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_35 = Dinimon(number=35, name='Strikematch', width=60, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Strikematch.png', type1=12, type2=14, line='Stickmatch', can_evolve=True, rarity=6, biomes='Mountain/Cave', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_36 = Dinimon(number=36, name='Stranglematch', width=90, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Stranglematch.png', type1=12, type2=14, line='Stickmatch', can_evolve=False, rarity=3, biomes='Mountain/Cave', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_37 = Dinimon(number=37, name='Salaburn', width=50, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Salaburn.png', type1=9, type2=14, line='Salaburn', can_evolve=True, rarity=15, biomes='Grasslands/Mesa/Cave/Volcano', health_range='50', energy_range='10-15', possible_moves='Burning Attack/')

    dinimon_38 = Dinimon(number=38, name='Baskisinge', width=80, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Baskisinge.png', type1=9, type2=14, line='Salaburn', can_evolve=True, rarity=5, biomes='Grasslands/Mesa/Cave/Volcano', health_range='50', energy_range='10-15', possible_moves='Burning Attack/')

    dinimon_39 = Dinimon(number=39, name='Fareodo', width=100, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Flareodo.png', type1=9, type2=14, line='Salaburn', can_evolve=False, rarity=2, biomes='Grasslands/Mesa/Cave/Volcano', health_range='50', energy_range='10-15', possible_moves='Burning Attack/')

    dinimon_40 = Dinimon(number=40, name='Swiron', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Swiron.png', type1=10, type2=14, line='Swiron', can_evolve=True, rarity=15, biomes='Grasslands/Mountain/Jungle/Swamp', health_range='50', energy_range='10-15', possible_moves='Metal Attack/')

    dinimon_41 = Dinimon(number=41, name='Glintpig', width=70, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Glintpig.png', type1=10, type2=14, line='Swiron', can_evolve=True, rarity=5, biomes='Grasslands/Mountain/Jungle/Swamp', health_range='50', energy_range='10-15', possible_moves='Metal Attack/')

    dinimon_42 = Dinimon(number=42, name='Metaboar', width=90, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Metaboar.png', type1=10, type2=14, line='Swiron', can_evolve=False, rarity=2, biomes='Grasslands/Mountain/Swamp/Jungle', health_range='50', energy_range='10-15', possible_moves='Metal Attack/')

    dinimon_43 = Dinimon(number=43, name='Biosludge', width=45, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Biosludge.png', type1=13, type2=14, line='Biosludge', can_evolve=True, rarity=16, biomes='Grasslands/Swamp/Cave', health_range='50', energy_range='10-15', possible_moves='Toxic Attack/')

    dinimon_44 = Dinimon(number=44, name='Quagunk', width=95, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Quagunk.png', type1=13, type2=14, line='Biosludge', can_evolve=True, rarity=6, biomes='Grasslands/Swamp/Cave', health_range='50', energy_range='10-15', possible_moves='Toxic Attack/')

    dinimon_45 = Dinimon(number=45, name='Heximuck', width=90, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Heximuck.png', type1=13, type2=14, line='Biosludge', can_evolve=False, rarity=3, biomes='Grasslands/Swamp/Cave', health_range='50', energy_range='10-15', possible_moves='Toxic Attack/')
    
    dinimon_46 = Dinimon(number=46, name='Patty', width=60, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Patty.png', type1=12, type2=14, line='Patty', can_evolve=True, rarity=10, biomes='Grasslands', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_47 = Dinimon(number=47, name='Dubpatty', width=60, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Dubpatty.png', type1=12, type2=14, line='Patty', can_evolve=True, rarity=5, biomes='Grasslands', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_48 = Dinimon(number=48, name='Tripatty', width=60, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Tripatty.png', type1=12, type2=14, line='Patty', can_evolve=False, rarity=1, biomes='Grasslands', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_49 = Dinimon(number=49, name='Glowlure', width=30, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Glowlure.png', type1=1, type2=5, line='Glowlure', can_evolve=True, rarity=17, biomes='Cavelake/Ocean', health_range='50', energy_range='10-15', possible_moves='Bright Attack/')

    dinimon_50 = Dinimon(number=50, name='Danglure', width=70, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Danglure.png', type1=1, type2=5, line='Glowlure', can_evolve=True, rarity=6, biomes='Cavelake/Ocean', health_range='50', energy_range='10-15', possible_moves='Bright Attack/')

    dinimon_51 = Dinimon(number=51, name='Fanglure', width=90, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Danglure.png', type1=1, type2=5, line='Glowlure', can_evolve=False, rarity=2, biomes='Cavelake/Ocean', health_range='50', energy_range='10-15', possible_moves='Bright Attack/')

    dinimon_52 = Dinimon(number=52, name='Claymate', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Claymate.png', type1=7, type2=5, line='Claymate', can_evolve=True, rarity=16, biomes='Mesa/Swamp', health_range='50', energy_range='10-15', possible_moves='Earth Attack/')

    dinimon_53 = Dinimon(number=53, name='Claydos', width=80, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Claydos.png', type1=7, type2=5, line='Claymate', can_evolve=True, rarity=7, biomes='Mesa/Swamp', health_range='50', energy_range='10-15', possible_moves='Earth Attack/')

    dinimon_54 = Dinimon(number=54, name='Claymore', width=90, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Claymight.png', type1=7, type2=5, line='Claymate', can_evolve=False, rarity=2, biomes='Mesa/Swamp', health_range='50', energy_range='10-15', possible_moves='Earth Attack/')

    dinimon_55 = Dinimon(number=55, name='Slabma', width=80, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Slabma.png', type1=7, type2=9, line='Slabma', can_evolve=True, rarity=7, biomes='Volcano/Mountain', health_range='50', energy_range='10-15', possible_moves='Burning Attack/')

    dinimon_56 = Dinimon(number=56, name='Slabcanic', width=110, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Slabcanic.png', type1=7, type2=9, line='Slabma', can_evolve=False, rarity=2, biomes='Mountain/Volcano', health_range='50', energy_range='10-15', possible_moves='Burning Attack/')

    dinimon_57 = Dinimon(number=57, name='Kitcool', width=70, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Kitcool.png', type1=2, type2=14, line='Kitcool', can_evolve=True, rarity=12, biomes='Snow/Jungle', health_range='50', energy_range='10-15', possible_moves='Cold Attack/')

    dinimon_58 = Dinimon(number=58, name='Chillion', width=80, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Chillion.png', type1=2, type2=8, line='Kitcool', can_evolve=True, rarity=5, biomes='Snow/Jungle', health_range='50', energy_range='10-15', possible_moves='Cold Attack/')

    dinimon_59 = Dinimon(number=59, name='Vinlion', width=90, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Vinlion.png', type1=2, type2=8, line='Kitcool', can_evolve=False, rarity=1, biomes='Snow/Jungle', health_range='50', energy_range='10-15', possible_moves='Cold Attack/')

    dinimon_60 = Dinimon(number=60, name='Darkhold', width=30, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Darkhold.png', type1=3, type2=10, line='Darkhold', can_evolve=True, rarity=9, biomes='Swamp/Cave', health_range='50', energy_range='10-15', possible_moves='Shadow Attack/')

    dinimon_61 = Dinimon(number=61, name='Darksquire', width=45, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Darksquire.png', type1=3, type2=10, line='Darkhold', can_evolve=True, rarity=1, biomes='Swamp/Cave', health_range='50', energy_range='10-15', possible_moves='Shadow Attack/')

    dinimon_62 = Dinimon(number=62, name='Darksalot', width=75, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Darksalot.png', type1=3, type2=10, line='Darkhold', can_evolve=False, rarity=0, biomes='Swamp/Cave', health_range='50', energy_range='10-15', possible_moves='Shadow Attack/')

    dinimon_63 = Dinimon(number=63, name='Sprout', width=35, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Sprout.png', type1=8, type2=14, line='Sprout', can_evolve=True, rarity=17, biomes='Grasslands', health_range='50', energy_range='10-15', possible_moves='Growth Attack/')

    dinimon_64 = Dinimon(number=64, name='Zapcrop', width=45, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Zapcrop.png', type1=8, type2=6, line='Sprout', can_evolve=True, rarity=7, biomes='Grasslands', health_range='50', energy_range='10-15', possible_moves='Growth Attack/')

    dinimon_65 = Dinimon(number=65, name='Shockobb', width=80, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Shockobb.png', type1=8, type2=6, line='Sprout', can_evolve=False, rarity=2, biomes='Grasslands', health_range='50', energy_range='10-15', possible_moves='Growth Attack/')

    dinimon_66 = Dinimon(number=66, name='Shockle', width=48, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Shockle.png', type1=6, type2=14, line='Shockle', can_evolve=True, rarity=15, biomes='Grasslands', health_range='50', energy_range='10-15', possible_moves='Growth Attack/')

    dinimon_67 = Dinimon(number=67, name='Shox', width=100, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Shox.png', type1=6, type2=14, line='Shockle', can_evolve=False, rarity=2, biomes='Grasslands', health_range='50', energy_range='10-15', possible_moves='Growth Attack/')

    dinimon_68 = Dinimon(number=68, name='Vatbat', width=30, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Vatbat.png', type1=4, type2=13, line='Vatbat', can_evolve=True, rarity=17, biomes='Cave', health_range='50', energy_range='10-15', possible_moves='Toxic Attack/')

    dinimon_69 = Dinimon(number=69, name='Vatpire', width=50, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Vatpire.png', type1=4, type2=13, line='Vatbat', can_evolve=True, rarity=6, biomes='Cave', health_range='50', energy_range='10-15', possible_moves='Toxic Attack/')

    dinimon_70 = Dinimon(number=70, name='Slobbervat', width=80, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Slobbervat.png', type1=4, type2=13, line='Vatbat', can_evolve=False, rarity=2, biomes='Cave', health_range='50', energy_range='10-15', possible_moves='Toxic Attack/')

    dinimon_71 = Dinimon(number=71, name='Radinch', width=35, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Radinch.png', type1=1, type2=14, line='Radinch', can_evolve=True, rarity=17, biomes='Cave', health_range='50', energy_range='10-15', possible_moves='Bright Attack/')

    dinimon_72 = Dinimon(number=72, name='Radiosnake', width=65, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Radiosnake.png', type1=1, type2=13, line='Radinch', can_evolve=True, rarity=7, biomes='Cave', health_range='50', energy_range='10-15', possible_moves='Bright Attack/Toxic Attack/')

    dinimon_73 = Dinimon(number=73, name='Glowbra', width=85, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Glowbra.png', type1=1, type2=13, line='Radinch', can_evolve=True, rarity=3, biomes='Cave', health_range='50', energy_range='10-15', possible_moves='Bright Attack/Toxic Attack/')

    dinimon_74 = Dinimon(number=74, name='Snowlem', width=50, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Snowlem.png', type1=2, type2=10, line='Snowlem', can_evolve=True, rarity=8, biomes='Snow/Peaks', health_range='50', energy_range='10-15', possible_moves='Cold Attack/')

    dinimon_75 = Dinimon(number=75, name='Brrtanium', width=50, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Brrtanium.png', type1=2, type2=10, line='Snowlem', can_evolve=False, rarity=1, biomes='Snow/Peaks', health_range='50', energy_range='10-15', possible_moves='Cold Attack/')

    dinimon_76 = Dinimon(number=76, name='Dirust', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Dirust.png', type1=7, type2=10, line='Dirust', can_evolve=True, rarity=10, biomes='Mountain/Cave/Mesa', health_range='50', energy_range='10-15', possible_moves='Earth Attack/')

    dinimon_77 = Dinimon(number=77, name='Corrodeck', width=70, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Corrodeck.png', type1=7, type2=10, line='Dirust', can_evolve=True, rarity=1, biomes='Mountain/Cave/Mesa', health_range='50', energy_range='10-15', possible_moves='Earth Attack/')

    dinimon_78 = Dinimon(number=78, name='Tetanusaurust', width=150, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Tetanusaurust.png', type1=7, type2=10, line='Dirust', can_evolve=False, rarity=1, biomes='Mountain/Cave/Mesa', health_range='50', energy_range='10-15', possible_moves='Earth Attack/')

    dinimon_79 = Dinimon(number=79, name='Goobanut', width=25, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Goobanut.png', type1=12, type2=14, line='Goobanut', can_evolve=False, rarity=17, biomes='Grasslands', health_range='50', energy_range='10-15', possible_moves='Familiar Attack/')

    dinimon_80 = Dinimon(number=80, name='Dimbot', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Dimbot.png', type1=1, type2=10, line='Dimbot', can_evolve=True, rarity=14, biomes='Peaks', health_range='50', energy_range='10-15', possible_moves='Bright Attack/')

    dinimon_81 = Dinimon(number=81, name='Flashback', width=70, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Flashback.png', type1=1, type2=10, line='Dimbot', can_evolve=True, rarity=0, biomes='Peaks', health_range='50', energy_range='10-15', possible_moves='Bright Attack/')    

    dinimon_82 = Dinimon(number=82, name='Beacontron', width=85, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Beacontron.png', type1=1, type2=10, line='Dimbot', can_evolve=False, rarity=0, biomes='Peaks', health_range='50', energy_range='10-15', possible_moves='Bright Attack/')




    dinimon_0 = Dinimon(number=0, name='', width=40, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/DINIMON.png', type1=0, type2=14, line='', can_evolve=True, rarity=0, biomes='Grasslands', health_range='50', energy_range='10-15', possible_moves='Type Attack/')

    db.session.add(dinimon_1)
    db.session.add(dinimon_2)
    db.session.add(dinimon_3)
    db.session.add(dinimon_4)
    db.session.add(dinimon_5)
    db.session.add(dinimon_6)
    db.session.add(dinimon_7)
    db.session.add(dinimon_8)
    db.session.add(dinimon_9)
    db.session.add(dinimon_10)
    db.session.add(dinimon_11)
    db.session.add(dinimon_12)
    db.session.add(dinimon_13)
    db.session.add(dinimon_14)
    db.session.add(dinimon_15)
    db.session.add(dinimon_16)
    db.session.add(dinimon_17)
    db.session.add(dinimon_18)
    db.session.add(dinimon_19)
    db.session.add(dinimon_20)
    db.session.add(dinimon_21)
    db.session.add(dinimon_22)
    db.session.add(dinimon_23)
    db.session.add(dinimon_24)
    db.session.add(dinimon_25)
    db.session.add(dinimon_26)
    db.session.add(dinimon_27)
    db.session.add(dinimon_28)
    db.session.add(dinimon_29)
    db.session.add(dinimon_30)
    db.session.add(dinimon_31)
    db.session.add(dinimon_32)
    db.session.add(dinimon_33)
    db.session.add(dinimon_34)
    db.session.add(dinimon_35)
    db.session.add(dinimon_36)
    db.session.add(dinimon_37)
    db.session.add(dinimon_38)
    db.session.add(dinimon_39)
    db.session.add(dinimon_40)
    db.session.add(dinimon_41)
    db.session.add(dinimon_42)
    db.session.add(dinimon_43)
    db.session.add(dinimon_44)
    db.session.add(dinimon_45)
    db.session.add(dinimon_46)
    db.session.add(dinimon_47)
    db.session.add(dinimon_48)
    db.session.add(dinimon_49)
    db.session.add(dinimon_50)
    db.session.add(dinimon_51)
    db.session.add(dinimon_52)
    db.session.add(dinimon_53)
    db.session.add(dinimon_54)
    db.session.add(dinimon_55)
    db.session.add(dinimon_56)
    db.session.add(dinimon_57)
    db.session.add(dinimon_58)
    db.session.add(dinimon_59)
    db.session.add(dinimon_60)
    db.session.add(dinimon_61)
    db.session.add(dinimon_62)
    db.session.add(dinimon_63)
    db.session.add(dinimon_64)
    db.session.add(dinimon_65)
    db.session.add(dinimon_66)
    db.session.add(dinimon_67)
    db.session.add(dinimon_68)
    db.session.add(dinimon_69)
    db.session.add(dinimon_70)
    db.session.add(dinimon_71)
    db.session.add(dinimon_72)
    db.session.add(dinimon_73)
    db.session.add(dinimon_74)
    db.session.add(dinimon_75)
    db.session.add(dinimon_76)
    db.session.add(dinimon_77)
    db.session.add(dinimon_78)
    db.session.add(dinimon_79)
    db.session.add(dinimon_80)
    db.session.add(dinimon_81)
    db.session.add(dinimon_82)

def create_captured_dinimon():
    print("Captured_Dinimon")
    Captured_Dinimon.query.delete()

    dinimon1 = Captured_Dinimon(player_id=1, dinimon_id=79, nickname='Goobs', move1=12, move2=8, move3=14, move4=14, energy=15, max_energy=15, health=3, max_health=3, experience=400, max_experience=500, level=4, level_to_evolve=-1, in_party=True, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Goobanut.png')

    dinimon2 = Captured_Dinimon(player_id=1, dinimon_id=78, nickname='Rexy', move1=7, move2=10, move3=11, move4=14, energy=15, max_energy=15, health=15, max_health=20, experience=204, max_experience=600, level=5, level_to_evolve=-1, in_party=True, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Tetanusaurust.png')

    dinimon3 = Captured_Dinimon(player_id=1, dinimon_id=56, nickname='Slabcanic', move1=9, move2=7, move3=1, move4=13, energy=15, max_energy=15, health=60, max_health=60, experience=1000, max_experience=2000, level=19, level_to_evolve=-1, in_party=True, image='https://storage.cloud.google.com/property-runner/Dinimon/Creatures%20/Slabcanic.png')

    db.session.add(dinimon1)
    db.session.add(dinimon2)
    db.session.add(dinimon3)


def create_item():
    print('Item')
    Item.query.delete()

    item1 = Item(name='Springsnap I', buy_value=1, sell_value=1, image='https://storage.cloud.google.com/property-runner/Items/trap1.png')
    item2 = Item(name='Springsnap II', buy_value=2, sell_value=2, image='https://storage.cloud.google.com/property-runner/Items/trap2.png')
    item3 = Item(name='Springsnap III', buy_value=3, sell_value=3, image='https://storage.cloud.google.com/property-runner/Items/trap3.png')
    item4 = Item(name='Springsnap IV', buy_value=4, sell_value=4, image='https://storage.cloud.google.com/property-runner/Items/trap4.png')

    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)


def create_inventory():
    print('Inventory')
    Inventory.query.delete()

    inventory1 = Inventory(player_id=1, item_id=1, quantity=100, name='Springsnap I', buy_value=1, sell_value=1, image='https://storage.cloud.google.com/property-runner/Items/trap1.png')
    inventory2 = Inventory(player_id=1, item_id=2, quantity=10, name='Springsnap II', buy_value=2, sell_value=2, image='https://storage.cloud.google.com/property-runner/Items/trap2.png')
    inventory3 = Inventory(player_id=1, item_id=3, quantity=100, name='Springsnap III', buy_value=3, sell_value=3, image='https://storage.cloud.google.com/property-runner/Items/trap3.png')
    inventory4 = Inventory(player_id=1, item_id=4, quantity=100, name='Springsnap IV', buy_value=4, sell_value=4, image='https://storage.cloud.google.com/property-runner/Items/trap4.png')

    db.session.add(inventory1)
    db.session.add(inventory2)
    db.session.add(inventory3)
    db.session.add(inventory4)




if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)

    db.create_all()

    create_player()
    create_area()
    create_event()
    create_types()
    create_dinimon()
    create_move()
    create_captured_dinimon()
    create_item()
    create_inventory()

    db.session.commit()