#!/usr/bin/python

import cgi
import csv
from random import randint

def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


print "Content-type:text/html\r\n\r\n"
form = cgi.FieldStorage()
tries = form["tries"].value
inventory = form["inventory"].value



if tries == "4":

	introduction = """ <html>
		<head>
			<title>Dan's and Arty's Room</title>
			
			<style type="text/css">
				body {background-color: #CCCCCC}
				#center {position: relative; top: 20px;}
			</style>
		</head>
		
		<body>
			
		<!-- This is the image -->	
		<center><img src="http://www.brandonhall.com/blogs/wp-content/uploads/2013/09/classroom-1.jpg" width="666" height="500"></center>		
		
		<!-- This is the header -->
		<hr/>
			<center>
			<h1 title="This is the best room.">This is the math room.</h1>
			<h2> You have entered the game mode. Remember that you can type "QUIT" 
			to return to the main menu at any moment.
			The game is simple: you will have to enter the <i> ith</i> Fibonacci number. 
			When prompted, enter your guess in the textbox area. If you guess the correct 
			number three times, you win the game. Make a mistake, and its back
			to the books again.
			Get ready! 
			 </h2>
		<hr/> """
	print introduction

	box = """<form action="/cgi-bin/game.py" method="get" style="display: inline;">
			<input type="submit" value="submit">
			<input type="hidden" name="inventory" value="%s">
			<input type="hidden" name="tries" value="3">
		</form>""" % (inventory)
	print box

	

elif tries == "3":
	term = randint(1,12)
	game_start = """ <html>
		<head>
			<title>Dan's and Arty's Room</title>
			
			<style type="text/css">
				body {background-color: #CCCCCC}
				#center {position: relative; top: 20px;}
			</style>
		</head>
		
		<body>
			
		<!-- This is the image -->	
		<center><img src="http://www.brandonhall.com/blogs/wp-content/uploads/2013/09/classroom-1.jpg" width="666" height="500"></center>		
		
		<!-- This is the header -->
		<hr/>
			<center>
			<h1 title="This is the best room.">This is the math room.</h1>
			<h2> Enter the term number %d of the Fibonnaci sequence.
			 </h2>
		<hr/> """ % (term)
	print game_start
	
	box = """<form action="/cgi-bin/game.py" method="get" style="display: inline;">
			<input type="text" name="input">
			<input type="hidden" name="inventory" value="%s">
			<input type="hidden" name="tries" value="2">
			<input type="hidden" name="term" value="%d">
			<input type="submit" value="submit">

		</form>""" % (inventory, term)
	print box
elif tries == "2":
	#Print the head of head of the document.
	first_round_completed = """ <html>
		<head>
			<title>Dan's and Arty's Room</title>
			
			<style type="text/css">
				body {background-color: #CCCCCC}
				#center {position: relative; top: 20px;}
			</style>
		</head>
		
		<body>
			
		<!-- This is the image -->	
		<center><img src="http://www.brandonhall.com/blogs/wp-content/uploads/2013/09/classroom-1.jpg" width="666" height="500"></center>		
		
		<!-- This is the header -->
		<hr/>
			<center>
			<h1 title="This is the best room.">This is the math room.</h1>
			<h2> 
			 </h2>
		<hr/> """ 
	print first_round_completed

	#Interpret the input
	previous_term = form["term"].value
	given_answer = form["input"].value
	real_answer = fib(int(previous_term))

	if given_answer == "QUIT":
		print "<h1> Sorry to see you go. Come back soon! </h1>"

		box = """<form action="/cgi-bin/game.py" method="get" style="display: inline;">
				<input type="hidden" name="command" value="REFRESH">
				<input type="hidden" name="inventory" value="%s">
				<input type="submit" value="Return to Main Menu">

			</form>""" % (inventory)
		print box
	
	elif int(given_answer) == int(real_answer):
		print "<h2> Good job, you guessed right! Guess correctly twice more and you win! </h2>"
		second_term = randint(1,12)
		print "<h2> Guess the number %d of the Fibonnaci Sequence" % (second_term)

	
		box = """<form action="/cgi-bin/game.py" method="get" style="display: inline;">
				<input type="text" name="input">
				<input type="hidden" name="inventory" value="%s">
				<input type="hidden" name="tries" value="1">
				<input type="hidden" name="term" value="%d">
				<input type="submit" value="submit">

			</form>""" % (inventory, second_term)
		print box

	else:
		print "<h2> Sorry, you guessed wrong :( Click on submit to return to the main menu.</h2>"
		return_box = """<form action="/cgi-bin/a.out.cgi" method="get" style="display: inline;">
			<input type="hidden" name="inventory" value="5,0">
			<input type="hidden" name="command" value="refresh">
			<input type="submit" value="submit">
		</form>""" 
		print return_box

elif tries == "1":
	last_round =""" <html>
		<head>
			<title>Dan's and Arty's Room</title>
			
			<style type="text/css">
				body {background-color: #CCCCCC}
				#center {position: relative; top: 20px;}
			</style>
		</head>
		
		<body>
			
		<!-- This is the image -->	
		<center><img src="http://www.brandonhall.com/blogs/wp-content/uploads/2013/09/classroom-1.jpg" width="666" height="500"></center>		
		
		<!-- This is the header -->
		<hr/>
			<center>
			<h1 title="This is the best room.">This is the math room.</h1>
			<h2> 
			 </h2>
		<hr/> """ 
	print last_round
	before_last_term = form["term"].value
	second_given_answer = form["input"].value
	second_real_answer = fib(int(before_last_term))

	if second_given_answer == "QUIT":
		print "<h1> Sorry to see you go. Come back soon! </h1>"

		box = """<form action="/cgi-bin/game.py" method="get" style="display: inline;">
				<input type="hidden" name="command" value="REFRESH">
				<input type="hidden" name="inventory" value="%s">
				<input type="submit" value="Return to Main Menu">

			</form>""" % (inventory)
		print box

	elif int(second_given_answer) == int(second_real_answer):

		print "<h2> Good job, you guessed right! Guess correctly once more and you win! </h2>"
		third_term = randint(7,12)
		print "<h2> Guess the number %d of the Fibonnaci Sequence" % (third_term)
		box = """<form action="/cgi-bin/game.py" method="get" style="display: inline;">
				<input type="text" name="input">
				<input type="hidden" name="inventory" value="%s">
				<input type="hidden" name="tries" value="0">
				<input type="hidden" name="term" value="%d">
				<input type="submit" value="submit">

			</form>""" % (inventory, third_term)
		print box
	else:
		print "<h2> Sorry, you guessed wrong :( Click on submit to return to the main menu.</h2>"
		return_box = """<form action="/cgi-bin/a.out.cgi" method="get" style="display: inline;">
			<input type="hidden" name="inventory" value="5,0">
			<input type="hidden" name="command" value="refresh">
			<input type="submit" value="submit">
		</form>""" 
		print return_box
elif tries == "0":
	win_screen = """ <html>
		<head>
			<title>Dan's and Arty's Room</title>
			
			<style type="text/css">
				body {background-color: #CCCCCC}
				#center {position: relative; top: 20px;}
			</style>
		</head>
		
		<body>
			
		<!-- This is the image -->	
		<center><img src="http://www.brandonhall.com/blogs/wp-content/uploads/2013/09/classroom-1.jpg" width="666" height="500"></center>		
		
		<!-- This is the header -->
		<hr/>
			<center>
			<h1 title="This is the best room.">This is the math room.</h1>
			<h2> 
			 </h2>
		<hr/> """ 
	print win_screen
	last_term = form["term"].value
	third_given_answer = form["input"].value
	third_real_answer = fib(int(last_term))
	
	if third_given_answer == "QUIT":
		print "<h1> Sorry to see you go. Come back soon! </h1>"

		box = """<form action="/cgi-bin/game.py" method="get" style="display: inline;">
				<input type="hidden" name="command" value="REFRESH">
				<input type="hidden" name="inventory" value="%s">
				<input type="submit" value="Return to Main Menu">

			</form>""" % (inventory)
		print box

	elif int(third_given_answer) == int(third_real_answer):

		print """<h1>Congratulations! You have WON! Enter the amount of mana and gold you want in the following format
		and without spaces:
			"mana,gold". You can take up to 5 units. </h1>"""
	


		reward_box = """<form action="/cgi-bin/game.py" method="get" style="display: inline;">
					<input type="text" name="input">
					<input type="hidden" name="inventory" value="%s">
					<input type="submit" value="Submit to Receive!">
					<input type="hidden" name="tries" value="-1">

				</form>""" % (inventory)
		print reward_box
	else:
		print "<h2> Sorry, you guessed wrong :( Click on submit to return to the main menu.</h2>"
		return_box = """<form action="/cgi-bin/a.out.cgi" method="get" style="display: inline;">
			<input type="hidden" name="inventory" value="5,0">
			<input type="hidden" name="command" value="refresh">
			<input type="submit" value="submit">
		</form>""" 
		print return_box

elif tries == "-1":
	final_screen = """ <html>
		<head>
			<title>Dan's and Arty's Room</title>
			
			<style type="text/css">
				body {background-color: #CCCCCC}
				#center {position: relative; top: 20px;}
			</style>
		</head>
		
		<body>
			
		<!-- This is the image -->	
		<center><img src="http://www.brandonhall.com/blogs/wp-content/uploads/2013/09/classroom-1.jpg" width="666" height="500"></center>		
		
		<!-- This is the header -->
		<hr/>
			<center>
			<h1 title="This is the best room.">This is the math room.</h1>
			<h2> 
			 </h2>
		<hr/> """ 
	print final_screen
	print "<h1> Transferring your ressources </h1"

	to_add_inventory = form["input"].value
	list = to_add_inventory.split(",")
	to_add_mana = list[0]
	to_add_gold = list[1]
	current = inventory.split(",")
	new_mana = int(current[0]) + int(to_add_mana) 
	new_gold = int(current[1]) + int(to_add_gold)
	new_inventory = "str(%d),str(%d)" % (new_mana, new_gold)
	file = open('resources.csv', "rb")
	reader = csv.reader(file)
	for row in reader:
		pageMana = row[0]
		pageGold = row[1]
		pageStatus = row[2]
	file.close()

	with open("resources.csv", "w") as resourceFile:
		resourceWriter = csv.writer(resourceFile)
		resourceWriter.writerow([int(pageMana) - int(to_add_mana), int(pageGold) - int(to_add_gold), 1])
	resourceFile.close()


	final_box = """<form action="/a.out.cgi" method="get" style="display: inline;">
				<input type="hidden" name="command" value="refresh">
				<input type="hidden" name="inventory" value="%s">
				<input type="submit" value="Submit to Return to Main Menu">
			</form>""" % (new_inventory)
	print final_box





	
	





