from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
import pygame
import time

from Panel import Panel
from HorizontalLayout import HorizontalLayout
from VerticalLayout import VerticalLayout
from TextWidget import TextWidget

from Map import Map
from Player import Player
import sys

myMap = Map(100, 100, 21, 21, 7, 7)
myPlayer = Player([50,50])
myMap.center_on_player(myPlayer)
myMap.set_player(myPlayer)

masterLayout = HorizontalLayout(0, 0)
mapPanel = Panel(0, 0, myMap.displayHeight, myMap.displayWidth * 2)
mapPanel.widget = myMap
masterLayout.add_panel(mapPanel)

myText = TextWidget(["Hello", "This is my text widget", "", "Last Line"])
textPanel = Panel(0, 0, myText.height, myText.longestLine)
textPanel.widget = myText
masterLayout.add_panel(textPanel)

def handle_input(_screen):

    ev = _screen.get_event()

    if not isinstance(ev, KeyboardEvent):
        return
    key = ev.key_code
    
    if key in (ord('Q'), ord('q')):
        exit_game()

    movement = None
    if key == ord('k'):
        movement = [0, -1]
    if key == ord("j"):
        movement = [0, 1]
    if key == ord("l"):
        movement = [1, 0]
    if key == ord("h"):
        movement = [-1, 0]
    if not movement is None:
        myPlayer.tryMove(movement, myMap)
        myMap.on_player_movement(myPlayer)

def exit_game():
    sys.exit(0)

def render_map_partial(_screen, m):
    for h in range(displayHeight):
        for w in range(displayWidth):
            col = leftDisplay + w
            row = topDisplay  + h
            tile = m.tiles[col][row]
            tile.display(_screen, 2 * w, h)
            if col < m.width:
                _screen.print_at(' ', 2 * w + 1, h)
#    show_free_area(_screen)
    playerCol = 2 * (myPlayer.pos[0] - leftDisplay)
    playerRow = myPlayer.pos[1] - topDisplay
    myPlayer.display(_screen, playerCol, playerRow)

def show_free_area(_screen):
    for h in range(freeHeight * 2 + 1):
        for w in range(freeWidth * 2 + 1):
            offH = h - freeHeight - 0 + freePos[1] - topDisplay
            offW = w - freeWidth  - 0 + freePos[0] - leftDisplay
            _screen.print_at('f', 2 * offW, offH)

def render_output(_screen, out):
    for i in range(2 * myMap.width):
        _screen.print_at(' ', i, myMap.height)
    _screen.print_at(out, 0, myMap.height)

def update_map(delta, m):
    for row in m.tiles:
        for tile in row:
            tile._update(delta)

def run(_screen):
    pygame.init()
#    clock = pygame.time.Clock()
#    clock.tick()
    dt = 0
    t0 = time.time()
    
    while(True):
#        clock.tick(15)
        t1 = time.time()
        dt = ( t1 - t0 )
        t0 = t1
        handle_input(_screen)
        update_map(dt, myMap)
#        render_map_partial(_screen, myMap)
#        mapPanel.display(_screen)
        masterLayout.display(_screen)
        _screen.refresh()
Screen.wrapper(run)
