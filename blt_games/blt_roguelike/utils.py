class Vect2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def set_xy(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
    

    def get_xy(self):
        return (self.x, self.y)
    
    def get_x(self):
        return (self.x)
    
    def get_y(self):
        return (self.y)



from bearlibterminal import terminal
class Clamp:

    NOT_WALKABLE = (32, 43, 45, 124)
    WALKABLE = (46, 35)

    def movement_clamp(old_position, entity):
        terminal.layer(0)
        char_under_position = terminal.pick(entity.get_x(), entity.get_y())
        #print(char_under_position, entity.get_xy(), old_position.get_xy())
        if char_under_position not in Clamp.WALKABLE:
            entity.set_position(old_position.get_x(), old_position.get_y())


import time
class NonBlockingDelay:
    """ Non blocking delay class """
    def __init__(self):
        self._timestamp = 0
        self._delay = 0

    def timeout(self):
        """ Check if time is up """
        return ((millis() - self._timestamp) > self._delay)

    def delay_ms(self, delay):
        """ Non blocking delay in ms """
        self._timestamp = millis()
        self._delay = delay

def millis():
    """ Get millis """
    return int(time.time() * 1000)

def delay_ms(delay):
    """ Blocking delay in ms """
    t0 = millis()
    while (millis() - t0) < delay:
        pass