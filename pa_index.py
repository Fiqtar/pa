import json
import datetime

with open('pa_cfgs.json', 'r') as reader:
	cfgs = reader.read()

def notify(info):
	notify2.init('new notif')
	notif = notify2.Notification('pa', info)
	# notif.set_urgency(notify2.URGENCY_CRITICAL)
	notif.show()
	notif.set_timeout(10)

caps = json.loads(cfgs)['caps']
routines = json.loads(cfgs)['routines']

for routine in routines:
	currentdata = json.loads(readconfigfile())
	currentdata[str(configtoset)] = newvalue
	with open(datacore['jsonfilecap'], 'w') as modifyjfile:
		modifyjfile.write(json.dumps(currentdata, indent = 4))
	
while True:
	brk = '/'
	ctime = datetime.datetime.now()
	times = json.loads(cfgs)['times']
	
	for rtn_time in times:
		index = int(times.index(rtn_time))
		if rtn_time.startswith(brk):
			rtn = rtn_time[len(brk):]
			if ctime.hour == datetime.datetime.strptime(rtn, '%H%M').hour:
				info = routines[index].split(':')[1]
				
		elif brk in rtn_time:
			count, typ = rtn_time.split(brk) 
			info = 'every ' + count + ' ' + typ + '\n' + routines[index].split(':')[1]
			
		else:
			tm = datetime.datetime.strptime(rtn_time, '%d.%m.%y.%H.%M') 
			
			if ctime.year == tm.year and ctime.month == tm.month and ctime.day == tm.day and ctime.hour == tm.hour and ctime.minute == tm.minute:
				info = routines[index].split(':')[0] + '\n' + routines[index].split(':')[1]
				
		notify(info)
