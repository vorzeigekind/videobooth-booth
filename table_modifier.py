t = op('table1')

def insertVal(key, val):
	global t
	if t.findCell(key):
		t.replaceRow(key, [key, val])
	else:
		t.appendRow([key, val])
