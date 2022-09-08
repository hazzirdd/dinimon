from server_folder import app, db
from functions import move_sprite, spawn_events, event_check
from server_folder.model import Area, Event

from flask import redirect, render_template, request, url_for, session, flash


@app.route('/start_session')
def start_session():
    area = Area.query.get(2)
    session["left"] = 0
    session["top"] = 0
    session["sprite_xy"] = 800

    session["area"] = area.area_id
    session["arrow_up_left"] = 420
    session["arrow_up_top"] = 0

    events = spawn_events(area)

    return render_template('homepage.html', left=session["left"], top=session["top"], arrow_up_left=session["arrow_up_left"], arrow_up_top=session["arrow_up_top"], area=area, events=events)

@app.route('/')
def homepage():

    area = Area.query.get(session["area"])
    events = spawn_events(area)

    return render_template('homepage.html', left=session["left"], top=session["top"],arrow_up_left=session["arrow_up_left"], arrow_up_top=session["arrow_up_top"], area=area, events=events)

@app.route('/move', methods=['POST'])
def move():
    direction = request.form['direction']
    left, top, sprite_xy = move_sprite(direction=direction, left=session["left"], top=session["top"], sprite_xy=session["sprite_xy"])

    session["left"] = left
    session["top"] = top
    session["sprite_xy"] = sprite_xy

    event = event_check(session["area"], session["sprite_xy"])
    print(event)
    if event[0] == 'bottom_exit':
        print(event[1])
        session["area"] = event[1]
        session["left"] = 420
        session["top"] = 70
        session["sprite_xy"] = 706
    elif event[0] == 'top_exit':
        print(event[1])
        session["area"] = event[1]
        session["left"] = 420
        session["top"] = 420
        session["sprite_xy"] = 206
    elif event[0] == 'right_exit':
        print(event[1])
        session["area"] = event[1]
        session["left"] = 70
        session["top"] = 210
        session["sprite_xy"] = 501
    elif event[0] == 'left_exit':
        print(event[1])
        session["area"] = event[1]
        session["left"] = 770
        session["top"] = 210
        session["sprite_xy"] = 511
    else:
        pass




    # if exit == True:
    #     session["area"] = 'https://i.ytimg.com/vi/9TlmBmMonIc/maxresdefault.jpg'

    #     left, top, arrow_up_left, arrow_up_top = area_check(area=session["area"])
    #     session["left"] = left
    #     session["top"] = top
    #     session["arrow_up_left"] = arrow_up_left
    #     session["arrow_up_top"] = arrow_up_top

    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True)