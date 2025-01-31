from bearlibterminal import terminal
from pygame import time
from gui import Roguelike_gui, Dead_menu
from map import Map
from utils import Vect2, Clamp, NonBlockingDelay, millis, delay_ms
from entity import Entity, Player

clock = time.Clock()
is_running = True
#hero_timer = NonBlockingDelay()

lvl1 = None
mouse_position = Vect2(0, 0)
player_old_position = Vect2(None, None)

hero = None

FPS = 30

# char codes list:
# 32 = ' '
# 35 = '#'
# 43 = '+'
# 45 = '-'
# 46 = '.'
# 64 = '@'
# 124 = '|'
# 103 = 'g + ^'



def game_init():
    global hero
    global player_old_position
    global lvl1

    terminal.open()
    terminal.setf("window: title='%s'" % (Roguelike_gui.GAME_NAME))
    terminal.setf("window: size=%ix%i" % (Roguelike_gui.WINDOW["width"], Roguelike_gui.WINDOW["height"]))
    #terminal.set("terminal.encoding=utf8;")
    #terminal.set("0xE000: upheavtt.ttf, size=16;")
    terminal.set(
        "input:"
        "cursor-blink-rate = 800,"
        "precise-mouse = false,"
        "mouse-cursor = false,"
        "filter=[keyboard, mouse];"
        )

    lvl1 = Map()

    hero = Player(Vect2(Roguelike_gui.MAP_ZONE["width_start_position"]+2, Roguelike_gui.MAP_ZONE["height_start_position"]+2), '[color=red]@[/color]', "Player", 100, 10, 800, 3, 3, {"slot1":None, "slot2":None, "slot3":None, "slot4":None}, {"weapon":"stick", "armor":None})
    player_old_position = Vect2(hero.get_x(), hero.get_y())
    terminal.refresh()

def game_loop():
    while is_running:
        if hero.get_hp() <= 0:
            Dead_menu.print_dead()
        else:
            #print hero
            terminal.layer(1)
            terminal.printf(hero.get_x(), hero.get_y(), hero.get_char())
            #print tecnical stats
            terminal.layer(0)
            terminal.printf(Roguelike_gui.TECHNICAL_STATS["height_position"], Roguelike_gui.TECHNICAL_STATS["width_position"], f"FPS: {round(clock.get_fps(), 1)} \t MOUSE X: {mouse_position.get_x()} MOUSE Y: {mouse_position.get_y()}")
            terminal.printf(Roguelike_gui.MAP_ZONE["width_start_position"], Roguelike_gui.MAP_ZONE["height_start_position"], lvl1.get_terrain())
            for mob in lvl1.get_mobs():
                #print mob or remove
                if mob.get_hp() <= 0:
                    lvl1.get_mobs().remove(mob)
                    continue
                terminal.printf(mob.get_x(), mob.get_y(), mob.get_char())
                #move mobs or attack player
                if mob.scan_area(mob.get_atk_range()) != hero.get_xy():
                    #print(mob.scan_area(mob.get_atk_range()))
                    if mob.TIMER.timeout():
                        mob_old_position = Vect2(mob.get_x(), mob.get_y())
                        mob.move()
                        Clamp.movement_clamp(mob_old_position, mob)
                        mob.TIMER.delay_ms(mob.get_movement_spd())
                else:
                    if mob.TIMER.timeout():
                        hero.take_dmg(mob.get_dmg())
                        mob.TIMER.delay_ms(mob.get_atk_spd())
                #scan for attacking mobs
                if hero.scan_area(hero.get_atk_range(), hero.ENEMY_LIST) == mob.get_xy():
                    #print("interazione con il mob")
                    hero.can_attack(True)
                    if hero.get_i_atk() and hero.TIMER.timeout():
                        print(mob.take_dmg(hero.get_dmg()))
                        hero.TIMER.delay_ms(hero.get_atk_spd())
                else: hero.can_attack(False)
            #print gui bars
            terminal.layer(2)
            for position in range(0, Roguelike_gui.STATS_BAR["height"]):
                terminal.printf(Roguelike_gui.STATS_BAR["width_position"], position, '|')
            for position in range(0, Roguelike_gui.ACTIONS_BAR["width"]):
                terminal.printf(position, Roguelike_gui.ACTIONS_BAR["height_position"], '-')
            if hero.get_hp() > hero.get_max_hp() * 0.65:
                color = "green"
            elif hero.get_hp() <= hero.get_max_hp() * 0.25:
                color = "red"
            else:
                color = "yellow"
            terminal.printf(Roguelike_gui.STATS_LOG["width_position"], Roguelike_gui.STATS_LOG["height_position"], "hp: [color=%s]%i[/color]" % (color, hero.get_hp()))
            terminal.printf(Roguelike_gui.STATS_LOG["width_position"], Roguelike_gui.STATS_LOG["height_position"] + 1, "atk: [color=green]%i[/color]" % (hero.get_dmg()))


        #print cursor
        terminal.layer(3)
        #terminal.put_ext(mouse_x, mouse_y, 0, 0, '•⊡∴', [0xFF00FF00, 0xFF00FF00, 0xFF00FF00, 0xFF00FF00])
        terminal.printf(mouse_position.get_x(), mouse_position.get_y(), "[color=green][[•]][/color]")

        #input key detecting
        input_manager()

        #setting fps
        terminal.refresh()
        terminal.clear()
        clock.tick(FPS)
    terminal.close()

def input_manager():
    global is_running
    global mouse_position
    global player_old_position
    global hero

    while terminal.has_input():
        key = terminal.read()
        player_old_position = Vect2(hero.get_x(), hero.get_y())
        if key == terminal.TK_CLOSE or key == terminal.TK_ESCAPE:
            is_running = False
        if key == terminal.TK_MOUSE_MOVE:
            mouse_position.set_xy(terminal.state(terminal.TK_MOUSE_X), terminal.state(terminal.TK_MOUSE_Y))
        if key == terminal.TK_W:
            hero.move_up()
            Clamp.movement_clamp(player_old_position, hero)
        if key == terminal.TK_S:
            hero.move_down()
            Clamp.movement_clamp(player_old_position, hero)
        if key == terminal.TK_A:
            hero.move_left()
            Clamp.movement_clamp(player_old_position, hero)
        if key == terminal.TK_D:
            hero.move_right()
            Clamp.movement_clamp(player_old_position, hero)
        if key == terminal.TK_SPACE and hero.get_b_atk():
            hero.is_attacking(True)
    
game_init()
game_loop()