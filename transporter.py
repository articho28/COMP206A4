#!/usr/bin/python

import sys
import cgi
import csv

print "Content-type: text/html\r\n\r\n"
form = cgi.FieldStorage()
URL = form["URL"].value
#We store the inventory of the incoming player
inventory = form["inventory"].value

print URL
print inventory
'''#Parse the inventory
list = inventory.split(',')
playerMana = int(list[0])
playerGold = int(list[1])
#print inventory
#Returns True if the room is occupied
def isOccupied():
	file = open('resources.csv', "rb")
	reader = csv.reader(file)
	for row in reader:
		free = row[2]
		if "1" == free:
			return True
		else:
			return False
	file.close()


#Updates the status of the room		
def updateStatePage():
	file = open('resources.csv', "rb")
	reader = csv.reader(file)
	#pageMana = 0
	#pageGold = 0
	#pageStatus = 0
	for row in reader:
		pageMana = row[0]
		pageGold = row[1]
		pageStatus = row[2]
	file.close()

	with open("resources.csv", "w") as resourceFile:
		resourceWriter = csv.writer(resourceFile)
		resourceWriter.writerow([int(pageMana) + 1, int(pageGold), 1])
	resourceFile.close()

#We begin the transport process

#if the room is free, take mana and mark as occupied
#if mana is 0, launch death screen.
if False == isOccupied():
    updateStagePage()
    playerMana = playerMana - 1
    if playerMana <= 0:
        print "Location:http://localhost/deathscreen.html"
        print "Content-type:text/html\r\n\r\n"
    else:
        newInventory = "%s,%s" % (str(playerMana),str(playerGold))
        print "Location:http://www.cs.mcgill.ca/~dvanac/a.cgi?inventory=%s&command=REFRESH" % (newInventory)

else isOccupied():
    print "Location:%s?inventory=%s&command=REFRESH" % (inventory)
    print "Content-type:text/html\r\n\r\n"'''





	
	

