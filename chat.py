import operator
import random
import shelve

GREETING=['hi','hello','sup','howdy','hie','hlo','hey']
EXIT=['bye','gtg','stop','ttyl','exit']
NAME='chatter' 
AGREE=['yes','YES','Y','y','ya','sure','ok','gg']
RELATEDNAME=['your name','what is your name']
says=''
found=int(0)

def learn(word):
	print(NAME+':  would you like me to learn the response for future reference? \nyou:',end=' ')
	says=input()
	if says in EXIT:
		print(NAME+':  Goodbye!')
		exit()
	if says in AGREE:
		print(NAME+': so! what may i say for the next time \nyou:',end=' ')
		reply=input()
		if reply in EXIT:
			print(NAME+':  Goodbye!')
			exit()
		LEARNEDGREETING = shelve.open("name.txt",flag='c',writeback=True)
		LEARNEDGREETING[word] = str(reply)
		LEARNEDGREETING.close()	
		print(NAME + ': gotcha! will remember next time')
	else:
		print(NAME+':  Ok! i just forgot what you said!')

def filter(words):
	symbols = "!@#$%"
	for letter in words:
		if letter in symbols:
			words=letter.replace(letter,'')
	return words

def check(word):
	s=shelve.open("name.txt")
	try:
		print(NAME+': '+s[word])
		global found
		found=1
	except:
		print(NAME+':  sorry i dont got you :/')
	finally:
		s.close()
	return



print(' ->  hey! i am chatter!')
while True:
	says=str(input("you: ")).lower()
	says=filter(says)
	if says in GREETING:
		print(NAME +': '+ random.choice(GREETING) +' tell me soemthing to do! ')
	elif says in EXIT:
		print(NAME+':  Goodbye!')
		break
	else:
		check(says)		
		if found==0:
			learn(says)
		found=0
print(NAME+':  see you soon')