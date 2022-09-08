from model import connect_to_db, db, Area, Event

grasslands = 'https://media.istockphoto.com/vectors/lawn-grass-seamless-in-summervector-cartoon-nature-green-field-and-vector-id1365764072?b=1&k=20&m=1365764072&s=170667a&w=0&h=xqKHGZ4jdziOdjluNvopBAlAMZgfZVhwz2npDsMdjlY='

jungle = 'http://www.clker.com/cliparts/a/r/C/L/q/z/green-box-hi.png'

top_exit = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM3IDFgsGTTuet2AJnOrOVT0r0DStfyMSEV5wFeJb-qrMfsBH0ElY4B-V1TjJRyvUL_Eg&usqp=CAU"
left_exit = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM3IDFgsGTTuet2AJnOrOVT0r0DStfyMSEV5wFeJb-qrMfsBH0ElY4B-V1TjJRyvUL_Eg&usqp=CAU"
right_exit = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM3IDFgsGTTuet2AJnOrOVT0r0DStfyMSEV5wFeJb-qrMfsBH0ElY4B-V1TjJRyvUL_Eg&usqp=CAU"
bottom_exit = "https://www.freeiconspng.com/thumbs/up-arrow-png/black-up-arrow-png-6.png"



def create_area():
    print('Areas')
    Area.query.delete()

    area1 = Area(biome='Grasslands', coordinates='1/1', image=grasslands)
    area2 = Area(biome='Grasslands', coordinates='2/1', image=grasslands)
    area3 = Area(biome='Grasslands', coordinates='3/1', image=grasslands)
    area4 = Area(biome='Grasslands', coordinates='4/1', image=grasslands)
    area5 = Area(biome='Grasslands', coordinates='2/0', image=grasslands)
    area6 = Area(biome='Grasslands', coordinates='3/0', image=grasslands)
    area7 = Area(biome='Grasslands', coordinates='4/0', image=grasslands)
    area8 = Area(biome='Jungle', coordinates='3/-1', image=jungle)

    db.session.add(area1)
    db.session.add(area2)
    db.session.add(area3)
    db.session.add(area4)
    db.session.add(area5)
    db.session.add(area6)
    db.session.add(area7)
    db.session.add(area8)

def create_event():
    print('Events')

    event1 = Event(event='top_exit', area_id=1, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event2 = Event(event='top_exit', area_id=2, left_coord=346, top_coord=0, xy=806, image=top_exit)
    event3 = Event(event='left_exit', area_id=2, left_coord=-148, top_coord=210, xy=500, image=left_exit)
    event4 = Event(event='right_exit', area_id=2, left_coord=618, top_coord=210, xy=512, image=right_exit)
    event5 = Event(event='bottom_exit', area_id=2, left_coord=124, top_coord=490, xy=106, image=bottom_exit)

    db.session.add(event1)
    db.session.add(event2)
    db.session.add(event3)
    db.session.add(event4)
    db.session.add(event5)

# def create_area_event():
#     print('Area_Events')
    
#     area_event1 = Area_Event(area_id=1, event_id=1)
#     area_event2 = Area_Event(area_id=2, event_id=2)
#     area_event3 = Area_Event(area_id=2, event_id=3)
#     area_event4 = Area_Event(area_id=2, event_id=4)

#     db.session.add(area_event1)
#     db.session.add(area_event2)
#     db.session.add(area_event3)
#     db.session.add(area_event4)


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)

    db.create_all()

    create_area()
    create_event()
    # create_area_event()

    db.session.commit()