######################
# written by facitoo #
######################

#*********************************************************************************************************************#

##########################################
#### offline and need manual training ####
##########################################

import operator
import wikipedia
from tkinter import *
import random
import shelve


window = Tk()
#######--------------------------------------------------------------------------------------------------------------------------------------
MEMORY=['you said nothing!']
CHANGE=['change your name','change name','name change','change nam','change the name','i want to change your name','i dont like your name']
EXITGREETING=['GoodBye!','Sayonara','Will miss you!','Nice talking!','See you later Aligator!','Take care']
QUESTIONS=['what','is','can','how','howcome','will','would','can']
GREETING=['hi','hello','sup','howdy','hie','hlo','hey']
EXIT=['bye','gtg','stop','ttyl','exit']
AGREE=['yes','YES','Y','y','ya','sure','ok','gg']
RELATEDNAME=['your name','what is your name','whats your name']
OOPS=['  sorry i dont got you','i think thats not in my memory','try something else! i am not smart as you','thats not in my database']
#######-------------------------------------------------------------------------------------------------------------------------------------

####-------------------------------------------------------
name=shelve.open("name.txt",flag='c',writeback=True)
try:
	NEWNAME=name['nm']
except:
	name['nm']='chatter'
	NEWNAME=name['nm']
name.close()
####-------------------------------------------------------

###---------------------------------------------
window.title(NEWNAME)
NAME=NEWNAME
result=''
eventtype=int(0)
searchflag=int(0)
found=int(0)
lmode=int(0)
OOPSCOUNTER=int(0)
says=''
key='chatter'
###----------------------------------------------

###----------------------------------------------
messages = Text(window)
messages.pack()
input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)
frame = Frame(window)
messages.insert(INSERT, '%s\n' % (NAME+':  hey! i am '+NAME))
###----------------------------------------------

def key_input():
	global key,eventtype
	key=input_field.get()
	new_name=str('you: '+key)
	messages.insert(INSERT, '%s\n' % new_name)
	input_user.set('')
	eventtype=0
	return 

def changename():
	global key,eventtype,NAME
	eventtype=1
	name=shelve.open("name.txt",flag='w',writeback=True)
	input_field.bind("<Return>", Enter_pressed)
	if key in EXIT:
		messages.insert(INSERT, '%s\n' % str(NAME+':  '+random.choice(EXITGREETING)))
		exit()
	name['nm']=str(key)
	name['what is your name']=str(key)
	name.close()
	NAME=key
	return str(NAME+': ok! so my new name is '+NAME)

def search():
	global key,eventtype,searchflag
	eventtype=1
	messages.insert(INSERT, '%s\n' % str(NAME+':  what you want me to search?'))
	input_field.bind("<Return>", Enter_pressed)
	if key in EXIT:
		messages.insert(INSERT, '%s\n' % str(NAME+':  '+random.choice(EXITGREETING)))
		exit()
	try:
		global result
		result=wikipedia.summary(key,sentences=3)
	except:
		messages.insert(INSERT, '%s\n' % str(NAME+': be more presise!!'))
		search()
	if searchflag==0 :
		messages.insert(INSERT, '%s\n' % str('***************** heres what wiki says *************\n'))
		messages.insert(INSERT, '%s\n' % result)
	searchflag=1
	return

def learn(word):
	global key,eventtype
	eventtype=1
	messages.insert(INSERT, '%s\n' % str(NAME+':  would you like me to learn the response for future reference? '))
	input_field.bind("<Return>", Enter_pressed)
	if key in EXIT:
		messages.insert(INSERT, '%s\n' % str(NAME+':  '+random.choice(EXITGREETING)))
		exit()
	if key in AGREE:
		messages.insert(INSERT, '%s\n' % str(NAME+': so! what may i say for the next time?'))
		reply=input('you: ')
		if reply in EXIT:
			messages.insert(INSERT, '%s\n' % str(NAME+':  '+random.choice(EXITGREETING)))
			exit()
		LEARNEDGREETING = shelve.open("name.txt",flag='w',writeback=True)
		LEARNEDGREETING[word] = str(reply)
		LEARNEDGREETING.close()
		return str(NAME + ': gotcha! will remember next time')
	else:
		return str(NAME+':  Ok! i just forgot what you said!')

def filter(words):
	symbols = "!@#$%"
	for letter in words:
		if letter in symbols:
			words=letter.replace(letter,'')
	return words

def check(word):
	global OOPSCOUNTER,lmode
	s=shelve.open("name.txt")
	try:
		return str(NAME+': '+s[word])
		global found
		found=1
	except:
		if word == 'lrmodon':
			lmode=1
			return str(NAME+': *learning mode on*')
			OOPSCOUNTER=0
		elif word == 'lrmodof':
			lmode=0
			return str(NAME+': *learning mode off*')
			OOPSCOUNTER=0
		else:
			OOPSCOUNTER+=1
			if OOPSCOUNTER > 3 and OOPSCOUNTER < 5:
				return str(NAME+': stop messing with me!')
			elif OOPSCOUNTER>=5:
				return str(NAME+': this is not funny anymore!')
				OOPSCOUNTER=0
			else:
				return str(NAME+':  '+random.choice(OOPS))
	finally:
		s.close()
	return
def decision(says):
	global lmode,found
	says=str(says).lower()
	says=filter(says)
	if says in GREETING:
		return str(NAME +': '+ random.choice(GREETING) +' tell me soemthing to do! ')
	elif says in EXIT:
		return str(NAME+':  '+random.choice(EXITGREETING))
		exit()
	elif says == 'search':
		search()
	elif says in CHANGE:
		messages.insert(INSERT, '%s\n' % str(NAME+': I like my name a lot! but if you want to change you can change it!'))
		messages.insert(INSERT, '%s\n' % str(NAME+': what would you like to change my name to'))
		return str(changename())
	else:
		check(says)
		if found==0 and lmode == 1:
			if says != 'lrmodon':
				return str(learn(says))
		found=0
	return

def Enter_pressed(event):
	global eventtype
	if eventtype == 1:
		key_input()
	else:
		driver()


def driver():
	global says
	says=input_field.get()
	print('you: '+says)
	messages.insert(INSERT, '%s\n' % says)
	response=decision(says)
	says=str('you: '+says)
	messages.insert(INSERT, '%s\n' % response)
	messages.see("end")
	input_user.set('')
	return "break"


input_field.bind("<Return>", Enter_pressed)
frame.pack()
window.mainloop()
