#!/usr/bin/python3
import time

fmt_time = time.strftime('%H:%M:%S')

filename = 'sprink1_output.txt'
fh = open(filename, 'a')

sprinklers = [5,1,2,4,3]
duration = [5,10,10,10,5]

fh.write("TimeStamp :" + fmt_time + "\n")

for x in range(0, 5):
	if x > 0:
	  text = str("Sprinkler " + str(sprinklers[x-1]) + " off\n")
	  fh.write(text)
	text = str("Sprinkler " + str(sprinklers[x]) + " on for " + str(duration[x]) + "secs\n\n")
	fh.write(text)
	time.sleep(duration[x])

fh.write("\n\n")
fh.close()