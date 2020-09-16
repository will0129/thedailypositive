import os
import random
from datetime import datetime
import json
import http.client
import mimetypes


def picka_line(fname,offset):
    #// this was random but too many birthday paradox (requoting quotes) moving to datetimed format

    lines = open(fname).read().splitlines()
    incrementalWrap=datetime.now().timetuple().tm_yday%len(lines)
    offsetWrap=(incrementalWrap + offset)%len(lines)
    # // this takes "date of year" (1-365) and modulos it with the amount of lines
    return lines[offsetWrap]    

def thedailypositive(event):
    try:
        #we take an offset so that when we update quotes we can go back to where we can expect it since the modulo function can change quite a bit based on length of file. we can accept from gcp testing or pass as event. 
        event_json = event.get_json(silent=True)
        offset = int(event_json['offset'])
    except:
        offset=38
    roomId=os.environ['teamsRoomID-prod']
    teamsAPIKey=os.environ['teamsAPIKey']
    QUOTEORIG=picka_line("quotes.txt",offset)
    QUOTE=str(QUOTEORIG)
    GREETING=picka_line("greetings.txt",offset)
    TEAMSGREETING=GREETING+" the positive quote of the day is:"
    message=TEAMSGREETING
    conn = http.client.HTTPSConnection("api.ciscospark.com")
 
    payload = 'roomId='+roomId+'&text='+message


 
 
 
    headers = {'Authorization': 'Bearer '+teamsAPIKey,'Content-Type': 'application/x-www-form-urlencoded'}
    conn.request("POST", "/v1/messages", payload, headers)
    response=conn.getresponse()
    conn = http.client.HTTPSConnection("api.ciscospark.com")

 
    payload = 'roomId='+roomId+'&markdown=## '
    payload=payload.encode('utf-8')+QUOTE.encode('utf-8')
    conn.request("POST", "/v1/messages", payload, headers)




#This is for debug
 
#    return "message is {} quote is {} and roomId is {} and api key is {} ,".format(message,QUOTE, roomId, teamsAPIKey)
 #   return "message is {} and roomId is {} and api key is {}, and response status is {} and headers are {}".format(message, roomId, teamsAPIKey,response.status,headers)
