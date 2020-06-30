#!/home/pi/dailypositive/dailypositive/bin/python3


import os
import random
from datetime import datetime

from webexteamssdk import WebexTeamsAPI


def picka_line(fname):
    #// this was random but too many birthday paradox (requoting quotes) moving to datetimed format

    lines = open(fname).read().splitlines()
    incrementalWrap=datetime.now().timetuple().tm_yday%len(lines)
    # // this takes "date of year" (1-365) and modulos it with the amount of lines

    return lines[incrementalWrap-1]    # // we subtract 1 due to list starts at 0

QUOTE=picka_line("quotes.txt")

GREETING=picka_line("greetings.txt")

TEAMSGREETING=GREETING+" the positive quote of the day is: "


api = WebexTeamsAPI()

all_rooms = api.rooms.list()
for room in all_rooms:
	api.messages.create(room.id,text=TEAMSGREETING)
	api.messages.create(room.id,markdown="## "+QUOTE)








