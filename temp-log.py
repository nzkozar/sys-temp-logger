import psutil
import os
import time, datetime

while True:

	sensors = psutil.sensors_temperatures()

	coretemps = []
	for s in sensors:
		if s=="coretemp":
			for val in sensors[s]:
				name = val[0]
				if "Core" in name:
					temp = val[1]
					high = val[2]
					crit = val[3]
					coretemps.append(temp)
					#print("--->"+name+" "+str(temp)+" "+str(high)+" "+str(crit))

	coretempsText = "Core:"
	for temp in coretemps:
		coretempsText += " "+str(temp)

	f= os.popen('nvidia-smi -q --display=TEMPERATURE')
	gpuInfo = f.readlines()[9:12]

	tempNow = gpuInfo[0]
	tempNow = tempNow.split(':')[1]
	tempNow = tempNow[1:-3]

	tempSlow = gpuInfo[2]
	tempSlow = tempSlow.split(':')[1]
	tempSlow = tempSlow[1:-3]

	tempShutdown = gpuInfo[1]
	tempShutdown = tempShutdown.split(':')[1]
	tempShutdown = tempShutdown[1:-3]

	gpuTemps = "GPU: "+tempNow+" ("+tempSlow+","+tempShutdown+")"

	timeText = str(datetime.datetime.now())

	logText = timeText+" "+coretempsText+" "+gpuTemps
	
	with open('templog','a') as log:
		log.write(logText)

	time.sleep(5)