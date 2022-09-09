from turtle import right
from model import connect_to_db, db, Area, Event

grasslands = 'https://media.istockphoto.com/vectors/lawn-grass-seamless-in-summervector-cartoon-nature-green-field-and-vector-id1365764072?b=1&k=20&m=1365764072&s=170667a&w=0&h=xqKHGZ4jdziOdjluNvopBAlAMZgfZVhwz2npDsMdjlY='

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
    area3 = Area(biome='Grasslands', coordinates='3/1', image=grasslands)
    area4 = Area(biome='Grasslands', coordinates='4/1', image=grasslands)
    area5 = Area(biome='Grasslands', coordinates='2/0', image=grasslands)
    area6 = Area(biome='Grasslands', coordinates='3/0', image=grasslands)
    area7 = Area(biome='Grasslands', coordinates='4/0', image=grasslands)
    area8 = Area(biome='Jungle', coordinates='3/-1', image=jungle)
    area9 = Area(biome='Grasslands', coordinates='2/2', image="https://i.pinimg.com/originals/22/c1/89/22c18905c82e907b1548c7d89194e3a0.jpg")

    db.session.add(area1)
    db.session.add(area2)
    db.session.add(area3)
    db.session.add(area4)
    db.session.add(area5)
    db.session.add(area6)
    db.session.add(area7)
    db.session.add(area8)
    db.session.add(area9)

def create_event():
    print('Events')

    event1 = Event(event='top_exit', area_id=1, left_coord=346, top_coord=0, xy=806, image=top_exit)

    event2 = Event(event='top_exit', area_id=2, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event3 = Event(event='left_exit', area_id=2, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event4 = Event(event='right_exit', area_id=2, left_coord=618, top_coord=210, xy=512, image=right_exit)
    event5 = Event(event='bottom_exit', area_id=2, left_coord=124, top_coord=490, xy=106, image=bottom_exit)

    event6 = Event(event='top_exit', area_id=9, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event7 = Event(event='left_exit', area_id=9, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event8 = Event(event='right_exit', area_id=9, left_coord=618, top_coord=210, xy=512, image=right_exit)
    event9 = Event(event='bottom_exit', area_id=9, left_coord=124, top_coord=490, xy=106, image=bottom_exit)

    db.session.add(event1)
    db.session.add(event2)
    db.session.add(event3)
    db.session.add(event4)
    db.session.add(event5)
    db.session.add(event6)
    db.session.add(event7)
    db.session.add(event8)
    db.session.add(event9)


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)

    db.create_all()

    create_area()
    create_event()

    db.session.commit()