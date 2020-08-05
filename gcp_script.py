import os
import random
from datetime import datetime
import json
import http.client
import mimetypes


def picka_line(fname):
    #// this was random but too many birthday paradox (requoting quotes) moving to datetimed format
    lines = open(fname).read().splitlines()
    incrementalWrap=datetime.now().timetuple().tm_yday%len(lines)
    # // this takes "date of year" (1-365) and modulos it with the amount of lines
    return lines[incrementalWrap-1]    # // we subtract 1 due to list starts at 0

def thedailypositive(request):
    roomId=os.environ['teamsRoomID']
    teamsAPIKey=os.environ['teamsAPIKey']
    QUOTEORIG=picka_line("quotes.txt")
    QUOTE=str(QUOTEORIG)
    GREETING=picka_line("greetings.txt")
    TEAMSGREETING=GREETING+" the positive quote of the day is:"
    message=TEAMSGREETING
    conn = http.client.HTTPSConnection("api.ciscospark.com")
 
    payload = 'roomId='+roomId+'&text='+message

 #   payload = 'roomId='+roomId+'&text=test from gcp'
    headers = {'Authorization': 'Bearer '+teamsAPIKey,'Content-Type': 'application/x-www-form-urlencoded'}
    conn.request("POST", "/v1/messages", payload, headers)
    response=conn.getresponse()
    conn = http.client.HTTPSConnection("api.ciscospark.com")

 
    payload = 'roomId='+roomId+'&markdown=## '
    payload=payload.encode('utf-8')+QUOTE.encode('utf-8')
    conn.request("POST", "/v1/messages", payload, headers)




#This is for debug
#    return "message is {} and roomId is {} and api key is {}, and response status is {} and headers are {}".format(message, roomId, teamsAPIKey,response.status,headers)
