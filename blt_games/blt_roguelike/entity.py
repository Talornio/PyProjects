from utils import Vect2, NonBlockingDelay, millis, delay_ms
from bearlibterminal import terminal
import math
import random

class Entity:

    TIMER = NonBlockingDelay()

    def __init__(self, position, char, name, hp, atk, base_atk_spd, base_atk_range, trigger_area, inventory, equipped_items):
        self.position = position
        self.char = char # '[color=red]@[/color]'
        self.name = name
        self.hp = hp # 100
        self.atk = atk # 10
        self.base_atk_spd = base_atk_spd
        self.base_atk_range = base_atk_range
        self.trigger_area = trigger_area
        self.inventory = inventory # {"slot1":None, "slot2":None, "slot3":None, "slot4":None}
        self.equipped_items = equipped_items # {"weapon":"stick", "armor":None}
        self.c_atk = False
        self.i_atk  = False
        self.max_hp = hp

    def get_max_hp(self):
        return self.max_hp
    
    def get_atk_range(self):
        return self.base_atk_range

    def get_hp(self):
        return self.hp

    def get_atk_spd(self):
        return self.base_atk_spd

    def get_dmg(self):
        self.i_atk = False
        return self.atk

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
        return self.hp

    def can_attack(self, bool):
        self.c_atk = bool
    
    def get_b_atk(self):
        return self.c_atk
    
    def get_i_atk(self):
        return self.i_atk
    
    def is_attacking(self, bool):
        self.i_atk = bool

    def distance_from(self, entity):
        return math.sqrt(math.pow(entity.get_x() - self.get_x(), 2) + math.pow(entity.get_y() - self.get_y(), 2))
    
    def is_in_range(self, entity, distance):
        if self.distance_from(entity) < distance:
            return True
        return False

    def move_up(self):
        self.position.set_y(self.position.get_y() - 1)

    def move_down(self):
        self.position.set_y(self.position.get_y() + 1)
    
    def move_left(self):
        self.position.set_x(self.position.get_x() - 1)

    def move_right(self):
        self.position.set_x(self.position.get_x() + 1)

    def set_position(self, x, y):
        self.position.set_xy(x, y)
    
    def get_position(self):
        return self.position
    
    def get_xy(self):
        return (self.position.get_x(), self.position.get_y())
    
    def get_x(self):
        return self.position.get_x()
    
    def get_y(self):
        return self.position.get_y()

    def get_char(self):
        return self.char

    def get_code(self):
        return terminal.pick(self.get_x(), self.get_y())

class Enemy(Entity):

    PLAYER_LIST = [64]

    def __init__(self, position, char, name, hp, atk, base_atk_spd, base_atk_range, trigger_area, inventory, equipped_items, movement_spd):
        super().__init__(position, char, name, hp, atk, base_atk_spd, base_atk_range, trigger_area, inventory, equipped_items)
        self.movement_spd = movement_spd
    
    def get_movement_spd(self):
        return self.movement_spd

    def scan_area(self, diameter):
        terminal.layer(1)
        current_x = self.get_x()
        current_y = self.get_y()
        for nx in range(diameter):
            for ny in range(diameter):
                check_x = math.ceil(nx + current_x - diameter / 2)
                check_y = math.ceil(ny + current_y - diameter / 2)
                #terminal.printf(check_x, check_y, '[color=yellow]%[/color]')
                #print(check_x, check_y, terminal.pick(check_x, check_y))
                if terminal.pick(check_x, check_y) in Enemy.PLAYER_LIST:
                    #print("Player detected")
                    return check_x, check_y
    
    def move(self):
        n = random.randint(0, 3)
        if n == 0:
            self.move_up()
        elif n == 1:
            self.move_down()
        elif n == 2:
            self.move_left()
        elif n == 3:
            self.move_right()
        

class Player(Entity):

    ENEMY_LIST = [103]

    def scan_area(self, diameter, list):
        terminal.layer(0)
        current_x = self.get_x()
        current_y = self.get_y()
        for nx in range(diameter):
            for ny in range(diameter):
                check_x = math.ceil(nx + current_x - diameter / 2)
                check_y = math.ceil(ny + current_y - diameter / 2)
                #terminal.printf(check_x, check_y, '[color=yellow]%[/color]')
                #print(check_x, check_y, terminal.pick(check_x, check_y))
                if terminal.pick(check_x, check_y) in list:
                    #print("Enemy detected")
                    return check_x, check_y