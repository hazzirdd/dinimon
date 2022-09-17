from re import T
from server_folder import app, db
from server_folder.model import Area, Captured_Dinimon, Enemy_Dinimon, Event, Dinimon, Move, Item, Inventory, Dinidex, Type

from functions import create_enemy_dinimon, health_check, manage_party, move_sprite, nickname_dinimon, spawn_events, event_check, spawn_dinimon, get_party, setup_dini_moves, get_dini_health, run_attack_on_enemy, run_enemy_attack, get_dini_energy, get_dini_xp, catch_xp, collect_wild_battle_xp, evolution_check
from catching import add_dini_to_player, catch_dinimon

from flask import redirect, render_template, request, url_for, session, flash
from time import sleep


@app.route('/start_session', methods=['POST', 'DELETE', 'GET'])
def start_session():
    players_dinimon = Captured_Dinimon.query.all()
    for tamed_dini in players_dinimon:
        tamed_dini.health = tamed_dini.max_health
        tamed_dini.energy = tamed_dini.max_energy
        tamed_dini.in_party = False
        if tamed_dini.nickname == 'Rexy' or tamed_dini.nickname == 'Goobs' or tamed_dini.nickname == 'Slabcanic':
            tamed_dini.in_party = True
    Dinidex.query.delete()
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

    session["catch_try"] = -1
    session["message"] = 'none'
    session["enemy_turn"] = False
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
        main_dini_energy = get_dini_energy(main_dini)
    else:
        main_dini = 'none'
        main_dini_moves = 'none'
        main_dini_health = 'none'
        main_dini_energy = 'none'

    if 'enemy_dini' in session:
        enemy_dini = Enemy_Dinimon.query.get(session["enemy_dini"])
        enemy_dini_dex = Dinimon.query.get(enemy_dini.dinimon_id)
        enemy_dini_moves = setup_dini_moves(enemy_dini)
        enemy_dini_health = get_dini_health(enemy_dini)
        enemy_dini_energy = get_dini_energy(enemy_dini)

        if session['enemy_turn'] == True:
            move = run_enemy_attack(session["main_dini"], enemy_dini)
            health_status = health_check(main_dini, enemy_dini)
            if health_status == 'main_dini_dead':
                main_dini.in_party = False
                db.session.commit()
                session["battle_end"] = True
                return render_template('end_battle.html', dead_enemy='none', dead_main_dini=main_dini)
            session['message'] += f' {enemy_dini_dex.name} used {move.move}!'
            session['enemy_turn'] = False
            return redirect(url_for('homepage'))
            
    else:
        enemy_dini = 'none'
        enemy_dini_moves = 'none'
        enemy_dini_health = 'none'
        enemy_dini_energy = 'none'
        enemy_dini_dex = 'none'

    if "main_dini" not in session and "wild_battle" not in session:
        print('CHECKING FOR EVOLUTION!!!.........')
        evolving_dini_dex, evolving_dini, new_dini, evolve_status = evolution_check(session["player_id"])
        if evolve_status == True:
            all_dex = Dinidex.query.filter(Dinidex.player_id == session["player_id"])
            dinidex = []
            for dex in all_dex:
                dinidex.append(dex.dinimon_id)

            return render_template('evolve.html', dinimon=evolving_dini, dini_dex=evolving_dini_dex, new_dini=new_dini, dinidex=dinidex)

    return render_template('homepage.html', left=session["left"], top=session["top"],arrow_up_left=session["arrow_up_left"], arrow_up_top=session["arrow_up_top"], area=area, events=events, wild_battle=wild_battle, party=party, main_dini=main_dini, main_dini_moves=main_dini_moves, enemy_dini_moves=enemy_dini_moves, main_dini_health=main_dini_health, enemy_dini_health=enemy_dini_health, main_dini_energy=main_dini_energy, enemy_dini_energy=enemy_dini_energy, enemy_dini_dex=enemy_dini_dex, message=session["message"], enemy_dini=enemy_dini)


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
    return redirect(url_for('homepage'))


@app.route('/attack_enemy', methods=['GET', 'POST'])
def attack_enemy():
    session["message"] = 'none'
    move_id = request.form['move']
    dinimon = Captured_Dinimon.query.get(session["main_dini"])
    move = Move.query.get(move_id)
    enemy_dini = Enemy_Dinimon.query.get(session["enemy_dini"])
    run_attack_on_enemy(move_id, session["enemy_dini"], dinimon)
    health_status = health_check(dinimon, enemy_dini)
    enemy_dini_dex = Dinimon.query.get(enemy_dini.dinimon_id)
    main_dini = Captured_Dinimon.query.get(session["main_dini"])

    if health_status == 'enemy_dini_dead':
        session["message"] = f'{enemy_dini_dex.name} has been murdered!'
        session["battle_end"] = True
        collect_wild_battle_xp(session["player_id"], enemy_dini_dex, main_dini)
        return render_template('end_battle.html', dead_enemy=enemy_dini_dex, dead_main_dini='none')

    session["enemy_turn"] = True
    session['message'] = f'{dinimon.nickname} used {move.move}... and then '

    return redirect(url_for('homepage'))


@app.route('/end_battle', methods=['POST', 'GET'])
def end_battle():
    ####BUG Instead of taking the dini out of party on death, it will be sent to the graveyard in later updates. Create a new endpoint for this /dinimon_dies ####
    session.pop("wild_battle", None)
    session.pop("main_dini", None)
    session.pop("enemy_dini", None)
    session["message"] = 'none'
    session["enemy_turn"] = False
    session["catch_try"] = -1
    Enemy_Dinimon.query.delete()
    db.session.commit()
    return redirect(url_for('homepage'))


@app.route('/resume_battle', methods=['POST', 'GET'])
def resume_battle():
    main_dini = Captured_Dinimon.query.get(session["main_dini"])
    main_dini.in_party = False
    db.session.commit()
    session.pop("main_dini", None)
    session["enemy_turn"] = False
    session["message"] = 'none'
    return redirect(url_for('homepage'))


@app.route('/switch_dinimon', methods=['POST', 'GET'])
def switch_dinimon():

    session["message"] = 'You switched dinimon! '
    session.pop("main_dini", None)
    session["enemy_turn"] = False
    return redirect(url_for('homepage'))


@app.route('/open_inventory', methods=['POST', 'GET'])
def open_inventory():
    inventory_all = Inventory.query.order_by(Inventory.item_id.asc()).all()
    inventory = []
    for item in inventory_all:
        if item not in inventory and item.player_id == session["player_id"]:
            inventory.append(item)
    return render_template('inventory.html', inventory=inventory)


@app.route('/use_item/<item_id>', methods=['POST', 'GET'])
def use_item(item_id):
    item = Inventory.query.get(item_id)
    if 'Springsnap' in item.name:
        print(f'using:: {item.name}')
        print(f'Catch Try: {session["catch_try"]}')
        enemy_dini = Enemy_Dinimon.query.get(session["enemy_dini"])
        enemy_dini_dex = Dinimon.query.get(enemy_dini.dinimon_id)
        width = enemy_dini_dex.width * 4

        if session["catch_try"] == -1:
            session["catch_try"] += 1
            return render_template('catch.html', enemy_dini=enemy_dini_dex, width=width, item=item)

        catch = catch_dinimon(item, enemy_dini_dex)

        if catch == True:
            session["catch_try"] += 1

        if session["catch_try"] == 2:
            catch = catch_dinimon(item, enemy_dini_dex)
            if item.quantity == 1:
                db.session.delete(item)
            else:
                item.quantity -= 1
            db.session.commit()

        if catch == False:
            session["catch_try"] = -1
            session["enemy_turn"] = True
            catch = catch_dinimon(item, enemy_dini_dex)
            if item.quantity == 1:
                db.session.delete(item)
            else:
                item.quantity -= 1
            db.session.commit()
            session["message"] = f"{enemy_dini_dex.name} broke free! "
            return redirect(url_for('homepage'))

        return render_template('catch.html', enemy_dini=enemy_dini_dex, width=width, item=item)

    return redirect(url_for('homepage'))


@app.route('/collect_dinimon', methods=['POST', 'GET'])
def collect_dinimon():
    main_dini = Captured_Dinimon.query.get(session["main_dini"])
    enemy_dini = Enemy_Dinimon.query.get(session["enemy_dini"])
    enemy_dini_dex = Dinimon.query.get(enemy_dini.dinimon_id)
    discovered_dinimon = Dinidex.query.filter(Dinidex.player_id == session["player_id"]).all()
    discovered_ids = []
    is_discovered = True
    for i in discovered_dinimon:
        discovered_ids.append(i.dinimon_id)

    print(discovered_ids)
    for dinimon_id in discovered_ids:
        print(dinimon_id, '==', enemy_dini.dinimon_id)
        if dinimon_id == enemy_dini.dinimon_id:
            is_discovered = False

    print('Discovered:', is_discovered)
    width = enemy_dini_dex.width * 4
    new_dini = add_dini_to_player(enemy_dini, enemy_dini_dex, session["player_id"])
    catch_xp(session["player_id"], enemy_dini_dex, main_dini, is_discovered)
    return render_template('collect.html', dinimon=enemy_dini_dex, width=width, new_dini=new_dini, is_discovered=is_discovered)    


@app.route('/name_new_dinimon', methods=['POST', 'GET'])
def name_new_dinimon():
    captured_dini_id = request.form['new_dini']
    nickname = request.form['nickname']

    try:
        box = request.form['box']
    except:
        box = 'none'

    nickname_dinimon(nickname, captured_dini_id)

    if box == 'none':
        return redirect(url_for('end_battle'))
    else:
        return redirect(url_for('open_box'))


@app.route('/open_dinidex', methods=['POST', 'GET'])
def open_dinidex():
    registered_dinimon = []
    dinidex = {}
    registered_dinimon_ids = Dinidex.query.filter(Dinidex.player_id == session["player_id"]).all()
    all_dinimon = Dinimon.query.all()

    for id in registered_dinimon_ids:
        registered_dinimon.append(id.dinimon_id)

    for dinimon in all_dinimon:
        if dinimon.dinimon_id in registered_dinimon:
            dinidex[dinimon.dinimon_id] = {
                "name": dinimon.name,
                "number": dinimon.number,
                "image": dinimon.image
            }
        else:
            dinidex[dinimon.dinimon_id] = {
                "name": '???',
                "number": dinimon.number,
                "image": dinimon.image
            }

    return render_template('dinidex.html', dinidex=dinidex, all_dinimon=all_dinimon)


@app.route('/open_dinidex/<dinimon_id>', methods=['POST', 'GET'])
def dinidex_detials(dinimon_id):
    dinimon = Dinimon.query.get(dinimon_id)
    type1 = Type.query.get(dinimon.type1)
    type2 = Type.query.get(dinimon.type2)
    return render_template('dex_details.html', dinimon=dinimon, type1=type1, type2=type2, )


@app.route('/open_box', methods=['POST', 'GET'])
def open_box():
    all_party = Captured_Dinimon.query.filter(
        Captured_Dinimon.in_party == True,
        Captured_Dinimon.player_id == session["player_id"]
        )

    party = {}
    for dini in all_party:
        health = get_dini_health(dini)
        energy = get_dini_energy(dini)
        party[dini.captured_dinimon_id] = {
            "image": dini.image,
            "nickname": dini.nickname,
            "health": health,
            "energy": energy
        }

    all_dinimon = Captured_Dinimon.query.filter(
        Captured_Dinimon.in_party == False,
        Captured_Dinimon.player_id == session["player_id"]
        )

    return render_template('box.html', all_dinimon=all_dinimon, party=party, all_party=all_party)


@app.route('/open_box/<captured_dinimon_id>', methods=['POST', 'GET'])
def box_details(captured_dinimon_id):
    dinimon = Captured_Dinimon.query.get(captured_dinimon_id)
    dinimon_dex = Dinimon.query.get(dinimon.dinimon_id)
    type1 = Type.query.get(dinimon_dex.type1)
    type2 = Type.query.get(dinimon_dex.type2)
    move1 = Move.query.get(dinimon.move1)
    move2 = Move.query.get(dinimon.move2)
    move3 = Move.query.get(dinimon.move3)
    move4 = Move.query.get(dinimon.move4)
    health = get_dini_health(dinimon)
    energy = get_dini_energy(dinimon)
    xp = get_dini_xp(dinimon)
    return render_template('box_details.html', dinimon=dinimon, type1=type1, type2=type2, dinimon_dex=dinimon_dex, move1=move1, move2=move2, move3=move3, move4=move4, move1_type=Type.query.get(move1.type_id), move2_type=Type.query.get(move2.type_id), move3_type=Type.query.get(move3.type_id), move4_type=Type.query.get(move4.type_id), health=health, energy=energy, xp=xp)


@app.route('/remove_from_party/<captured_dinimon_id>', methods=['POST', 'GET'])
def remove_from_party(captured_dinimon_id):
    dinimon = Captured_Dinimon.query.get(captured_dinimon_id)
    manage_party(dinimon, 'remove', session['player_id'])
    return redirect(url_for('open_box'))


@app.route('/add_to_party/<captured_dinimon_id>', methods=['POST', 'GET'])
def add_to_party(captured_dinimon_id):
    dinimon = Captured_Dinimon.query.get(captured_dinimon_id)
    manage_party(dinimon, 'add', session['player_id'])
    return redirect(url_for('open_box'))


if __name__ == '__main__':
    app.run(debug=True)