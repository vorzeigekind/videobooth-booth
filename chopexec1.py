# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

import json
import TDJSON

ws = op('websocket1')


def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):   #bei einem valuechange des mit dem skript verknüpften channel operators wird der entsprechende skript ausgeführt: hier bei verifieduser valuechange
	global ws
	jsonvalue = TDJSON.datToJSON(op('New_ID_QR_txt'), orderedDict=True, showErrors=False)  #aus dem operator new_id_qr_txt wird die neu erzeugte id ausgelesen und in json format verpackt
	ourData = {'wsIDTD': jsonvalue}
	#ws.sendText(jsonvalue)
	ws.sendText(json.dumps(ourData))  #websocket senden der neuen id im json format
	return
	
