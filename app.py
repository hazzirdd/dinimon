from server_folder import app, db
from server_folder.model import Area, Captured_Dinimon, Enemy_Dinimon, Event, Dinimon, Move
from functions import create_enemy_dinimon, move_sprite, spawn_events, event_check, spawn_dinimon, get_party, setup_dini_moves, get_dini_health, run_attack_on_enemy

from flask import redirect, render_template, request, url_for, session, flash


@app.route('/start_session', methods=['POST', 'DELETE', 'GET'])
def start_session():
    Enemy_Dinimon.query.delete()
    dinimon = Event.query.filter(Event.event == 'dinimon').all()
    for dini in dinimon:
        db.session.delete(dini)
    db.session.commit()

    area = Area.query.get(1)
    session["player_id"] = 1
    session["left"] = 420
    session["top"] = 70
    session["sprite_xy"] = 706

    session["area"] = area.area_id
    session["arrow_up_left"] = 420
    session["arrow_up_top"] = 0
    session.pop("wild_battle", None)
    session.pop("main_dini", None)
    session.pop("enemy_dini", None)

    spawn_dinimon(area)

    return redirect(url_for('homepage'))



@app.route('/')
def homepage():

    area = Area.query.get(session["area"])
    events = spawn_events(area)
    party = get_party(session["player_id"])

    if 'wild_battle' in session:
        dinimon = Dinimon.query.get(session["wild_battle"])
        wild_battle = dinimon
    else:
        wild_battle = 'none'

    if 'main_dini' in session:
        main_dini = Captured_Dinimon.query.get(session["main_dini"])
        print('MAIN DINI:', main_dini.nickname)
        main_dini_moves = setup_dini_moves(main_dini)
        main_dini_health = get_dini_health(main_dini)
    else:
        main_dini = 'none'
        main_dini_moves = 'none'
        main_dini_health = 'none'

    if 'enemy_dini' in session:
        enemy_dini = Enemy_Dinimon.query.get(session["enemy_dini"])
        enemy_dini_moves = setup_dini_moves(enemy_dini)
        enemy_dini_health = get_dini_health(enemy_dini)
    else:
        enemy_dini = 'none'
        enemy_dini_moves = 'none'
        enemy_dini_health = 'none'


    return render_template('homepage.html', left=session["left"], top=session["top"],arrow_up_left=session["arrow_up_left"], arrow_up_top=session["arrow_up_top"], area=area, events=events, wild_battle=wild_battle, party=party, main_dini=main_dini, main_dini_moves=main_dini_moves, enemy_dini_moves=enemy_dini_moves, main_dini_health=main_dini_health, enemy_dini_health=enemy_dini_health)



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
    elif event[0] == 'wild_battle':
        session["wild_battle"] =  event[1].dinimon_id
        print('Battle with:::', event[1].name)
        enemy = create_enemy_dinimon(event[1].dinimon_id)
        session["enemy_dini"] = enemy
    else:
        pass

    return redirect(url_for('homepage'))



@app.route('/choose_main_dini', methods=['GET', 'POST'])
def choose_main_dini():
    
    dinimon_id = request.form['dinimon']
    session["main_dini"] = dinimon_id
    print("DINI ID:",dinimon_id)

    return redirect(url_for('homepage'))


@app.route('/attack_enemy', methods=['GET', 'POST'])
def attack_enemy():
    move_id = request.form['move']
    run_attack_on_enemy(move_id, session["enemy_dini"])

    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True)