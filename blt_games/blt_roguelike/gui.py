class Roguelike_gui:

    GAME_NAME = "blt_roguelike"

    WINDOW = {
        "width":100, 
        "height":35
        }

    STATS_BAR = {
        "height":WINDOW["height"],
        "width_position":round((WINDOW["width"]/4)*3)
        }

    ACTIONS_BAR = {
        "height_position":round((WINDOW["height"]/5)*4),
        "width":WINDOW["width"]-(WINDOW["width"]-STATS_BAR["width_position"])
        }
    
    TECHNICAL_STATS = {
        "width_position":1,
        "height_position":2
    }

    MAP_ZONE = {
        "width_start_position":TECHNICAL_STATS["width_position"]+3,
        "height_start_position":TECHNICAL_STATS["height_position"]+2,
        "width_end_position":STATS_BAR["width_position"]-3,
        "height_end_position":ACTIONS_BAR["height_position"]-2
    }

    STATS_LOG  = {
        "width_position":STATS_BAR["width_position"] + 2,
        "height_position":TECHNICAL_STATS["height_position"] - 1
    }


from bearlibterminal import terminal
class Dead_menu:
    def print_dead():
        dead_phrase = "YOU DIED"
        terminal.layer(0)
        terminal.print_(2, 1, dead_phrase, 64, 64, align=terminal.TK_ALIGN_CENTER)
        #terminal.printf(terminal.TK_WIDTH / 2)