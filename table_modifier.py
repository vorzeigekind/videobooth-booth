#websocket nachrichten werden zur weiterverarbeitung in programmiernodes(operator) in eine touchdesigner tabelle eingetragen und gegebenenfalls aktualisiert oder neu angelegt.

t = op('table1')

def insertVal(key, val):
	global t
	if t.findCell(key):
		t.replaceRow(key, [key, val])
	else:
		t.appendRow([key, val])
