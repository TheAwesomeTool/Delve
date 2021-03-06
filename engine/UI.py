from gfx import *
import debug
import sys
import traceback
import world
import Player

_logWindowWidth = 25
_logWindowHeight = 4
_logWindowXPos = 0
_logWindowYPos = 26

_infoWindowWidth = 15
_infoWindowHeight = 30
_infoWindowXPos = 26
_infoWindowYPos = 0


class UI:

    def __init__(self):
        self.world = world.World(200, 200)
        self.log = Ventana(
            _logWindowWidth, _logWindowHeight,
            _logWindowXPos, _logWindowYPos)
        self.info = Ventana(
            _infoWindowWidth, _infoWindowHeight,
            _infoWindowXPos, _infoWindowYPos)

    def movement(self, ginput):
        px = Player.getPlayPos()[0]
        py = Player.getPlayPos()[1]
        if ginput == 'left' and (self.world.grid[px - 1][py] != '#' or debug.debug):
            Player.getPlayPos()[0] -= 1
        elif ginput == 'right' and (self.world.grid[px + 1][py] != '#' or debug.debug):
            Player.getPlayPos()[0] += 1
        elif ginput == 'up' and (self.world.grid[px][py - 1] != '#' or debug.debug):
            Player.getPlayPos()[1] -= 1
        elif ginput == 'down' and (self.world.grid[px][py + 1] != '#' or debug.debug):
            Player.getPlayPos()[1] += 1


if __name__ == '__main__':
    try:
        Player.initPlayer('dummy')
        debug.debug = True
        start()
        ui = UI()
        while 1:
            ui.world.drawMap()

            # LOG
            log = ['%' * _logWindowWidth] * _logWindowHeight
            for i in range(len(log[0])):
                for j in range(len(log)):
                    draw(i, j, '%', ui.log, 5)
            # INFO
            info = ['$' * _infoWindowWidth] * _infoWindowHeight
            for i in range(len(info[0])):
                for j in range(len(info)):
                    draw(i, j, '$', ui.info, 5)
            ui.log.refresh()
            ui.info.refresh()

            # INPUT
            q = get_input()
            if q == 'q':
                break
            elif q == 'enter':
                debug.debug = not debug.debug
            ui.movement(q)
        stop()
    except:
        stop()
        print(traceback.format_exc())
        sys.exit(-1)
sys.exit(0)
