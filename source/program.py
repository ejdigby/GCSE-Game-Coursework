#Import Modules
import random
import time
import math

#Define Menu
def menu():
	choice = "NULL"
	print("""Main Menu
Please choose a difficulty level
Enter exit to exit the program
A) Easy
B) Hard
""")

	while choice != "A" or choice != "B" or choice != "EXIT":
		choice = input("Please choose an option: ")
		choice = choice.upper()
		if choice == "A":
			#Run the run function with the parameter 9 (the total number of words needed)
			run(9)
		elif choice == "B":
			#Run the run function with the parameter 16 (the total number of words needed)
			run(16)	
		elif choice == "EXIT":
			exit()
		else:
			print (choice, " is not recongised")
			print ("Please try again")
			choice = "NULL"

#Define read words function
def readwords(level):
	#Set the path to the square root of the level + x = square root of the level + .txt. E.g. 3x3.txt
	path = str(int(math.sqrt(level))) +  "x" + str(int(math.sqrt(level))) + ".txt"
	#Set words to empty array to put the words in
	words = []
	try:
		#Opening file using with
		with open(path) as f:
			#Adding each word to the array words
			words += f.readlines()
		
		#If there arent enough words from the file show an error
		if len(words) < level + 1:
			exit()

		#For each element of the array strip it from \n
		for i in range(0,len(words)):
			words[i] = words[i].rstrip()
		return words
	except:
		print("I'm sorry there has been an error; the word files are invalid")
		exit()


#Define the grabwords function
def grabwords(words, level):
	#Define the arryas toprint and numsused
	toprint = []
	numsused = []
	#For every number between 0 and the level (total words needed)
	for i in range(0, level):
		newnum = True
		while newnum == True:
			#Set x to a random number between 0 and the level
			x = random.randrange(0, len(words))
			#Check If the number has been used
			if numsused.count(x) == 0:
				numsused.append(x)
				newnum = False
			else:	
				newnum = True
	#For every number in numsused add the equivelent words to the array to print
	for i in numsused:
		toprint.append(words[i])

	#Find a random number between 0 and the total elements in the array nums used
	toremove = random.randrange(0, len(numsused))

	#For each number between 0 and the level
	for i in range(0, level):
		#If it is in the array pass
		if i in numsused:
			pass
		#Else set the variable toadd to the word that isn't getting printed
		else:
			toadd = words[i]
	#Return the array to print and the variables toremove and toadd
	return toprint, toremove, toadd

#Define the print grid function
def printgrid(toprint, level):
	#Set the variable count to o0
	count = 0
	#For every word in the array to print
	for i in toprint:
		#If count is devisible by the sqaure root of the level print a new line
		if count % (math.sqrt(level)) == 0:
			print("\n", end="")
		print(i, end="")
		print("   |    ", end="")
		count += 1
	print("\n")
	return
#Define the run function
def run(level):
	#Read the words from the file
	words = readwords(level)
	#Find the words to print
	finalwords, toremove, toadd = grabwords(words, level)
	#Print the first grid
	printgrid(finalwords, level)
	#Sleep for 30 or 60 seconds
	if level == 16:
		time.sleep(60)
	else:
		time.sleep(30)
	#Clear the screen
	print(chr(27) + "[2J")
	#Set the variable removed to the word to remove
	removed = finalwords[toremove]
	#Replace the word that is to be removed
	finalwords[toremove] = toadd
	#Shuffle the array
	random.shuffle(finalwords)
	#Print the second grid
	printgrid(finalwords, level)
	#Ask the questions
	askquestions(removed, toadd, level)

#Define the askquestions function
def askquestions(removed, added, level):
	#Define the variables wrong and attempt
	wrong = True
	attempt = 0
	#Start a while loop for while they don't have the right answer
	while wrong == True:
			#Ask the user to enter the word that was removed
			askremoved = input("Which word was removed: ")
			#Check if it is the right word
			if askremoved.upper() == removed.upper():
				print("You got it right!")
				#Exit the while loop
				wrong = False
			else:
				#Add 1 to the number of attempts
				attempt += 1
				#If they have had 3 attempts restart the game
				if attempt == 3:
					print("You Lost!")
					menu()
				else:
					#Ask them to try again
					print("Try again")
					wrong = True

	wrong = True
	attempt = 0
	#Start a while loop for while they don't have the right answer
	while wrong == True:
			#Ask the user to enter the word that was added
			askadded = input("Which word was added: ")
			#Check if the word is right
			if askadded.upper() == added.upper():
				print("You got both right!")
				wrong = False
				asking = True
				#While they haven't entered an option
				while asking == True:
					#Ask them if they would like to play again
					playagain = input("Play again? [Yes/No]: ")
					#Check what option they chose
					if playagain.upper() == "YES":
						asking = False
						#Run the game again
						run(level)
					elif playagain.upper() == "NO":
						asking = False
						#Exit the game
						exit()
					else: 
						print("Please try again")
						asking = True
			else:
				#Add one to the number of attempts
				attempt += 1
				if attempt == 3:
					print("You Lost!")
					menu()
				else:
					print("Try again")
					wrong = True


menu()