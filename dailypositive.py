#!/home/pi/dailypositive/dailypositive/bin/python3


import os
import random

from webexteamssdk import WebexTeamsAPI


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

QUOTE=random_line("quotes.txt")

GREETING=random_line("greetings.txt")

TEAMSGREETING=GREETING+" the positive quote of the day is: "


api = WebexTeamsAPI()

all_rooms = api.rooms.list()
for room in all_rooms:
	api.messages.create(room.id,text=TEAMSGREETING)
	api.messages.create(room.id,markdown="## "+QUOTE)








